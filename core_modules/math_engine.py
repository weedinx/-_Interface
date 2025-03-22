
from sympy import symbols, Eq, solve

def solve_equation(expr: str):
    x = symbols('x')
    eq = Eq(eval(expr), 0)
    return solve(eq)
