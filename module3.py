import matplotlib.pyplot as plt
from numpy import linspace

x = linspace(-1, 15, 100)
y1 = 115.0/10.0 - (3.0/10.0)*x
y2 = 95.0/4.0 - (11.0/4.0)*x

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'b')
plt.legend(['3x+10y=115', '11x+4y=95'])
plt.title('Solving a System of Equations with a Unique Solution')
plt.show()