import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

#c.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")

c.execute("INSERT INTO stocks VALUES ('2022-01-05','BUY','Gosia',100,35.14)")

conn.commit()

print(c.execute("Select * from stocks"))
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

#Napisz program w języku Python, aby utworzyć połączenie bazy danych SQLite z bazą danych znajdującą się w pamięci.
conn1 = sqlite3.connect(':memory:')
print(("Baza danych pamięci utworzona i połączona z SQL"))
conn1.close()
print("Połączenie zakmnięte")



'''Napisz program w Pythonie, aby utworzyć bazę danych SQLite w pliku i połączyć się z bazą danych
oraz wydrukować wersję bazy danych SQLite i numer wersji modułu sqlite3 w postaci ciągu.'''

conn = sqlite3.connect('temp.db')
c = conn.cursor()
print("Baza danych stworzona i połączona z sqlite")
query = "Select sqlite_version()"
c.execute(query)
record = c.fetchall()
print("Wersja bazy danych SQLite to: ", record)
print("Wersja modułu sqlite3 to: ", sqlite3.version)
conn.close()
print("Połączenie SQLite jest zamknięte.")

#Napisz program w Pythonie, aby utworzyć bazę danych SQLite i połączyć się z bazą danych
# oraz zabezpieczyć się przed wyjątkami. Wywołaj sztucznie wyjątek, wykonując błędne zapytanie.

try:
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("Select * from uczniowe")
except sqlite3.Error as error:
    print("Błąd podczas łączenia się z SQLite", error)
finally:
    conn.close()

#Napisz program w Pythonie, który wyświetli listy zawartości tabel pliku bazy danych SQLite CodeBrainers.
conn = sqlite3.connect('CodeBrainers.db')
c = conn.cursor()
print("Wykaz zawartości tabel:")
c.execute("SELECT * FROM product")
print(c.fetchall())
c.execute("SELECT * FROM customer")
print(c.fetchall())
c.execute("SELECT * FROM order_product")
print(c.fetchall())
conn.close()
print("Połączenie SQLite jest zamknięte.")

#Napisz program w Pythonie, aby połączyć bazę danych SQLite i utworzyć tabelę w bazie danych:

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE users(login VARCHAR(8) NOT NULL, name VARCHAR(40) NOT NULL, phone_no VARCHAR(15));")
c.execute("INSERT INTO users VALUES ('user', 'Jan Nowak', '1234567890');")
c.execute("SELECT * FROM users;")
record = c.fetchall()
print(record)
conn.close()

#Napisz program w Pythonie, który wstawi listę kilku rekordów do podanej tabeli SQLite o kilku kolumnach
# (jednym poleceniem). Policz liczbę wierszy w danej tabeli SQLite (przed i po wstawieniu wierszy).

conn = sqlite3.connect(':memory:')
c = conn.cursor()
# Utwórz tabelę
c.execute("CREATE TABLE users(id SMALLINT, name VARCHAR(30), city VARCHAR(35));")
cursor = c.execute("Select * from users")
print(len(cursor.fetchall()))
print("Liczba wierszy : ", len(cursor.fetchall()))
c.execute("INSERT INTO users (id, name, city) VALUES ('5001', 'Piotr Nowak', 'Warszaa');")
cursor = c.execute("Select * from users")
print("Liczba wierszy po wstawieniu 1 użytkownika: ", len(cursor.fetchall()))

query = "INSERT INTO users (id, name, city) VALUES (?, ?, ?);"
rows = [(5002,'Piotr Nowak',          'Warszawa'),
        (5003,'Anna Kowalska',        'Kraków'  ),
        (5004,'Krzysztof Wiśniewski', 'Łódź'    ),
        (5005,'Maria Wójcik',         'Kraków'  ),
        (5006,'Andrzej Kowalczyk',    'Wrocław' )]
c.executemany(query, rows)
conn.commit()

cursor = c.execute('SELECT * FROM users;')
print("Liczba rekordów po wstawieniu 5 dodatkowych wierszy:", len(cursor.fetchall()))
conn.close()

#Napisz program w Pythonie, który będzie wstawiał wartości do tabeli z danych wejściowych użytkownika.
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE users (id SMALLINT, name VARCHAR(30), city VARCHAR(35));")
input_id = input('Podaj id: ')
input_name = input('Podaj nazwisko: ')
input_city = input('Podaj miasto: ')
c.execute("INSERT INTO users (id, name, city) VALUES (?, ?, ?);",(input_id, input_name, input_city))
conn.commit()
c.execute("SELECT * FROM users;")
record = c.fetchall()
print(record)
conn.close()
