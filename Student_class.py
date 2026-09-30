class Student:
    College_name="NCMT"
    def __init__(self, name, age, rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    
    def display(self,mark):
        if mark>50:
            print(f' My name is {self.name} from {self.College_name}, I am {self.age} and my roll no is {self.rollno}')
        else:
            print(f'{self.name}Sorry you are fail')
    @classmethod
    def updateCollege(cls,goldencollege):
         cls.College_name = goldencollege
    @staticmethod
    def Welcome():
        print("THis run no matter what")
    
st1=Student("Sujan", 21,20)
st1.display(55)
print(st1.College_name)

st2=Student("Pritamber", 20,9)
st2.display(55)
print(st2.College_name)

st2.College_name="budhalnilkantha"
print(st2.College_name)
print(st1.College_name)

Student.updateCollege("children ")
print(st1.College_name)
print(st2.College_name) #st2.College_name → still "Novel" because its instance attribute shadows the class variable.

st1.Welcome()
