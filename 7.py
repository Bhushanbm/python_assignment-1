import sys

def script_5(height, weight):
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

if __name__ == '__main__':
    name = sys.argv[1]
    name = sys.argv[1]
    height = float(sys.argv[2])
    wieght = float(sys.argv[3])
    print(f"Name: {name}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")
    print(script_5(height, weight))
