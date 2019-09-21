
/*Name- Gautam Bakliwal

Course- CS 1411 lab 505

Date- 11/28/2017

Problem-
 * Write and test a C function named straw() that accepts the number of students and the total pounds picked as input
arguments, and returns the number of strawberries each student receives.

Given are the cases
 * Enter the number of students(0-5000)=> 3
 * Enter the number of pounds of strawberries picked by students(0-5000)=> 40
 * Result -Of 40.000000 pounds, students will receive 20.000000 pounds plus the owners are adding 1 strawberries for a total of 321.000000 strawberries
 * Each Student receives 107.000000 strawberries

 * Enter the number of students(0-5000)=> 2
 * Enter the number of pounds of strawberries picked by students(0-5000)=> 5
 * Result - Of 5.000000 pounds, students will receive 2.500000 pounds for a total of 40.000000 strawberries
 * Each Student receives 20.000000 strawberries

Method/Algorithm

 * defining variables to be used
 * Asking input again and again until user enter right value 
 * Asking input of number of students
 * Asking input again and again until user enter right value
 * Asking input of pounds picked by students
 * pounds that students should receive except extra strawberries
 * pounds to strawberry conversion 
 * To check if strawberries can be equally devided between students
 * if strawberries can be equally devided, print the straberries
 * if not, print the strawberries including extra strawberries that would be added by owners
 * strawberries + extra that should be added

program */

#include <stdio.h>

int main()
{
int n=0;                                              /* defining variables to be used */
int students, x;
float st_receive, pounds, st_straw, new_rec;
printf ("Welcome to pick your Strawberry Program");
while (n==0)                                          /* Asking input again and again until user enter right value */
{
    printf ("\nEnter the number of students(0-5000)=>");              /* Asking input of number of students */
    scanf("%d", &students);                                                 
    if (students>0 && students<5000)
        n=1;
}
n=0;
while (n==0)                                          /* Asking input again and again until user enter right value */
{
    printf ("Enter the number of pounds of strawberries picked by students(0-5000)=>");         /* Asking input of pounds picked by students */
    scanf("%f", &pounds);
    if (pounds>0 && pounds<5000)
        n=1;
}
st_receive=pounds/2;                          /* pounds that students should receive except extra strawberries */

st_straw=st_receive*16;                        /* pounds to strawberry conversion */
x= (int) st_straw % students;                  /* To check if strawberries can be equally devided between students */
printf("\n");

if (x==0)                                       /* if strawberries can be equally devided, print the straberries */
{
    printf("Of %f pounds, students will receive %f pounds for a total of %f strawberries ", pounds, st_receive, st_straw);
    printf("\nEach Student receives %f strawberries", st_straw/students);  
}
else                                          /* if not, print the strawberries including extra strawberries that would be added by owners */
{
    new_rec=st_straw+students-x;             /* strawberries + extra that should be added */
    printf("Of %f pounds, students will receive %f pounds plus the owners are adding %d strawberries for a total of %f strawberries ", pounds, st_receive, students-x, new_rec);
    printf("\nEach Student receives %f strawberries", new_rec/students);
}

return 0;
}            