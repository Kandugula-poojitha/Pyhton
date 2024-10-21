"""
tuple1=(12,6,-8,'jenny',True)
tuple2=(34,)
tuple3=(34)
print(tuple1[1])
print(tuple1[-1])
print(type(tuple2))
print(type(tuple3))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


name=("Haii","Hello","Good")
name1=list(name)
name1[1]="Joy"
name=name1
print(name)

name=("haiii","hello","Pooja")
for i in name:
    print(i)
"""
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
