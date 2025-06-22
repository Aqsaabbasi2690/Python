# tuples
t = (23,34,445,545, 34)
print(t.count(34))



# sets

a1 = {3,4,5,67,6755,343}
a2 = {3,4 , 4,5,6,}
print(a1.union(a2)) 
print(a1)
print(a2)
#  unio means add a1 elements to a2 and in the place of union, intersection means common numbers

# empty set
a = {}
b = set()
print(a, type(a ))
print(b, type(b))


# dic key value pairs aqsa : 23 aqsa is key and 23 is value, immutable
marks = {"aqsa": 93, "jawan": 89, "ab":34}
print(marks["aqsa"])


# if else

age = int(input('Enter your age:'))

if (age >= 18):
    print("you can drive")
elif(age == 15):
        print ("your not eligible")
else:
            print("no")
print("end of pg")

# match case


a = int(input("enter number:"))
match a:
  case 1 :
    print("case is 1")
  case 2 :
    print("case is 2")
  case 3 :
    print("case is 3")
  case 4 :
    print("case is 4")



    # table
a = int(input("enter num between 1-10="))
def table(x):
 for i in range(1,11):
    print("Multiplication of ",x,"*",i,"=",x*i)
match a:
  case 1 :
    table(1)
  case 2 :
   table(2)
  case 3 :
   table(3)
  case 4 :
    table(4)


# for loop use to repeat anything

for i in range(5):
  print(i+1)

print("Printing set...")
a = [1,34,434,534]
s = {3,4,53,54}
for item in s:
  print(item)

# while loop 

# i = 0 
# while (i<10):
#   print(i)
#   i = 1

# this is infinite we use break 

# functions
def greetHello(name,ending):
  print("hello " + name)
  print("hello")
  print(ending)

def letterGenertor(name, date):
  st = f"hi,mam,n\This is {name} and i will see {date}"
  print(st)
  greetHello("aqsa", "Thank you")


