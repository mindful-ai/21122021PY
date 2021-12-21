# Program to create a character histogram
# input: apples
# output: {'a':1, 'p':2, 'l':1, 'e':1, 's':1}

# input
text = input("Enter some text:")

# process
hist = {}
for ch in text:
    if(ch in hist.keys()):
        hist[ch] = hist[ch] + 1
    else:
        hist[ch] = 1

# output
print('-'*60)
# print(hist)
for key, value in hist.items():
    print(key, ' ---> ', value)
