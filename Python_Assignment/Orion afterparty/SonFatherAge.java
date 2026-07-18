//collect user input
//input as current fathers age and current sons age
//a variable as father years before as twice the son 
//a variable for years he will be twice as sons age 
//fathers current and  sons current age to the fathers age when he was twice the sons age
//fathers current age plus or equal to sons age
//print years twice as old 
//print years when he was twice as sons age
import java.util.Scanner;
public class SonFatherAge{
	public static void main(String[] args){
	
	Scanner input= new Scanner(System.in);
	
	System.out.print("Enter fathers age from 1 to 80");
	int fathersAge = input.nextInt();
	
	System.out.print("Enter sons age from 1 to 80 ");
	int sonsAge = input.nextInt();
	
	int yearsDifference = 0;
	int fathersAgeAgo = 0;
	int twiceAsOld = 0;
	
	if(fathersAge > sonsAge){
		yearsDifference = sonsAge * 2;
		sonsAge = yearsDifference;
		yearsDifference = (fathersAgeAgo - sonsAge);
	}
	
	if(fathersAge > sonsAge){
		twiceAsOld = fathersAge + sonsAge;
		fathersAge = twiceAsOld / 2;
		twiceAsOld = fathersAge;		
	}
	System.out.printf("\n%d \n%d", yearsDifference, twiceAsOld);
	
	}
}
