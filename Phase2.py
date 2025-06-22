# functions
#1 default arguments, we provide default
# value while creating function this way the function assumes default value even if a value is not provided in function call.
# def average(a=9,b=2):
#     print("average",(a+b)/2)
# average(4,6)

#2 keyword arguments we can change order,we can provide arguments with key = value
# in default argument we need to maintain order but we dont need to maintain order in keyword argument
# def average(a=9,b=2):
#     print("average",(a+b)/2)
# average(b=4,a=6)

#3 requirement arguments,the value we must need to pass to a function in correct order,
# we dont pass key = value then it is necessary to pass
# def greet(name, age):
#     print("Hello", name, "You are", age, "years old")
#
# greet("Aqsa", 22)

# greet("Aqsa")
# # ❌

#3 variable-length arguments
# Sometimes, you don’t know how many values (arguments) will be passed to a function.
# In that case, you can use variable length arguments.
# tuples , Used when you want to pass multiple values and handle them as a group.
# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     print("Total is:", total)
#
# add(2, 4)           # Total is: 6
# add(1, 2, 3, 4, 5)

# dic,Used when you want to pass many named values like key=value.
# def show_info(**student):
#     for key, value in student.items():
#         print(key, ":", value)
#
# # Call function with key=value pairs
# show_info(name="Aqsa", age=22, city="Lahore")

# return statement is used to return the value of expression back to the calling functions

# list, list ordered collection of data, we use to
# store multiple things in single variable, list are changeable,seperated with commas,enclosed with square bracket
# list index in a list has its own unique index,it can be used to access any specific item from list

# marks = [3,4,5]
# print(marks[2])
#
# # to see one num in list or not we use for loop
# if 3 in marks:
#     print("yes")
# else:
#     print("no")

# Jump index means skipping elements in a list using a step while looping or slicing.
# colors = ["red", "blue", "green", "yellow", "pink", "black"]
# print(colors[0:5:2])

# # Jump every 2 elements
# output red
# green
# pink

# List comprehension
# it is used to create new lists from other iterables like list,tuples,dic
# lst = [i*i for i in range(10)]
# print(lst)
# # with condition for even num
# lst = [i * i for i in range(10) if i%2==0]
# print(lst)


# list methods
#1 append means add value at the end
# l = [2,3,4,5,6]
# l.append(7)
# print(l)

# #2 sort means arrange  value in ascending order l.sort(reverse=True) for descending order ,
# l = [2,3,4,5,6]
# l.sort()
# print(l)
#3 l.reverse complete change l like reverse end value come to the first and vice versa
#4 l.index(1)
#5 print(l.count(1)) tells how many times 1 in list
# 6 copy method
# l = [2,3,4,5,6]
# m = l.copy()
# m[0]=0
# print(l)

# 7 insert that means add 1 in 0 index

# l.insert(0,1)
# print(l)

# 8extent means add 2,3,4,5,6, in list means l change but if dont want to chanhe list we use k = l + m
# l = [345.556, 656, 554]
# m = [2,3,4,5,6]
# l.extend(m)
# print(l)

# l = [345.556, 656, 554]
# m = [2,3,4,5,6]
# k = l + m
# print(k)

# Tuples ,tuples are  ordered collection of data, difference is we cannot change it length, value
# if we want to change tupes first covert into list then perform operation and again convert into tuple
# commas is neccesery if there is not num and we dont put , then it return int instead of tuple tup = (1,), slicing ky bd new tuple banta hae osi mae change value nhi hoti like list
# tuples are immutable means not change we use list if we want constant values
# marks = [3,4,5]
# if 3 in marks:
#   print("yes")
# else:
#    print("no")

# tup = (345,556, 656, 554,3444)
# tup2 = tup[1:4]
# print(tup2)

# concatenate tuple
# countries = ("Pakistan","India")
# countries2 = ("france","spain")
# country = countries + countries2
# print(country)
# count
# tuple = (3,4,53,343,4,5,54)
# count = tuple.count(4)
# print(count)


import time

# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
#
# hour = int(input("Enter hour: "))
# print(hour)
#
# if(hour >= 0 and hour < 12):
#     print("Good Morning Sir!")
# elif(hour >= 12 and hour < 17):
#     print("Good Afternoon Sir!")
# elif(hour >= 17 and hour <= 23):
#     print("Good Night Sir!")

questions = [
    ["What is the capital of India?", "A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai", "B"],
    ["Which planet is known as the Red Planet?", "A. Earth", "B. Jupiter", "C. Mars", "D. Venus", "C"],
    ["Who wrote the Ramayana?", "A. Tulsidas", "B. Ved Vyas", "C. Kalidas", "D. Valmiki", "D"],
    ["What is the national animal of India?", "A. Lion", "B. Tiger", "C. Elephant", "D. Leopard", "B"],
    ["Which river is the longest in India?", "A. Yamuna", "B. Ganga", "C. Godavari", "D. Narmada", "C"]
]

price = [1000,2000,3000,4000,5000]
total = 0
for i in range (len(questions)):
    print(f"\nQuestion:{i+1} {questions[i][0]}")
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])
    answer = input("your answer(A/B/C/D):").strip().upper()
    if answer == questions[i][5]:
        total += price[i]
        print(f"Correct! You won {price[i]}")
    else:
        print("Incorrect! You lose ")
        break
    print(f"\n you are taking home: {total}.Thank you for playing KBC!")

#  f strings means now we can add variables in our strings
name = "Aqsa"
age = 22
print(f"My name is {name} and I am {age} years old.")