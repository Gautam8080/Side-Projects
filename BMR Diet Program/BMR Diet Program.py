#program
import csv                                                           #Importing necessary libraries
from tempfile import NamedTemporaryFile
import shutil

print('The Following program can do-\n *Take input of client name\n *Check if it exists in csv file\n *If existes, then print the previous details and ask for new details\n *New details will replace the previous details\n *If name does not exist, then add the name to the file with entered details\n *With the entered details, it will calculate as required\n *Will ask user if he wishes to losse weight\n *Gives recomendations on healthy foods and fat food calories\n')
client_name=input('Enter Full Name of Client: ')                      #Take input of client name      
d=open('client.csv', 'r+')                                            #opening file for reading
e=open('client.csv', 'a+', newline='')                                #opening file for writing(append)
reader = csv.reader(d)
writer = csv.writer(e)
gender='f'
weight=0
height=0
age=0
act_level=0
n=0
bmr=0
row=0
valid_input_bool=False

######################################################

for row in reader:                                                    #Checking if the name already exists and break search when found
    if row[0]==client_name:
        gender_read=row[1]
        weight_read=float(row[2])
        height_read=float(row[3])
        age_read=int(row[4])
        act_level_read=int(row[5])
        n=1
        break


if n==1:                                                              #If exist, then print the previous details
    print('Client information based on previous data is as follows-')
    print('Gender:', gender_read)
    print('Weight:', weight_read, 'pounds')
    print('Height:', height_read, 'inches')
    print('Age:', age_read, 'years')
    print('Level of activity:', act_level_read)
    print()
    print('Enter new details below-')
    print()

########################################################
    
while not valid_input_bool:                                           #Taking input of all details of client and asking again until user enter right type of value
    gender=input('Enter your Gender(m/f): ')   
    if gender=='m' or gender=='f':
        valid_input_bool=True
    else:
        continue
    
valid_input_bool = False
    
while not valid_input_bool:
    try:
        weight=float(input('Enter your weight in pounds: '))
        valid_input_bool = True
    except ValueError:
        print("Bad Input. Enter again.")
        valid_input_bool = False
          
valid_input_bool = False
    
while not valid_input_bool:
    try:
        height=float(input('Enter your height in inches: '))
        valid_input_bool = True
    except ValueError:
        print("Bad Input. Enter again.")
        valid_input_bool = False
            
valid_input_bool = False
    
while not valid_input_bool:
    try:
        age=int(input('Enter your age in years: '))
        valid_input_bool = True
    except ValueError:
        print("Bad Input. Enter again.")
        valid_input_bool = False
        
valid_input_bool = False
    
while not valid_input_bool:
    try:    
        act_level=int(input('Enter your level of activity on a scale of 1 to 5(1 being low, 5 being high): '))
        if act_level>=1 and act_level<=5:
            valid_input_bool = True
        else:
            print('Enter from 1 to 5 only')
            valid_input_bool=False
    except ValueError:
        print("Bad Input. Enter again.")
        valid_input_bool = False

print()

#########################################################

if n==0:                                                              #If the name does not exist then append the details with name to the file
    writer.writerow([client_name, gender, weight, height, age, act_level])

tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')     #Opening temporary file and writing in it and then moving its contents to original file at the end

fields = ['Name', 'Gender', 'Weight', 'Height', 'Age', 'Activity Level']

with open('client.csv', 'r') as csvfile, tempfile:        
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:                                                #checking if the name exists in the file. If yes then replace the details of name with new details in the temporary file
        if row['Name'] == client_name:
            print('updating row of', row['Name'])
            row['Gender'], row['Weight'], row['Height'], row['Age'], row['Activity Level'] = gender, weight, height, age, act_level
        writer.writerow(row)
shutil.move(tempfile.name, 'client.csv')                              #Moving the contents of temporary file to original file

#########################################################

if gender=='m':                                                       #Calculating bmr and hbf according to values entered by the user
    bmr= 66 + ( 6.23 * weight) + ( 12.7 * height) - ( 6.8 * age)
else:
    bmr= 65.5 + ( 4.35 * weight) + ( 4.7 * height) - ( 4.7 * age)

if act_level==1:
    hbf=bmr*1.2
if act_level==2:
    hbf=bmr*1.375
if act_level==3:
    hbf=bmr*1.55
if act_level==4:
    hbf=bmr*1.725
if act_level==5:
    hbf=bmr*1.9
print()
print('Your BMR is ', bmr, '\nYour Daily Calorie need is ', hbf, '\nYour Daily fat calorie should range from {} to {}'.format(0.2*hbf, 0.3*hbf), '\nIn Fat grams from {} to {}'.format(0.2*hbf/9, 0.3*hbf/9))
print()
wish=input('Do you wish to loose weight(y/n):')
print()
if wish=='y':                                                         #Asking user if he wishes to loose weight. If yes then show him new daily cal need
    print('To loose weight, decrease calorie intake by 10%. Eat only {} calories'.format(0.9 * hbf))
    print('Keep daily fat calories from {} to {}'.format(0.9*0.2*hbf, 0.9*0.3*hbf))
    print('In fat grams from {} to {} grams daily'.format(0.9*0.2*hbf/9, 0.9*0.3*hbf/9))

print('\nFood recomendations-')
print('Breakfast-\n*Oats/n*Cottage Cheese\n*Any 3 fruits\n*Peanut butter\n*Whole wheat or multigrain bread\n')
print('Lunch-\n*Brown Rice\n*Lentils\n*Veggie Sandwich\n*Tortillas+veggies\n')
print('Snacks-\n*Juice\n*bread with cheese\n*Sub\n*Nuts\n')
print('Dinner-\n*Whole wheat pasta\n*Whole wheat noodles\n*Tortillas with beans\n')
print('Keep track of your fat calories-\nFrench Fries, 570, 30\nOnion Rings, 350, 16\nHamburger, 670, 39\nCheeseburger, 760, 47\nGrilled Chicken Sandwich, 420, 10\nEgg Biscuit, 300, 12\nMozzarella Sticks, 849, 56\nCheese Pizza, 300, 11\nMacaroni and Cheese, 300, 7\nGlazed Chicken and Veggies, 497, 7')
d.close()
e.close()

