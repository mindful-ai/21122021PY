# Write a program to convert the temperature
# C -> F or F -> C should be determined by the last charecter of the input

# input

t = input("Enter temperature: \nEx: 100C, 212F...\n->")


# process

lastchar = t[-1]
if(lastchar.upper() == 'F'):
    # conver from F -> C
    res = (float(t[:-1]) - 32)/(9/5)
    msg = str(res) + 'C'
elif(lastchar.upper() == 'C'):
    # conver from C -> F
    res = (float(t[:-1])* (9/5)) + 32
    msg = str(res) + 'F'
else:
    msg = "Invalid Input"

# output

print('-'*50)
print(msg)
