class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self,name,age,roll_no,course):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.course = course
    def display_student_info(self):
        print(f"--- Student Info ---")
        self.display_info()
        print(f"Roll no : {self.roll_no}")
        print(f"Course : {self.course}")

class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)
        self.salary = salary
        self.subject = subject
    def display_teacher_info(self):
        print(f"--- Teacher Info ---")
        self.display_info()
        print(f"Salary : {self.salary}")
        print(f"Subject : {self.subject}")

p1 = Student("Shayan",23,21106,"Computer-Science")
p2 = Teacher("Sidra-Rehman",30,1250000,"OOP")
p3  = Student("ali",21,21107,"BBA")
p4 = Teacher("Aruba",29,120000,"OOP-LAB")

p1.display_student_info()
p2.display_teacher_info()
p3.display_student_info()
p4.display_teacher_info()