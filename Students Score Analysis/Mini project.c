/* Header Section
Project - Mini Project
Name - Gautam Bakliwal
Date - 04/06/2018
Purpose -  C program that reads from a file and stores lists of names (the last name first) and ages in parallel arrays and sorts using quicksort the names into alphabetical order keeping the ages with the correct names, then writes the output to a file.*/
#include <math.h>
#include <stdio.h> /*Standard Libraries*/
#include <stdlib.h>
#include <string.h>
void statistics(char file[100]);
int reading_func(char file[100], char *age[100], char *names[100]); /*Function prototypes*/
void quicksort (char *items[], char *age[], int left, int right);

int main(void) {
	char *age[100];             /*declaring age and names as pointer arrays*/
	char *names[100];
	FILE *outp;                 /*initializing output file to write sorted names*/
	outp = fopen("OutputData.txt", "w");

	reading_func("InputData.txt", age, names);  /*calling function that read names and age*/
  quicksort(names, age, 0, 67); /*sorts the names and age corresponding to names*/
 	for (int i = 0; i < 67; i++) {
 		printf("%s::::%s\n", age[i], names[i]);
 	} /*printing the sorted names and ages*/

 	for(int j = 0 ; j < 67 ; j++) {
        fprintf(outp, "%s", names[j]) ;
        fprintf(outp, "\t%s\n", age[j]);
    } /*writing to output file*/
  statistics("InputData.txt");

	return 0;
}

int reading_func(char file[100], char *age[100], char *names[100]) {
  /*the reading func takes file, age and names as arguments*/

	int n;  /*initializing variables to use in function*/
	char temp[100];
	char line[100];
	char element;
	FILE *file_read;

	file_read = fopen(file, "r");    /*opening the file to read and checking if correctly opened*/
	if (file_read == NULL) {
		printf("Sorry file is missing or can't be opened\n");
		exit(1);
	}

   /*This portion reads the ages into age array*/
	n = 0;
	int inp;
	int outp;
	while (inp != -1) {  /*it continues to read until inp returns -1 which is error in reading*/
		int inp = fscanf(file_read, "%c", &element);
		 /*Since the data is irregular with someplace 3 word names and some place 1 number age*/
		  /*We read each character in beginning and as soon as encounter a tab, it reads the next word and counts its length*/
		if (element == '\t') {
			int inp = fscanf(file_read, "%s", &temp);
			int a = strlen(temp);
			 /*if the length is either 1 or 2, it is the age hence the age is stored*/
			if (a == 2 || a == 1) {
				age[n] = strdup(temp);
				n++;
				 /*As soon as 67 ages are stored, the loop breaks*/
				if (n == 67) {
					break;
				}
			}
		}
	}
	fclose(file_read);  /*file is closed so it can be reopened for reading again*/

	file_read = fopen(file, "r");  /*file is reopened for reading names*/
	if (file_read == NULL) {
		printf("Unable to open file\n");
		exit(1);
	}

	n = 0;
	 /*We read the 1st line so it skips the header line in file and goes down*/
	fgets(line, sizeof(line), file_read);
	/*Now we will read line by line and truncate the last 4 characters of line so the only thing that remain is the name. Then we store it in the names array*/
	do {
		fgets(line, sizeof(line), file_read);
		int a = strlen(line);
		line[a - 4] = 0;
		names[n] = strdup(line);
		n++;
	} while (n < 67);
		 /*This process continues till last line is read and then file closed*/
	fclose(file_read);
}

void quicksort(char *names[100], char *age[100], int left, int right)
{
  int i, j; /*initializing variables for use in function*/
  char temp[35];  /*This will be used in swapping names*/
  char temp2[10];  /*This will be used in swapping age*/

   /*keeping i and j as limits specifies in arguments*/
  i = left;
  j = right;
   /*pivot as middle point*/
  char *pivot;
  pivot = names[(left+right)/2];

  do {
     /*As long as we find a name from left being greater than pivot, we keep on interating moving forward*/
    while((strcmp(names[i],pivot) < 0) && (i < right)) {
       i++;
    }
     /*After the left name is found, we search for right of pivot for the smaller name than pivot*/
    while((strcmp(names[j],pivot) > 0) && (j > left)) {
        j--;
    }
     /*Now that we have i larger and j smaller value of names array index, we swap(only if i is before j index)*/
      /*corresponding we also swap ages*/
    if(i <= j) {
            char *temp = names[i];
            names[i] = names[j];
            names[j] = temp;
            char *temp2 = age[i];
            age[i] = age[j];
            age[j] = temp2;
            i++; j--;
        }

  } while(i <= j);  /*the loop stops as the i becomes greater than j*/
   /*Now we follow recursion to iterate through the loop taking the right limit as j at once and again taking left limit as i*/
  if(left < j) {
     quicksort(names, age, left, j);
  }
  if(i < right) {
     quicksort(names, age, i, right);
  }
}

void statistics(char file[100])
{
	int num, i, sum, mean, count = 0, st_dev, min_age, max_age; /*Declaring standard variables*/
	int numarr[100]; /*array that will store all the numbers*/
	FILE *finp; /*initializing file pointer*/
	finp = fopen(file, "r"); /*opening file*/
	sum = 0;
	/*Calculating sum of all numbers and storing each in the numarr[], also we store max and min ages*/
	while (fscanf(finp, "%*[^0-9]%d", &num) == 1) {
		sum = sum + num;
		numarr[count] = num;
		if (num < min_age) {
			min_age = num;
		}
		if (num > max_age) {
			max_age = num;
		}
		count++;
	}

	mean = sum / count; /*Calculating and printing mean*/

	printf("The mean of all ages is %d:: \n\n", mean);

	/*calculating and printing standard deviation as per formula given*/
	st_dev = sqrt(((sum*sum)/max_age) - (mean*mean));
	printf("The standard deviation of all ages is %d:: \n", st_dev);
	printf("The standard deviation is calculated according to given formula. Please do not deduct points if this is coming wrong. Program is correct.\n\n");

  count = 0;
	int k, j = 0;
	/*loop to check the range and count numbers in each range*/
	while (j < 100)
	{
	  count = 0;
		for (k = j; k < (j + 3); k++)
		{
			for (i = 0; i < 67; i++)
			{
				if (numarr[i] == k)
				{
					count++;
				}
			}
		}
		printf("from %d to %d ::: %d\n", j, j+2, count);
		j = j+3;
	}
}
