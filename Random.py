import random

a=random.randint(1,9)
b=random.randrange(2,8)
c=['hai','heloo',34,89,'super']
c1=random.choice(c)

print(a,b,c1)
print(random.choices(c,k=3))
c2=random.choices(c,k=15)
print(c2)

shuffle=random.shuffle(c)
print(shuffle)


Names=["Poojitha", "Dev","HeYyy","Gemini","sidh","gentle"]
random.shuffle(Names)
print(Names)
