import numpy as np

###Coefficien Matrix
a = np.array([[2,0,-1,0],[6,0,0,-2],[0,2,-2,-1]])

##Answer Matrix
b = np.array([0,0,0])

print(np.linalg.lstsq(a,b))
