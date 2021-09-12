import numpy as np
from scipy import linalg

a = np.array([[1,0,0],[-14,7,2],[-6,3,1]])
print(linalg.inv(a))
