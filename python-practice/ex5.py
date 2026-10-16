import numpy as np

scores = np.array([88, 92, 75, 100, 63, 81, 79, 88, 94, 70])

#Print the array and its type

print(scores, type(scores))

#Print the mean (average)

print(scores.mean())

#Print the max and min

print(scores.max())

#Print only the scores > 80 (boolean masking)

print(scores[scores > 80])

#Print all scores + 5 (bonus points for everyone)

print(scores + 5)

#Print how many scores are above the mean

print((scores > scores.mean()).sum())