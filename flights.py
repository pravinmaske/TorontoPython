def report_status(sst_time,est_time):
	'''
	Return the flight staus
	(Float,Float)-> str
	>>>report_status(14.3,14.3)
	'On Time'
	>>>report_status(14.3,11.2)
	'Early'
	>>>report_status(2.2,4.20)
	'Delayed'
	'''
	if sst_time == est_time:
		return 'Flight is on Time'
	elif sst_time > est_time:
		return 'Flight is Early'
	else:
		return 'Flight is delayed'

