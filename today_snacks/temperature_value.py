

def temperature_conversion(temperature):
	
	fahrenheit = 32 +(temperature * 1.8)

	threshold = 60
	
	
	if fahrenheit < threshold:
		return "cold advisory"
	
	elif fahrenheit >= threshold:
		return "Heat alert"
		
temperature = float(input("temperature in celsius"))
result = temperature_conversion(temperature)	
print(result)			
