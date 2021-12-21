# Program to count the number of vowels

# input
text = input("Enter some text: ")
text = text.lower()

# process/output
vowels = 'aeiou'
for c in vowels:
    print(c.upper(), ' --> ' , text.count(c))




