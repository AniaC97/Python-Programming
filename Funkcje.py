# Spójrz na następującą definicję funkcji:

# def my_function(a,b,c):
#     d = (a+b) / c
#     print(d)
# Napisz w programie wywołanie tej funkcji dla następujących parametrów: 

# a=2, b=4 oraz c=6.

def my_function(a,b,c):
    d = (a+b) / c
    print(d)

my_function(2,4,6)


# Napisz funkcję get_integer() oraz get_double(), która będzie pobierać od użytkownika odpowiednio liczbę całkowitą oraz rzeczywistą.

# Napisz wyłącznie funkcje.

def get_integer():
    a = int(input())
    return a

def get_double():
    b = float(input())
    return b

def main():
    to = get_integer()
    tamto = get_double()
    return to, tamto


# Napisz funkcję o nazwie is_even(number), która będzie jako argument przyjmować liczbę całkowitą. Ponadto ma zwracać wartość True, jeżeli liczba ta jest parzysta, a False w przeciwnym przypadku.

# Napisz wyłącznie funkcje.

def is_even(number, k=2):
    if number%k == 0:
        return True
    return False


# Napisz funkcję is_palindrome(word), która wyrzuci wartość True dla słowa, który jest palindromem lub False w przeciwnym przypadku.

# Weź pod uwagę wielkość liter: litera A i a dla palindromu to jest to samo!!!

# Można skorzystać z gotowej funkcji lower().

# Napisz tylko samą funkcję!!!

def is_palindrome(word):
    word = word.lower()
    slowo = word[::-1]
    if word == slowo:
        return True
    else:
        return False


# Napisz funkcję get_largest_size(words), która jako argument przyjmuje listę słów a w wyniku zwraca długość najdłuższego słowa w liście words.

# Napisz wyłącznie samą funkcję.

def get_largest_size(words):
    
    largestW = ''
    largestL = 0
    for word in words:
        if largestL < len(word):
            largestL = len(word)
            largestW = word
    return largestL


# Napisz funkcję is_pangram(word), który sprawdza czy dany ciąg tekstowy jest pangramem.

# Pangramem nazywamy ciąg tekstowy, w którym każda litera alfabetu łacińskiego występuje co najmniej raz.

# W przypadku pozytywnej odpowiedzi funkcja powinna zwracać True, w przeciwnym przypadku False.

# Przykładowo:

# is_pangram('') == False
# is_pangram('abcdefghijklmnopqrstuvwxyz') == True


def is_pangram(word):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for litera in alfabet:
        if litera not in word.lower():
            return False
    return True
        



