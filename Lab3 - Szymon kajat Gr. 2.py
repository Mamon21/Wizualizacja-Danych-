import random
#Zad 1 - Lab3.
# A = {1-x: x∈<1,10>} B = {1,4,16,…,47} C = {x: x∈B i x jest liczbą podzielną przez 2}
# listaA = [x+1 for x in range(10)]
# listaB = [4**x for x in range(7)]
# listaC = [x for x in listaB if x%2==0]
# print(listaA)
#Zad2 - Lab3.
# liczby_losowe = [random.randint(0,200) for x in range(10)]
# liczby_parzyste = [x for x in liczby_losowe if x%2==0]
# print(liczby_losowe)
# print(liczby_parzyste)
#Zad3 - Lab3.
# lista_Produktow = {'ziemniaki':'kg','jabłka':'kg','CocaCola':'litry','Cytryny':'sztuki'}
# SprzedawaneNaSztuki = [x for x in lista_Produktow if x == 'sztuki']
# print(SprzedawaneNaSztuki)
#Zad 4- Lab3.
# a = 6
# b = 8
# c = 4
#
# if ((a+b>c) and (a+c>b) and (b+c>a)):
#     if ((a*a+b*b==c*c) or (a*a+c*c==b*b) or (c*c+b*b==a*a)):
#         print("Jest to trójkąt prostokątny")
#     else:
#         print("Nie jest to trójkąt prostokątny")
#Zad5 - Lab3.
# def pole_trapezu(a = 3,b = 6,h = 8):
#     pole = ((a+b)*h) / 2
#     return pole
# print(pole_trapezu())
#Zad 6 - Lab3.
# def iloczyn_elementu_ciagu(a = 1, b = 4, ile = 10):
#     for a in range(10):
#         a = a * b
#         return a
# print(iloczyn_elementu_ciagu())