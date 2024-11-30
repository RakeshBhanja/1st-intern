import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '?']

print("Welcome to Password Generator :)")
nletters = int(input("How many letters do you want in your password?\n"))
nnumbers = int(input("How many numbers do you want in your password?\n"))
nsymbols = int(input("How many symbols do you want in your password?\n"))

password = []

for _ in range(nletters):
    char = random.choice(letters)
    password.append(char)

for _ in range(nnumbers):
    char = random.choice(numbers)
    password.append(char)

for _ in range(nsymbols):
    char = random.choice(symbols)
    password.append(char)

random.shuffle(password)
# Shuffle the password list to ensure randomness


final_password = ''.join(password)
#join the list into a string

print("Your generated password is:", final_password)
print("Thank you ")