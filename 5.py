name = input("What is your name:")
print(name)
age = int(input(f"Hi {name}, What is your age :"))
print(age)
weight = float(input("what is your weight in kg:"))
print(weight)
height = float(input("what is your height in metres:"))
print(height)
BMI = round(weight/ (height * height), 1)
print(f"your BMI is {BMI}");
if BMI <= 18.5:
   print(f"Your BMI is {BMI} which means you are underweight")
elif BMI <= 24.9:
    print(f"Your BMI is {BMI} which means you are healthy")
elif BMI <= 29.9:
    print(f"Your BMI is {BMI} which means you are overweight")
elif BMI >= 30.0:
    print(f"Your BMI is {BMI} which means you are obese")



