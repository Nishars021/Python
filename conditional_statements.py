# colour = (input("Enter colour : "))
# if(colour == "red"):
#   print("Stop")
# elif(colour == "yellow"):
#   print("Wait")
# elif(colour == "green"):
#   print("Go")
# else:
#   print("Light is broken")

# marks = int(input("Enter marks : "))

# if(marks >= 95):
#  print("Grade : A ")
# elif(marks <= 95 and marks >= 80):
#  print("Grade : B ")
# elif(marks <= 80 and marks >= 70):
#  print("Grade : C ")
# else:
#  print("Fail")

# age = int(input("Enter age : "))
# if(age>=18):
#  print("Vote")

# marks = int(input("Enter marks : "))
# print("Pass") if marks >= 70 else print("Fail")

#Check eligibity to vote using clever ternary conditional statement
# age = int(input("Enter age : "))
# vote = ("Vote","Not eligible") [age<18]
# print(vote)

#Used clever ternary conditional statement to add tax for the salary
# salary = float(input("Enter your salary : "))
# tax = salary*(0.1,0.2) [salary>50000]
# print(tax)

#Used clever ternary conditional statement to check if the soup si hot or cold
# temp = float(input("Enter the temperature of soup : "))
# result = ("Hot","Cold") [temp<30]
# print("Soup is",result)

#Calculating simple interest
p=float(input("Enter principle amount : "))
r=float(input("Enter rate of interest : "))
t=int(input("Enter time : "))
si=(p*r*t)/100
print("Simple interest : ",si)
