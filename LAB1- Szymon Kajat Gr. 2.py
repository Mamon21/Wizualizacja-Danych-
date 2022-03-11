import math

#Zad1 - Lab1.
zmienna1 = 3
zmienna2 = 4
zmienna3 = 5.5
zmienna4 = 6
zmienna5 = "Kormoran"
zmienna6 = "Łomża"
print(zmienna1)
print(zmienna2)
print(zmienna3)
print(zmienna4)
print(zmienna5)
print(zmienna6)

#Zad2 - Lab1.
zmienna1 = 3
zmienna2 = 4
dodawanie = zmienna1 + zmienna2
odejmowanie = zmienna1 - zmienna2
mnożenie = zmienna1* zmienna2
dzielenie = zmienna1 / zmienna2

print(dodawanie)
print(odejmowanie) 
print(mnożenie)
print(dzielenie)

#Zad3- Lab1.
zmienna1 = 2
zmienna1 += 5
zmienna1 -= 4
zmienna1 *= 2
zmienna1 /= 3
zmienna1 **= 2
zmienna1 %= 2

#Zad4 - Lab1.
e = 3
potęga = e **10
print(potęga)
pierwiastek = pow(math.log(5+pow(math.sin(8),2)),1/6)
print(pierwiastek)
wartosc_bezwzględna = math.fabs(3.55)
print(wartosc_bezwzględna)
wartosc_bezwzględna = math.fabs(4.80)
print(wartosc_bezwzględna)

#Zad5 - Lab1.
imie = "SZYMON"
nazwisko = "KAJAT"
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie + " " + nazwisko)

#Zad6 - Lab1.

piosenka = "la la la la la la la la la la la la la la la la la"
a = piosenka.count("la")
print(a)

#Zad7 - Lab1.
string = "Paradoksalnie to głównie dieta"
print(string[1] + " " + string[len(string) - 1])

#Zad8 - Lab1.
print(piosenka.split(" "))

#Zad9 - Lab1.
a = "Skrypt"
b = 21.5 #float 
c = 0x61 #liczba w systemie szestnastkowym
print(a)
print(b)
print(c)




