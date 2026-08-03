import java.util.Scanner;
public class conversion{
	public static String temperatureValue(String temperature){
	
	Scanner input = new Scanner(System.in);
	
	System.out.print("Enter temperature in celsius: ");
	double temperature = input.nextDouble();
	
	double fahrenheit = 32 +(temperature * 1.8);
	
	double threshold = 60;
	
	if(fahrenheit < threshold){
		return "cold advisory";
		
	}else{
		return "Heat alert";
	}
	
	}
	
public static void main(String[] args){

String result = temperatureValue();

System.out.println(result);
}
}


