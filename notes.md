# Filtering grouped results with `HAVING`

Use `HAVING` when you need to filter a group of rows based on an aggregate value, such as a count, total, or average. `WHERE` and `HAVING` often appear in the same query, but they work at different stages:

- `WHERE` filters individual rows before they are grouped.
- `GROUP BY` forms groups from the remaining rows.
- `HAVING` filters those groups after an aggregate has been calculated.

## Example: candidates with every required skill

Suppose `candidates` has one row per candidate skill. To find candidates who know Python, Tableau, and PostgreSQL, first keep only those three skill rows. Then group them by candidate and retain groups containing all three distinct skills.

```sql
SELECT candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(DISTINCT skill) = 3
ORDER BY candidate_id;
```

### How the query works

1. `WHERE skill IN (...)` removes skills that are not required for this role, such as `R` or `SQL Server`.
2. `GROUP BY candidate_id` collects each candidate's remaining skill rows into one group.
3. `COUNT(DISTINCT skill)` counts the different required skills in each candidate's group.
4. `HAVING ... = 3` keeps only candidates with all three required skills.
5. `ORDER BY candidate_id` returns the qualifying candidates in ascending ID order.

## When to use this pattern

Use this pattern when a requirement means “has all of these values,” such as a customer who bought every product in a set or a student who completed every required course. Change the list in `IN (...)` and the number in `HAVING` together so that the count matches the number of required values.

## Common mistakes

- Do not use `WHERE COUNT(...)`: `WHERE` runs before aggregate values exist. Put aggregate conditions in `HAVING`.
- Use `COUNT(DISTINCT skill)` when duplicate skill rows are possible; `COUNT(skill)` could make a candidate appear to have more required skills than they actually do.
- `HAVING COUNT(DISTINCT skill) = 3` is correct here only because there are three required skills. If the required list changes, update the count too.
