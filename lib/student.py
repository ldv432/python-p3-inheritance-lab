#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(first_name, last_name)
        self.knowledge = [""]

    def learn(self, learned_knowledge=None):
        if learned_knowledge:
            self.knowledge.append(learned_knowledge)