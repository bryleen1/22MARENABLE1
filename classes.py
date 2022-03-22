"""
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "age"))
"""

class Students:
    def __init__(self, name, age, _class="student"):
        self.name = name
        self.age = age
        self._class = _class

    def score(self):
        mark = int(input("Enter your mark "))
        if mark > 85:
            print(f"{self.name} is {self.age} years old in the {self._class} class. {self.name}'s score is a Distinction")
        elif mark >=65:
            print(f"{self.name} is {self.age} years old in the {self._class} class. {self.name}'s score is a Pass")
        else:
            print(f"{self.name} is {self.age} years old in the {self._class} class. {self.name}'s score is a Fail")

    def __repr__(self):
        return f"{self.name} is {self.age} years old in the {self._class} class."

student1 = Students("John", 12)
student1.score()
print(student1)