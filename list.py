
"""
roll_no=[1,2,3,4,5,5,6,7,8]
multiple=[1,2,0.000,0.000,-343,-343, "Poojitha", "Haii"]
print(roll_no[2:9])
print(multiple[2])
print(multiple[2:6])
print(multiple[3])
print(multiple[-1])
#print(multiple[11])       #IndexError
print(multiple[:])
print(multiple[2:])
print(multiple[:7])
print(max(roll_no))
print(min(roll_no))
print((roll_no))
multiple.insert(3,6)
print(multiple)
multiple.extend([34,00000,999999,88888888,666666666])
print(multiple)
multiple[2:7]={78,90,45,345}
print(multiple)
print(len(roll_no))



names=["Poojitha","kandugula","pooja","JOy","happy"]
print(len(names))
print(f"Hello{names[3]}")
print(f"haii{names[len(names)-1]}")


##########################
#Nested List
num=[23,89,90,45,[23,45,67],76,97]
print(num)
print(num[3])
print(num[4])
print(num[4][0])
print("Length of the num is: " ,len(num))

print(num[-3])

print(num[len(num)-1]) 
print(num[len(num)-3])


print(num[:]) #########Slicing
print(num[4][:])
"""
list=[23,34,['Mohan','kathi'], 34,78,90 ]
print(list[2][0])
print(len(list))