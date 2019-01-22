# BASICS OF MAKING CALCULATOR BY USING PYTHON 
def add (x, y):
	"""this function adds 2 numbers"""
	return x + y
def subtract (x, y):
	"""this function subtract 2 numbers"""	
	return x - y
def multiply (x, y):
	"""this function multiply 2 numbers"""
	return x * y
def divide (x, y):
	"""this function divide 2 numbers"""
	return x /y
def power (x, y):
	"""this function gives power of  2 numbers"""
	return pow (x,y)
       
# take input from users 
print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.power")
choice = input("enter choice (1/2/3/4/5):")
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if choice == '1':
	print(num1, "+" , num2, "=" ,  add(num1, num2))
elif choice == '2':
	print(num1, "-", num2, "=" , subtract(num1, num2))
elif choice == '3':
	print(num1, "*", num2, "=" , multiply(num1, num2))
elif choice == "4":
	print(num1, "/", num2, "=" , divide(num1, num2))
elif choice == "5":
	print(num1, "^", num2, "=" ,power(num1, num2))
else :
	print("invalid input")
