# Engineering Notes

A public, hands-on record of what I am learning as an engineer. Each topic is one continuous note that grows as I learn more: concept explanations in my own words, small readable examples, the mistakes worth avoiding, and a revision block of takeaways and self-check questions. Practice problems sit alongside, with the reasoning behind each solution.

The notes are also published on my website at **[chinmaysingh.me/notes](https://chinmaysingh.me/notes)**.

## Why this repository exists

I want to learn deliberately rather than collect isolated answers. Each entry turns a concept or exercise into a reusable reference I can revise from later.

For recruiters and collaborators, it is a transparent view of how I learn: I break problems into clear steps, write down why something works, and keep the corrections visible instead of pretending I got everything right the first time.

## How it works

![I write in a notebook or in Markdown and drop the pages into inbox/. An agent with the engineering-notes skill transcribes them, merges them into one note per topic with revision questions and an occasional diagram, and commits. When I push, CI validates the notes, syncs them to my website, builds it, and publishes.](docs/how-it-works.svg)

1. I study as usual, in a paper notebook or a quick Markdown file, and drop photos, PDFs or `.md` files into [`inbox/`](inbox/). The inbox is git-ignored, so the raw pages stay private.
2. I ask my agent to "process my notes". It follows the [`engineering-notes` skill](https://github.com/SinghChinmayy/agent-skills/tree/main/skills/learning/engineering-notes): it transcribes, keeps my understanding, merges into the right topic, adds a revision block, and draws a diagram only when it helps.
3. I review the commit and push. [CI](.github/workflows/publish.yml) checks every note with [`scripts/check_notes.py`](scripts/check_notes.py), copies the notes into my website, builds it, and publishes only if the build passes.

## Notes

### SQL

| Note | What it covers |
| --- | --- |
| [Filtering grouped results with HAVING](notes/sql/filtering-groups-with-having.md) | `WHERE` vs `HAVING`, evaluation order, and the "has all of these values" pattern |

## Practice

### SQL

| # | Exercise | Focus |
| --- | --- | --- |
| 001 | [Data Science Skills](practice/sql/001-data-science-skills.md) | Filtering grouped data with `HAVING` and `COUNT(DISTINCT ...)` |
| 002 | [Histogram of Tweets](practice/sql/002-histogram-of-tweets.md) | Two-stage aggregation with a CTE and date-range filtering |

## How to use this repository

Start with a note for a concept refresher, and use its **Check yourself** questions to test your recall. Then try a practice problem before opening its solution. Practice files are numbered so progress is easy to follow over time.

## License

This project is available under the [MIT License](LICENSE), so you are welcome to use, copy, modify, and share the material.
