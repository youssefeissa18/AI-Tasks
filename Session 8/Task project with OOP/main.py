class person:
    counter = 0
    def __init__(self, name, nationalID):
        self.name = name
        self.nationalID = nationalID
        self.counter += 1

    def printinfoperson(self):
        return f"{self.counter}-Name: {self.name}\tnationalID: {self.nationalID}"


class Student(person):
    counter = 0
    def __init__(self, name, nationalID, Gpa, ID):
        super().__init__(name,nationalID)
        self.Gpa = Gpa
        self.ID = ID
        self.counter += 1
    def printinfoperson(self):
        return f"{str(self.counter)}-Name: {self.name}\tnationalID: {self.nationalID}\tGPA: {str(self.Gpa)}\tID: {str(self.ID)}"


class Teacher(person):
    counter = 0
    def __init__(self, name, nationalID, salary, ID):
        super().__init__(name,nationalID)
        self.salary = salary
        self.ID = ID
        self.counter += 1
    def printinfoperson(self):
        return f"{str(self.counter)}-Name: {self.name}\tnationalID: {self.nationalID}\tGPA: {str(self.salary)}\tID: {str(self.ID)}"


class UNI:

    def __init__(self):
        self.name = input("Enter the name: ")
        self.students = []
        self.teachers = []

    def addstudent(self, student):
        self.students.append(student)
        print(f"Student {self.name} add Successfully ")

    def addteacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {self.name} add Successfully ")

    def removestudent(self, student):
        self.students.remove(student)
        print(f"Student {self.name} remove Successfully ")

    def removeteacher(self, teacher):
        self.teachers.remove(teacher)
        print(f"Teacher {self.name} remove Successfully ")

    def display_students(self):
        print(f"Students at {self.name}:")
        for student in self.students:
            print(student)

    def display_teachers(self):
        print(f"Teachers at {self.name}:")
        for teacher in self.teachers:
            print(teacher)

    def display_university_info(self):
        print(f"University: {self.name}")
        print("===========")
        self.display_students()
        self.display_teachers()

