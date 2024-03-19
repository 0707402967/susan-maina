# this is a programme to solve geometric progression
# date : 21/02/2024
# name : Susan Maina
import math

#geometric progression

a = float(input("enter the first term :"))
r = float(input("enter the common ratio :"))
n = float(input("enter the number of terms :"))

sol = (a *(r**(n-1)))
sum = ((a * (r**n-1))/(r-1))

print("the value of the term is :",sol)
print("the sum of the term is :",sum)

