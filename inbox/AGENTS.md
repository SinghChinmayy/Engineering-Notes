# Inbox processing

Files in this directory are incoming learning material. Process each Markdown input file in this directory (excluding `AGENTS.md` and `changes.md`) and classify its contents before making an update:

- If it explains a SQL concept, reference, or topic learned, add it to `../notes.md` under the relevant topic or subtopic. Preserve existing notes and keep any necessary edits limited to that topic or directly affected content.
- If it asks for a SQL exercise, challenge, or interview problem (including a supplied solution), add it as a new file in `../questions/` named `<next question number>. <question name>.md`. Use the next unused sequential number and a concise descriptive question name.

Keep the material self-contained, clearly separate the question from any attempt or solution, and do not remove older notes or questions while processing inbox files. After successfully incorporating an input file, record the file and its destination changes in `changes.md`, then delete the processed input file from this directory. Do not delete a file until its updates and change-log entry are complete.
