#----------------------------------------------Assignment 2-----------------------------------------------------------------------------

#We use float and input to take in two numbers that can be a decimal, if we use int it will have an error as int can only take whole numbers
Number_1 = float(input("Enter first number!"))
Number_2 = float(input("Enter second number!"))

#We have our calculations as well as a message that reads out the solution to our calculations
Sum = Number_1 + Number_2
Difference = Number_2 - Number_1
Product = Number_1 * Number_2
print(f"The Sum of those numbers are {Sum}. The difference of those numbers is {Difference}. The product of those numbers is {Product}.")

#if the second number is 0 then we tell the user that we cannot divide by zero and avoid a error, if not we print the message and solution
if Number_2 == 0:
    print("The quotient cannot be calculated because you cannot divide by 0!")
else:
    Quotient = Number_1 / Number_2
    print(f"The quotient is {Quotient}")



