# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

def bmi(weight, height):
	bmi = weight/(height**2)	# weight**2 = weight*weight

	if bmi <= 18.5:
		print("Underweight")
		return "Underweight"
	if bmi <= 25.0:
		print("Normal")
		return "Normal"
	if bmi <= 30.0:
		print("Overweight")
		return "Overweight"
	if bmi > 30:
		print("Obese")
		return "Obese"



bmi(50, 1.80) #"Underweight"
bmi(80, 1.80) #"Normal"
bmi(90, 1.80) #"Overweight"
bmi(110, 1.80) #"Obese"
bmi(50, 1.50) #"Normal"