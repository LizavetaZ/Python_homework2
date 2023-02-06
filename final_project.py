from sympy import *
from sympy.plotting import plot,plot3d

x = symbols('x')
y = -12*(x**4)*sin(cos(x))-18*(x**3)+5*(x**2)+10*x-30

#график
plot(-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30)

#корни
nonlinsolve([y], x)

#возрастание фнукции
solveset(y>0)

#убывание фнукции
solveset(y<0)

#вершины
holms = y.diff(x)
nonlinsolve([holms],[x])

#f(x)>0
solveset(y>0)

#f(x)<0
solveset(y<0)