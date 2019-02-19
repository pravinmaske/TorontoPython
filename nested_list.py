def calculate_average(asn_grades):
	"""
	(list of list of(number,str))-> float
	Return the average of the grades in asn_grades.
	>>>calculate_average(['A1',80],[A2,90])
	85.0
	"""

	total=0

	for item in asn_grades:
		total+=item[1]
	return total / len(asn_grades)	

print(calculate_average([['A1',80.0],['A2',90.0]]))
