import calendar as cl
from getpass import getpass
import getch


#task 1
print("----------------------------------Task1---------------------------\n")
num = int(input("Enter The Number\n"))
if num < 0:
    print("The positive number is :- ", abs(num), end=" ")
else:
    print("This number is already Positive: ")


#--------------------------------------------------------------------------------------
#task 2
print("----------------------------------Task2---------------------------\n")
year = int(input("Enter the number of year\n"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# another solution by import Calender lib (Has a built in function the make this problem without any code)
years = int(input("Enter the number of year\n"))
check = cl.isleap(years)
if check:
    print("Leap Year")
else:
    print("Not Leap Year")

#---------------------------------------------------------------------------------------
#task 3
print("----------------------------------Task3---------------------------\n")
Age1 = int(input("Enter The Age for person one\n"))
Age2 = int(input("Enter The Age for person two\n"))
Age3 = int(input("Enter The Age for person three\n"))

old = Age1
young = Age1
if Age2 > old:
    old = Age2
if Age3 > old:
    old = Age3
if Age2 < young:
    young = Age2
if Age3 < young:
    young = Age3
print("oldest : ", old, "Youngest : ", young)

# another solution
oldest = max(Age1, Age2, Age3)
youngest = min(Age1, Age2, Age3)
print("oldest : ", oldest, "Youngest : ", youngest)

#   another solution
if Age1 > Age2 and Age1 > Age3 and Age3 > Age2: # old 1 young 2
    print("oldest : ", Age1, "Youngest : ", Age2, end=" ")
elif Age1 > Age2 and Age1 > Age3 and Age3 < Age2: # old 1 young 2
    print("oldest : ", Age1, "Youngest : ", Age3, end=" ")
elif Age2 > Age1 and Age2 > Age3 and Age1 > Age3: # old 2 youg 3
    print("oldest : ", Age2, "Youngest : ", Age3, end=" ")
elif Age2 > Age1 and Age2 > Age3 and Age1 < Age3: # old 2 youg 3
    print("oldest : ", Age2, "Youngest : ", Age1, end=" ")
elif Age3 > Age1 and Age3 > Age2 and Age1 < Age2: #old 3 young 1
    print("oldest : ", Age3, "Youngest : ", Age1, end=" ")
elif Age3 > Age1 and Age3 > Age2 and Age1 > Age2: #old 3 young 1
    print("oldest : ", Age3, "Youngest : ", Age2, end=" ")

#---------------------------------------------------------------------------------------
# task 4
# we have somthing as getpass this make password hidden from visible
# and we have another thing and this is getch use to when enter any word that appear as star but this refused to installion in my PC
# and we have another thing and this is Mask
print("----------------------------------Task4---------------------------\n")
password = ""
while True:
    symbol = getch.getch()
    if symbol == "\n" or symbol == "\r":
        break
    print("*",end="",flush=True)
    password += symbol

print("Password",password)

#this solution does not work
password = getpass("Enter your password: ")

print("Password entered:", password)