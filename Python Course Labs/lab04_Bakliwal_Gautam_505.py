#Name- Gautam Bakliwal
#
#Course- 1411
#
#Date- 09/26/2017
#
#Problem-Encription and decryption of user input
# 
#Given- Utilize the encryption method described in the Programming 
#Section where the ciphertext becomes the even letters followed by 
#the odd letters in the message.
#
#Analysis-
#Test Cases
#Input- I have a ball, n
#Output- aeabl Ihv  al, I have a ball
#Do you want to try another numbers[y/n]
#Bye. Have a Good day
#
#Input- CS is ez af
#Output- Si za C se f, CS is ez af
#Do you want to try another numbers[y/n]
#Prompts again
#
#Input- Hello user
#Output- el sr Hloue, Hello user
#Do you want to try another numbers[y/n]
#Bye. Have a Good day
#
#Algorithm
#Introduce Program to the user
#Define a function to decript and encrypt

#Take input
#Process of encryption
#Process decryption
#Take lenght of str in a
#Take b as 0 and increment till a and alternatively

#print characters from encripted parts
#Call the function to execute and ask to try again
#Ask user if he wants to execute the function again
#Perform action according to user choice
#
#Program
#
#Introduce Program to the user
print("Welcome to the encryption program")

#Define a function to decript and encrypt

def ask():

#Take input

  str= input("Enter a string that needs to be encripted:")

#Process of encryption

  part_1=str[1: :2]

  part_2=str[0: :2]

  print("The cyphertext is:", part_1, part_2)

#Process decryption

#Take lenght of str in a

#Take b as 0 and increment till a and alternatively

#print characters from encripted parts

  a=len(str)

  b=0

  x=0

  y=0

  print("The message decrypted is: ", end='')

  while b<a:

    if b%2==0:

      print(part_2[x], end='')

      x=x+1

    elif b%2==1:

      print(part_1[y], end='')

      y=y+1

    b=b+1

#Call the function to execute and ask to try again
ask()

print("")
check_str=input("Do you want to try another numbers[y/n]")


#Perform action according to user choice

while check_str=="y":


  ask()

  print("")
  check_str=input("Do you want to try another numbers[y/n]")



print("Bye. Have a Good day")