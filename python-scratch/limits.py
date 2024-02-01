import numpy as np
import sympy as sp

def GFG(arr,prec):
    """Set better print options
    from: https://www.geeksforgeeks.org/print-a-numpy-array-without-scientific-notation-in-python/
    """
    np.set_printoptions(suppress=True,precision=prec)
    print(arr)

def make_limit_table(expr, symbol, limit):
	"""Build a limit table for expression with for the given symbol and limit"""
	limit_offsets = [-.1, -.01, -.001, 0, .001, .01, .1]
	table = np.zeros((len(limit_offsets), 2))
	for i, offset in enumerate(limit_offsets):
		x_val = limit + offset
		y_val = expr.subs(symbol, x_val)
		table[i] = [x_val, y_val]
  
	return table

