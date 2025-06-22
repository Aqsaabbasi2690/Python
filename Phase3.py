# A docstring (short for documentation string) is a special kind of string used to document what your function, class, or module does.
#
# It helps other programmers (and your future self!) understand your code easily.
#
# Always written just after the function, class, or module definition.
#
# Written using triple quotes """...""" or '''...'''. access through --doc--

# comments not print doc print, doc write just after function , with doc program can change but with commits not change



def greet(name):
    """
    This function takes a name as input
    and prints a greeting message.
    """
    print(f"Hello, {name}!")


# pep 8 python enhancement proposal
# provide best practice and guideline to write python code, main focus this is to make code consistence, readable, easy

# import this, zen of python it prints

# recursion,
# recursion means a function calling itself to solve smaller parts of a big problem.





# sets are unordered collection of data items,
# unordered means it is not maintain order.
# it stores data in single variable, sets are unchangeable, enclose in curly brackets

# empty dic
aqsa ={}
print(type(aqsa))

# empty set
aqsa = set ()
print(type(aqsa))

# we use it with for loop
# set = {23,45, 12}
# for value in set:
#     print(value)


# methods of sets
# 1union
# a = {1, 2}
# b = {2, 3}
# print(a.union(b))  # {1, 2, 3}
s1 = {1,2,3,4,5,2}
s2 = {34 , 44 ,33, 343}


# s1.union(s2)
# 2 intersecton Returns common elements.
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))  # {2, 3}
# print(s1.intersection(s2)) means  wo  values ju dono sets mae
# same ho osko print karky deta hae
# s1.intersection.update(s2)

# 3 update
s1.update(s2)
print(s1, s2)

# 4 symmetric difference means ju same hain onko chor ky baki values
# s3 = s1.symmetric_difference(s2)

# 5 difference
# Returns elements only in the first set.
# a = {1, 2, 3}
# b = {2, 3}
# print(a.difference(b))  # {1}
s3 = s1.difference(s2)

# 6 superset,subset
# Check relationships between sets.
# a = {1, 2}
# b = {1, 2, 3}
# print(a.issubset(b))   # True
# print(b.issuperset(a)) # True

# 7 add()
# Adds an element to the set.
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # {1, 2, 3, 4}


#dictionaries
#dic, are ordered collection of data,, they store mutiple items in single var,close with {}
# Used when you want to pass many named values like key=value.
dic = {
    "aqsa": "human",
     "spoon": "object",
    456: "aqsa2"
}

print(dic["aqsa"])


dic = {
    "aqsa": "human","spoon": "object",456: "aqsa2","name": "aqsa3"
}

print(dic["name"])
print(dic.get["name"])# it through nun value if key and value not exist in dic, it tell us to error handling
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])



    # methods of dic
ep1 = {122:55,123:67,577:90}
ep2= {156:55,198:67,87:90}
ep1.update(ep2)
ep1.clear()
ep1.pop(122)# remove key value
ep1.popitem(577)# remove last key value pair
empty ={}
del ep1[122]
print(ep1)


# for loop, else with loop,agr loop break kiya giya to else ka content print nhi hoga
# for i in range(5)
# i = 0
# while i <7:
#     print(i)
# i = i + 1
# if i == 4:
#     break
# else:
#     print("loop not executed")

# # error handling, Exception handling in Python means managing errors in your code without crashing the program.
# a = input("Enter the num:")
# print(f"Multiplication of {a} is:")
# try:
#  for i in range(1,11):
#     print(f"{int(a)} x {i} = {int(a) * i}")
# except:
# print("invalid input")

# # 2 method
# try
# a = int(input("Enter the num:"))
# except ValueError:
# print("Number is not integer")
# except IndexError:
# print("index input")


#  finally always executed if error occurred or not
def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")
        # print("I am always executed")

x = func1()
print(x)


# custom error
#in python we can raise custom error by using raise keyword
a = int(input("Enter the num between 5 and 9:"))
if (a<5 or a>9):
    raise ValueError('value should be between 5 and 9')

# quiz
user_input = input("Enter the number: ")

if user_input.lower() == "quit":
    print("quit")
else:
    a = int(user_input)
    if a < 5 or a > 9:
        raise ValueError("Enter ther Number Between 5-9")










