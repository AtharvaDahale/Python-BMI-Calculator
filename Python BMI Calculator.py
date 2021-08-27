height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in Kg: "))
height = height/100
BMI = weight/(height*height)
print("Your BMI is: ",BMI)
if (BMI > 0):
    if(BMI<=16):
        print("Your are severely underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("You are healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are severely overweight")
else:("enter valid details")