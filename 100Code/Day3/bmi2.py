
def bmiCalculator(height, weight):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return f"Your BMI is {bmi:.2f}, You are underweight"
    elif bmi < 25:
        return f"Your BMI is {bmi:.2f}, You have a normal weight."
    elif bmi < 30:
        return f"Your BMI is {bmi:.2f}, You are slightly overweight"
    elif bmi < 35:
        return f"Your BMI is {bmi:.2f}, You are obese"
    else:
        return f"Your BMI is {bmi:.2f}, You are clinically obese"


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

result = bmiCalculator(height, weight)
print(result)
