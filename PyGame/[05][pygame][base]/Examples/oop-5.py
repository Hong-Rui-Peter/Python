'''
OOP--示範程式-5[繼承]
'''

class People:
    def __init__(self,nation,name):
        self.nation=nation
        self.name=name
        
    def where(self):
        print(self.nation)
        
    def called(self):
        print(self.name)
        
    def bmi(self,weight,height):
        print(weight/(height/100)**2)
        

class Person(People):
    def __init__(self,nation,name,sex):
        self.nation=nation
        self.name=name
        self.sex=sex

    def gender(self):
        print(self.sex)
        
        
        
p1=Person("Taiwan","林照陽","M")
p2=Person("Korea","tzuyang","F")
 
p1.where()
p1.called()
p1.bmi(70,175)
p1.gender()

p2.where()
p2.called()
p2.gender()
p2.bmi(44,158)


 