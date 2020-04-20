import pickle
class Student:
    def __init__(self,id,name,score):
        self.id=id
        self.name=name
        self.score=score
    def displaystudent(self):
        print(self.id,self.name,self.score)