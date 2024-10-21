mystr=input("Enter the string")
str=mystr.lower()
revstr=reversed(str)
if(list(str)==list(revstr)):
    print("it is a palindrom")
else:
    print("Not a palindrome")