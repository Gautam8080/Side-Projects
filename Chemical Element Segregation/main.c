#include <math.h>
#include <stdio.h> /*Standard Libraries*/
#include <stdlib.h>
#include <string.h>

typedef struct {
  char *at_no;
  char *symbol;
  char *at_mass;
  char *name;
  char *el_class;
} element_t; /*defining our structt*/

void reading_func(element_t []);  /*function prototypes*/
void class_elements (element_t []);

int main(void) {
  element_t info[120];
  reading_func(info);
  class_elements (info);
  return 0;
}   /*called other functions that perform different operations*/

void reading_func(element_t info[120])
{

  char line[300]; 
  
  FILE *inp; int num, j;
  inp = fopen("Periodic.txt", "r");
  char *chunk;
  const char delim[2] = "\t";
  
  fgets(line, sizeof(line), inp); /*used to skip the header line in inputdata*/
  for (int i=0; i<118; i++)
  {
    fgets(line, sizeof(line), inp);  /*iterates through everyline*/
    int len = strlen(line);  
    line[len - 2]= 0; /*truncates the extra \n character at the end of line*/
    chunk = strtok(line, delim);  /*returns a pointer to the first string found in the line before delimiter tab*/
    if ( chunk != NULL) /*we iterate through line until we get null character at finish of line*/
    {
      info[i].at_no = strdup(chunk);
      chunk = strtok(NULL, delim); /*Splitting 2nd word.*/
      info[i].symbol = strdup(chunk);
      chunk = strtok(NULL, delim); /*Splitting 3rd word.*/
      info[i].at_mass = strdup(chunk);
      chunk = strtok(NULL, delim); /*Splitting 4th word.*/
      info[i].name = strdup(chunk);
      chunk = strtok(NULL, delim); /*Splitting 5th word.*/
      info[i].el_class = strdup(chunk);
    }
  }

} /*reads through the input file and stores the items in variables of struct*/

void class_elements (element_t info[])
{
  FILE *outp; /*opening the output file*/
  outp = fopen("OutputFile.txt", "w");
  int count;
  char *class_set[10] = {"nonmetal","metalloid", "noble gas", "alkali metal", "alkaline earth metal", "metal", "halogen", "transition metal", "lanthanoid", "actinoid"}; /*defining pure classes manually to check with all classes in the file*/
  for (int i = 0; i<10; i++) /*iterating through every class and checking it with all classes in file*/
  {
    fprintf(outp, "\nIn our class %s, the elements are as follows:\n", class_set[i]);
    count = 0;
    for (int k=0; k<118; k++)
    {
      int rec = strcmp(class_set[i], info[k].el_class);  /*comparing classes of file with our class set classes*/
      if (rec == 0)
      {
        count++;
        fprintf(outp, "%s\n", info[k].name);
        
      }
    }

    printf("\nNumber of elements that belong to %s class are:: %d", class_set[i], count);
  }
  printf("\n\nWe didn't make a seperate function for output file because it would have been repetition of the same code and the output to new file took barely 4 lines of extra code in this function");
} /*counts the elements in each class and prints that out. It also prints the class and its elements in the output file.*/
  


