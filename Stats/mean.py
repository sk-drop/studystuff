import pandas as pd
import math

X = [1,2,3,3,4,4,4,4,4,4,5,5,5]

z = 0

for x in X:
    z += (x - mean)**2

s2 = z/(len(X)-1)

s = math.sqrt(s2)

print(s)


