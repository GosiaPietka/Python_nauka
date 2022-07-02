napis = "Ala ma kota"
print(napis[0])
print(type(napis[0]))
print(napis[-1])
print(napis[-3:-1])
print(napis[::2])

zmienna = 127
zmienna = "127"*127
print(zmienna)

#zadanie 1
s1 = "Dzisiajjestwtorek"
s2 = "byl"
middleIndex = int(len(s1) /2)
print("Oryginalne ciągi są", s1, s2)
middleThree = s1[:middleIndex]+ s2 +s1[middleIndex:]
print("Po dołączeniu nowego ciągu w środku", middleThree)

#zadanie 2
s1 = "America"
s2 = "Japan"
first_char = s1[:1] + s2[:1]
middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
res = first_char + middle_char + last_char
print("Mix String to ", res)

#listy
lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
print(lista[1:6])
print(lista[2:6:2])
print(lista[:4])
print(lista[::-1])
lista.append("zebra")
lista.insert(2,"zebra")
print(lista)

#zadanie3
#utworz liste kursantow i posortuj alfabetycznie oraz ile ona ma elementow
listaKursantow = ['Janek', 'Marek', 'Krysia', 'Basia', 'Piotrek', 'Tomek', 'Oskar']
listaKursantow.sort()
print(listaKursantow)
print('Lista ma ', len(listaKursantow), ' elementów')
#slowniki

#zadanie4
#odwroc ciąg
str1 = "Python"
print(str1[::-1])


#range
for i in range(5):
    print(i)

for i in range(2, 11, 2):
    print(i)

print(list(range(2, 11, 2)))

##zad
'''Przypisz 8 do zmiennej x i 15 do zmiennej y
Utwórz 2 instrukcje warunkowe
Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa '''
x = 8
y = 15

if x > 3 or y % 2 == 0:
  print("Co najmniej jeden z warunków jest spełniony")

if x <= 3 and y % 2 == 1:
  print("Żaden warunek nie jest spełniony")

#for
string = 'Python'

for litera in string:
    print('litera:', litera)

'''Utwórz listę zawierającą imiona wszystkich kursantów
Następnie ją posortuj alfabetycznie, oraz
Policz ile z osób na liście jest kobietami
W tym celu możesz sprawdzić czy imię kończy się na „a”'''

imiona = ['Marek', 'Krysia', 'Piotr', 'Maria', 'Teresa', 'Marek']
imiona.sort()
print('Posortowana lista: ', imiona)
ile = 0
for imie in imiona:
    if imie[-1]=='a':
        print(imie)
        ile+=1

print('W grupie są/jest: ', ile, ' kobiet')

#range
print('Lista od tylu: ')
for i in range(2, 11, 2)[::-1]:
    print(i)
#wprowadzanie tekstu do momentu pustej liniisd
lines = list()
print('Wprowadź tekst po linijce.')
print('Żeby zakończyć wprowadź pustą linię.')
line = input('Następna linijka: ')
while line != '':
    lines.append(line)
    line = input('Następna linijka: ')  # reset
print(lines)

#liczba pierwsza
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            break
    else: # normalny koniec pętli
        print(n, 'jest liczbą pierwszą')

#lista i słownik
'''Poniżej znajdują się dwie listy. Napisz program w Pythonie konwertujący je na słownik w taki sposób, że pozycja z listy 1 jest kluczem, a pozycja z listy 2 jest wartością
In [ ]:
keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]'''

keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]

dict = dict()

for i in range(len(keys)):
    dict.update({keys[i]: values[i]})
print(dict)

'''Znajdź liczby, które są podzielne przez 7 i są wielokrotnością 5 w zakresie
Napisz program w Pythonie, aby znaleźć liczby podzielne przez 7 
i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)'''

tab = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        tab.append(str(x))

print(';'.join(tab))

'''tabliczka mnozenia'''
number = int(input('Podaj dowolna liczbe: '))
for i in range (1,11):
    print (i*number)


'''suma liczb'''
num = int(input ('Suma ilu kolejnych liczb: '))
suma = 0
for i in range(0,num+1):
    suma+=i

print('Suma kolejnych liczb: ', suma)


