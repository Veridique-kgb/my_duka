class Student:
    def __init__(self,name,student_no,course):
        self.name=name
        self.student_no=student_no
        self.course=course

    def study(self,unit):
        print(f"{self.name} studies {unit}")

    def do_exam(self,course):
        print(f"{self.name} does {course} exam ")

    def attent_class(self,time):
        print(f"{self.name} attends class {time}")

    def get_details(self):
        print(f"name:{self.name} -student_no:{self.student_no} -course:{self.course}")
        print("---------------------------------------------------------------------")

# object1

student1=Student("John","S101","Programming")

print(type(student1))
print(student1)
student1.get_details()
student1.study("OOP")
student1.do_exam("Python")
student1.attent_class("at 11am")

# object2
student2=Student("Jack","S102","Math")

print(type(student2))
print(student2)
student2.get_details()
student2.study("Algebra")
student2.do_exam("basic algebra")
student2.attent_class("at 7am")

