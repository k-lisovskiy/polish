# Lesson format

This file says **how** lessons are built. `course-plan.md` says **what** is taught (units, grammar, goals).
The format can change here without touching the plan.

Last updated: 2026-11-09

## Weekly rhythm

| What | How much |
| --- | --- |
| Lessons | 3 a week, 60 min each |
| Anki | Every day: 15–20 new cards plus due reviews (about 20–35 min) |
| One unit | 2–3 lessons |

About 3 h of lessons plus about 3–4 h of Anki is roughly 6.5 h a week, which matches the schedule in `intent.md`.

**Anki load.** After about a month, daily reviews settle at roughly 8–10 times the number of new cards per day.
At 20 new cards a day that is 160–200 reviews, about 30 min with audio. Start at 15. Go up to 20 only if reviews stay under 30 min.
15 a day for a year is about 5,500 cards, which covers the B1 vocabulary target (about 4,000 words).

## Splitting a unit

| Lesson | Focus | Grammar | Drills |
| --- | --- | --- | --- |
| 1. Input | New dialogue, new words, first grammar point | Point A | 1 short set (8 items) |
| 2. Drill | Same dialogue heard again or a second short text; second grammar point, or point A in more depth | Point B or A in depth | 2 sets (10–12 items each) |
| 3. Use and check | Mixed review, translation drill, writing, speaking, unit check | No new grammar | 1 mixed set + 1 translation set |

- At most one new grammar point per lesson, and at most two per unit.
- Use 2 lessons when the unit is light or mostly known (often in the repair block). Use 3 when it is new or heavy (A2.3, A2.4, A2.6, A2.10, A2.11 and most of B1).
- Lesson 3 ends with a 10-item unit check. The result goes into `progress/log.md`.

## One 60-minute lesson

Two 25-minute blocks with a real break between them. Reading and writing tire a dyslexic learner faster than listening and speaking do, so the break and the change of activity keep the second half useful.

### Block 1 (25 min): take in

1. **Warm-up (5 min):** 6–8 items taken from errors in the last 3 log entries, answered aloud.
2. **Listen first (5 min):** a short dialogue (60–120 words at A1–A2, up to 200 at B1), heard twice before any text is shown.
3. **Read along (5 min):** the same text with audio, in chunks of 3–4 lines, key words in bold.
4. **New words (5 min):** no more than 10. Each one has audio, its stress marked in bold (uniwer**sy**tet), a Russian gloss, and its word family.
5. **Grammar point (5 min):** one colour-coded table and one model sentence. Short explanation, no long prose.

### Break (5 min)

Away from the screen. Stand up and move.

### Block 2 (25 min): produce

6. **Oral drill (5 min):** the same pattern said aloud from audio or picture cues, before anything is written.
7. **Written drill (10–12 min):** see "Grammar drills" below.
8. **Real task (5 min):** a role-play or a voice message that uses the new pattern.
9. **Exit check (3 min):** 3 items, plus the new Anki rows for `decks/`.

In lesson 3, steps 2–5 are replaced by a mixed review and a 3–5 sentence writing task with sentence frames.

## Grammar drills

Drills are written exercises in the style of Golitsynsky's *Grammar*: many short sentences, one pattern, done until the form comes automatically.
Each lesson has at least one set.

### Drill types

Order them from easiest to hardest across a unit:

| Type | Example | What gets written |
| --- | --- | --- |
| Choose | Nie mam (czas / czasu) | One word |
| Open the brackets | Nie mam (czas) → czas**u** | One word |
| Transform | Mam samochód. → Nie mam samochod**u**. | Whole short sentence |
| Translate from Russian | Я слушаю музыку. → Słucham muzyk**i**. | Whole short sentence |

Translating from Russian matters most. It trains exactly the spots where Russian interferes: which case a verb takes, the genitive after negation, masculine-personal forms.

### Rules for a drill set

- **One pattern per set.** Mix patterns only after each one has been drilled on its own. Never put confusable forms in the same set the first time (for example *-a/-u* in the genitive, or *-li/-ły*).
- **8–12 items, numbered.** The set has a visible end.
- **Item 0 is a worked example** at the top of the set.
- **Known words only.** No new vocabulary in drills, so effort goes to grammar, not decoding. Sentences stay short (up to 8 words) and natural.
- **Say it, then write it.** The learner says each answer aloud before writing it.
- **Write only what is being practised.** For fill-in items, write just the word, not the whole sentence. Whole sentences only for transformation and translation.
- **Typing is the default** because of dysgraphia: Polish keyboard, autocorrect and spell-check off (they hide mistakes). Handwriting is fine for short sets if it helps memory.
- **Answer key** at the end of the file, below a clear separator, with each answer readable by TTS. The learner checks by listening as well as reading.
- **Mistakes are recycled.** Missed items go into the next lesson's warm-up, into `progress/log.md`, and, if they are missed twice, into Anki as sentence cards.

## Formatting rules (all materials)

| Area | Rule |
| --- | --- |
| Typography | Sans-serif font (Lexend, Verdana or Arial), 12–14 pt, 1.5 line spacing, left-aligned, cream or off-white background. Bold for emphasis, never italics or underline. |
| Colour code (same everywhere) | Masculine blue, feminine red, neuter green, masculine-personal purple. Each case also has a fixed colour for its endings. |
| Ending tables | Ending in bold, stem in plain text: dom**u**. One table per topic. |
| Stress | Marked in bold in new words: uniwer**sy**tet. |
| Diacritics | Shown large in early units. Confusable pairs (ś/ź/ć, ą/ę, ó/o) practised in separate lessons, never together. |
| Spelling | Taught as patterns with memory aids and word families (*mój – moja* explains ó; *morze – morski* explains rz), not as lists to memorize. |
| Reading load | Every text has audio. Glossary on the same page. Reading tasks are short and visibly finite. |
| Writing load | No copying out of long texts. Sentence frames and starters. TTS for self-checking. |
| Dictation | Phrase by phrase, never a full paragraph. Checked against audio, not only against text. |
| Review | Anki with Polish audio, plus small doses of cumulative review in every warm-up. |
| Tests | Mostly oral or recognition-based until B1. Timed exam-format practice only from the B1 exam module on. |
