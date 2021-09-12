
import numpy as np
import Cramer

def test_Cramer():
    L = [2,-1,6,6,
         -2,-6,-4,-16,
         4,-3,5,-4]   
    A = np.array(L)
    A.shape = (3,4)
    result = Cramer.solve(A)
    if result:
        x,y,z = result
        print('solution')
        print('x =', x)
        print('y =', y)
        print('z =', z, '\n')
        Cramer.check(A,x,y,z)

test_Cramer()
