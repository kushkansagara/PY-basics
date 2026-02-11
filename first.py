# # comment
# # comment 2
# '''
# comment
# comment 2
# '''
# print("\"Kush\" \n Patel")
# print("kush", "kansagara", sep='~', end='day\n')
# print(5)
# # print(5)
# # print(1234568451* 65461654987)

# day 6

# a = 1
# b = "kush"
# c = True
# d = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# list = [3,5,[4.5,6],['kush', 'patel']]
# print(type(list))
# print(list)

# tupp = (("kush", "patel"),(3,5))
# print(type(tupp))
# print(tupp)

# day 7

# a = 50
# b = 3

# print("the value of", a, "+", b, '=', a+b)
# print("the value of", a, "-", b, '=', a-b)
# print("the value of", a, "*", b, '=', a*b)
# print("the value of", a, "/", b, '=', a/b)
# print("the value of", a, "//", b, '=', a//b)


# day 9
# a = '1'
# b = '3'
# print(a+b)
# print(int(a)+int(b))

# c = 4.5
# d = 5
# print(c+d)

#day 10
# a = input("Enter your name: ")
# print(a)

# x = input("Enter First Number : ")
# y = input("Enter second Number : ")
# print(x + y)
# print(int(x) + int(y))

#day 11
# a = 'kush'
# b = 'patel'
# print(a + b)

# c = '''lsfdjgsd fasdf adfa
# df sadf
# sd fsdf
# s dfsd
# f '''
# print(a[0])
# print(a[1])

# for ca in c:
#     print(ca)


#day 12
# name = "kush.kansagara"
# print(name[0:4])

#day 13
# a = "kush@@@@@"
# a = "kush kush"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("@"))
# print(a.replace("kush", "patel"))
# print(a.split(" "))
# b = "my name is KUSH"
# print(b.capitalize())
# print(a.count("kush"))

# c = "hello how are you"
# print(c.center(50)) # add space

# d = "askdjfb kush asdjf asdlfj kush"
# print(d.endswith("ks"))
# print(d.endswith("kush"))
# print(d.endswith("fb",1,7))
# print(d.find("kush")) # not then return -1
# print(d.index("kush")) # not then error

# e = "adfgjdfghksje4t&"
# print(e.isalnum())
# print(e.isalpha())

# print(e.islower())
# d = "          askdjfb kush asdjf asdlfj kush\n"
# print(d.isprintable())

# print(d.isspace())

# e = "My Name Is Kush"
# e = "My Name is KUsh"
# print(e.istitle())
# print(e.title())
# print(e.swapcase())

#day 14
# a = int(input("Enter your age: "))
# print(a)
# if(a==18):
#     print("50%")
# elif(a>18): 
#     print("drive")
# else:
#     print("not drive")

#day 15
# import time
# print(time.strftime('%H:%M:%S'))
# hour = int(time.strftime('%H'))

# if(hour<12):
#     print("good morning")
# elif(hour<15):
#     print("good Afternonon")
# elif(hour<20):
#     print("good evening")
# else:
#     print("good night")

#day 16
# a = 15
#     match a:
#         case 15:
            
#day 17
# name = "kush"
# name = ["kush","patel"]
# for i in name:
#     print(i, end=', ')

# a = 20
# for n in range(0,a,6):
#     print(n, end=', ')

#day 18
# i = 0
# while(i<3):
#     print(i)
#     i = i + 1
# else:
#     print("while over")

#day 19
# i = 20
# for i in range(i):
#     if((i%2)==0):
#         continue
#     print(i)
    # if(i==20):
    #     break

#day 20
# def calGmean(a,b):
#     mean = (a*b)/(a+b)
#     return mean
# def greater(a,b):
#     if(a>b):
#         return a
#     else:
#         return b

# a = 9 
# b = 8
# gmean = calGmean(a,b)
# gmean = greater(a,b)
# print(gmean)

