#Name- Gautam Bakliwal
#
#Course- 1411
#
#Date- 09/18/2017
#
#Problem-The Russian Peasant or Ancient Egyptian method for multiplication. 
# 
#Given- If A and B are two integers to be multiplied, we repeatedly multiply A by 2 and divide B by 2 
#until B becomes zero.  To figure out the product of A and B, we keep a running total 
#where we add A every time the result of dividing B by 2 is an odd number.
#
#Analysis-
#Test Cases
#Input-34, 19, n
#Output- 34 x 19 = 646 in 5 iterations
#Do you want to try another numbers[y/n]
#Bye. Have a Good day
#
#Input-2, 10, y
#Output- 2 x 10 = 20 in 4 iterations
#Do you want to try another numbers[y/n]
#Prompts again
#
#Input-23, 11, n
#Output- 23 x 11 = 253 in 4 iterations
#Do you want to try another numbers[y/n]
#Bye. Have a Good day
#
#Algorithm
#Introduce Program to the user
#Check validity of values to be entered by user
#Introduce a function to calculate the product
#Count number of iterations by count_int
#Take input of values from user
#Store original values entered
#Calculations- Till the 2nd number>0, check if 2nd number is odd/even
#If odd, add 1st number to product. Multiply 1st number by 2 and devide
#2nd number by 2. Follow process till b becomes zero
#Call the function to execute
#Ask user if he wants to execute the function again
#Perform action according to user choice
#
#Program
#
#Introduce Program to the user
print("Welcome to the ancient egyption method of multiplication")

#Check validity of values to be entered by user

def input_integer (prompt_str):

  requested_bool = False

  while requested_bool == False:

    in_str=input(prompt_str)

    if (in_str[0]=='+' or in_str[0]=='-') and in_str[1:].isdigit():

      number_int = int(in_str)

      requested_bool = True

    elif in_str.isdigit():

      number_int = int(in_str)

      requested_bool=True

    else:

      print(in_str, "is not an integer. Try again!")

  return number_int

#Introduce a function to calculate the product
def egypt():
#Take input of values from user
 a=int(input_integer("Enter an interger"))

#Store original values entered
 store_a=a

 b=int(input_integer("Enter Another integer"))

 store_b=b

 product=0

#Count number of iterations by count_int
 count_int=0

#Calculations- Till the 2nd number>0, check if 2nd number is odd/even
#If odd, add 1st number to product. Multiply 1st number by 2 and devide
#2nd number by 2. Follow process till b becomes zero
 while b>0:

   count_int+=1

   if b%2==1:


     product+=a


   b//=2


   a=a*2


 print(store_a, "x", store_b, "=", product, "in", count_int, "iterations")
#Call the function to execute
egypt()

#Ask user if he wants to execute the function again
check_str=input("Do you want to try another numbers[y/n]")

#Perform action according to user choice
while check_str=="y":

  egypt()

  check_str=input("Do you want to try another numbers[y/n]")


print("Bye. Have a Good day")
