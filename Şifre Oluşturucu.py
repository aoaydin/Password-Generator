import random
import string
import time
try:  
    while True:
        def generate_password (length,level,output=[]):
            chars = string.ascii_letters
            if level > 1:
                chars = "{},{}".format(chars,string.digits)
            if level > 1:
                chars = "{},{}".format(chars,string.punctuation)
            #if level > 1:
                #chars = "{},{}".format(chars,string.hexdigits)


            for i in range(length):
                output.append(random.choice(chars))
            
            return"".join(output)
        
        print ("""
        Level 0 = Çok kolay
        Level 1 = Kolay
        Level 2 = Orta
        Level 3 = Zor 
        Level 4 = Çok Zor
        """)
        print("Lütfen Bekleyin...")
        time.sleep(5)
        password_length = int(input("Uzunluk: "))
        password_level = int(input("Zorluk Derecesi: "))
        password = generate_password(password_length, password_level)
        print("\nSenin Şifren: {}".format(password))
        continue
except KeyboardInterrupt:
    print ("\n Çık & Resetle ")
    print ("\n Developer Abdurrahman Aydın")
    time.sleep(3)