# c = 8
# d = 7
# gmean = calGmean(c,d)
# gmean = greater(c,d)
# print(gmean)

#day 21
# def average(a=9,b=1):
#     print("average is : ", (a+b)/2)
# average(5,6)
# average(b=9,a=35)

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print(sum/len(numbers))

# average(5,6)

#day 22
# l = [1,3,34,6]
# if 4 in l:
#     print("yes")
# else:
#     print("no")

# print(l[:])

# lst = [i for i in range(4)]
# lst = [i for i in range(4) if i%2==0]
# print(lst)

#day 23
# l = [34,5,2,6,7]
# l.append(20)
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(2))
# print(l.count(2))

# m = l #change main
# m = l.copy() #not change main
# m[0] = 100

# l.insert(0,500)
# print(l)

# m = [10,20,30]
# k = l+m
# l.extend(m)
# print(l)

#day 24
# tup = (1,5,6)
# print(tup)

#day 25
# con = ("india","USA", "ING", "SA")
# con1 = ('Russia')
# temp = list(con)
# temp.append("Russia")
# temp.pop(2)
# con = tuple(temp)
# print(con)
# tup = (123,4,5,43,2,1,3,5)
# print(tup.count(4))

#day 28
# letter = "Hey my name is {} and I am from {}."
# country = "india"
# name = "Kush"
# print(letter.format(name,country))
# letter = "Hey my name is {1} and I am from {0}."
# print(letter.format(country, name))

# print(f"Hey my name is {name} and I am from {country}.")
# print(f"Hey my name is {{name}} and I am from {{country}}.")


#day 29
# def square(n):
#     '''given an number for argument and return square of it.'''
#     print(n**2)
#     '''given an number for argument and return square of it.'''
# square(5)
# print(square.__doc__)

# #day 30
# def fectorical(n):
#     if(n==0 or n==1):
#         return n
#     return n * fectorical(n-1)
# print(fectorical(5))

# def fecto(n):
#     if(n==0 or n==1 or n==2):
#         return n
#     else:
#         return fecto(n-1) + fecto(n-2)
# print(fecto(6))

#day 31
# s = {2,34,5,3,21,2}
# print(s)
# kush = {} #dec
# kush = set()
# print(type(kush))

# for val in s:
#     print(val)

#day 32
# l = {1,2,4,5}
# l2 = {4,5}
# print(l.union(l2))
# l.update(l2)
# print(l)

# print(l.intersection(l2))
# l.intersection_update(l2)
# print(l)

# print(l.symmetric_difference(l2))

# print(l.difference(l2))
# print(l.isdisjoint(l2))
# print(l.issuperset(l2))
# print(l2.issubset(l))
# l.discard(64)
# print(l)
# l.remove(64)
# print(l)

# l.clear()
# print(l)
# del l

#day 33
# dic = {
#     1: "kush",
#     2: "param",
#     3: "jenil",
#     3: "yashu"
# }
# print(dic[1])
# print(dic.get(1))
# print(dic.keys())
# print(dic.items())

# for keys in dic.keys():
#     print(dic[keys])

#day 34
# ep1 = {122: 45, 123: 89, 865:86}
# ep2 = {98:68, 456:786}
# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem()
# del ep1
# print(ep1)

#day 35
# for i in range(5):
#     print(i)
#     if(i==4):
#         break

# else:
#     print("complete")

#day 36
# a = (input("Enter any number : "))

# print(f"Multiplication table of {a}")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# # except Exception as e:
# #     print(e)
# except ValueError:
#     print("Value error")
# except IndexError:
#     print("Index error")


#day 37
# try:
#     int(input("Enter your name: "))
# except:
#     print("some error")
# finally:    
#     print("i am finally") # call in functon after retutn 

# print("i am finally") #not after return 

#day 38
# age = int(input("Enter your age: "))
# if(age < 18):
#     raise ValueError("not valid")

