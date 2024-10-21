#How many days weeks and months left if we live 90 years old 
#input current age
#output you have 2 days, b weeks and c months

"""
age=int(input("Enter your age"))
years_left=90-age
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52
print(f" no.of days left are {days_left},no. of months left are {months_left} and no. of years left are {years_left}" )


#############################################


#2....
#Check whether given number is even or odd

number=int(input("Enter your number"))
if(number%2==0):
    print(f"Entered number  {number}  is even")
else:
    print(f" Enterd {number} is odd number")

#########################
    
#Nested if _____________if inside if
citizen=input("Enter your citizen   "  )
#age=int(input("enter your age   " ))
if(citizen=="india"):
    age=int(input("enter your age   " ))
    print("your citizen is iNdia")
    if(age>=18):
        print("you are eligible")
    else:
        print("You are not eligible to vote")
else:
    print("you are not the indian to participate in voting")


##################################

#check height if eligible check age and if requires coffee add bill +50

height=int(input("Enter your height"))
bill=0
if(height>=3):
    print("can ride")
    age=int(input("Enter your age"))
    if(age<18):
        bill=100
        print("your prise is 100")
    elif(age<20):
        bill=200
        print("your price is 200")
    else:
        bill=500
        print("your price is 500")
    coffee=input("Do you want to have Coffee(Y/N)")
    if(coffee=="Y" or coffee=="y"):
        print(f"your bill is {bill}+50",bill+50 )
        
else:
    print("cant ride")

    
    """

pizza=input("Enter your size if Pizza S/M/L")
bill=0
if(pizza=='S'):
    bill=200
    print("your bill is 200")
elif(pizza=='M'):
    bill=300
    print("your bill is 300")
else:
    bill=500
    print("your bill is 500")
papperone=input("Do you want papperone Y/N")
if(papperone=='Y' or papperone=='y'):
    if(pizza=='S'):
        bill=bill+20
        print(f"your bill is {bill}")
    elif(pizza=='m' or pizza=='M'):
        bill=bill+50
        print(f"your bill is {bill}")
    else:
        bill=bill+80
        print(f"your bill is {bill}")
    cheese=input("DO you want extra cheese Y/N")
    if(cheese=='Y' or cheese=='y'):
        bill=bill+50
    print(f"your tottal bill is {bill}")
