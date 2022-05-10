# Napisz program, który pobierze liczbę rzeczywistą, a następnie wyświetli komunikat czy liczba jest większy od zera czy nie.

liczba = float(input())
if(liczba > 0):
    print("Liczba", float(liczba), "jest większa od zera")
else:
    print("Liczba", float(liczba), "jest mniejsza od zera")


# Napisz program, który pobierze dwie liczby całkowite większe od zera i wyświetli ich średnią arytmetyczną.

# W przypadku podania liczby ujemnej program powinien wypisać komunikat: BŁĄD

liczba=int(input())
liczba2=int(input())
if (liczba > 0) and (liczba2 > 0):
    print(float((liczba+liczba2)/2))
else:
    print("BŁĄD")


# Przedstawiony poniżej kod zawiera kilka zagnieżdżonych konstrukcji if-else. Niestety kod ten jest pozbawiony wcięć. Popraw kod zgodnie z konwencją zapisu instrukcji if-else, wyrównując odpowiednio linie i wstawiając wcięcia.

score = int(input())
A_score = 10
B_score = 8
C_score = 6
D_score = 4
if score >= A_score:
    print('Twoja ocena to 5.')
else:
    if score >= B_score:
        print('Twoja ocena to 4.')
    else:
        if score >= C_score:
            print('Twoja ocena to 3.')
        else:
            if score >= D_score:
                print('Twoja ocena to 2.')
            else:
                print('Twoja ocena to 1.')


# Napisz program, który będzie realizował grę pod tytułem FizzBuzz. Reguły tej gry są następujące:

# Pobieramy liczbę całkowitą od użytkownika
# Jeżeli liczba ta jest podzielna przez 15 wypisujemy na ekran "FizzBuzz" (wraz z cudzysłowiami)
# W przeciwnym przypadku jeżeli liczba ta jest podzielna przez 3 wypisujemy na ekran "Fizz" (wraz z cudzysłowami)
# W przeciwnym przypadku jeżeli liczba ta jest podzielna przez 5 wypisujemy na ekran "Buzz" (wraz z cudzysłowiami)
# W przeciwnym przypadku wypisujemy tę liczbę z cudzysłowiami np: "17"
# Wskazówka: Aby wykonać to zadanie należy pamiętać, że liczbę należy zamienić na typ string. Służy do tego funkcja str(napis).


a=int(input())
a2=(str(a))
a3=('"'+a2+'"')
if (a%15 == 0):
    print('"FizzBuzz"')
elif (a%3 == 0):
     print('"Fizz"')
elif (a%5 == 0):
     print('"Buzz"')
else:
    print(a3)


# Napisz program, który pobierze dwa ciągi tekstowe i wypisze napis większy od niego.

a=input()
b=input()
if (a>b):
    print(a)
else:
    print(b)


# Napisz program, który pobierze literkę z alfabetu i wypisze komunikat czy litera ta jest samogłoską czy nie.

słowo=input()
słowo2=("'"+słowo+"'")
if (słowo == 'a') or (słowo == 'ą') or (słowo == 'u') or (słowo == 'e') or (słowo == 'ę') or (słowo == 'i') or (słowo == 'o') or (słowo == 'ó') or (słowo == 'y'):
    print("Litera", słowo2, "jest samogłoską")
else:
    print("Litera",słowo2,"nie jest samogłoską")


# Napisz program, który dla podanej liczby z odpowiedniego zakresu wyświetli jaki to miesiąc i ile ma on dni.

# Zakładamy, że rok tutaj nie jest przestępny.

# W przypadku niepoprawnych danych program ma wypisać komunikat: BŁĄD

a=int(input())
if (a == 1):
    print("Styczeń: 31 dni")
else:
    if (a == 2):
        print("Luty: 28 dni")
    else:
        if (a == 3):
            print("Marzec: 31 dni")
        else:
            if (a == 4):
                print("Kwiecień: 30 dni")
            else:
                if (a == 5):
                    print("Maj: 31 dni")
                else:
                    if (a == 6):
                        print("Czerwiec: 30 dni")
                    else:
                        if (a == 7):
                            print("Lipiec: 31 dni")
                        else:
                            if (a == 8):
                                print("Sierpień: 31 dni")
                            else:
                                if (a == 9):
                                    print("Wrzesień: 30 dni")
                                else:
                                    if (a == 10):
                                        print("Październik: 31 dni")
                                    else:
                                        if (a == 11):
                                            print("Listopad: 30 dni")  
                                        else:
                                            if (a == 12):
                                                print("Luty: 31 dni")
                                            else:
                                                print("BŁĄD")


# Napisz program, który wczyta trzy ciągi tekstowe i wypisze je od najmniejszego ciągu do największego.

a=input()
b=input()
c=input()
if (a<b<c):
    print(a,b,c) 
else:
    if (b<a<c):
        print(b,a,c)
    else:
        if(b<c<a):
            print(b,c,a)
        else:
            if(c<b<a):
                print(c,b,a)
            else:
                if(a<c<b):
                    print(a,c,b)
                else:
                    if(c<a<b):
                        print(c,a,b)


