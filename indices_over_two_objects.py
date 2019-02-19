def count_matches(s1,s2):
	"""
	Return the number of positions in s1 that contains the same character
	at the corresponding position of s2.

	Precondition: len(s1) == len(s2)

	>>>count_matches('ate','ape')
	2
	>>>count_matches('head','hard')
	2
	"""
	count_match=0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			count_match+=1
	return count_match
def sum_items(list1,list2):
	"""
	(list of number, list of number) -> list of number
	Return a new list in which each item is the sum of the items at 
	the corrosponding position of list1 and list2

	>>>sum_items([1,2,3],[2,4,5])
	[3,6,8]
	>>>sum_items([2,3,1],[3,2,1])
	[5,5,2]
	"""

	sum_items=[]

	for i in range(len(list1)):
		#sum_items[i]=list1[i]+list2[i]
		sum_items.append(list1[i]+list2[i])
	return sum_items

print(sum_items([1,2,3],[2,4,5]))
print(count_matches('headi','hardi'))