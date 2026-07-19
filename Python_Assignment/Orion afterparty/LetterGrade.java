//collect input from user five times import java.util.Scanner;
//check average sum divide by frequency
//assign grade to each number of it 
//condition each grade to their letter grades
//print the average associated with each grade
import java.util.Scanner;
public class LetterGrade{
	public static void main(String[] args){
	
	Scanner input= new Scanner(System.in);
	
	System.out.print("Enter first grade");
	int score1 = input.nextInt();
	
	System.out.print("Enter second grade");
	int score2 = input.nextInt();
	
	System.out.print("Enter third greade");
	int score3 = input.nextInt();
	
	int sum = 0;
	int grade = 0;
	
	grade = score1 + score2 + score3;
	
	sum = grade;
	
	grade = sum / 3;
	
	if(grade > 90 && grade <= 100){
		System.out.print("A");
	}
	else if(grade > 80 && grade <= 90){
		System.out.print("B");
	}
	else if(grade > 70 && grade <= 80){
		System.out.print("C");
	}
	else if(grade > 60 && grade <= 70){
		System.out.print("D");
	}
	else if(grade < 60){
		System.out.print("F");
		System.out.print("Repeat the course");
	}
	
	System.out.print(grade);
	}
 }
