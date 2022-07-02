'''Mając listę Pythona, napisz program, który doda wszystkie jej elementy do danego zbioru.

Dane:
sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]'''

sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]

sample_set.update(sample_list)
print(sample_set)

#zad2
'''Poniżej znajdują się dwie listy. Napisz program w Pythonie konwertujący je na słownik w taki sposób, że pozycja z 
listy 1 jest kluczem, a pozycja z listy 2 jest wartością

keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]'''

keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]

nowa = dict(zip(keys,values))
print(nowa)

#zad3
'''Policz całkowitą liczbę cyfr w liczbie

Napisz program do zliczania całkowitej liczby cyfr w liczbie za pomocą pętli while.
Na przykład liczba to 75869, więc wynik powinien wynosić 5.'''

num = 75869
x = 0

while num > 0:
    num = num//10
    x+=1

print(x)

#zad4
'''Napisz program, w którym użyjesz pętli for do wydrukowania następującego wzorca liczb odwrotnych
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1'''

x = list(range(5,0,-1))

for element in x:
    for y in range (element, 0, -1):
        print (y,end=" ")
    print("")

#Zad 5
#Rekurencyjny ciąg Fibonacciego w Pythonie.'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print (fib(10))