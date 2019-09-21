/*
Name - Gautam Bakliwal
Group 30
R number - R11498749
Contribution - 100% (We are writing indivisual codes)

Q3. Write a menu driven program which using switch-case and dowhile loop. Input option using JOpionPane. Write methods for each of
the following task. Invoke these methods from cases of switch
statement:
a) Use random number to fill an array of size 10 such that the 1st
element is divisible by 2, 2nd element by 3, 3rd element by 4 and
so on.
b) Display the array elements as a single string using JOptionPane. 
c) Readjust the elements of array such that the even entries
precede the odd entries and display the array elements as a
single String
d) Display the array list such that the second largest element of the
array is the last element of array
e) Exit the program 

Input
'a' or 'b' or 'c' or 'd' based on above options

Output
The program runs from scratch with every option so the output is different for every option. Look at the code!
a - "Great! The random numbers have been Generated"
b - Displaying the List of array based on given on a) option in question [44,9,12,70,24,35,16,90,40,44]
c - List of array based on option c) in question [44,12,70,24,16,90,40,44,9,35]
d - List of array based on option d) in question [44,12,35,24,16,90,40,44,9,70]
 */
package menudriven;

import java.util.Random;
import java.util.*;
import javax.swing.JOptionPane;
import static menudriven.Menudriven.requirementArr;

/**
 *
 * @author Gautam
 */
public class Menudriven {
    public static int[] requirementArr = new int[10];
    public static void main(String[] args) {
        String length = JOptionPane.showInputDialog("Enter your choice.\n - 'a' for generating random number with given conditins\n - 'b' to display array\n - 'c' for readjusting odd and even entries\n - 'd' for display list with 2nd largest at end");
        switch (length){
            case "a":
                HelperFunc.randomnum();
                JOptionPane.showMessageDialog(null, "Great! The random numbers have been Genrated", "Messege", JOptionPane.PLAIN_MESSAGE);
                break;
            case "b":
                HelperFunc.randomnum();
                HelperFunc.showmsg();
                break;
            case "c":
                HelperFunc.randomnum();
                HelperFunc.oddeven();
                break;
            case "d":
                HelperFunc.randomnum();
                HelperFunc.secondlarge();
                break;
            default:
                JOptionPane.showMessageDialog(null, "Wrong Choice! Restart the pogram.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    }


public class HelperFunc {
    public static void randomnum() {
        Random rand = new Random();
        int i=0;
        do {
            int n = rand.nextInt(100);
            if (n % (i+2) == 0){
                Menudriven.requirementArr[i] = n;
                i++;
            }
        }
        while (i<10);
        }
    public static void showmsg(){
        String strArray ;
        strArray = Arrays.toString(Menudriven.requirementArr);
        JOptionPane.showMessageDialog(null, strArray, "Display of numbers", JOptionPane.PLAIN_MESSAGE);
    }
    public static void oddeven(){
        List<Integer> evenarr = new ArrayList<Integer>();
        String strArray ;
        List<Integer> oddarr = new ArrayList<Integer>();
        //int a = 0;
        //int b = 0;
        for (int j = 0; j<10; j++) {
            if (Menudriven.requirementArr[j]%2 == 0) 
                evenarr.add(Menudriven.requirementArr[j]);
            else 
                oddarr.add(Menudriven.requirementArr[j]);
        }
        evenarr.addAll(oddarr);
        int[] arr = new int[evenarr.size()];
        for(int i = 0; i < evenarr.size(); i++) arr[i] = evenarr.get(i);
        String reqarr = Arrays.toString(Menudriven.requirementArr);
        strArray = Arrays.toString(arr);
        String msg = "original Arr : " + reqarr + "\nEven Odd rearranged Arr : " + strArray;
        JOptionPane.showMessageDialog(null, msg, "Result", JOptionPane.PLAIN_MESSAGE);
    }
    public static void secondlarge(){
        String strArray;
        int arr[] = Menudriven.requirementArr;
        int max = 0;
        int temp = 0;
        int maxindex = 0;
        int secmaxindex = 0;
        int secmax = 0;
        for (int i = 0; i < 10; i++) {
            if (arr[i] > max) {
                secmax = max;
                secmaxindex = maxindex;
                max = arr[i];
                maxindex = i;
            }
        }
        temp = arr[secmaxindex];
        arr[secmaxindex] = arr[9];
        arr[9] = temp;
        strArray = Arrays.toString(arr);
        JOptionPane.showMessageDialog(null, strArray, "Array with 2nd largest at end", JOptionPane.PLAIN_MESSAGE);
    }
}
    