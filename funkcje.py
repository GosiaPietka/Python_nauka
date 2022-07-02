# #funkcja dodawanie
# def add(x, y):
#     return x + y
#
# print(add(2, 3))

''' zwraca liczby Fibonacciego mniejsze od n '''
# def fibbonaci_numbers(n):
#
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
#
# #Wywołanie funkcji
# x = fibbonaci_numbers(10)
# print(x)

'''
def dlugosc (tekst):
    dlugosc = 0
    for i in tekst:
        dlugosc+=1
    return dlugosc

tekst = input('Podaj dowolny tekst: ')
print ('Twoj tekst ma: ', dlugosc(tekst), ' znaków.') '''

'''
#sumowanie elementów listy
list = [1, 2, -3, 4, -4]

def sumuj_lista (lis):
    suma = 0
    for i in lis:
        suma += i
    return suma

print('suma listy to: ', sumuj_lista(list))
'''


#Napisz funkcję w Pythonie, aby uzyskać największą liczbę z listy.

def max_in_list(lis):
    max = lis[0]
    for i in lis:
        if i > max:
            max = i
    return max

print(max_in_list([8, 2, -8, 0]))