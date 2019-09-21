#Name- Gautam Bakliwal
#
#Course- CS 1411
#
#Date- 10/24/2017
#
#Problem-
#Write a function to take a 70-character string of Myers Briggs responses and return a list of the percentage of B’s in each
#dimension. For the 70-character string in the Problem Background, the list that should be returned is [30,45,10,10].
#Write another function to take a list of percentages and return the Myers Briggs 4-dimension types as single letters. In
#the case of [30,45,10,10], the function should return the string ‘ISTJ’.
#Write a program to test the first function by placing in a list the following 70-character strings like the example in the
#Programming Section above:
#
#Given are the cases
#  A 70-character string of all A’s
#• A 70-character string of all B’s
#• A 70-character string of half A’s then half B’s
#• A 70-character string of alternating ABABABA….
#• The string in the problem background.
#• BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA
#• AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB
#
#Analysis
#Output
#Test 1: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#Result 1: [0.0, 0.0, 0.0, 0.0]
#
#Test 2: BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#Result 2: [100.0, 100.0, 100.0, 100.0]
#
#Test 3: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#Result 3: [50.0, 50.0, 50.0, 50.0]
#
#Test 4: ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB
#Result 4: [50.0, 50.0, 50.0, 50.0]
#
#Test 5: BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA
#Result 5: [30.0, 45.0, 10.0, 10.0]
#
#Test 6: BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA
#Result 6: [60.0, 30.0, 10.0, 20.0]
#
#Test 7: AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB
#Result 7: [80.0, 30.0, 40.0, 50.0]
#
#Test 1:  [0.0, 0.0, 0.0, 0.0]
#Result:  ISTJ
#
#Test 2:  [100.0, 100.0, 100.0, 100.0]
#Result:  EIFP
#
#Test 3:  [50.0, 50.0, 50.0, 50.0]
#Result:  EIFP
#
#Test 4:  [50.0, 50.0, 50.0, 50.0]
#Result:  EIFP
#
#Test 5:  [30.0, 45.0, 10.0, 10.0]
#Result:  ISTJ
#
#Test 6:  [60.0, 30.0, 10.0, 20.0]
#Result:  ESTJ
#
#Test 7:  [80.0, 30.0, 40.0, 50.0]
#Result:  ESTP
#
#Method/Algorithm
#
#defined the function to calculate percent and return percent list
#input in b is string. This converts to list of char
#first list of chars with answers of 1st test
#2nd list of char with test 2 and 3 answers
#3rd list of char with test 4 and 5 answers
#4th list of char based on test 6 and 7 answers
#if list 1,2,3,4 has any B --> Value of number increases and percent of B is calculated in each list
#List of calculated percents made and returned
#defined 2nd function to check the results based on the percentage calculated in previous function
#if percents is less than 50, one result comes else alternative result obtained.
#All results concatenated
#Prints the results when function is called
#Calling function in print and inputting given values in all cases
#prints the percent according to input as required
#check function is called which prints results according to the value entered in previous calc function in all cases
#
#Program
def calc(b):          #defined the function to calculate percent and return percent list
  c=list(b)           #input in b is string. This converts to list of char
  list1=c[::7]        #first list of chars with answers of 1st test 
  list2=c[1::7]
  list2= list2 + c[2::7]   #2nd list of char with test 2 and 3 answers 
  list3=c[3::7]
  list3=list3+ c[4::7]     #3rd list of char with test 4 and 5 answers 
  list4=c[5::7]
  list4=list4 + c[6::7]    #4th list of char based on test 6 and 7 answers
  number1=0
  number2=0
  number3=0
  number4=0
  global percent1 
  global percent2
  global percent3
  global percent4
  global percent
  
  for option in list1:          #if list 1,2,3,4 has any B --> Value of number increases and percent of B is calculated in each list
    if option == 'B':
      number1=number1+1
  percent1=(number1/10)*100

  for option in list2:
    if option == 'B':
      number2=number2+1
  percent2=(number2/20)*100

  for option in list3:
    if option == 'B':
      number3=number3+1
  percent3=(number3/20)*100

  for option in list4:
    if option == 'B':
      number4=number4+1
  percent4=(number4/20)*100
  
  percent=[percent1, percent2, percent3, percent4]    #List of calculated percents made and returned
  return percent
  
def check():                      #defined 2nd function to check the results based on the percentage calculated in previous function
  if percent1 < 50:                #if percents is less than 50, one result comes else alternative result obtained.
    result1='I'
  else:
    result1='E'
  
  if percent2 < 50:
    result2='S'
  else:
    result2='I'
  
  if percent3 < 50:
    result3='T'
  else:
    result3='F'
  
  if percent4 < 50:
    result4='J'
  else:
    result4='P'
  result=result1+result2+result3+result4    #All results concatenated
  print('Result: ', result)                  #Prints the results when function is called
  
  
print('Test 1: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA') 
print('Result 1:', calc('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))  #Calling function in print and inputting given values in all cases
print()

print('Test 2: BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB') 
print('Result 2:', calc('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'))   #prints the percent according to input as required
print()

print('Test 3: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB') 
print('Result 3:', calc('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
print()

print('Test 4: ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB') 
print('Result 4:', calc('ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB'))
print()

print('Test 5: BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA') 
print('Result 5:', calc('BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA'))
print()

print('Test 6: BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA') 
print('Result 6:', calc('BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA'))
print()

print('Test 7: AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB') 
print('Result 7:', calc('AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB'))
print()




print("Test 1: ",calc('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))   
calc('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
check()                                         #check function is called which prints results according to the value entered in previous calc function in all cases
print()

print("Test 2: ",calc('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
calc('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
check()
print()

print("Test 3: ",calc('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
calc('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
check()
print()

print("Test 4: ",calc('ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB'))
calc('ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB')
check()
print()

print("Test 5: ",calc('BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA'))
calc('BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA')
check()  
print()

print("Test 6: ",calc('BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA'))
calc('BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA')
check()
print()

print("Test 7: ",calc('AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB'))
calc('AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB')
check()
  
  
