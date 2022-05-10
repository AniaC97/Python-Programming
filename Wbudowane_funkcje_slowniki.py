# Napisz program, który usunie n-ty znak niepustego ciągu tekstowego podanego przez użytkownika.

# W przypadku podania nieprawidłowego indeksu program powinien poprosić użytkownika o wczytanie poprawnego indeksu.

s = input()
i = int(input())
new = s[:i] + s[i+1:]
print(new)


# Napisz program, który wyjustuje w rozmiarze 10 na lewo/prawo i w centrum daną liczbę podaną przez użytkownika.

a = input()

print(a.ljust(10))
print(a.rjust(10))
print(a.center(10))


# Napisz program, który pobierze dwie liczby rzeczywiste a i b i wyświetli na ekran wynik dzielenia 
# a/b. W przypadku dzielenia przez zero program powinien wyświetlić komunikat: Nie dziel przez zero! W przypadku błędnego sformatowania danych program powinien wypisać komunikat: Błędny format danych wejściowych!

try:
    a = int(input())
    b = int(input())
    print(a/b)
except ValueError:
    print("Błędny format danych liczbowych!")
except ZeroDivisionError:
    print("Nie dziel przez zero!")


# Napisz program, który stworzy następujący słownik składający się z następujących imion:

# Jan - John
# Mateusz - Matthew
# Anna - Anne
# Krzysztof - Christopher
# Aleksandra - Alexandra
# Joanna - Joan
# Patryk - Patrick
# Maciej - Matthias

persons = {'Jan': 'John', 'Mateusz': 'Matthew', 'Anna': 'Anne', 'Krzysztof': 'Christopher', 'Aleksandra': 'Alexandra', 'Joanna': 'Joan', 'Patryk': 'Patrick', 'Maciej': 'Matthias'}
print(persons)


# Napisz program, który wczyta następujący zbiór elementów: 'ala',1,2,3,2.5,"ala ma kota" i wyświetli go na ekranie.

a = {'ala',1,2,3,2.5,"ala ma kota"}
print(a)


# Napisz program, który pobierze liczbę naturalną n, następnie 
# n słów do zbioru, a następnie wyświetli ten zbiór na ekranie posortowane.

# Należy skorzystać z funkcji sorted() na zbiorze.

a = input()
b = input()
c = input()
d = input()
e = input()

zbior = [b,c,d,e]

nowy = sorted(zbior)
nowy = list(dict.fromkeys(nowy))

print(nowy)


# Napisz program, który pobierze od użytkownika 4 zbiory liczb całkowitych (każdy w osobnej linii) 
# A,B,C,D, a następnie wykona następujące działania (każdy wynik w osobnej linii):

# A | ( B & C) ^ D
# A ^ B ^ C ^ D
# A - B | B - A
# D - A & A - D

A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
C = set(list(map(int,input().split())))
D = set(list(map(int,input().split())))


print(A | (B & C) ^ D)
print(A ^ B ^ C ^ D)
print(A - B | B - A)
print(D - A & A - D)

