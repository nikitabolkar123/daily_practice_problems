# Write a Python program to add two strings as if they were numbers (positive integer values). Return a message if
# the numbers are strings. Go to the editor Sample Output: 42 Error in input! Error in input!
def test(n1, n2):
    n1, n2 = '0' + n1, '0' + n2
    if n1.isnumeric() and n2.isnumeric():
        return str(int(n1) + int(n2))
    else:
        return 'Error in input!'


print(test("10", "32"))
print(test("10", "22.6"))
print(test("100", "-200"))
