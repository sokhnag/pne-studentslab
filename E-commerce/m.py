import sympy as sp
from rich.jupyter import display

from sympy import (
    symbols, sqrt, cos, sin, tan, atan2, acos, pi, exp, log,
    Matrix, Rational, Function, simplify, trigsimp, latex, Abs,
    diff, solve, Eq, oo, limit, Piecewise,
)
from sympy.vector import CoordSys3D
from sympy.plotting import plot3d, plot

# Pretty printing in the notebook
sp.init_printing(use_latex='mathjax')

# Common symbols used throughout
x, y, z, t, s, k, r, theta, phi, rho = symbols(
    'x y z t s k r theta phi rho', real=True
)
alpha, beta, lam = symbols('alpha beta lambda', real=True)

print('Setup complete — SymPy version:', sp.__version__)

def gradient(f, variables):
    """Compute ∇f as a column Matrix."""
    return Matrix([diff(f, var) for var in variables])

def hessian(f, variables):
    """Compute the Hessian matrix H_f."""
    n = len(variables)
    H = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            H[i, j] = diff(f, variables[i], variables[j])
    return H


f_ex2 = x**3 - 3*x*y + y**3
# 1. Gradient
grad_ex2 = gradient(f_ex2,[x,y])   # TODO: use the gradient() helper defined above
print('∇f =', grad_ex2)


# 2. Critical points
cps = solve(grad_ex2, [x,y])        # TODO: solve(grad_ex2, [x, y])
print('Critical points:', cps, "\n")

# 3. Hessian
H_ex2 = hessian(f_ex2, [x,y])
# TODO: use the hessian() helper
print('Hessian H_f =')
print(H_ex2)

# 4. Second derivative test at each critical point
# For each cp, compute D = H[0,0]*H[1,1] - H[0,1]^2
# and check sign of H[0,0] to classify

for cp in cps:
    H_val = H_ex2.subs({x: cp[0], y: cp[1]}) # TODO: substitute the critical point
    D_val = H_val[0,0]*H_val[1,1] - H_val[0,1]^2             # TODO: compute discriminant
    fxx = H_val[0,0]               # TODO:
    print(f'At {cp}: D = {D_val}, f_xx = {fxx} →',
           'min' if D_val > 0 and fxx > 0 else
          'max' if D_val > 0 and fxx < 0 else
          'saddle' if D_val < 0 else 'inconclusive')

# 5. Directional derivative at (1,1) in direction u = (3/5, 4/5)
u = (3/5, 4/5)
u_ex2 = Matrix([Rational(3, 5), Rational(4, 5)])
grad_at_11 = simplify(grad_ex2.subs({x: 1, y: 1}))  # TODO: evaluate gradient at (1,1)
D_u_ex2 = grad_at_11.dot(u)     # TODO: dot product
print('D_u f(1,1) =', D_u_ex2)

f_ex3 = x * y * z
g_ex3 = x**2 + y**2 + z**2 - 3

# Build the system ∇f = λ∇g and g = 0
grad_f_ex3 = gradient(f_ex3, [x,y])   # TODO
grad_g_ex3 = gradient(g_ex3, [x,y])   # TODO
print(grad_f_ex3)
print(grad_g_ex3)
system_ex3 = [grad_f_ex3[0] - lam * grad_g_ex3[0],
grad_f_ex3[1] - lam * grad_g_ex3[1],  # TODO: 3 equations from ∇f = λ∇g
g_ex3,  # TODO: constraint g = 0
]
print(system_ex3)

sol_ex3 = solve(system_ex3, [x, y, z, lam])
print('Solutions:', sol_ex3)

# Evaluate f at each solution to find max and min
for s in sol_ex3:
    print(f'f{s[:3]} = {f_ex3.subs([(x,s[0]),(y,s[1]),(z,s[2])])}')
