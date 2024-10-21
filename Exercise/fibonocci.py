terms=int(input("Enter your number of terms "))
#n1=0
#n2=1
#count=0
if(terms==0):
    print("Enter a positive number")
if(terms==1):
    print(f"fibonoccies of {terms} is {terms}")
else:
    
   print(f"Fibonacci sequence of {terms}:")
   n1=0
   n2=1
   count=0
while(count<terms):
  
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1