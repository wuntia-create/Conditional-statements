#Take height and weight input from user
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
#Calculate BMI
bmi = weight / (height ** 2)
#display BMI value
print(f"Your BMI is: {bmi:2f}")
#determine BMI category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi <29.9:
    print("You are overweight.")
else:
    print("You are obese.")