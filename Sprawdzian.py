import string

plik = open("napisy.txt", "r")
Plik = plik.readline().split

#zad A
Parzyste = 0

if(Plik % 2):
   Parzyste = Parzyste + 1
   print("Jest" + Parzyste + "liczb pazystych")
else:
    print("Liczba nie parzysta")

#zad B
Zera = Plik
Jedynki = Plik

if(len(Zera) == len(Jedynki)):

    print("Jest palindromem")
else:
    print("Nie palindromem")

#zad C
Zera = 0
Jedynki = 0

if Plik.rfind("0"):
    Zera = Zera + 1
elif Plik.rfind("1"):
    Jedynki = Jedynki + 1

print(Zera)
print(Jedynki)

#zad D


#zad E
Palindrom = 0
Palindrom_a = plik.readline()
Palindrom_b = plik.readline()

while(Plik > 1000):
    if(Palindrom_a == Palindrom_b):
        Palindrom = Palindrom + 1
    print("Jest palindromem")
else:
    print("Nie palindromem")

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
