def merge(L):
    merged=[]
    for i in range(0,len(L),3):
        merged.append(L[i]+L[i+1]+L[i+2])
    return merged

print(merge([1,2,3,4,5,6,7,8,9]))


def mystery(s):

    matches = 0
    for i in range(len(s)//2):
        if s[i] == s[len(s)-1-i]:
            matches+=1
            print(matches)
    return matches == (len(s)//2)

print(mystery('civil'))



def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item
    return L
L=[1,2,3,4,5]    
print(shift_right(L))
