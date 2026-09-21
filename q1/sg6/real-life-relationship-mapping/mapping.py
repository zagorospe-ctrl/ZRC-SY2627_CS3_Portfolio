class Student:

    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students += [student]
    
python = Course("CS 100")

student1 = Student("Mimi")
student2 = Student("Triple T. Sahur")
student3 = Student("Sam")


python.add_student(student1)
python.add_student(student2)
python.add_student(student3)

for student in python.students:
  print(student.name)