#day 39 - KBC
# questions = [
#     ["Which language was used to create FB?", "PHP", "PY", "Node", "None", 'D'],
#     ["Which language was used to create FB?", "PHP", "PY", "Node", "None", 'D'],
#     ["Which language was used to create FB?", "PHP", "PY", "Node", "None", 'D'],
#     ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

# totalWin = 0
# for i in range(0, len(questions)):
#     question = questions[i]
#     print(f"Question for Rs. {levels[i]}")
#     print(f"Question is : {question[0]}")
#     print(f"A.  {question[1]}          B.  {question[2]}          C.  {question[3]}          D.  {question[4]}")
#     ans = (input("enter Your ans : "))
#     if(ans == question[5]):
#         print(f"Correct Ans") 
#         totalWin = totalWin + levels[i]
#     else:
#         print(f"You win total {totalWin} Rs.") 
#         break

# day 41
# a = 456 
# b = 456
# print("A") if a > b else print("=") if a==b else print("B")

#day 42
# a = [34,56,76,86,77]
# for index,mark in enumerate(a):
#     print(mark)
#     if(index==3):
#         print("Wow Kush")        

# day virtual Envi
# python -m venv "name"
# source name/Scripts/activate.bat

#day 44
# import math
# import math as m
# from math import *
# from math import sqrt,pi
# from kush import welcome
# print(dir(math))

#day 45
# import kush
# kush.welcome()

#day 46
# import os
# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(0,100):
#     # os.mkdir(f"data/Day{i+1}")
#     os.rename(f"data/Day{i+1}", f"data/Day {i+1}")

#day 47

# a = input("Enter Your Word : ")
# print(a)
# words = a.split(" ")
# arr = []
# for word in words:
#     if(len(word) >=3):
#         r1 = "sdg"
#         r2 = "ery"
#         temp = r1 + word[1:] + word[0] + r2
#         arr.append(temp)
#     else:
#         arr.append(word[::-1])
# print("Decoad String:")
# print(" ".join(arr))

# new = " ".join(arr)
# words = new.split(" ")
# arr = []
# for word in words:
#     if(len(word) >=3):
#         word = word[3:-3]
#         temp = word[-1] + word[0:-1]
#         arr.append(temp)
#     else:
#         arr.append(word[::-1])
# print("Encode String:")
# print(" ".join(arr))

#day 48
# a = 10
# def change():
#     global a #use globle variable
#     a = 5

# print(a)
# change()
# print(a)

#day 49
# f = open('temp.txt','r')
# text = f.read()
# print(text)
# f = open('temp.txt','w')

# f = open('temp.txt','a')
# text = f.write("Kush Patel")
# f.close()

# with open("temp.txt", "a") as f:
#     f.write("Kush Patel")

#day 50
# f = open("temp.txt" , "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open("temp.txt" , "w")
# line = ['line 1\n' , 'line 2\n', 'line 3\n']
# f.writelines(line)
# f.close()

#day 51
# with open("temp.txt", "r") as f:
#     f.seek(3)
#     print(f.tell())
#     data = f.read(10)
#     print(data)

# with open("temp.txt", "w") as f:
#     f.write("kush patel")
#     f.truncate(4)

#day 52
# def double(x):
#     return x*2
# double = lambda x: x * 2
# print(double(5)) 
# def sum(a,b):
#     return 10 + a(b)
# print(sum(double,5))

#day 53
# def sq(x):
#     return x*x
# print(sq(4))

# l = [2,4,5,4,94,5,6,8]
# new = []
# for item in l:
#     new.append(sq(item))
# print(new)
# newl = list(map(sq , l))
# print(newl)

#FILTER
# filterL = list(filter(lambda x: x>4 , l))
# print(filterL)

#reduce
# from functools import reduce
# reduceList = reduce(lambda x,y: x+y,l)
# print(reduceList)

#day 54
# a = 5
# b = 5
# print(a is b) #exact location in memory
# print(a == b) #value

#day 55 
# snak water gun game

#day 56
# introduction of oops

