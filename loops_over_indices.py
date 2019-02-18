def shift_left(L):

	"""
	(list)->NontType
	Shifts each item in L one position to the left and shift first element to the last position 
	"""
	first_item=L[0]

	for i in range(1,len(L)):
		L[i-1]=L[i]
	L[-1]=first_item
	print(L)	

shift_left(['a','b','c','d','e'])
def count_adjacent_repeates(s):

	"""
	(str)-> int
	Returns the number of occurences of a character and an adjacent character being the same.

	>>>count_adjacent_repeates('abccdeffggh')
	3
	"""

	repeates=0

	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			repeates+=1
	return repeates		

print(count_adjacent_repeates('abccdeffggh'))