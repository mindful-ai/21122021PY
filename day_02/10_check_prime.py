# Project A - re-written with functions
# Program to determine if a number if a number is prime or not

'''
def <function name>(<input args>):
    <statement>
    return <value/expression>
'''

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# ------------------------------------

# input
n = int(input("Enter a number: "))

# process/output
if(checkprime(n) == True):
    print("The number is prime")
else:
    print("The number is not prime")