#day 57
# class Person:
    # name = "kush"
    # age = 21
    # def __init__(self,n,a):
    #     self.name = n
    #     self.age = a
    # def info(self):
    #     print(f"{self.name} is {self.age} year old.")

# a = Person()
# b = Person()
# b.name= "patel"
# a.info()
# b.info()

#day 58
# a = Person("Kush", "Developer")
# b = Person("patel", "Developer")
# a.info()
# b.info()

#day 59  decorators

# def greet(fn):
#     def mfx(*args, **kwargs):
#         print("good Morning")
#         fn(*args, **kwargs)
#         print("Thank you")
#     return mfx

# @greet
# def hello():
#     print("Hello World")

# @greet
# def add(a,b):
#     print(a+b)
# hello()
# greet(hello())
# add(5,4)

#day 60
# class MyClass:
#     def __init__(self,value):
#         self._value = value
    
#     def show(self):
#         print(f"value is {self._value}")
    
#     @property
#     def ten_value(self):
#         return 10*self._value
    
#     def ten_value(self, a):
#         self._value = a
    
# obj = MyClass(50)
# obj.ten_value = 5
# print(obj.ten_value)

#day 61
# class Emp:
#     def __init__(self , name, id):
#         self.name = name
#         self.id = id
    
#     def show(self):
#         print(f"the name of employee is {self.name}")
    

# class Programmer(Emp):
#     def showLen(self):
#         print("PY is default len")

# e1 = Emp("kush", 1)
# e1.show()
# e1 = Programmer("patel", 2)
# e1.show()
# e1.showLen()

#day 62
# class Emp:
    # def __init__(self):
        # self.name = "kush" # public
        # self.__name = "kush"
        # self._name = "kush"

# a = Emp()
# print(a.__name) #not access directly
# print(a._Emp__name) #can be access indirectly
# print(a._name) 

#day 63
# import random
# print("1. Snack\n2. water\n3. Gun")
# l = {1 : "Snack", 2: "Water", 3: "Gun"}
# outputArray = [
#     [0, 1, -1],
#     [-1, 0, 1],
#     [1, -1, 0]
# ]
# userInput = int(input("Please choose 1, 2, or 3 : "))
# if userInput<1 or userInput>3:
#     print("Choose another time")
# else:
#     print(f"You choose : {l[userInput]}")
#     computerInput = random.randint(1,3)
#     print(f"computer choose : {l[computerInput]}")
#     output = outputArray[userInput-1][computerInput-1]
#     if(output == 0):
#         print("Draw")
#     elif(output==1):
#         print("Win")
#     else:
#         print('Lose')

# day 64
# library management

#day 65
# class Math:
#     def __init__(self, num):
#         self.num = num

#     def addToNum(self, num2):
#         self.num += num2
    
#     @staticmethod
#     def add(a,b):
#         return a+b
# a = Math(5)
# print(a.num)
# a.addToNum(6)
# print(a.num)
# print(a.add(5,6))

#day 66
# class Emp:
#     company = "google" # class veriable
#     def __init__(self, name):
#         self.name = name # instance variable
#     def show(self):
#         print(f"Employee name is {self.name} and company name is {self.company}")
# e = Emp("kush")
# e.show()

# day 67
# class Library:
#     def __init__(self):
#         self.numberOfBook = 0
#         self.books = []
#     def addBook(self, book):
#         self.books.append(book)
#         self.numberOfBook = len(self.books)
#     def showInfo(self):
#         print(f"the book has {self.numberOfBook} books are")
#         for b in self.books:
#             print(b)

# li = Library()
# li.addBook("Rech dad poor dad")
# li.addBook("Rech dad poor dad")
# li.addBook("Rech dad poor dad")
# li.showInfo()
# l2 = Library()
# l2.showInfo()

#day 68
# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")
    
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany

# e1 = Employee()
# e1.name = "kush"
# e1.changeCompany("Google")
# e1.show()
# print(Employee.company)

