# Napisz program, który pobierze od użytkownika 5 liczb i wyświetli je jako listę.

l = []
for i in range(5):
    a = int(input())
    l = l + [a]
print(l)


# Napisz program, który pobierze od użytkownika 5 liczb i wyświetli je jako krotkę.

# Należy wczytać te liczby do listy a następnie użyć funkcji wbudowanej tuple()

l = []
for i in range(5):
    a = int(input())
    l = l + [a]
lista = tuple(l)
print(lista)


# Napisz program, który pobiera 10 liczb całkowitych, a następnie wypisuje je w odwrotnej kolejności.

l = []
for i in range(10):
    a = int(input())
    l = l + [a]
print((*l[::-1]), sep='\n')


# Napisz program, który wyrzuci z podanej listy element o indeksie 0,2 i 4.

# Należy skopiować do innej listy bez elementów o podanych wyżej indeksach.

l = ["red", "yellow", "green", "pink", "black", "white"]
l2 = (l[1], l[3], l[5])
l3 = list(l2)
print(l3)


# Napisz program, który wczyta słowo od użytkownika, a następnie wypisze ilość samogłosek (a,e,i,o,u,y) oraz spółgłosek.

lit = input()
samog = 0
spol = 0
for l in lit:
    if l == "a" or l == "e" or l == "o" or l == "i" or l == "u"  or l == "y"  or l == "A"  or l == "E"  or l == "O"  or l == "I"  or l == "U"  or l == "Y":
        samog +=1
    else:
        spol += 1
print("Liczba samogłosek:",samog) 
print("Liczba spółgłosek:",spol)


# Napisz program, który pobierze od użytkownika listę liczb całkowitych (w jednej linii), a następnie policzy i wypisze na ekran sumę tych liczb.

# Skorzystaj z pokazanej wcześniej funkcji map().

n = list(map(int,input().split()))
print(sum(n))


# Napisz program, który wczyta od użytkownika ciąg znakowy, a następnie sprawdzi czy ciąg ten jest palindromem czy nie.

# W wyniku program ma zwracać ma wartość prawda (jeżeli jest palindromem) lub fałsz (w przeciwnym przypadku).

sl = input()

if (sl == (sl[::-1])):
    print("True")
else:
    print("False")


# Napisz program, który wczyta ciąg znakowy w jednej linii, a następnie dla każdego słowa wypisze jego długość.

slo = list(input().split())

length = 0
index = 0

for index in range (len(slo)):
    length += 1
    print(slo[index],"==",len(slo[index]))


# Napisz program, który pobierze od użytkownika liczby całkowite (zapisane w jednym wierszu).

# Następnie pobierze od użytkownika liczbę całkowitą, a potem program ma wypisać informację czy liczba ta znajduje się w liście czy nie.

# Nie używaj żadnych wbudowanych funkcji (dotyczące znajdowania elementów na liście).

a = input().split()
b = input()

if a[0] == b or a[1] == b or a[2] == b or a[3] == b:
    print("Liczba znajduje się w liście")
else:
    print("Liczba nie znajduje się w liście")


# Napisz program, który pobierze od użytkownika liczby całkowite (zapisane w jednym wierszu), następnie wypisze liczbę największą oraz najmniejszą tej listy.

# Nie używaj żadnych wbudowanych funkcji (dotyczące odnajdywanie elementów największych oraz najmniejszych).

lista = list(map(int,input().split()))

mini = None
maxi = None

for i in lista:
    if mini == None or mini > i: 
        mini = i
      
    if maxi == None or maxi < i:
        maxi = i
        
print ("min ==",mini)
print ("max ==",maxi)


# Napisz program, który wczytuje od użytkownika 4 wiersze ciągów znakowych i zapisuje je jako lista list.

a = input().split()
b = input().split()
c = input().split()
d = input().split()

lista = [a,b,c,d]

print(lista)


# Napisz program, który pobiera od użytkownika liczbę wierszy , pobiera wiersze liczb całkowitych od użytkownika (zapisując je w liście dwukierunkowej), a następnie wyświetla tę listę każdy wiersz w osobnym wierszu.

wiersze = int(input())

for wiersz in range(wiersze):
    lista = list(map(int,input().split()))
    print(lista)


