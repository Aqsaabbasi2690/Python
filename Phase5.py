  # exception handling means error handling
try:
 a = int(input("enter num:"))
 print(a+8)
except Exception as e:
    print("some errors:",e)




# fileI/O file data store  read or write or append  these three modes 


# writing a file mode
s = "aqsa is good girl and bad sometime."
#  context manager
with open("text.txt", "w") as f:     
    f.write(s)

# reading a file mode
s = "aqsa is good girl."
#  context manager
with open("text.txt", "r") as f:     
   s = f.read()
   print(s)


   # appending to a file mode use that all previous data remain save 
s = "aqsa is good girl and bad sometime."
#  context manager
with open("text.txt", "a") as f:     
    f.write("aqsa is good girl and bad sometimes.")






# Object oriented programming, classes ,methods, funtions, objects 

# classes
# (it is like a template which is used to make object e.g roilways blank form is class fill form is object) ,
# for different classes we which constructer, it is funtion which run automatically  when an object is created 


class Employee:
    # constructor function, self automatically pass. sekf is reference of object which this mehtod is call
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
     print(self.salary)


aqsa = Employee("Aqsa","233434")
print(aqsa.salary)
print(aqsa.name)
aqsa.getSalary()
    
harry = Employee("Harry","23234443434")
print(harry.salary)
print(harry.name)
harry.getSalary()