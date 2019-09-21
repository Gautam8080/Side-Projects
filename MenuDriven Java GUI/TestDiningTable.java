package testdiningtable;

/*
Name - Gautam Bakliwal
R - R11498749
Group - 30
Contribution - 100% (We are submitting indivisual codes)

Q} Create a class DiningTable with attributes cost, weight, length and width. Provide methods that calculate the Table’s perimeter and area. 
It has set and get methods for weight, length and width. The set methods should verify that weight, length and width are all floating-point 
numbers larger than 0.0 and less than 20.0. Also provide the cost method which generates the cost of DiningTable in dollars using the formula:
cost = weight * length * width
Write a class TestDiningTable to test the class DiningTable. In the TestDiningTable class, use a ‘while’ loop to call each method of DiningTable 
class using input from keyboard (using Scanner class). If the values are not correct input again and show the results in a formatted manner 
using JOptionPane. Program stops if there is no more test data. Data encapsulation required.

Input
length, width and weight

Output 
Area of Table
Perimeter of atable
Cost of Table
*/
import java.util.Scanner;
import javax.swing.JOptionPane;
class DiningTable {
  private double cost, weight, length, width;
  public DiningTable() {
    weight = 0;
    length = 0;
    width = 0;
  }

  public double getWeight() {
    return weight;
  }

  public double getLength() {
    return length;
  }

  public double getWidth() {
    return width;
  }

  public void setWeight(double wght) {
    if (wght > 0.0 && wght < 20.0) {
      weight = wght;
    } else {
      System.out.println("weight is not in range!");
    }
  }

  public void setLength(double len) {
    if (len > 0.0 && len < 20.0) {
      length = len;
    } else {
      System.out.println("length is not in range!");
    }
      
  }

  public void setWidth(double wid) {
    if (wid > 0.0 && wid < 20.0) {
      width = wid;
    } else {
      System.out.println("width is not in range!");
    }
   
  }

  public double calcPerim() {
    return 2 * (length + width);
  }

  public double calcArea() {
    return (length * width);
  }

  public double calcCost() {
    return (weight * length * width);
  }

}

class TestDiningTable{
  public static void main(String[] args) 
  {
    //JOptionPane.showMessageDialog(null, "5", "Formatted Results", JOptionPane.PLAIN_MESSAGE)
    //JOptionPane.showInternalMessageDialog("null", "information","information", JOptionPane.INFORMATION_MESSAGE);
    double num1, num2, num3;
    DiningTable d = new DiningTable();
    Scanner sc = new Scanner(System.in);

    double weight, weight2;
    System.out.println("Enter the weight: ");
    weight = sc.nextDouble();
    d.setWeight(weight); 
    num1 =d.getWeight();
    
    while(num1 == 0.0)
    {
        System.out.println("Enter the weight again: ");
        weight2 = sc.nextDouble();
        d.setWeight(weight2); 
        num1 = d.getWeight(); 
    }
     
    double length, length2; 
    System.out.println("Enter the Lenghth: ");
    length = sc.nextDouble();
    d.setLength(length); 
    num2 = d.getLength();
    
    while(num2 == 0) 
    {
        System.out.println("Enter the Lenghth again: ");
        length2 = sc.nextDouble();
        d.setLength(length2); 
        num2 = d.getLength(); 
    }
     
    double width, width2; 
    System.out.println("Enter the Width: ");
    width = sc.nextDouble();
    d.setWidth(width); 
    num3 = d.getWidth(); 
    
    while(num3 == 0) 
    {
        System.out.println("Enter the Width again: ");
        width2 = sc.nextDouble();
        d.setWidth(width2); 
        num3 = d.getWidth(); 
    }
    String msg = "Area of Dining Table : " + Double.toString(d.calcArea()) + "\nPerimeter of Dining Table: " + Double.toString(d.calcPerim()) + "\nCost of TDining Table : " + Double.toString(d.calcCost());
    JOptionPane.showMessageDialog(null, msg , "Formatted Results", JOptionPane.PLAIN_MESSAGE);
    System.ut.println("Minimize this screen if can't view result in JOption Box")
    //System.out.println("Area of rectangle with length="+d.getLength()+" and width="+ d.getWidth() + "is :" + d.calcArea());
    //System.out.println("Perimeter of rectangle with length="+d.getLength()+" and width="+ d.getWidth() + "is :" + d.calcPerim());
    //System.out.println("Cost of table with length="+d.getLength()+", width="+ d.getWidth() + "and weight = " + d.getWeight() + "is :" + d.calcCost());
     
  }
}
