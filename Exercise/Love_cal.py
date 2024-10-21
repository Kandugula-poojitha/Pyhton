name1=input("Enter your name")
name2=input("Enter name2")
name=name1+name2
lower_case=name.lower()
print(lower_case)
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')
love=l+o+v+e
true_love=str(true)+str(love)
print(true_love)

if( int(true_love)<10 or int(true_love)>90):
    print(f"your love score is{ture_love}, you go together like coke and mentos")
elif(int(true_love)>=40 and int(true_love)<=60):
    print(f"your love score is {true_love}, your love is good and balanced")
else:
    print("your love score is ", true_love)

