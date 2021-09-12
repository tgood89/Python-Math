from pulp import LpVariable, LpProblem, LpMinimize, LpMaximize, LpStatus, value

#declare non negative variables
x = LpVariable("x", 0, None, cat='Integer') #x>1 and is a whole number
y = LpVariable("y",0, None, cat='Integer') #y>1 and is a whole number
z = LpVariable("z", 0, None, cat='Integer') #z>1 and is a whole number
#w = LpVariable("w", 1, None, cat='Integer') #w>1 and is a whole number

#define the problem
prob = LpProblem("problem", LpMinimize)

#define constraints
prob += 20*x + 25*y >= 830
#prob += 20*x + 25*z >= 880

#define the objective function to minimize
prob += .07*x*z + .11*x*y + 3*(.04 *x*y)

#solve
status = prob.solve()
LpStatus[status]

#print solution
print(value(x))
print(value(y))
print(value(z))
#print(value(w))
