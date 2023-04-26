def reverse(str):
    if len(str)==1:
        return str
    else:
        return reverse(str[1:]) + str[0]


str=input('enter the string')
str2=reverse(str)
print("reverse string is",str2)