import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
from sympy import symbols, Matrix, Symbol
from sympy import lambdify


n = 3
m = Matrix(n*n*[0.01]).reshape(n,n) - Matrix.diag(n*[0.01])
y = symbols('y:{}'.format(3*n), real=True, nonnegative=True )
nu = symbols('nu:{}'.format(n), real=True, nonnegative=True)
mu = symbols('mu:{}'.format(n), real=True, nonnegative=True)
beta = symbols('beta:{}'.format(n), real=True, nonnegative=True)
gamma = symbols('gamma:{}'.format(n), real=True, nonnegative=True)

ydot = [nu[k] - beta[k]*y[k]*y[k+n] - mu[k]*y[k] #dS/dt
        + sum(Matrix(y[:n]).T * m) 
        - sum(m @ Matrix(y[:n])) for k in range(n)]

ydot += [beta[k] * y[k+n] * y[k]- (gamma[k] + mu[k])*y[k+n]  #dI/dt
        + sum( m @ Matrix(y[n:2*n])) 
        - sum(Matrix(y[n:2*n]).T @ m ) for k in range(n)]

ydot += [ - nu[k] + gamma[k]*y[k+n] for k in range(n)] #dR/dt

t = Symbol('t')

f = lambdify((y,t)+nu+mu+beta+gamma, ydot)


tout = np.linspace(0, 10, 100)
nu = n*[0.0]
mu = n*[0.0]
beta = [1.66 for i in range(n)]
gamma = [0.4545-0.1*i for i in range(n)]
k_vals = (*nu, *mu, *beta, *gamma)
y0 = n*[0.95]+n*[0.05]+n*[0]
legends = ['$S_{}$'.format(i) for i in range(n)]
legends += ['$I_{}$'.format(i) for i in range(n)]
legends += ['$R_{}$'.format(i) for i in range(n)]
plt.plot(tout, spi.odeint(f, y0, tout, k_vals))
plt.legend(legends)
plt.show()