#day 70
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def fromStr(cls, s):
#         return cls(s.split('-')[0], s.split('-')[1])

# e1 = Employee("kush", 21)
# print(e1.name)
# print(e1.age)

# s = "patel-21"
# e2 = Employee.fromStr(s)
# print(e2.name)
# print(e2.age)

#day 71
# x = [1,2,4]
# print(dir(x))
# print(x.__add__)

# class Emp:
#     def __init__(self, name):
#         self.name = name
# e1 = Emp("kush")
# print(e1.__dict__)

# print(help(x))

#day 72
# class ParentMethod:
#     def __init__(self,name):
#         self.name = name
#     def parent_method(self):
#         print("parent")

# class Child(ParentMethod):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def parent_method(self):
#         print("child parent method")

#     def child_method(self):
#         print("child")
#         self.parent_method()
#         super().parent_method()
# c1 = Child("kush" , 21)
# c1.child_method()
# print(c1.name)
# print(c1.age)

#day 73
# class Emp:
#     name = "kush"

#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i+1
#         return i
#     def __str__(self):
#         return f"The name of emp is {self.name} str"
#     def __repr__(self):
#         return f"The name of emp is {self.name} repr"

# e = Emp()
# print(e)
# print(len(e))
# print(str(e))
# print(repr(e))

#day 74
# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def area(self):
#         return self.x * self.y

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#         super().__init__(r,r)
#     def area(self):
#         return 3.14 * super().area()
        
# rec = Shape(4,5)
# print(rec.area())
# c = Circle(5)
# print(c.area())

#day 75
# import os

# files = os.listdir("clutteredFolder")
# i = 1
# for file in files:
#     if(file.endswith(".png")):
#         os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
#         i = i + 1


# day 76
# pyPDF pdf merge

#dat 77
# class Vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
    
#     def __add__(self, x):
#         return Vector(self.i + x.i , self.j + x.j , self.k + x.k)
# v = Vector(3,5,6)
# print(v)
# v2 = Vector(1,2,9)
# print(v2)

# print(v+v2)
# print(type(v+v2))

#day 78 single inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):
#         print("animal sound")

# class dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def sound(self):
#         print("Bark")

# a = Animal("Animal")
# a.sound()

# b = dog("Dog")
# b.sound()

#day 79

# class Employee:
#     def __init__(self, name):
#         self.name = name
    
#     def show(self):
#         print(f"the name is {self.name}")

# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance

#     def show(self):
#         print(f"the dance is {self.dance}")
    

# class dancerEmp(Employee, Dancer):
#     def __init__(self, name, dance):
#         self.name = name
#         self.dance = dance

    # def __str__(self):
    #     return f"name is {self.name} and dance is {self.dance}"
# d = dancerEmp("Kush", "bd")
# d.show()

#day 80
# class Animal: 
#     def __init__(self, name):
#         self.name = name

#     def show_detail(self):
#         print(f"Animal name is {self.name}")

# class Dog(Animal):
#     def __init__(self, name, sound):
#         Animal.__init__(self, name)
#         self.sound = sound
    
#     def show_detail(self):
#         Animal.show_detail(self)
#         print(f"Sound is {self.sound}")
    
# class Gernen(Dog):
#     def __init__(self, name, sound, color):
#         Dog.__init__(self, name, sound)
#         self.color = color
#     def show_detail(self):
#         Dog.show_detail(self)
#         print(f"Dog color is {self.color}")
    
# g = Gernen("jimi", "bark", "black")
# g.show_detail()

#day 81
#Hybride
# class BaseClass:
#     pass

# class D1(BaseClass):
#     pass

# class D2(BaseClass):
#     pass

# class D3(D1,D2):
#     pass

#hirichical
# class BaseClass:
#     pass

# class D1(BaseClass):
#     pass

# class D2(BaseClass):
#     pass

# class D3(D1):
#     pass
# class D4(D3):
#     pass

