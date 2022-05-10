# Napisz program, który wypisze liczby od 1 do n, gdzie n jest podane przez użytkownika. W przypadku błędnych danych program powinien wypisać komunikat BŁĄD oraz zakończyć działanie.

n = int(input())
for i in range(1,n+1):
    print(i)
if (n < 1):
    print("BŁĄD")


# Napisz program, który będzie liczył iloczyn liczb całkowitych wprowadzanych przez użytkownika liczb do momentu wprowadzenia przez użytkownika wartości 0. Program ma wypisać obliczona wartość. W przypadku podania od razu liczby 0 program ma wypisać wartość 1.

total = 1

liczba = int(input())

while liczba != 0:
    total *= liczba
    liczba = int(input())

print(total)


# Napisz program, który pobierze od użytkownika liczbę całkowitą większą od zera n, a następnie wypisze tabelę o 
# n wierszach i n kolumnach, w której to każdym i-tym wierszu będzie występowała wartość i.

# Nie zakładamy tutaj niepoprawnych danych!!!

n = int(input())

if n > 0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j < n:
                print(i, end=' ')
            else:
                 print(i)


# Napisz program, który pobierze dwie liczby całkowite a,b większe od zera i wyświetli następujący prostokąt o długości 
# a i szerokości b.

# Nie zakładamy tutaj błędnych danych wyjściowych.


a=int(input())
b=int(input())

for i in range (1, a+1):
    for j in range (1, b+1):
        if (i == 1 or i == a or
            j == 1 or j ==b):
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Napisz program, który pobierze od użytkownika liczbę całkowitą 
# n, a następnie wypisze sumę jej cyfr.

def sumaLiczb(liczba):
    suma = 0
    length = str(liczba)
    for i in range(1, len(length)+1):
        suma += i
    return suma


print(sumaLiczb(1234))


