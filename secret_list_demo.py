def secret(s):
    i=0
    result=''

    while s[i].isdigit():
        result=result+s[i]
        i+=1
    return result       
