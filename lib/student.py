#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, knowledge):
        self.knowledge.append(knowledge)


my_student = Student("Jerome", "Chauncey")
my_student.learn("Python")

for k in my_student.get_knowledge():
    print(f"{my_student.first_name} {my_student.last_name} learnt {k}")