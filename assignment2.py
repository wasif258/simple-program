#1
# bornyear=int(input("enter your born year: "))
# currentyear=2024
# calculate_age=currentyear-bornyear
# print(calculate_age)

#2
# lenght_of_recatangle=int(input("enter lenght of recantagle"))
# width_of_recatangle=int(input("enter width of recatangle"))
# area_of_recatangle=lenght_of_recatangle*width_of_recatangle
# print(area_of_recatangle)

#3
# radius_of_circle=int(input("enter the radius of circle"))
# pi=3.14
# circle_of_circle=pi*radius_of_circle
# print(circle_of_circle)

#4
# surface_of_cube=int(input("enter the surface of cube"))
# area_of_cube=6*(surface_of_cube*surface_of_cube)
# print(area_of_cube)

#5 create a programe to convert the celcius tempreature into farnheight and vice versa
# temprature_celcius=int(input("enter celcius temprature"))
# farenheight=9/5*temprature_celcius+32
# print(farenheight)
# temprature_farnheight=int(input("enter celcius temprature"))
# celcius=(temprature_farnheight-32)*5/9
# print(celcius)

#6 convert the given number into second and minute
# second=int(input("enter the number"))
# minute=second//60
# sec=second%60
# print(minute,"minute",sec,"second")

#7 write a programe to calculate the percantage 
# n=int(input("enter a number"))
# total=int(input("enter the total number"))
# percantage=(n/total)*100
# print(percantage)

#8
# days=int(input("enter the days"))
# weeks=days//7
# day=days%7
# print(weeks,"weeks",day,"days")

# #9 check if number is positive , negative or zero
# number=int(input("enter a number"))
# if number>0:
#     print("number is positive",number)
# elif number<0:
#     print("number is negative",number)
# else:
#     print('number is zero',number)

#10 check that given year is a leap year or not
# year=int(input("enter a year"))
# if year%4==0:
#     print('This is leap year',year)
# else:
#     print("this is not a leap year",year)

#11 implement a simple claculator with elif condition
# int1=int(input("enter a number"))
# operator=input("enter operator which you perform")
# int2=int(input('enter a second number'))
# if operator=="+":
#     print("sum=",int1+int2)
# elif operator=="-":
#     print("subtration",int1-int2)
# elif operator=="*":
#     print("multiply",int1*int2)
# elif operator=="/":
#     print("division",int1/int2)

#12 check given number is even or odd
# number=int(input("enter a number"))
# if number%2==0:
#     print("number is even",number)
# else:
#     print("number is odd",number)

#13 compare three number and find the largest one
# n1=int(input("enter the number"))
# n2=int(input('enter a 2 number'))
# n3=int(input("enter a 3 number"))
# if n1> n2 and n3:
#     print("lagest number is n1:",n1)
# elif n2> n1 and n3:
#     print("lagest number is n2:",n2)
# elif n3> n1 and n2:
#     print("largest nunber is n3:",n3)

#14 write a programe to calculate the factorial of the number
# number=int(input("enter a number"))
# fact=1
# i=1
# while i<=number:
#     fact=fact*i
#     i=i+1
# print(fact)

#  15 write a function to calculate the square of the number
# number=int(input("enter a number"))
# def abc():
#     square=number*number
#     print(square)
# abc()

 #16 write a programe to check that given number is prime or not
# number=int(input("enter a number"))
# for i in range(2,number):
#     if number%i==0:
#         print("number is not prime:",number)
#         break
# else:
#     print("number is prime :",number)

# number=int(input("enter a number "))
# count=0
# for i in range(2,number+1):
#     if number%i==0:
#         count=+1
# if count==1:
#     print("mumber is prime",number)
# else:
#     print("number is not a prime",number)

#17 write a programe to reverse of string
# string=input("enter the string")
# reverse_string=string[::-1]
# print(reverse_string)

#18 write a programe to count the vowel of string
# string=input("enter the string")
# def count_vowels():
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     print(count)
# count_vowels()

#19 create a list of integer and find the sum of all integer
# list=[1,2,3,4,5]
# sum=sum(list)
# print("sum of the list is",sum)

#20 check that specific element is exist in list
# number=int(input("enter a specific element: "))
# list=[1,2,3,4,5]
# if number in list:
#     print("yes this number is in list:",number)
# else:
#     print("this number is not in list",number)
    
#21 find the maximum and mimmum number in list
# list=[1,2,3,4,5,0,9,8,7,6,]
# maximum_number=max(list)
# minimum_number=min(list)
# print("maximum number is :",maximum_number)
# print("minimum number is :",minimum_number)

# 22 create a programe to remove all duplicate in list
# list=[1,2,3,2,1,6,7,6]
# remove_duplicate=set(list)
# single=[remove_duplicate]
# print(single)

#23 use list comprehension to create a new list for even number in exist list
# list=[1,2,3,4,5,6,7,8,9,10]
# count=[]
# for i in list:
#     if i%2==0:
#         count.append(i)
# print(count)

#24 write a programe to check that string is palindrome or not
# string=input("enter a string")
# palindrome=string[::-1]
# print(palindrome)
# if string==palindrome:
#     print("string is palindrome",string)
# else:
#     print("string is not palindrome",string)

#25 crate a simple ligin system with predefine username and password
# name="wasif"
# password="abc123"
# press="enter"
# Name=input("enter your name")
# Password=input("enter password")
# Press=input("enter the press button")
# if name==Name and password==Password and press==Press:
#     print("Your system is now open")
# else:
#     print("something went wrong, please check name or password")

# 26 write a programe to print all natural number in python using while loop
# number=int(input("enter a number: "))
# i=1
# while i<number:
#     print("natural number are:",i)
#     i=i+1
    
#27 write a prigrame to print all natural number in reverse position
# number=int(input("enter a number"))
# i=0
# while number>i:
#     print(number)   
#     number=number-1

#28 print all even number from 1 to 100 using while loop
# a=1
# b=100
# while a<b:
#     if a%2==0:
#         print(a)
#     a=a+1

#29 print all odd number from 1 to 100 using while loop
# a=1
# b=100
# while a<b:
#     if a%2==1:
#         print(a)
#     a=a+1

#30 find the sum of all natural number from 1 to 100
# number=int(input("enter a number: "))
# list=[]
# i=1
# while i<number:
#     list.append(i)
#     i=i+1
# sum=sum(list)
# print(sum)

#31 find the first and last number
# number=int(input("enter a number"))
# if number<10:
#     print("number is a single digit:",number)
# else:
#     print("last number is :",number%10)
    
# i=0
# while number>9:
#     number=number//10
#     i=+1
# print("first number is:",number)

#32 write a programe to count the digit of number 
number=int(input("enter a number"))
i=0
while number>0:
    number=number//10
    i=i+1
print("total digit of number is:",i)


  
        

    


    
    

    
    
