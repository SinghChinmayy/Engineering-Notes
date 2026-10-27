# Repository guidance

This repository holds my engineering notes: one continuous note per topic, written from my notebook and Markdown notes, kept useful for revision, and published to [chinmaysingh.me/notes](https://chinmaysingh.me/notes) by CI. It is meant to be useful to both me and other learners.

## Processing the inbox

When asked to "process my notes" or "process the inbox", follow the `engineering-notes` skill. It is installed in this repository (`.claude/skills/` and `.agents/skills/`). If your agent cannot see it, install it with:

```bash
npx skills add SinghChinmayy/agent-skills --skill engineering-notes
```

This repository uses the skill's default layout:

- `inbox/`: raw input, git-ignored except `inbox/README.md`.
- `notes/<subject>/<topic>.md`: one growing note per topic, with diagrams in `notes/<subject>/assets/`.
- `practice/<subject>/NNN-<slug>.md`: solved exercises and interview problems.
- `log.md`: what was processed and where it went.
- `scripts/check_notes.py`: run it before every commit. CI runs it too, and nothing is published unless it passes.

## Writing

- Write notes as an experienced teacher helping a learner revisit the material later, but in my voice: keep my own analogies and the way I understood it.
- Make each note self-contained, accurate and polished: introduce the concept in plain language, explain why and when to use it, show a small readable example, explain the important parts of that example, and call out common mistakes or distinctions when useful.
- Prefer clear headings and short sections over dense prose. Define unfamiliar terms on first use, use consistent terminology, and do not assume the reader remembers the original question or context.
- Preserve existing notes. Keep edits limited to the relevant topic, subtopic or directly affected content, and record them in the note's `## History`.
- When a note or practice file is added, update the index in `README.md`.

## Publishing

Pushing to `main` publishes. CI validates the notes, copies `notes/` and `practice/` into the website repository, builds the site, and pushes only if the build passes. Commit freely, but push only when I say so.
