plik = open("napisy.txt", "r")
Plik = plik.readline().split

#zad A
Parzyste = 0

while(Plik > 1000):
if(Plik % 2):
   Parzyste = Parzyste + 1
else:
    print("Liczba nie parzysta")

print(Parzyste)
#zad B
Zera = Plik
Jedynki = Plik
Tyle_samo = 0

while(Plik > 1000):
if(len(Zera) == len(Jedynki)):
    Tyle_samo = Tyle_samo + 1
else:
    print("Liczba nie ma tyle samo jedynek i zer")

print(Tyle_samo)

#zad C
Napisy_jeden = 0
Napisy_zero = 0

while(Plik > 1000):
    if(Napisy_zero == 0):
        Napisy_zero = Napisy_zero + 1
    elif(Napisy_jeden == 1):
        Napisy_jeden = Napisy_jeden + 1

print(Napisy_zero)
print(Napisy_jeden)

#zad D

#zad E
Palindrom = 0
Palindrom_a = Plik
Palindrom_b = Plik

while(Plik > 1000):
    if(Palindrom_a == Palindrom_b):
        Palindrom = Palindrom + 1
else:
    print("Nie palindromem")

print(Palindrom)
#zad F
K2 = 0
K3 = 0
K4 = 0
K5 = 0
K6 = 0
K7 = 0
K8 = 0
K9 = 0
K10 = 0
K11 = 0
K12 = 0
K13 = 0
K14 = 0
K15 = 0
K16 = 0
