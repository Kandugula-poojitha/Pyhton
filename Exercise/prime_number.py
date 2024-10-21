
"""
num=int(input("Enter your number: "))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print(f"{num} is prime number")
            break
        else:
            print(f"{num} is not an prime number")
else:
    print("You have enterd an invalid number")
"""

"""
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

    """

num=int(input("Enter your number:"))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("its not a prime number")
            break
    else:
         print("its  a prime number")
else:
    print("YOu have entered an invalid number")
    
