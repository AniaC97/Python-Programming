# Guessing game

import random
my_number = random.randint(0,20)
guess = -1
trials = 0

print('GUESS MY NUMBER')


while guess != my_number:
    guess = int(input())
    if guess > my_number:
        print('Sorry- my number is smaller than your guess, Try again!')
    elif guess < my_number:
        print('Sorry- my number is greater than your guess, Try again!')
    else:
        print('You win! Your trials: ', trials)
    trials += 1



# Ten tekst to definicja pewnego pojęcia. Twoim zadaniem jest zbudowanie streszczenia tej definicji poprzez wyświetlenie pierwszych 20 słów

# text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'


words = text.split(' ')

short_text = ''

counter = 0

for n in words:
    short_text += (n + ' ')
    counter += 1
    if counter >= 20:
        print(short_text)
        break



# Dana jest lista definicji. Twoim zadaniem jest zbudowanie streszczeń tych definicji poprzez wyświetlenie tylko pierwszych 20 słów z każdej definicji. Zmień w odpowiedni sposób rozwiązanie zadania 1, tak aby przetwarzana była cała lista.

definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
    ]

for pojLista in definitions:
    short_text = ''
    counter = 0
    slowa = pojLista.split(' ')
    for skrot in slowa:
        short_text += (skrot + ' ')
        counter += 1
        if counter >= 20:
            print(short_text)
            break



# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

string = 'ala ma kota'
vowels = 0

def vowelsCounter():
    vowels = 0
    for i in string:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels += 1
    return vowels

print(vowelsCounter())

# Utwórz pętlę while, która poprosi użytkownika o wprowadzenie dwóch liczb. Liczby te należy zsumować i wyświetlić ich obliczoną wartość.
# Pętla powinna pytać użytkownika, czy chce wykonać działanie ponownie. Jeżeli tak, cała procedura powinna zostać powtórzona.
# W przeciwnym przypadku pętla powinna zakończyć działanie.


odp=str(input('Do you want some help with counting?'))


while odp == 'Yes' or odp == ' Yes' or odp == 'yes':
    a = int(input('Give me first number: '))
    b = int(input('Give me second number: '))
    print('Here you are:', a+b)
    odp = str(input('Do you want me to count something else?'))
    if odp == 'No' or odp == ' No' or odp == 'no':
        print('Ok, bye!')
    else:
        print('Sorry, I don\'t understand. Bye!')
        break


# Utwórz pętlę, która poprosi użytkownika o podanie liczby. Pętla powinna wykonać 10 iteracji i zapisywać sumę bieżącą liczb
# podawanych przez użytkownika.


przejscie = 0
suma = 0

while przejscie < 10:
    liczba = int(input('Please, give me a number: '))
    przejscie += 1
    suma += liczba
    print('Suma:', suma, 'Podejście:', przejscie)


# Kolekcjoner owadów
# Kolekcjoner codziennie poluje na owady. Opracuj program, który będzie obliczał sumę owadów zebranych w ciągu pięciu dni. Program powinien
# w pętli pytać użytkownika, ile owadów zebrał każdego dnia, a po zakończeniu pętli wyświetlić sumę zebranych owadów.

dzien = 0
owady = 0

while dzien < 5:
    ilosc = int(input('Hej! Ile owadów zebrałeś dzisiaj? '))
    dzien += 1
    owady += ilosc
    if ilosc > 4 or owady > 4:
        print('Super! Na dzień', dzien, 'masz', owady, 'owadów. Brawo!')
    elif ilosc > 1 or owady > 1:
        print('Super! Na dzień', dzien, 'masz', owady, 'owady. Brawo!')
    else:
        print('Super! Na dzień', dzien, 'masz', owady, 'owada. Brawo!')

#Spalone kalorie
#Biegając na bieżni, można w ciągu minuty spalić 4,2 kalorii. Opracuj program, który w pętli wyświetli liczbę spalonych kalorii
# po 10, 15, 20, 25 i 30 minutach biegania.


print('ILE SPALIŁEŚ KALORII PODCZAS BIEGANIA?\n')
print('MINUTA \t KALORIE')

for min in range(10,35,5):
    kalorie = min*4.2
    print(min, '\t\t', kalorie)


# Budżet
# Opracuj program, który poprosi użytkownika o podanie wielkości budżetu miesięcznego. Następnie w pętli poproś użytkownika o podanie
# poszczególnych wydatków w danym miesiącu i zapisz sumę bieżącą wydatków. Po wyjściu z pętli program powinien wyświetlić wartość,
# o którą użytkownik przekroczył budżet lub która pozostała we wskazanym budżecie.

budzet = int(input('Podaj swój miesięczy budżet: '))
kwota = 0

l = 0

while l == 0:
    prad = int(input('Ile płacisz za prąd? '))
    kwota += prad
    gaz = int(input('A za gaz? '))
    kwota += gaz
    jedzenie = int(input('Napisz swoje wydadki za jedzenie. '))
    kwota += jedzenie
    if kwota > budzet:
        print('Niestety ale przekroczyłeś swój budżet! Wydajesz:', kwota, 'miesięcznie. To o', (kwota-budzet), 'więcej niż powinieneś :(')
    elif kwota == budzet:
        print('Twoje wydatki na życie są równe budżetowi!')
    else:
        print('Super! W tym miesiącu zaoszczędzisz:', (budzet-kwota), '. Brawo! :)')
    l += 1


# Przebyta odległość
# Odległość, którą pokona pojazd, można obliczyć za pomocą następującego wzoru:

# odległość = szybkość × czas

# Przykładowo pociąg jadący przez trzy godziny z szybkością 40 km/h przejedzie 120 km. Opracuj program, który będzie prosił użytkownika
# o podanie szybkości pojazdu (w km/h) i czasu trwania podróży. Następnie program za pomocą pętli powinien wyświetlić odległość przebytą
# przez pojazd w ciągu każdej godziny jazdy. Oto przykład działania programu.

# Z jaką szybkością poruszał się pojazd? 40 (Enter)
# Jak długo trwała podróż? 3 (Enter)

# Godzina        Przebyta odległość
# ---------------------------------
# 1                             40
# 2                             80
# 3                             120

szybkosc = int(input('Z jaką szybkością poruszał się pojazd? '))
czas = int(input('Jak długo trwała podróż? '))

print('Godzina \t Przebyta odległość')
print('-'*32)

for i in range(1, czas+1):
    odleglosc = i*szybkosc
    string = str(odleglosc)
    align = string.rjust(30)
    print(i, align,)



