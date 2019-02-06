def convert_to_celcius(fahrenheit):
	""" (number) -> number
	Prints the number of celcius degrees equivalent to fahrenhit degrees
	
	>>>convert_to_celcius(32)
	0.0
	>>convert_to_celcius(32)
	100.0

	"""convert_to_celcius(32)
	#y = fahrenheit
	celcius = (fahrenheit -32) * 5 /9
	print('Temperature from ',fahrenheit,'fahrenheit to Temperature : ',celcius,'celcius')

if __name__ == '__main__':
	f= int(input("Please enter the temperature in fahernheit  "))
	convert_to_celcius(f)
