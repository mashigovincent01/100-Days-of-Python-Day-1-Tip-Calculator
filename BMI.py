#formula BMI = weight (kg)/ (height^2) (m^2)
#get the height and weight and output the BMI as a whole number

height = float(input('Enter your height in meters: '))
weight = float(input("Enter your weight in kilograms: "))

BMI = weight // (height**2)
print(f"Your BMI is {BMI}")