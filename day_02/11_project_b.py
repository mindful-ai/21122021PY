# Project B
# Program to collect numeric values from the user
# print the maximum, minimum, average, median, mode
# and separate the evens, odds and prime numbers

import statistics
import myprimes


print("01_project_b.py __name__ = ", __name__)

# input

n = []
while True:
    uin = input("-> (q to exit) ")
    if(uin.lower() == 'q'):
        break
    else:
        if(uin.isdigit()):
            n.append(int(uin))


    
# process

ma = max(n)
mi = min(n)
mean = statistics.mean(n)
median = statistics.median(n)
mode = statistics.mode(n)

odds = []
evens = []
primes = []

for i in n:
    if(i % 2 == 0):
        evens.append(i)
    else:
        odds.append(i)

for i in n:
    if(myprimes.checkprime(i)):
        primes.append(i)

#if(myprimes.checkprime(i) == False) => if(not myprimes.checkprime(i))
#if(myprimes.checkprime(i) == True) => if(myprimes.checkprime(i))


# output

print('-'*60)
print("MAXIMUM : ", ma)
print("MINIMUM : ", mi)
print("MEAN    : ", mean)
print("MEDIAN  : ", median)
print("MODE    : ", mode)
print("EVENS   : ", evens)
print("ODDS    : ", odds)
print("PRIMES  : ", primes)
