def print_every_third_char(s):
	"""
	(str)--> str
	Returns every third character of string
	>>>print_every_third_char('abcABCabcABC')
	a
	A
	a
	A
	"""

	for i in range(0,len(s),3):
		#print(s[i])
		print(s[i:i+1])
