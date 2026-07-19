#collect user input
#input as current fathers age and current sons age
#a variable as father years before as twice the son 
#a variable for years he will be twice as sons age 
#fathers current and  sons current age to the fathers age when he was twice the sons age
#fathers current age plus or equal to sons age
#print years twice as old 
#print years when he was twice as sons age

fathersAge = print("Enter fathers age from 1 to 80")
	
sonsAge = print("Enter sons age from 1 to 80")
	
yearsDifference = 0
fathersAgeAgo = 0
twiceAsOld = 0
	
if(fathersAge > sonsAge):
	yearsDifference = sonsAge * 2
	sonsAge = yearsDifference
	yearsDifference = (fathersAgeAgo - sonsAge)
	
if(fathersAge > sonsAge):
	twiceAsOld = fathersAge + sonsAge
	fathersAge = twiceAsOld / 2
	twiceAsOld = fathersAge		
	
	print(yearsDifference, twiceAsOld)
	


