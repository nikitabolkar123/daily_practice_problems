iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

lst = [1, 2, 3, 4, 5]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

# raise an error bcoz extra ele

lst = [1, 2, 3, 4, 5]
it = iter(lst)
while True:
    try:
        print(next(it))
    except Exception as e:
        break


# generator---are a funcion that returns a sequence of a value. we use yield statement to return value of function

# yield:--- statement returns elements from a generator function into a generator object
# next---used to retrieve elements by elements from a generator object e.g next(gen_obj)

def display(a, b):
    yield a
    yield b


res = display(3, 4)
print(res)
print(type(res))
lst = list(res)
print(lst)
print(type(lst))


def show(a, b):
    while a <= b:
        yield a
        a += 1


res = show(1, 5)
print(list(res))
# print(type(res))
print(next(res))

# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
# is not part of haystack.
