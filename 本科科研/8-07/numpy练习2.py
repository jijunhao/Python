import numpy as np
A = np.arange(1,37).reshape((6,6))
B =np.diagflat([1,3,5,7,9,11])
print(np.dot(A,B))
