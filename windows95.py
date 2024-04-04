import random

parola = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("şifre uzunluğunu girin"))

sifre = ""

for j in range(uzunluk):
    sifre += random.choice(parola)

print(sifre)
