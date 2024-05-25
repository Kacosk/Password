
import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Parolanın uzunluğunu girin:"))

password = ""

for _ in range(password_length):
    password += random.choice(characters)

print("Oluşturulan parola:", password)