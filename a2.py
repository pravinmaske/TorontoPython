def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
	"""
	(str) -> bool
	
	Return True if and only if the DNA sequence is valid(i.e. it contains no characters other than 'A','C','T' and 'G')

	>>>is_valid_sequence('AGCTA')
	True

	>>>is_valid_sequence('AFHDTC')
	False

	>>>is_valid_sequence('dasdACT')

	False
	"""
	#return dna in 'AGTC'

	
	sequence='AGTC'
	var=True
	for char in dna:
		if char not in sequence:
			var= False

	return var
		#if not sequence.find(char)
		#	var= False


def insert_sequence(dna1,dna2,index):
    """
    (str,str,int) -> str
    Returns the DNA sequence obtained by inserting the second into the
    first DNA sequence at the given index

    >>>insert_sequence(CCGG,AT,2)
    'CCATGG'
    >>>insert_sequence(CTAGG,TT,3)
    'CTATTGG'
    ''
    """
    return dna1[:index]+dna2+dna1[index:]
    
def get_complement(str1):
    """
    (str)->str

    Returns the nucleotide's complement.

    >>>get_complement('ACGTACG')
    'TGCATGC'
    >>>get_complement('AAATTTGGGCCC')
    'TTTAAACCCGGG'

    """

    '''  if not is_valid_sequence(str1):
        return False

    if not get_length(str1) == 1:
        return False
    '''
    str2=''
    for char in str1:
        if char =='T':
            str2=str2+'A'
        elif char =='A':
            str2=str2+'T'
        elif char =='C':
            str2=str2+'G'
        elif char =='G':
            str2=str2+'C'
    return str2


def get_complementary_sequence(dna):
    if not is_valid_sequence(dna):
        return False
    out=''
    for char in dna:
        out= out+ get_complement(char)

    return out
