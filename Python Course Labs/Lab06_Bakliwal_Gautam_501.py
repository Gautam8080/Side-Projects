#Name- Gautam Bakliwal
#
#Kindly copy this in python compiler
#Course- CS 1411
#
#Date- 10/17/2017
#
#Problem- Write a recursive helper function called writeChars that accepts
#an integer parameter n and prints out a string returned
#by another recursive method that is called by writeChars 
#
#Given
#writeChars(0) prints out: The string is
#writeChars(1) prints out: The string is *
#writeChars(2) prints out: The string is **
#writeChars(3) prints out: The string is <*>
#writeChars(4) prints out: The string is <**>
#writeChars(5) prints out: The string is <<*>>
#writeChars(6) prints out: The string is <<**>>
#writeChars(7) prints out: The string is <<<*>>>
#writeChars(8) prints out: The string is <<<**>>>
#
#Analysis
#
#Method/Algorithm
#Function to deal with even input number of string wanted 
#Function to deal with even input number of string wanted  
#Function to deal with choosing which function to execute based upon input of user(odd/even)
#Execution of function for first time
#
#Test Cases
#input-5
#Output-<<*>>
#input- 6
#Output-<<**>>
#input- 0
#Output- 
#
#Program
#function to deal with odd input number of strings
def writeChars1(n):
  global input_str
  f=int(n)
  g=int(input_str/2)
  if f>(g+1):
    print('<', end="")
    writeChars1(n-1)
  elif f==(g+1):
    print('*', end="")
    writeChars1(n-1)
  elif  f<(g+1) and f>0:
    print('>', end="")
    writeChars1(n-1)
    return 1
  else:
    print("")
    try_again=input("Do you want to try again [yes/no]:")
    if try_again=='yes':
      input_str=int(input("Enter an integer for string size:"))
      choice()
    else:
      print("Good Bye!!")
#Function to deal with even input number of string wanted     
def writeChars2(n):
  global input_str
  f=int(n)
  g=int(input_str/2)
  if f>(g+1):
    print('<', end="")
    writeChars2(n-1)
  elif f==(g+1) or f==g and f!=0:
    print('*', end="")
    writeChars2(n-1)
  elif  f<(g) and f>0:
    print('>', end="")
    writeChars2(n-1)
    return 1
  else:
    print("")
    try_again=input("Do you want to try again [yes/no]:")
    if try_again=='yes':
      input_str=int(input("Enter an integer for string size:"))
      choice()
    else:
      print("Good Bye!!")  

#Function to deal with choosing which function to execute based upon input of user(odd/even)
def choice():
  global input_str
  try:
    if input_str%2==1:
      writeChars1(input_str)
    elif input_str%2==0:
      writeChars2(input_str)
  except ValueError:
    print("Invalid input")
    input_str=int(input("Enter an integer for string size:"))
    choice()
#Execution of function for first time
input_str=int(input("Enter an integer for string size:"))  
choice()   
 
  
