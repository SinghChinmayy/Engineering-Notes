# Processing log

What the agent processed and where it went, newest first.

## 2026-10-27 · MD5

- Processed `md5-page1-basics.jpg`, `md5-page2-how-it-works.jpg`, `md5-page3-words-and-operations.jpg` (three notebook pages) and the RareSkills video [How the MD5 hash function works (from scratch)](https://www.youtube.com/watch?v=5MiMK45gkTY):
  - Created `notes/cryptography/md5.md`: hex length, the step-by-step algorithm, one step up close, a from-scratch implementation checked against `hashlib`, security status, and four visible corrections (input length and padding, `.encode()` vs `.hexdigest()`, `~` for NOT, SHA-1 is broken too).
  - Added diagrams `notes/cryptography/assets/md5-pipeline.svg` and `md5-one-step.svg`.
  - Kept the three pages as `notes/cryptography/sources/md5-page-1.jpg` to `md5-page-3.jpg` (resized to 1500×2000, metadata stripped) and linked them from the note under "My notebook pages".

## 2026-10-27

- Restructured the repository: `notes.md` became `notes/sql/filtering-groups-with-having.md`, and questions moved to `practice/sql/`.

## 2026-10-04

- Processed `q.md`:
  - Added the exercise and solution to `practice/sql/002-histogram-of-tweets.md`.
- Processed `question.md`:
  - Added the question and solution to `practice/sql/001-data-science-skills.md`.
  - Added notes on `WHERE`, `GROUP BY`, `HAVING`, and `COUNT(DISTINCT ...)` to `notes/sql/filtering-groups-with-having.md`.
