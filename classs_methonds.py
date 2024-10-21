
"""
class Name:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
        #self.followers=0
        self.age=23

    def display(self,sub):
        self.sub=sub
        print(f"Haii, im {Name1.name}")
        print(f"Haii, im {self.name}, iam interested in codig {self.sub}")
Name1=Name("Poojtha","Pasaragonda")
print(Name1.name)
Name2=Name("Poojtha1","Pasaragonda1")
print(Name2.name)
print(Name2.followers)
print(Name1.age)
Name1.display("python")

class Haii:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print(self.name)
H=Haii("Poojitha",23)
H.func()




class pooja:
    def __init__(myobject,name,age):
        myobject.name=name
        myobject.age=age
    def myfunc(abc):
        print(abc.name)
        print(abc.age)
    
Poojitha=pooja("Poojitha",23)
Poojitha.myfunc()
       """


class Sravanthi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print(f"Haii my name is {self.name}")
class Pooja(Sravanthi):
    def __init__(self,name,age):  
        Sravanthi().__init__(name,age)
sravanthi1=Sravanthi("Rajitha",23)
sravanthi1.myfun()
       
     

        