
import java.io.*; 
import static java.lang.Math.*; 
class Quadraticequation 
{ 
  public static void main(String args[]) 
    { 
       Quadraticequation obj = new Quadraticequation(); 
       int a = 1, b = -7, c = 12; 
       obj.findRoots(a, b, c); 
    } 
  
    // Prints roots of quadratic  
    //equation ax * 2 + bx + x 
    void findRoots(int a, int b, int c) 
    { 
      
     int d  = b*b - 4*a*c; 
     double sqrt_val = sqrt(abs(d)); 
     
     if (a == 0) 
     { 
         // If a is 0, then equation is not      
     //quadratic, but linear 
        System.out.println("euation is not quadratic but linear"); 
        return; 
     } 
   
   
     if (d > 0) 
     { 
        System.out.println("Roots are real and different \n"); 
  
        System.out.println((double)(-b + sqrt_val) / (2 * a) + "\n" 
                            + (double)(-b - sqrt_val) / (2 * a)); 
     } 
     else // d < 0 
     { 
        System.out.println("Roots are complex \n"); 
  
        System.out.println( -(double)b / ( 2 * a ) + " + i" 
                          + sqrt_val + "\n"  + -(double)b / ( 2 * a ) 
                          + " - i" + sqrt_val); 
     } 
    } 
   
 // main code
 
} 
