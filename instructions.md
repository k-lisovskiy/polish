# Instructions for Claude

Read `intent.md` first. It holds the goal, the learner and the current state.

## Repository layout

| Path | Contents |
| --- | --- |
| `course-plan.md` | Master syllabus, A0–C1. The source of truth for units and grammar. Changes rarely. |
| `lesson-format.md` | How lessons are built: unit split, 60-min lesson steps, grammar drills, formatting rules. Can change independently of the plan. |
| `lessons/<level>/<unit>-<slug>/` | Lesson materials, e.g. `lessons/a1/05-genitive/lesson-1.md` (create as needed) |
| `progress/` | Placement results, retest results, a session log (`progress/log.md`) |
| `tools/` | Interactive HTML tools (placement test, drills). Self-contained, no build step. |
| `decks/` | Anki decks, one file per course-plan unit (`a1-01-introductions.csv` …), 30–40 rows: `Russian|Polish|IPA`, pipe-separated with `#separator:Pipe` and `#columns:` header lines. IPA in square brackets, Warsaw standard, stress marked with ˈ, with voicing assimilation and final devoicing shown ([lɔˈdufka], [f ˈpɔlst͡sɛ]). Masculine nouns show the genitive (chleb, -a); verbs show the forms the unit drills. |

## Writing lesson materials

- **Language:** explanations in English, examples in Polish. Add a short Russian contrast note when Russian interferes (the "Uwaga, rusycyzm!" box).
- **Lesson format:** follow `lesson-format.md`. 60 min in two blocks, at most 10 new words and one grammar point per lesson, 2–3 lessons per unit. File lessons as `lessons/<level>/<unit>-<slug>/lesson-<n>.md`.
- **Dyslexia formatting:**
  - Short paragraphs and lots of white space.
  - Bold for emphasis, never italics or underline in learner-facing material.
  - Endings in bold inside tables (dom**u**).
  - One table per topic.
  - Mark word stress in bold, e.g. uniwer**sy**tet.
- **Colour code (HTML tools):** masculine blue, feminine red, neuter green, masculine-personal purple. Keep these colours fixed across all files.
- **Audio first:** every dialogue and word list needs text a TTS voice can read (pl-PL). HTML tools use `speechSynthesis` with a Polish voice.
- **Accuracy:** double-check every Polish form: declension, aspect, spelling, stress. Flag any form you're unsure of instead of guessing.
- **Exercises:** every lesson has spoken practice and at least one written grammar drill set (rules in `lesson-format.md`). Free writing stays at 3–5 sentences with sentence frames.

## Workflow

1. Before a lesson, read `intent.md`, `lesson-format.md`, the latest `progress/` entry and the relevant unit in the plan.
2. Generate the lesson in `lessons/`. Repair lessons use the decks of the A1 units they repair; add rows to a unit deck only for words it is missing. Generate IPA with `tools/pl_ipa.py` from stress-marked syllables (lo-DÓW-ka) and review the output by hand.
3. After the learner reports results, append them to `progress/log.md`: date, unit, what was hard, errors to recycle.
4. Recycle errors: put items from the last 3 log entries (including missed drill items) into the next lesson's warm-up.
5. When the syllabus or the current state changes, update `intent.md` and the plan. When only the lesson format changes, update `lesson-format.md` and leave the plan alone.

## Conventions

- Dates are ISO (YYYY-MM-DD), units are metric.
- Commit messages are short and in the imperative ("Add A1.5 genitive lesson 1").
- Commit after each completed lesson or progress update, and push to `main`.
- Don't add personal data beyond what's already in `intent.md`.

## Communication

- Concise and direct, with reasoning. Point out mistakes and weak spots proactively.
- Reply in English unless the learner writes in Russian; Polish is fine for practice exchanges.
