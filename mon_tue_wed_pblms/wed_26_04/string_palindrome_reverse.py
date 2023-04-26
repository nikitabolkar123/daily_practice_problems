number = int(input('enter the number'))
string = str(number)
reverse_str = string[::-1]
print('reversed:', reverse_str)
if string == reverse_str:
    print('string pallindrome')
else:
    print('string not pallindrome')
