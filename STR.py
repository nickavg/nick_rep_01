#import pandas as pd
A = [3, 3, 6, 4, 1, 8, 2, 5, 7, 12]
B = []
C = []
x = 0
y = 0
z = 0
for N in A:
  if N not in B:
    B.append(N)
    B.sort()
for N in B:
  y = N - z
  if y > 1:
    z = z + 1
    C.append(z)
    break
  z = N
else:
  z = z + 1
  C.append(z)
print(B)
print(C)