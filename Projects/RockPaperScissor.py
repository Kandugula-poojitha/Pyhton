import random
user_choice=int(input("Enter your choice 0 is for Rock , 1 is for Paper and 2 is for Scissor"))
if(user_choice>=3 or user_choice<0):
    print("YOu entered an INvalid nUmber")
else:
    computer_choice=random.randint(0,2)
    print(computer_choice)
    if(computer_choice==user_choice):
        print("Its Draw😛.........")
    if(user_choice==0 and computer_choice==2 ):
        print("You Win")
    elif(user_choice==2 and computer_choice==0):
        print("You Loss")
    elif(user_choice>computer_choice):
        print("You Win")
    elif(user_choice<computer_choice):
        print("YOu Loss")
