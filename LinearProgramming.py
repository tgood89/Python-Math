from pulp import LpVariable, LpProblem, LpMinimize, LpMaximize, LpStatus, value

#declare non negative variables
x = LpVariable("x", 0, None) #x>1 and is a whole number
y = LpVariable("y", 0, None) #y>1 and is a whole number
z = LpVariable("z", 0, None) #z>1 and is a whole number
w = LpVariable("w", 0, None) #w>1 and is a whole number

#define the problem
prob = LpProblem("problem", LpMinimize)
#prob = LpProblem("problem", LpMaximize)



#define constraints
prob += 25*x + 40*y + 25*z >= 1840
prob += 10*x +15*z >= 480
prob += 10*x + 20*y >= 620
#prob += 160*x + 350*y <= 8850


#define the objective function to minimize/maximize
prob += 670*x + 660*y + 630*z


#solve
status = prob.solve()
LpStatus[status]


#print solution
print(value(x))
print(value(y))
print(value(z))
#print(value(w))

