import numpy as np

print(np.__version__)   # should print something like 2.x.x

import numpy as np

# Python list
scores_list = [3, 7, 1, 8, 9, 0]

# NumPy array
scores = np.array([3, 7, 1, 8, 9, 0])

print(scores)          # [3 7 1 8 9 0]   (note: no commas)
print(type(scores))    # <class 'numpy.ndarray'>

scores_list = [3, 7, 1, 8, 9, 0]
#python
scores_list * 2      # [3, 7, 1, 8, 9, 0, 3, 7, 1, 8, 9, 0]  ← repeats
#numpy
scores * 2           # [ 6 14  2 16 18  0]   ← multiplies each

scores + 10     # [13 17 11 18 19 10]      add 10 to each
scores / 2      # [1.5 3.5 0.5 4.  4.5 0. ]  divide each by 2
scores ** 2     # [ 9 49  1 64 81  0]      square each

scores.sum()      # 28
scores.mean()     # 4.666...
scores.max()      # 9
scores.min()      # 0
scores.std()      # standard deviation (new!)

scores = np.array([3, 7, 1, 8, 9, 0])

scores > 4              # [False  True False  True  True False]
scores[scores > 4]      # [7 8 9]   ← the actual values > 4

# Day 3 style
result = []
for s in scores:
    if s > 4:
        result.append(s)

# NumPy style
scores[scores > 4]      # one line, same result

