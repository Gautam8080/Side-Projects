import csv
import random
csvfile  = open("emailwithpass.csv", "r")
passfile  = open("10millionpass.txt", "r")
textfile  = open("fil11.txt", "w")
csv_reader = csv.reader(csvfile, delimiter=',')
txt_reader = csv.reader(passfile, delimiter='\n')
line_count = 0
n=0
a=0
listpass = []
for line in txt_reader:
    if (a == 100000):
        print(line)
        break
    if ((len(line[0])) < 4):
        continue
    listpass.append(line[0])
    a = a + 1
for row in csv_reader:
    if (n == 5000):
        break
    strarr = row[1].split()
    if (len(strarr) > 2) or (len(strarr) < 2) or (len(strarr[-1]) == 1) or (len(strarr[0]) == 1):
        continue
    textfile.write(row[0])
    textfile.write("\n")
    textfile.write(strarr[0])
    textfile.write("\n")
    textfile.write(strarr[-1])
    textfile.write("\n")
    miden = int((len(row[0]) - 10)/2)
    midend = int(3*(len(row[0]) - 10)/4)
    
    password = ""
    while (len(password) > 12 or len(password) < 4 ):
        miden = int((len(row[0]) - 10)/2)
        midend = int(3*(len(row[0]) - 10)/4)
        
        no1 = listpass[random.randint(0,len(listpass)-1)]
        
        stringrand = [strarr[-1], row[2], row[0][miden:midend]]
        no2 = no1 + stringrand[random.randint(0,len(stringrand)-1)]
        
        no3 = listpass[random.randint(0,len(listpass)-1)] + row[2]
        
        ran = [no1, no2, no3]
        password = ran[random.randint(0,len(ran)-1)]
        
    textfile.write(password)
    textfile.write("\n")
    n=n+1

csvfile.close()
textfile.close()
passfile.close()
