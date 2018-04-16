import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import symbols, Symbol
from sympy.plotting import plot
from sympy.utilities.autowrap import ufuncify

points = [(-2,21),(-1,1),(0,-1),(1,-3),(2,1)]
x = [ p[0] for p in points ]
y = [ p[1] for p in points ]
X = Symbol('x')
k = len(x)-1
L = 0
for j in range(k+1):
    l = 1
    for m in range(k+1):
        if (m != j ):
            l *= (X - x[m]) / (x[j]-x[m])
    L += y[j] * l
 
L.expand()
plot(L,(X,-2,2))

f = ufuncify([X], L, backend='f2py') 

t = np.linspace(-2,2,100)
plt.plot(t, f(t), 'b-', x, y, 'bo')
#plt.scatter(*zip(*points));
plt.show()
