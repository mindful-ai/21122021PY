class NegativeNumberException(Exception):

    def __init__(self, message="Exception Occured!"):
        super().__init__(message)



# ------------------------------------------


def nfactorial(n):
    if n <= 0:
        raise NegativeNumberException('Negative numbers not allowed for factorial')
    else:
        if(n == 1):
            return 1
        else:
            return n * nfactorial(n - 1)


def divide(a, b):
    if (b == 0):
        raise ZeroDivisionError('Cannot Divide by Zero!!!!')
    else:
        return a/b

# -----------------------------------------
m = int(input('Enter a dividend: '))
n = int(input('Enter a divisor: '))
x = 0

try:
    x = divide(m, n)
except Exception as E:
    print(E)

print('Quotient = ', x)
print("-" * 60)

try:
    print(nfactorial(n))
except Exception as E:
    print('There was an exeception')
    print(E)

