'''
OOP示範程式-2
'''
class Score:
    def __init__(self, chinese=None, english = None, math=None):
        self.chinese = chinese
        self.english = english
        self.math = math
    
    def calculateAverage(self):
        count = 0
        scoreSum = 0
        if self.chinese != None:
            count += 1
            scoreSum += self.chinese
        if self.english != None:
            count += 1
            scoreSum += self.english
        if self.math != None:
            count += 1
            scoreSum += self.math
        if count !=0:
            return scoreSum/count
        else:
            return None
        
class Student:
    def __init__(self,name, id,chinese =None, english = None, math=None):
        #put attribute here
        self.name = name
        self.__id = id
        self.score = Score(chinese,english,math)
        
    def getId(self):
        return self.__id
    
    def getAverage(self):
        avg = self.score.calculateAverage()
        if avg != None:
            return avg
        else:
            return 'No score.'

studA = Student(name='Scott',id=123, chinese = 60, math=100)
studB = Student(name='Peter',id=456,english=70, math=80)
print(studA.name, studA.getId(),studA.getAverage())
print(studB.name, studB.getId(),studB.getAverage())

        