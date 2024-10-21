"""
import random
names=input("Enter your name")
split_names=names.split(" ")
print(split_names)
bill_pay=random.choice(split_names)
print(f"{bill_pay} will pay the bill")i
"""
import random
names=input("Enter your names")
split_names=names.split(" ")
print(split_names)
length=len(split_names)
print(length)
bill_pay=random.randint(0,length-1)
print(f"{split_names[bill_pay]} will pay the bill")
