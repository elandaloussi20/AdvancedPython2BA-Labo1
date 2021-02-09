# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

import cmath

def fact(n):
	if n == 0:
		return 1
	else:
		F = 1
		for k in range (2, n+1):
			F = F*k
		return F
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	pass

def roots(a, b, c):
	d = (b**2) - (4*a*c)
	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)
	print('The solution are {0} and {1}'.format(sol1,sol2))

	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	pass

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))


import unittest
import utils
class Test(unittest.TestCase):
	def test_compute ( self ):
		self . assertEqual (utils.fact(5) , 5)
		
suite = unittest . TestLoader () . loadTestsFromTestCase ( Test )
runner = unittest . TextTestRunner ()
print ( runner . run( suite ))


		
