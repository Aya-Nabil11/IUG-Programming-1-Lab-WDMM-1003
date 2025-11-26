# Take inputs using input functions
# Enter teh weight in KG (int)
# Enter the height in metters (float)
# calculate BMI = weight /height^2
# i need the BMI result to be an integer value;
weight=int(input("enter a weight: "))
height=float(input("enter a height: "))
bmi=int(weight/(height**2))
print("the bmi is "+str(bmi))