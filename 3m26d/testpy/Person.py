class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        return "my name:"+ self.name +" , my age:"+ str(self.age)
        