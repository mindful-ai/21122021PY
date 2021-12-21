# Program to subtract two numbers
# Also tell if the difference is positive, negative or zero

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# process
res = a - b

# output
print("------------------------------------")
print("DIFFERENCE: ", abs(a-b))
if(res > 0):
    print("The difference is positive")
elif (res < 0):
    print("The result is a negative number")
else:
    print("The result is zero")

    
