'''
OOP示範程式-1
'''

class Circle:
    PI = 3.14
    def __init__(self, r=1):
        self.radius = r
 
    def getArea(self):
        return self.PI * self.radius * self.radius
    
    
C1 = Circle()
print("半徑為", C1.radius, "的圓面積為", C1.getArea()) #利用變數存取類別中的變數
C2 = Circle(7)
print("半徑為", C2.radius, "的圓面積為", C2.getArea())