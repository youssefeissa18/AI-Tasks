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

name = input("Enter your name: ")
nationalID = input("Enter your NationalID : ")
gpa = float(input("Enter Your Gpa: "))
id1 = int(input("Enter Your ID: "))
p1 = person(name, nationalID)
print(p1.printinfoperson())
S1 = Student(name, nationalID, gpa, id1)
print(S1.printinfoperson())
salary = float(input("enter your salary: "))
S1 = Teacher(name, nationalID, salary, id1)
print(S1.printinfoperson())
