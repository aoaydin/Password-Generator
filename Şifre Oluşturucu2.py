import random
import string

password = []
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

try:
    input_letters = int(input("Kaç adet harf olsun ?: "))
except:
    print ("Lütfen sayı gir")
    exit()

try:
    input_numbers = int(input("Kaç adet sayı olsun ?: "))
except:
    print ("Lütfen sayı gir")
    exit()

try:
    input_symbol = int(input("Kaç adet sembol olsun: "))
except:
    print ("Lütfen sayı gir")
    exit()

for z in range(input_letters):
    n = random.choice(letters)
    password.append(n)

for x in range(input_numbers):
    n = random.choice(numbers)
    password.append(n)

for c in range(input_symbol):
    n = random.choice(symbols)
    password.append(n)

password = "".join(password)


print("Şifre hazır!")
print("Şifren ---> ",password," <---")