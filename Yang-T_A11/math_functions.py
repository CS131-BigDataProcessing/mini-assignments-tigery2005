def power(b, e):
	if b == 0 and e == 0:
		return 1
	if b == 0 and e < 0:
		raise ValueError("0 cannot be raised to negative exponent")
	if e == 0:
		return 1
	return b ** e

def divide(n, d):
	if d == 0:
		raise ValueError("Cannot divide by 0")
		
	return n/d
