from Person import *
class Student(Person):
    def __init__(self,name,age,gender,score):
        super().__init__(name,age)
        self.gender = gender
        self.score = score
        
   
    def infoo(self):
        mystr = super().info()
        return mystr + ", gender:" +self.gender+ ", score:"+ str(self.score)
