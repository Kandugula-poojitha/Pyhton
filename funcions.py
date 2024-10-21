
"""
def fun_name():
    print("heloo")
fun_name()

def fun_name1(name):
    print("Heyyy my name is " +name)
fun_name1("Pooojittha")

def greek():
    print("haii ramm")
    print("are you from cs department")
greek()

def pooja(name):
    print(f"Haii{name}")
    print("ARe you form cd department")
pooja('ram')
pooja('kavi')
pooja('ravi')

def add(a,b):
    c=a+b
    print(c)
add(10,35)

def add(*numbers):
  c=0
  for i in numbers:
    c=c+i
  print(c)
add(2,3,4,5,6)
add(6,5,8,8)
add(9,0,8,7,6)
"""
def add(name,age,fruit,*numbers):
    print(name,age,fruit,numbers)

add("pooja",35,["apple","banana","grape"],46,5475,76578)

def add(**kwargs):
    print(kwargs)
add(name="poojitha",age="45")




 