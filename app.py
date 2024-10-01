import numpy as np

m = np.zeros((8,8))

for i in range(len(m)):
    if i%2 == 0:
        m[i][1::2] = 1
    else:
        m[i][::2] = 1

print(m)