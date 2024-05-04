'''
OOP--示範程式-3[類別+物件+屬性]
'''

class People:
    def __init__(self,nation,name):
        self.nation=nation
        self.name=name
        
p1=People("Taiwan","林照陽")
p2=People("Korea","tzuyang")
 
print(People,"類別(Class)")       
print(p1,"物件(Object)") 
print(p2.nation,"屬性(attribute)")        
print(p2.name,"屬性(attribute)")        
 