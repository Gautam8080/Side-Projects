#Name- Gautam Bakliwal
#
#Course- CS 1411 lab 505
#
#Date- 10/31/2017
#
#Problem-
#Write a function to return a randomly generated 6-element integer set which represents one lotto ticket. For each
#drawing in the dictionary, check the matching numbers between the randomly generated ticket and the drawing. Total
#the winnings and report to the customer what s/he would have won had that ticket been played since the first reported 
#drawing in 1992. Also let the customer know what they would have spent on the lotto tickets by checking the length of
#the dictionary.
#
#Given are the cases
#Your lotto ticket is: [44, 46, 17, 20, 23, 27]
#Your total winnings from 1992 to 2017 are:  876
#You would have spent 2605 dollars on Texas Lotto Tickets from 1992 to 2017
#
#Your lotto ticket is: [32, 40, 41, 9, 19, 31]
#Your total winnings from 1992 to 2017 are:  1480
#You would have spent 2605 dollars on Texas Lotto Tickets from 1992 to 2017
#
#Method/Algorithm
#
#importing class csv and random
#opens the file lottotexas
#reads the file to reader
#Dictionary function to create dictionary of data as asked
# Function to generate random tickets with set of random numbers
#converting set to list to work upon
#to check number of tickets he bought in total
#checks all the numbers of the ticket generated with each list of csv file. 
#if the number maches then match_n0 is incremented
#Based on match_no account balance is increased acc to question
#match_no is again made 0 so that it can again be worked upon
#After all iterations and summing up, acc balace is printed
#As each iteration cost $1, amount of spend printed
#
#program
import csv                  #importing class csv and random
import random                
lottotexas=open('lottotexas.csv', 'r')  #opens the file lottotexas
reader = csv.reader(lottotexas)         #reads the file to reader
                             
def diction():
    dict={}
    for rows in reader:
        name=rows[1]+'/'+rows[2]+'/'+rows[3]                                        #Dictionary function to create dictionary of data as asked
        dict[name]={rows[4], rows[5], rows[6], rows[7], rows[8], rows[9]}

        
aset = set()
def gen():
    for i in range(0,6):                                          # Function to generate random tickets with set of random numbers
        aset.add(random.randint(1,54))
    return aset
acc=0
gen()
list1=list(aset)                                            #converting set to list to work upon
print('Your lotto ticket is:',list1)
i=0
x=0
match_no=0
for rows in reader:
    x+=1                                                   #to check number of tickets he bought in total
    for i in range(0,6):                                   #checks all the numbers of the ticket generated with each list of csv file. 
        if list1[i]==int(rows[4]):
            match_no+=1
        if list1[i]==int(rows[5]):                      #if the number maches then match_n0 is incremented
            match_no+=1
        if list1[i]==int(rows[6]):
            match_no+=1
        if list1[i]==int(rows[7]):
            match_no+=1
        if list1[i]==int(rows[8]):
            match_no+=1
        if list1[i]==int(rows[9]):
            match_no+=1

    if match_no == 2:                                    #Based on match_no account balance is increased acc to question
        acc+=2

    if match_no == 3:
        acc+=10

    if match_no == 4:
        acc+=100

    if match_no == 5:
        acc+=10000

    if match_no == 6:
        acc+=1000000

    match_no=0                 #match_no is again made 0 so that it can again be worked upon
print('Your total winnings from 1992 to 2017 are: ', acc)                                     #After all iterations and summing up, acc balace is printed
print("You would have spent {} dollars on Texas Lotto Tickets from 1992 to 2017".format(x))   #As each iteration cost $1, amount of spend printed


