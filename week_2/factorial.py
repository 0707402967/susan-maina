#This is aprogram that gets the factorial of numbers
#Date :22/02/2024
#Name : Susan Maina

# change the value for a different result
num= 10

#to take input from the user 
#num = int(input("enter a number: ")

factorial = 1

#check if the number is negative , positive or zero
if num < 0 :
    print("sorry, factorial does not exist for negative numbers ")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range (1,num + 1 ):
        factorial = factorial * i
    print("the factorial of",num,"is",factorial)