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
- `notes/<subject>/sources/`: kept notebook pages (see below).
- `log.md`: what was processed and where it went.
- `scripts/check_notes.py`: run it before every commit. CI runs it too, and nothing is published unless it passes.

## Keep notebook pages

Yes: keep my handwritten pages with each note so I can look at the originals later. For every photo or scanned page:

1. Resize it to about 1500×2000 and compress it: `sips -Z 2000 -s format jpeg -s formatOptions 72 in.jpg --out notes/<subject>/sources/<topic>-page-N.jpg`.
2. Strip its metadata: `python3 scripts/strip_metadata.py notes/<subject>/sources/*.jpg`. Phone photos can carry GPS location; `check_notes.py` rejects any page that still has metadata or is over 800 KB.
3. Link the pages from the note under `## My notebook pages`, inside a `<details>` block, with a one-line caption per page.

Skip any page that shows personal content and ask me instead. The raw files in `inbox/` stay git-ignored either way.

## Writing

- Write notes as an experienced teacher helping a learner revisit the material later, but in my voice: keep my own analogies and the way I understood it.
- Make each note self-contained, accurate and polished: introduce the concept in plain language, explain why and when to use it, show a small readable example, explain the important parts of that example, and call out common mistakes or distinctions when useful.
- Prefer clear headings and short sections over dense prose. Define unfamiliar terms on first use, use consistent terminology, and do not assume the reader remembers the original question or context.
- Preserve existing notes. Keep edits limited to the relevant topic, subtopic or directly affected content, and record them in the note's `## History`.
- When a note or practice file is added, update the index in `README.md`.

## Publishing

There are two ways to publish, and both run the same checks:

- **Push to `main`**: CI validates the notes, copies `notes/` and `practice/` into the website repository, builds the site, and pushes only if the build passes.
- **Open a pull request** from a branch in this repository: CI validates it, merges it automatically if it only changes notes content (`notes/`, `practice/`, `log.md`, `README.md`), then publishes. Pull requests that touch scripts or workflows wait for a manual merge, and forks are never auto-merged.

Commit freely, but push or open a pull request only when I say so: both end up on the website.
