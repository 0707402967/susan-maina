#this is a programme to find  hire purchase 
#date :21/02/2024
#name : Susan Maina

import math 

# find the hire purchase

cash_p= float(input("enter the cash price"))
dep = float(input("enter the deposit"))
months = float(input("enter the number of months"))
inst = float (input("enter the instalments"))

h_p = dep + (months * inst )

print ("the hire purchase is :", h_p)
