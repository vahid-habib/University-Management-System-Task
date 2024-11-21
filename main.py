class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def set_details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_details(self):
        print(f"Name: [{self.name}], Age: [{self.age}], Gender: [{self.gender}]")

class Student(Person):
    def __init__(self,name,age,gender,studentID,course):
        super().__init__(name,age,gender)
        self.studentID = studentID
        self.course = course
        self.grades= []
    def set_student_details(self,course,studentID):
        self.course = course
        self.studentID = studentID

    def add_grade(self,grade):
        self.grades.append(grade)
    
    def calculate_average_grade(self):
        if len(self.grades) > 0:
            self.avg = sum(self.grades)/ len(self.grades)
        else:
            self.avg = 0

    def get_student_summary(self):
        print(f"Name: [{self.name}], Age: [{self.age}], Gender: [{self.gender}], Student ID: [{self.studentID}, Course: [{self.course}, Average Grade: [{self.avg}]")
    #Extension Task

    def get_mentor(self,Professor):
        if Professor.mentee == self.name:
            print(f"{self.name} is being mentored by {Professor.name}")
        pass
class Professor(Person):
    def __init__(self,name,age,gender,staffID,department,salary):
        super().__init__(name,age,gender)
        self.staffID = staffID
        self.department = department
        self.salary = salary
        self.mentee = []
        

    def set_professor_details(self,staffID,department,salary):
        self.staffID = staffID
        self.department = department
        self.salary = salary
    
    def give_feedback(self,student,feedback):
        print(f"Feedback for {student.name}: {feedback}")
    
    def increase_salary(self,percentage):
        self.salary *= (1+int(percentage)/100)
    def get_professor_summary(self):
        print(f"Name: [{self.name}], Age: [{self.age}], Gender: [{self.gender}], Staff ID: [{self.staffID}, Department: [{self.department}, Salary: [{self.salary}]")

    # Extension Task

    def mentor_student(self,Student):
        self.mentee.append(Student.name)
        print(f"Professor {self.name} is now mentoring Student {Student.name} on {Student.course}.")
    def get_mentored_students(self):
        print(f"{self.name} is mentoring {self.mentee}")

class Administrator(Person):
    def __init__(self,name,age,gender,adminID,office,yearsOfService):
        super().__init__(name,age,gender)
        self.adminID = adminID
        self.office = office
        self.yearsOfService = yearsOfService
    
    def set_admin_details(self,adminID,office,yearsOfService):
        self.adminID = adminID
        self.office = office
        self.yearsOfService = yearsOfService

    def increment_service_years(self):
        self.yearsOfService += 1
    
    def get_admin_summary(self):
        print(f"Name: [{self.name}], Age: [{self.age}], Gender: [{self.gender}], Admin ID: [{self.adminID}, Office: [{self.office}, Years Of Service: [{self.yearsOfService}]")



vahid = Student("Vahid",16, "Male","S1234","Computer Science")
daniel = Student("Daniel", 16, "Male","S1235","Computer Science")

mahdi = Professor("Mahdi", 20 ,"Male","P1234","Computer Science",100000)
walkden = Professor("Walkden", 58 ,"Male","P1235","Computer Science",10000)

admin = Administrator("admin", 8, "Female","A1234","LAET",12)

vahid.add_grade(9)
vahid.add_grade(8)
vahid.add_grade(7)
vahid.add_grade(7)
vahid.add_grade(4)
vahid.calculate_average_grade()

mahdi.give_feedback(vahid,"Wow. This is a great piece of code. Keep it Up!!")
mahdi.increase_salary(10)
mahdi.get_professor_summary()

admin.get_admin_summary()
admin.increment_service_years()
admin.get_admin_summary()



