# Instructions for Claude

Read `intent.md` first. It holds the goal, the learner and the current state.

## Repository layout

| Path | Contents |
| --- | --- |
| `plan/course-plan.md` | Master syllabus, A0–C1. The source of truth for units, grammar and lesson format. |
| `lessons/<level>/<unit>-<slug>/` | Lesson materials, e.g. `lessons/a1/05-genitive/session-1.md` (create as needed) |
| `progress/` | Placement results, retest results, a session log (`progress/log.md`) |
| `tools/` | Interactive HTML tools (placement test, drills). Self-contained, no build step. |
| `decks/` | Anki-importable CSVs: `polish;russian;english;notes;audio-hint` |

## Writing lesson materials

- **Language:** explanations in English, examples in Polish. Add a short Russian contrast note when Russian interferes (the "Uwaga, rusycyzm!" box).
- **Session format:** follow the 8-step session in the plan. Keep it to 25–30 min, with at most 8–10 new words and one grammar point.
- **Dyslexia formatting:**
  - Short paragraphs and lots of white space.
  - Bold for emphasis, never italics or underline in learner-facing material.
  - Endings in bold inside tables (dom**u**).
  - One table per topic.
  - Mark word stress, e.g. uniwer**sy**tet.
- **Colour code (HTML tools):** masculine blue, feminine red, neuter green, masculine-personal purple. Keep these colours fixed across all files.
- **Audio first:** every dialogue and word list needs text a TTS voice can read (pl-PL). HTML tools use `speechSynthesis` with a Polish voice.
- **Accuracy:** double-check every Polish form: declension, aspect, spelling, stress. Flag any form you're unsure of instead of guessing.
- **Exercises:** prefer recognition and spoken production. Writing comes in 3–5 sentence tasks with sentence frames.

## Workflow

1. Before a session, read `intent.md`, the latest `progress/` entry and the relevant unit in the plan.
2. Generate the session in `lessons/`, plus any new deck rows in `decks/`.
3. After the learner reports results, append them to `progress/log.md`: date, unit, what was hard, errors to recycle.
4. Recycle errors: put items from the last 3 log entries into the next session's warm-up.
5. When the plan or the current state changes, update `intent.md` and the plan.

## Conventions

- Dates are ISO (YYYY-MM-DD), units are metric.
- Commit messages are short and in the imperative ("Add A1.5 genitive session 1").
- Commit after each completed lesson or progress update, and push to `main`.
- Don't add personal data beyond what's already in `intent.md`.

## Communication

- Concise and direct, with reasoning. Point out mistakes and weak spots proactively.
- Reply in English unless the learner writes in Russian; Polish is fine for practice exchanges.
