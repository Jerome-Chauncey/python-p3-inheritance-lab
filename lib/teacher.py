#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Javascript", "C", "Python", "CSS"]

    def teach(self):
        return random.choice(self.knowledge)
        # return self.knowledge[0]
    

teacher = Teacher("Stella", "Margy")
print(f"{teacher.first_name} {teacher.last_name} teaches: {teacher.teach()}")
# print(teacher.teach())
        