import numpy as np

a = np.array([1, 2])

b= np.array([2, 1])

dot = 0

for e,f in zip(a, b):
    dot += e*f

dot

np.sum(a*b)

(a*b).sum()

np.dot(a, b)

a.dot(b)

b.dot(a)

amag = np.sqrt( (a*a).sum() )

amag = np.linalg.norm(a)

cosangle = a.dot(b) / ( np.linalg.norm(a) * np.linalg.norm(b) )

angle = np.arccos(cosangle)

