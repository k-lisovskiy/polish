"""Polish -> IPA (narrow-ish, Warsaw standard) from stress-marked syllabified strings like 'lo-DÓW-ka'."""
import re, sys

VOWELS = set('aeiouyąęó')
PAIRS = {'b':'p','d':'t','ɡ':'k','v':'f','z':'s','ʐ':'ʂ','ʑ':'ɕ','d͡z':'t͡s','d͡ʐ':'t͡ʂ','d͡ʑ':'t͡ɕ'}
DEV = PAIRS; VOI = {v:k for k,v in PAIRS.items()}
VOICELESS = set(PAIRS.values()) | {'x'}
OBSTR = set(PAIRS) | VOICELESS
PALAT_I = {'c':'t͡ɕ','s':'ɕ','z':'ʑ','n':'ɲ','dz':'d͡ʑ'}
PLAIN = {'ch':'x','cz':'t͡ʂ','sz':'ʂ','rz':'ʐ','dż':'d͡ʐ','dź':'d͡ʑ','dz':'d͡z','ć':'t͡ɕ','ś':'ɕ','ź':'ʑ','ń':'ɲ',
         'ł':'w','w':'v','c':'t͡s','h':'x','j':'j','b':'b','d':'d','f':'f','g':'ɡ','k':'k','l':'l','m':'m',
         'n':'n','p':'p','r':'r','s':'s','t':'t','z':'z','ż':'ʐ'}
VOW = {'a':'a','e':'ɛ','i':'i','o':'ɔ','u':'u','ó':'u','y':'ɨ','ą':'ɔ̃','ę':'ɛ̃'}
PALATALIZABLE = {'p','b','m','f','v','k','ɡ','x'}

def word_phones(word):
    """word: syllables joined by '-', stressed syllable uppercase. Returns list of [phone, syl, flags]."""
    syls = word.split('-')
    stress = next((i for i,s in enumerate(syls) if any(c.isupper() for c in s)), None)
    letters = []
    for i,s in enumerate(syls):
        for ch in s.lower():
            letters.append((ch, i))
    out = []; j = 0; n = len(letters)
    L = lambda k: letters[k][0] if k < n else ''
    while j < n:
        c, syl = letters[j]
        if c in VOWELS:
            # 'au' in one syllable -> a + w
            if c == 'u' and out and out[-1][0] == 'a' and out[-1][1] == syl and j>0 and L(j-1)=='a':
                out.append(['w', syl, '']); j += 1; continue
            if c == 'i' and j > 0 and L(j-1) not in VOWELS and L(j+1) in VOWELS and out and not out[-1][2]=='pal':
                # palatalisation marker after consonant: silent
                j += 1; continue
            out.append([VOW[c], syl, '']); j += 1; continue
        two = c + L(j+1); three = two + L(j+2)
        # palatal series before i
        if three == 'dzi':
            out.append(['d͡ʑ', syl, 'pal']); j += 2
            if L(j+1) in VOWELS: j += 1
            continue
        if c in 'csnz' and L(j+1) == 'i' and two not in ('cz','sz','rz'):
            out.append([PALAT_I[c], syl, 'pal']); j += 1
            if L(j+1) in VOWELS: j += 1
            continue
        if two in PLAIN and len(two) == 2:
            ph = PLAIN[two]; flag = 'rz' if two == 'rz' else ''
            out.append([ph, syl, flag]); j += 2
        else:
            ph = PLAIN[c]; flag = 'w' if c == 'w' else ''
            out.append([ph, syl, flag]); j += 1
        if L(j) == 'i' and out[-1][0] in PALATALIZABLE:
            out[-1][0] += 'ʲ'
            if L(j+1) in VOWELS: j += 1
    return out, stress

def base(p): return p.replace('ʲ','')

