import random
print('Welcome to Password generator')
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ().,/?^@!$%&*0123456789'
number = input('Number of password to generate:')
number = int(number)


length = input('Input the password length:')
length = int(length)

print('\nhere is the password:')
for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(char)
        print(password)