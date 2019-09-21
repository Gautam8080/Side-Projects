#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  double mnt;
  int exp;
} sci_not_t;
double numberret(sci_not_t number1);
double quotient(sci_not_t number1, sci_not_t number2);
double product(sci_not_t number1, sci_not_t number2);
sci_not_t scan_sci(char str1[50]);

int main() 
{    
    sci_not_t number1;
    number1.mnt = 0; 
    sci_not_t number2;
    number2.mnt = 0;
    char input1[50],input2[50];

    while(number1.mnt == 0){
      printf("\nEnter first number:");
      scanf("%s", input1);
      number1 = scan_sci(input1);
      printf("Mantissa: %f", number1.mnt);
      printf("\nExponent: %d", number1.exp);    
    }

    while(number2.mnt == 0){
      printf("\n\nEnter Second number:");
      scanf("%s", input2);
      number2 = scan_sci(input2);
      printf("Mantissa: %f", number2.mnt);
      printf("\nExponent: %d", number2.exp);
    }

    printf("\n\nNumber 1: %f", numberret(number1));
    printf("\nNumber 2: %f", numberret(number2));
    product(number1, number2);
    quotient(number1, number2);
    return 0; 
} 

sci_not_t scan_sci(char str1[50]) {
  sci_not_t number;
  char str31[50];
  char str32[50];

  for (int i=0; i<50; i++)
  {
    if(str1[i] == 'e')
    {
      str32[0] = str1[i+1];
      break;
    }
    str31[i] = str1[i];
  }

  number.mnt = atof(str31);
  if(number.mnt < 0.1 || number.mnt > 0.9){
    printf("\nPlease Enter a number between 0.1 to 0.9 as mantissa\n");
    number.mnt = 0;
  }
  number.exp = atof(str32);
  return number;
}

double numberret(sci_not_t number) {
  double result = 1;
  int exponent = number.exp;
  int base = 10;
    while (exponent != 0)
    {
        result *= base;
        --exponent;
    }
  return result*number.mnt;
}

double product(sci_not_t number1, sci_not_t number2) {
 double num = numberret(number1)*numberret(number2);
 
 int exponent = (int)log10(fabs(num));
 double mantissa = num / pow(10, exponent);
 printf("\n\nProduct: %fe%d", mantissa/10, exponent+1);
 return num;
}

double quotient(sci_not_t number1, sci_not_t number2){
  double num = numberret(number1)/numberret(number2);

  int exponent = (int)log10(fabs(num));
  double mantissa = num / pow(10, exponent);
  printf("\nQuotient: %fe%d\n", mantissa/10, exponent+1);
  
  return num;
}
