class Person:
    counter = 0

    def __init__(self, name, nationalID):
        self.name = name
        self.nationalID = nationalID
        Person.counter += 1
        self.ID = Person.counter

    def print_info_person(self):
        return f"ID: {self.ID} - Name: {self.name}\tNationalID: {self.nationalID}"


class Student(Person):
    def __init__(self, name, nationalID, Gpa, ID):
        super().__init__(name, nationalID)
        self.Gpa = Gpa
        self.ID = ID


class Teacher(Person):
    def __init__(self, name, nationalID, salary, ID):
        super().__init__(name, nationalID)
        self.salary = salary
        self.ID = ID


class UNI:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully to {self.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added successfully to {self.name}")

    def remove_student(self, student):
        self.students.remove(student)
        print(f"Student {student.name} removed successfully from {self.name}")

    def remove_teacher(self, teacher):
        self.teachers.remove(teacher)
        print(f"Teacher {teacher.name} removed successfully from {self.name}")

    def display_students(self):
        print(f"Students at {self.name}:")
        for student in self.students:
            print(student.print_info_person())

    def display_teachers(self):
        print(f"Teachers at {self.name}:")
        for teacher in self.teachers:
            print(teacher.print_info_person())

    def display_university_info(self):
        print(f"University: {self.name}")
        print("===========")
        self.display_students()
        self.display_teachers()

print("--------------------------------------- FCAI ---------------------------------------------------")

uni = UNI("FCAI")

while True:
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Display University Info")
    print("4. Remove Student")
    print("5. Remove Teacher")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        nationalID = input("Enter student national ID: ")
        gpa = float(input("Enter student GPA: "))
        student_id = int(input("Enter student ID: "))
        student = Student(name, nationalID, gpa, student_id)
        uni.add_student(student)
    elif choice == '2':
        name = input("Enter teacher name: ")
        nationalID = input("Enter teacher national ID: ")
        salary = float(input("Enter teacher salary: "))
        teacher_id = int(input("Enter teacher ID: "))
        teacher = Teacher(name, nationalID, salary, teacher_id)
        uni.add_teacher(teacher)
    elif choice == '3':
        uni.display_university_info()
    elif choice == '4':
        student_id = int(input("Enter student ID to remove: "))
        for student in uni.students:
            if student.ID == student_id:
                uni.remove_student(student)
                break
        else:
            print("Student not found.")
    elif choice == '5':
        teacher_id = int(input("Enter teacher ID to remove: "))
        for teacher in uni.teachers:
            if teacher.ID == teacher_id:
                uni.remove_teacher(teacher)
                break
        else:
            print("Teacher not found.")
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
