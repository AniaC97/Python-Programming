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



