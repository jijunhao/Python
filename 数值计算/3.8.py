import numpy as np
x_0 = np.array([1,1,1,1,1,1,1,1,1])
x_1 = np.array([8,10,12,16,20,30,40,60,100])
x_2 = x_1*x_1.T
A = [[sum(x_0*x_0.T),sum(x_0*x_1.T),sum(x_0*x_2.T)],
     [sum(x_1*x_0.T),sum(x_1*x_1.T),sum(x_1*x_2.T)],
     [sum(x_2*x_0.T),sum(x_2*x_1.T),sum(x_2*x_2.T)]]
print(A)
y = np.array([0.88,1.22,1.64,2.72,3.96,7.66,11.96,21.56,43.16])
b = [[sum(y*x_0.T)],
     [sum(y*x_1.T)],
     [sum(y*x_2.T)]]
print(b)
a = np.linalg.solve(A,np.array(b))
print(a)