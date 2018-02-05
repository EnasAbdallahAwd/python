def calcarea(shape,num1,num2=1):
	if shape == "r":

		return num1*num2*0.5




	elif shape == "t":

		return num1*num2




	elif shape == "s":

		return num1*num1


	elif shape == "c":
		return 3.14*num1*num1


if __name__=='__main__':
	shape=input("enter shape:")
	num1=float(input("Enter length:"))
	num2=float(input("Enter width:"))
	print(calcarea(shape,num1,num2))
