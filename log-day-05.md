# Day 5 — October 16, 2025

## Learned
- What NumPy is: fast vectorized math on arrays
- `import numpy as np` convention
- Arrays: `np.array([...])` — same type, math on whole array
- Vectorized ops: `scores * 2`, `scores + 5`, `scores ** 2`
- Stats methods: `.mean()`, `.max()`, `.min()`, `.std()`, `.sum()`
- The `()` rule: `scores.mean` = the method; `scores.mean()` = the value
- Boolean masking: `scores[scores > 80]`

## Practiced
- Stats on a 10-score array
- Filtered values above 80
- Counted values above mean with `(scores > scores.mean()).sum()`

## Next
- 2D arrays (rows × columns)
- Then Pandas: Series + DataFrame