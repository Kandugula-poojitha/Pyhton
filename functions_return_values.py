

"""
def add(a,b):
    c=a+b
    return c
print(add(3,5))


def add(a,b):
    c=a+b
    return c
value=(add(3,5))
print(value)

def add(a,b):
    return a+b
    
valus=(add(3,5))
print(valus)


def format_name(fname,lname):
    a=fname.title()
    b=lname.title()
    c=a+b
    print(f"{a} {b}")
format_name("poojitha","kanduguala")
"""

####################################################################   multi values

"""
import statistics
def mean_median_mode(list1):
    #return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    
print(mean_median_mode([2,3,4,5,6,7,8,9]))
value=(mean_median_mode([2,3,4,5,6,7,8,9]))
a,b,c=(mean_median_mode([2,3,4,5,6,7,8,9]))
print(f"mean is{a},\nmedian is {b},\nmode is {c}")
print(value)

"""

def add(a,b):
    if(a==0 & b==0):
        return
    else:
        return a+b
var1=int(input("Enter you nymber"))
var2=int(input("Ente 2nd number"))
result=add(var1,var2)
print(result)


