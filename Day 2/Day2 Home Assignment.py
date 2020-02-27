#Q1. Write a python program to input two numbers from the user and print its addition.
x = int(input("Number 1:"))
y = int(input("Number 2:"))

print ("Answer:", x+y)

#Q2. Write a python program to input name, age, address and print the details in one line

name = input("Name?")
age = int(input ("Age?"))
address = input ('Address?')

print ("Name:", name, "Age:", age, "Address:", address)

#Q3. Write a python program to input a number from user and check if the number is even or odd

print ("Check on odd(greater than 0)/even=0:", x%2)


#Q4. Write a python program to input the number of drivers in their household.
#Each driver costs 70 per month for insurance, but receives a 10 dollar discountfor every 3 drivers, calculate the total cost

drivers = int(input("drivers in household"))

drivercost = (drivers*70)-(((drivers-(drivers%3))/3)*10)

print("Policy Cost:", drivercost)