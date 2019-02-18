def compress_list(L):
    """
    >>>compress_list(['a','b','c','d'])
    ['ab', ['cd']]
    """
    compressed_list=[]
    i=0
    while i <len(L):
        compressed_list.append(L[i]+L[i+1])
        i=i+2
    return compressed_list
    
