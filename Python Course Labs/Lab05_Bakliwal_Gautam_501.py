#Name- Gautam Bakliwal
#
#Course- 1411
#
#Date- 10/10/2017
#
#Problem-Web page maker
# 
#Given- Iwrite a program to enable a user to create a web page like 
#the one above. The user will be prompted for the name of the web 
#page file and its title.
#
#Analysis-
#Test Cases
#Input-myweb, mytitle, t, i, e
#Output- as expected
#
#Algorithm
#Introduce Program to the user
#open a new file for web page
#input title of web page 
#define functions for various tasks on webpage
#If user exits, give him the prepared web_page in the new file created in beggining
#Prepare webpage according to user input choices
#
#Program
#
#Introduce Program to the user
print("Welcome to webpage creator")

#Take input of file name
file_name=input("Enter a file name for the webpage:")

c=True

#open a new file for web page
while c==True:

  try:

    read_file=open(file_name, 'r')

    print("Enter a new File. This already exists.")

    file_name=input("Enter a file name for the webpage:")

  except:

    new_file=open(file_name, 'w')

    c=False

#input title of web page     

title=input("Please Enter Title of webpage")

body= '<html>\n<head>\n<title>'+title+'</title>\n</head>\n<body>\n'
#define functions for various tasks on webpage
def textline():

  global body

  text=input("Enter a textline to add to webpage:")

  ct1='<p>'+text+'</p>'

  body+=ct1



def imageline():

  global body

  img=input("Enter the name of image to be entered:")

  ct2="<img src="+img+">"

  body+=ct2



def boldtextline():

  global body

  boldtext=input("Enter the text to be in bold:")

  ct3= "<b>"+boldtext+"</b>"

  body+=ct3


#If user exits, give him the prepared web_page in the new file created in beggining
def colortextline():

  global body

  color=input("Enter text to be in color:")

  colortext=input("Enter color of font")

  ct4= "<font color="+color+">"+colortext+"</font>"

  body+=ct4



def exitprog():

  global body

  print("Preparing the web page....")

  print(body,file=new_file)

  print("The web page is now in"+file_name+"\nEnjoy your new web page")



#Prepare webpage according to user input choices
x=True

while x==True:

  a=input("""Web page Menu Addition Choices\n[t]extline\n[i]mage\n[b]boldtextline\n[c]colortextline\n[e]xit\nEnter choice to add in web page(t, i, b, c, e):""")
  

  if a=='t':

    textline()

  elif a=='i':

    imageline()

  elif a=='b':

    boldtextline()

  elif a=='c':

    colortextline()

  elif a=='e':

    exitprog()

    x=False

  else:

    print("Wong choice!!")
                
              
    
