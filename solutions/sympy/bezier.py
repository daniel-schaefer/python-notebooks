import numpy as np
import matplotlib.pyplot as plt
from sympy import binomial
from sympy import Matrix, Symbol
from sympy import lambdify

def Bpoly(t,n,i):
    return binomial(n,i)*t**i*(1-t)**(n-i)

t = Symbol('t')
x = Symbol('x')
y = Symbol('y')

p0 = Matrix([1,0])
p1 = Matrix([x,y])
p2 = Matrix([0,1])

bezier = Bpoly(t,2,0)*p0+Bpoly(t,2,1)*p1+Bpoly(t,2,2)*p2

p = (bezier[0], bezier[1])  # we remove the Matrix type
f = lambdify((t,x,y), p)

t = np.linspace(0,1,100)
for px, py in [(0,0),(0.5,0.5),(1,1)]:
    u,v = f(t,px,py)
    plt.plot(u,v,'-',px,py,'o')
    
plt.show()
# bonus interact point(x,y) with sliders
from ipywidgets import interact

try:
    shell = get_ipython()
    @interact(x=(0,1.0),y=(0,1.0))
    def bezier(x, y):
        u, v = f(t,x,y)
        plt.plot(u, v, x, y, 'o')
except:
   print("ipywidget does not work outside jupyter")
