# Anki decks

There is one deck per course-plan unit (`a1-01-introductions.csv` … `a1-10-plans.csv`), each with 36–40 cards.

## Columns

| Column | Example | Notes |
| --- | --- | --- |
| Russian | холодильник | The front of the card. Brackets warn about false friends: owoce = фрукты (не овощи!) |
| Polish | chleb, -a · móc (mogę, możesz) | Masculine nouns show the genitive. Verbs show their key forms. |
| IPA | [lɔˈdufka] | Warsaw standard, stress marked ˈ, with voicing assimilation shown |
| Type | noun-f | See below |

### Type values

| Type | Meaning | Colour |
| --- | --- | --- |
| noun-m | masculine noun | blue |
| noun-f | feminine noun | red |
| noun-n | neuter noun | green |
| noun-mp | masculine-personal noun (male people: student, brat, kolega) | purple |
| noun-pl | plural-only noun (drzwi, urodziny) | |
| verb-impf / verb-pf | imperfective / perfective verb | |
| adj, adv, num, pron, prep, part | adjective, adverb, numeral, pronoun, preposition, particle | |
| phrase | fixed phrase | |

Watch for the words where gender doesn't match the ending:
- kolega and tata are masculine-personal although they end in -a.
- imię is neuter.
- sól, jesień and podróż are feminine.

## One-time setup in Anki

1. **Tools → Manage Note Types → Add → Add: Basic.** Name it **Polish**.
2. **Fields:** rename Front to **Russian** and Back to **Polish**, then add **IPA** and **Type**. Keep this order.
3. **Cards:** paste the three parts below.

**Front template**

```html
<div class="ru">{{Russian}}</div>
```

**Back template**

```html
{{FrontSide}}
<hr id="answer">
<div class="pl {{Type}}">{{Polish}}</div>
<div class="ipa">{{IPA}}</div>
<div class="type">{{Type}}</div>
{{tts pl_PL:Polish}}
```

**Styling**

```css
.card { font-family: Lexend, Verdana, Arial, sans-serif; font-size: 28px; line-height: 1.5;
        text-align: center; background: #fbf7ee; color: #222; }
.pl { font-weight: bold; margin-top: 8px; }
.ipa { font-size: 22px; color: #555; }
.type { font-size: 15px; color: #888; margin-top: 6px; }
.noun-m  { color: #1f5fbf; }
.noun-f  { color: #c0392b; }
.noun-n  { color: #1e8449; }
.noun-mp { color: #7d3c98; }
.nightMode .card { background: #1e1e1e; color: #eee; }
.nightMode .ipa { color: #bbb; }
.nightMode .noun-m  { color: #7fb0ff; }
.nightMode .noun-f  { color: #ff8a80; }
.nightMode .noun-n  { color: #7ed99a; }
.nightMode .noun-mp { color: #d29bf0; }
```

`{{tts pl_PL:Polish}}` reads the Polish side aloud with your system's Polish voice. Remove that line if you don't have a Polish voice installed.

## Importing a deck

1. **File → Import** and choose the `.csv` file. The header lines set the separator (pipe) and the column names.
2. Set **Note type** to **Polish**. Map Russian → Russian, Polish → Polish, IPA → IPA, Type → Type.
3. Choose a deck, for example **Polish::A1::05 Shop and café**.

To use Type as a tag as well, so you can search for `tag:noun-f`, map the Type column to **Tags** in addition to the Type field.
