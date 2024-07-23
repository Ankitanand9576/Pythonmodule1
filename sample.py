# if 5>3:
#     print ("i am ankit") #indentation 

# x=4
# y="ankki"
# z=898989898.566589
# x=str("ddgfdgfc")
# y=int(65)
# r=float(5454)
# """
# for multiple comment
# """


# def myfunc() :
#     global x 
#     x= "awsome1"
#     print("test local" +x)



# myfunc()
# print("test global" +x)
# x=str ("i am ankit")
# y=int (5)
# z=float (8.56)
# t= complex(5+8j)
x1=[1,2,3,] #
# x2=("a","b","c")
# x3= range (6)
# print(x)
# print(y)
# print(z)




# print(x1)
# print(x2)
# print(x3)
# import random
# print(random.randrange(1,90))
# a = "Hello, world"
# print(a[0])

# for d in a:
   
#     print(len(d))
# class ankit:
#     myName="ankit anand"
#     age =25
#     def h(self):
#         d=4
#         b=5
#         c= d+b
#         return c
# ali= ankit()
# print(ali.h())
# class Person:
    
    
#     def __init__(self,name,age,location) :
#         self.name=name
#         self.age=age
#         self.location=location
    
#     def print_details(self):
#         return f"{self.name} {self.age} {self.location}" # i have to  declear in flower bracket
    
    
# p1=Person("ankit",28,"Bangalore")
# p2=Person("ram",30,"Mumbai")

# print(p2.print_details())
# # print(p2)

# a = 30

# print(f"My age is {a}")

# class Ali:
#     pass

# class Person:
#     def __init__(self,fname,lname):
#         self.firstame=fname
#         self.lastname=lname
#     def __str__(self):
#         print(self.firstame,self.lastname)
# x=Person("Ankit","Anand")
# x.__str__()

# 

# address="in am ankit anand"
# print(address[-1::-2])
# ageList=[23,34,56,78] #list is ordered but with help of some method we can change order,list is changeable means we can change items in list,list allow dublicate

# print (ageList[0])
# print (ageList)
# print (ageList[-1])
# print (type(ageList))
# print (len(ageList))
# a = "Hello, World!"
# print(a.split("e"))
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)
# thislist = ["apple", "banana", "cherry","ankit"]
# if "apple"  in thislist:
#   print("Yes, 'apple' is in the fruits list")
# thislist [1]="ankit"
# print(thislist)
# thislist[1:2] =["anup ","raj"]
# print (thislist)
# thislist1=[1,3,4,4]

# thislist.insert(2,"name")
# thislist.insert(3,"ankit")
# thislist.remove(4)
# print(thislist1)

# age = 36
# txt = "My name is John, and I am {}"
# print(
    # txt.format(age))
# list1=[5,2,3,4,5,6,7]
# for x in (range(len(list1))):
#      print (x)

# firstVariable=1
# SecondVariable=2
# ThirdVariable=3

# if firstVariable>SecondVariable or ThirdVariable>ThirdVariable:
#     print (f"greatest no is {firstVariable}")
# elif SecondVariable > firstVariable or SecondVariable >ThirdVariable:
#     print (f"greatest no is {SecondVariable}")
# else :
#     print (f"greatest no is {ThirdVariable}")
    
#################################################################################################################################################
# while True:
#     print ("ankit")
#     f=0
#     if 10>f:
#         print ("i am good")
#         f+=1
#     else :
#         break
# adj =["ankit","anup","raj",]
# asd= ["ram","mohan","sohan"]
# for x in adj:
#     for y in asd:
#         print(x,y)

    
# def my_function(fname,lname):
#     print(fname +" " +lname)
# my_function("ankit","anand")

# def my_function(*kids):
#     print("the youngest child is " + kids[2])
# my_function("Email","school","device")

# def my_function(child3,child2,child1):
#     print("the youngest child is" +child3)
# my_function(child1="ankit",child2="anup",child3="anjali")
# def my_function(countary ="norway"):
#     print ("i am from " + countary)
# my_function("sadcfgb")
# my_function("waedsfg")
# my_function("8541")
# my_function()
# my_function("ww")
# def my_function(food):
#     for x in food:
#         print(x)
# fruits=["apple","banana","cherry"]
# my_function(fruits)
# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(56))
# print(my_function(90))

# def my_function():
#     pass
# class Person:
#     def __init__(self,name,age):
#       self.name=name
#       self.age=age
#     def __str__(self) -> str:
#        return f"{self.name} {self.age}"
# p1 =Person ("ankity",34)
# print(p1)
# class Person:
#     def __init__(self,firstName,LastName):
#         self.firstName =firstName
#         self.lastName =LastName
#     def __str__(self):
#         return print(f"my first name is {self.firstName} {self.lastName}")
    
# x =Person("ankit","anand")
# x.__str__()

# class PersonSon(Person):
#     pass
 
# y = PersonSon("Rohit","Sharma")
# y.__str__()

# class test:
#     def __init__(self,name,age): 
#         self.name=name
#         self.age=age
#     def __str__(self):
#      return f"{self.name}, {self.age}"

#     def work(self):
#         print("i am working")
# class testrun(test):
#     def __init__(self, name, age):
#         super().__init__(name, age)
        
# firstObject=test("ankit",29)
# secondObject=testrun("anup",28)
# secondObject.work()
# print(secondObject.age)
# print(secondObject.name)
# print(secondObject.__str__())

# thisdict ={
#     "brand":"ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(len(thisdict))
# KeyVariable=thisdict.keys
    
# print (KeyVariable)
       
# import platform

# x= dir(platform)
# for i in x:
#     print(i)
    
# import datetime
# x =datetime.datetime.now()
# print(x)

# try block
# except Block
# else Block
# finally Block

# txt =f"the price is 49 dollars"
# print(txt)

# print ("Hell,World!")
# First Question
# for i in range(100):
#     if i%2 ==0:
#         print(f"{i} is even")
        
#     else:
#         print(f"{i} is odd")
# Second Qestion
# count=0
# for i in range(100):
#     if i%2 ==0:
#       count=count+1      
# print (count)   
# Third Question

# for i in range(1, ):
#     print("Enter any value")
#     Usearinput=input()
#     if (Usearinput=="quit"):
#      break
#     else:
#      continue
# isValid=True
# while(isValid):
#     print("enter a value")
#     Userinput=input()
#     if (Userinput=="quit"):
#         break
#     else:
#         continue
# for i in range(100):
#     if (i<=40):
#         print()
#     else:
#      if():
# for i in range(1,51):
#     if (i%2!=0):
#         print(i)
#     else:
#         print()
# listDemo=[21,34,5,78,45,2,9,4,]
# sumOfDigit=0
# for i in listDemo:
#     if (i>10):
#         sumOfDigit=sumOfDigit+i

# print(f"sum of digit greater than 10 in list {sumOfDigit}")
# MarkOfStudent=[92,83,78,65,45,30]
# for i in MarkOfStudent:
#     if (i>=90 and i<=100):
#         print (f"grade of student a")
#     elif (i>=70 and i<=90):
#         print("grade of student is b")
#     elif (i>=50 and i<=70):
#         print("grade of student is c")
#     elif (i>=50 and i<=30):
#         print("grade of student is d")
#     else:
#         print("grade of student is E")
    
    
    
    
        
    

    
         
    
    

   
    



        


       
    
    



    
    
