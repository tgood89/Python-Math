import numpy as np

###Coefficien Matrix
a = np.array([[1,1,1],[60,.70,.80]])

##Answer Matrix
b = np.array([44000,3050])

print(np.linalg.solve(a,b))


#CramersRule
#FindDeterminant
#Enter values Row wise
#A = np.array([[5,-1,-16],[6,2,-34],[-3,-5,26]])
#D = np.linalg.det(A)
#print(D)

#get D cramer
#CoeffMatrix = np.array([[2,-1,6],
#                        [-2,-6,-4],
#                        [4,-3,5]])
#D = np.linalg.det(CoeffMatrix)
#print("This is D:")
#print(D)
#print()

##Dx
#DxMatrix = np.array([[6,-1,6],
#                     [-16,-6,-4],
#                     [-4,-3,5]])
#Dx = np.linalg.det(DxMatrix)
#print("This is Dx:")
#print(Dx)
#print()

##Dy
#DyMatrix = np.array([[2,6,6],
#                     [-2,-16,-4],
#                     [4,-4,5]])
#Dy = np.linalg.det(DyMatrix)
#print("This is Dy:")
#print(Dy)
#print()

##Dz
#DzMatrix = np.array([[2,-1,6],
#                     [-2,-6,-16],
#                     [4,-3,-4]])
#Dz = np.linalg.det(DzMatrix)
#print("This is Dz:")
#print(Dz)
#print()

##x
#print("This is x:")
#print(Dx/D)
#print()

##y
#print("This is y:")
#print(Dy/D)
#print()

##z
#print("This is z:")
#print(Dz/D)
#print()