# day 82
# from pypdf import PdfWriter
# import os

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")

#day 83
# shoutout

# day 84
# import time
# print(time.time())

# print("kush")
# time.sleep(3)
# print("Patel")
# t = time.localtime()
# format_time = time.strftime("%D-%M-%Y %H-%M-%S", t)
# print(format_time)

# day 85
# comment line input

#day 86 walrus operator
# print(a := True)
# foods = []
# while(food := input("write food do you like? : ")) != "quit":
#     foods.append(food)

# day 87
# import shutil

# shutil.copy('first.py', "second.py")
# shutil.copytree('data', "merged")
# shutil.move("clutteredFolder/6.txt",'6.txt')
# shutil.rmtree('merged')

#import 88
# import win32com.client as wincom

# speaker = wincom.Dispatch("SAPI.SpVoice")

# list = ['kush', 'patel', 'param', 'yashu', 'jenil']
# for i in list:
#     speaker.Speak(f"shoutoUt to {i}")

#day 89
# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

#day 90
# news app

# day 91
# def my_generator():
#     for i in range(5):
#         yield i
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for i in gen:
#     print(i)

# day 92
# import functools
# import time

# @functools.lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5
# print(fx(2))
# print(fx(10))
# print(fx(2))
# print(fx(10))

# day 93
# import requests
# import json
# query = input("What type of news in : ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-05&sortBy=publishedAt&apiKey=7816e3f62eb1425ca1ea90b78adee24e"
# r = requests.get(url)
# news = json.loads(r.text)
# for artical in news["articles"]:
#     print(artical["title"])
#     print(artical["description"])
#     print("=--------------------------------------------")

#day 94
# import re

# pattern = r"[A-Z]+ush"
# text = "Kush Bush"
# match = re.search(pattern,text)
# print(match)
# match = re.finditer(pattern,text)
# for m in match:
#     print(m)

#day 95
# water reminder


#day 97
# import time
# import asyncio
# async def function1():
#     print(1)
#     time.sleep(3)
# async def function2():
#     print(2)
#     time.sleep(3)
# async def function3():
#     print(3)
#     time.sleep(3)

# async def main():
#     # task = asyncio.create_task(function1())
#     L = await asyncio.gather(
#         await function1(),
#         await function2(),
#         await function3()
#     )

# asyncio.run(main())

#day 97
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor
# def func(seconds):
#     print(f"Sleeping fot {seconds}")
#     time.sleep(seconds)
#     return seconds

# func(4)
# func(2)
# func(1)

# time1 = time.perf_counter()
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[1])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# print(time2-time1)

# def poolingDemo():
#     with ThreadPoolExecutor() as ex:
        # future1 = ex.submit(func,3)
        # future2 = ex.submit(func,2)
        # future3 = ex.submit(func,1)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
#         l = [2,4,3,1]
#         result = ex.map(func, l)
#         for re in result:
#             print(re)
# poolingDemo()

#day 98
# import multiprocessing
# import concurrent.futures
# import requests
# def downloadFile(url,name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")

# if __name__ == "__main__":
#     multiprocessing.freeze_support()  # safe on Windows

# url = "https://picsum.photos/2000/3000"
#     pros = []

#     for i in range(5):
#         p = multiprocessing.Process(target=downloadFile, args=(url, i))
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()
# if __name__ == "__main__":
#     url = "https://picsum.photos/2000/3000"
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         l1 = [url for i in range(6)]
#         l2 = [i for i in range(6)]
#         results = executor.map(downloadFile, l1, l2)
#         for r in results:
#             print(r)

#day 99

# from win10toast import ToastNotifier
# import time

# toast = ToastNotifier()

# while True:
#     toast.show_toast(
#         "Drink Water 💧",
#         "Kush, drink water first!",
#         duration=1,
#         icon_path="icon.ico",
#         threaded=False,
#     )

#     while toast.notification_active():
#         time.sleep(1)

#     time.sleep(10)
