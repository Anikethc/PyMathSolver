# Quadratic - PyMathSolver

# Imports
from termcolor import colored
import cmath

# Function - About
def definition():
    print(colored('\nA quadratic equation is an algebraic expression of the second degree in X.\n', 'green'))
    print(colored('The standard form is ax\u00b2 + bx + c = 0. A and B are the coefficients and X is the variable.\n', 'green'))
    print(colored('To find the roots of a Quadratic Equation, use the "findRoots()" function while entering the 3 values of a, b, and c respectively.\n', 'green'))

# Function - Find Roots
def findRoots(a, b, c):
    newA = float(a)
    newB = float(b)
    newC = float(c)

    discriminant = (b**2) - (4*a*c)

    alpha = (-b + cmath.sqrt(discriminant)) / (2*a)
    beta = (-b - cmath.sqrt(discriminant)) / (2*a)

    print(colored('\nThe roots of the equation is {0} and {1}.\n'.format(alpha, beta), 'green'))