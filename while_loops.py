def up_to_vowel(s):
	'''
	(str) -> str
	Return a substring of s from index 0 up to but not including the first vowel in s.
	
	>>>up_to_vowel('hello')
	'h'
	>>>up_to_vowel('there')
	'th'
	>>>up_to_vowel('cs')
	'cs'

	'''
	before_vowel=''
	i=0
	while i <len(s) and not (s[i] in 'aeiouAEIOU'):
		before_vowel= before_vowel+ s[i]
		i+=1
	return before_vowel
