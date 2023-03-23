import math
import numpy as np
import numpy.matlib as nm
import matplotlib.pyplot as plt
np.seterr(divide='ignore',invalid='ignore')

n = 200
a = nm.linspace(0,nm.pi,n/2)
x_u= np.c_[nm.cos(a)+0.5,nm.cos(a)-0.5].reshape(n,1)
u = -10*x_u+nm.randn(n,1)
x_v= np.c_[nm.sin(a),-nm.sin(a)].reshape(n,1)
v= 10*x_v+nm.randn(n,1)
x = np.c_[u,v]
y=np.zeros((n,1))
y[0]=1
y[n-1]=-1
x2=np.sum(np.power(x,2),1)
hh=2*1**2
k=nm.exp(-(nm.repmat(x2,1,n)+nm.repmat(x2.T,n,1)-2*x*x.T)/hh)
w=k
t_tmp1 = k**2+1*np.eye(n)+10*k*(nm.diag(sum(w))-w)*k
t = np.linalg.inv(t_tmp1)*(k*y)

m=100
X=nm.linspace(-20,20,m).T
X2=np.power(X,2)
U = nm.exp(-(nm.repmat(np.power(u,2),1,m)+nm.repmat(X2.T,n,1)-2*u*X.T)/hh)
V = nm.exp(-(nm.repmat(np.power(v,2),1,m)+nm.repmat(X2.T,n,1)-2*v*X.T)/hh)

plt.figure()
plt.xlim(-20, 20)
plt.ylim(-20, 20)
# plt.colormap([1,0.7,1; 0.7,1,1])
z_tmp = np.sign((V.T)*(np.multiply(U,nm.repmat(t,1,m))))
X, Y = np.meshgrid(X, X)
# print(Y)
# print(z_tmp)
plt.contourf(X,Y,z_tmp)
plt.plot(x[0,0],x[0,1],'bo')
plt.plot(x[-1,0],x[-1,1],'rx')
plt.plot(x[:,0],x[:,1],'k.')
plt.show()
