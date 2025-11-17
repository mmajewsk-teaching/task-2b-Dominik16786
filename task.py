# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


class Diary:
    def __init__(self, subject):
        self.subject = subject

    def average(subject):
        avg = 0
        for grade in self.subject.grades:
            score = score + grade
        x = len(self.subject.grades)
        avg = avg / x
        return avg
        
    

class Subject:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


if __name__ == "main":
    grades = [1,2,3,5]
    subject_1 = Subject("History", grades)
    diary = Diary(subject_1)
    print(diary.average())