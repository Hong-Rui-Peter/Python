'''
OOP--示範程式-4[方法(Method)]
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
        
p1=People("Taiwan","林照陽")
p2=People("Korea","tzuyang")
 
p1.where()
p1.called()
p1.bmi(70,175)

p2.where()
p2.called()
p2.bmi(44,158)

 