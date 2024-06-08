
import random
#koyulabilen karakterler
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#uzunluk
password_length = int(input("Parolanın uzunluğunu girin:"))
#şifre
password = ""
for _ in range(password_length):
    password += random.choice(characters)

print("Oluşturulan parola:", password)
