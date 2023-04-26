# keeps a counter to iterable to
# [val1,val2,val3]
# [(counter1,value1,counter2,value2,counter3,value3)]
# Python program to illustrate
# syntax of enumerate()
# enumerate(iterable,[start=0])
# iterable:--- any object that support iteration e.g list,tuple,dict,string
# start:--starting point of counter
# enumerate function
import json

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

sports = ['criket', 'kabbadi', 'tennis', 'football']
for pos, ele in enumerate(sports):
    print(f"{pos}:{ele}")
# conversion  into dictionary
sports = ['criket', 'kabbadi', 'tennis', 'football']
print(list(enumerate(sports,1))) # list gives u list of tuple [(1, 'criket'), (2, 'kabbadi'), (3, 'tennis'), (4,
# 'football')]
print(dict(list(enumerate(sports,1))))

sports = ['criket', 'kabbadi', 'tennis', 'football']
data=dict(list(enumerate(sports,1)))
f=open('data.json','w')
json.dump(data,f)
f.close()

