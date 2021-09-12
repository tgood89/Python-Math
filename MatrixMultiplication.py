import numpy as np

#price matrix
A = np.array([[.07,0,0,0],[0,.14,0,0],[0,0,.1,0],[0,0,0,.21]])
B = np.array([[17000,16000],[20000,23000],[33000,31000],[46000,50000]])
np.dot(A,B)
product = np.dot(A,B)

print(product)

#A = np.array([[80,40,120],[60,30,150]])
#B = np.array([[1/2,1/5],[1/4,1/5],[1/4,3/5]])
#np.dot(A,B)
#product = np.dot(A,B)

#print(product)