def resolve(words):
    """words: list of (phones, stress, is_prep). Applies nasals, n->ŋ, voicing."""
    flat = []
    for wi,(ph,st,prep) in enumerate(words):
        for k,p in enumerate(ph):
            flat.append({'p':p[0],'syl':p[1],'f':p[2],'w':wi,'end':k==len(ph)-1,'prep':prep})
    N = len(flat)
    # nasal vowels
    for i,x in enumerate(flat):
        if x['p'] in ('ɔ̃','ɛ̃'):
            oral = x['p'][0]
            nxt = base(flat[i+1]['p']) if i+1<N and flat[i+1]['w']==x['w'] else None
            if nxt is None:
                x['p'] = 'ɛ' if oral=='ɛ' else 'ɔ̃'
            elif nxt in ('p','b'): x['p'] = oral+'m'
            elif nxt in ('t','d','t͡s','d͡z','t͡ʂ','d͡ʐ'): x['p'] = oral+'n'
            elif nxt in ('t͡ɕ','d͡ʑ'): x['p'] = oral+'ɲ'
            elif nxt in ('k','ɡ'): x['p'] = oral+'ŋ'
            elif nxt in ('l','w'): x['p'] = oral
    for i,x in enumerate(flat):
        if x['p']=='n' and i+1<N and flat[i+1]['w']==x['w'] and base(flat[i+1]['p']) in ('k','ɡ'):
            x['p']='ŋ'
    # voicing, cluster by cluster
    isob = lambda x: base(x['p']) in OBSTR
    i = 0
    while i < N:
        if not isob(flat[i]): i += 1; continue
        j = i
        while j+1 < N and isob(flat[j+1]): j += 1
        cl = flat[i:j+1]
        last = cl[-1]
        # what follows the cluster?
        k = j+1
        final = False
        if last['end'] and not last['prep']:
            final = True
        else:
            # only sonorant consonants until end of word -> devoice (jadł, mógł)
            kk = k
            while kk < N and flat[kk]['w']==last['w'] and base(flat[kk]['p']) not in set(VOW.values())|{'ɔ̃','ɛ̃'} and flat[kk]['p'] not in ('ɔ','ɛ','a','i','u','ɨ') and not flat[kk]['p'][0] in 'ɔɛaiuɨ':
                kk += 1
            if kk > k and (kk>=N or flat[kk]['w']!=last['w']):
                final = True
        state = 'vl' if final else None
        for x in reversed(cl):
            b = base(x['p']); pal = 'ʲ' if x['p'].endswith('ʲ') else ''
            transparent = x['f'] in ('w','rz')
            if state is None:
                if not transparent:
                    state = 'vl' if b in VOICELESS else 'vd'
                continue
            if state=='vl' and b in DEV: b = DEV[b]
            elif state=='vd' and b in VOI and b!='x': b = VOI[b]
            x['p'] = b+pal
            if not transparent or True:
                state = 'vl' if b in VOICELESS else 'vd'
        # progressive devoicing of w / rz after voiceless
        for a,bx in zip(cl, cl[1:]):
            if bx['f'] in ('w','rz') and base(a['p']) in VOICELESS:
                b = base(bx['p']); pal = 'ʲ' if bx['p'].endswith('ʲ') else ''
                if b in DEV: bx['p'] = DEV[b]+pal
        i = j+1
    # render
    res = []
    for wi,(ph,st,prep) in enumerate(words):
        s = ''
        for x in [y for y in flat if y['w']==wi]:
            if st is not None and x['syl']==st and not x.get('mk'):
                if not any(y.get('mk') for y in flat if y['w']==wi):
                    s += 'ˈ'; x['mk']=True
            s += x['p']
        res.append(s)
    out = ''
    for wi,s in enumerate(res):
        out += s if (wi==0 or words[wi-1][2]) else ' '+s
        if words[wi][2]: out += ' '
    return '['+out.replace('  ',' ').strip()+']'

PREPS = {'w','z'}
def form_ipa(form):
    words = []
    for w in form.split():
        ph, st = word_phones(w)
        words.append((ph, st, w.lower() in PREPS))
    return resolve(words)

def entry_ipa(phon):
    parts = re.split(r'( — |, | / )', phon)
    return ''.join(p if p in (' — ',', ',' / ') else form_ipa(p) for p in parts)

if __name__ == '__main__':
    for a in sys.argv[1:]: print(a, entry_ipa(a))
