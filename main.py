

# a)	Podaj, ile haseł ma parzystą, a ile nieparzystą liczbę znaków.

# b)	Utwórz zestawienie haseł (po jednym w wierszu), które są palindromami. Wynik wyświetl na ekranie i skopiuj do pliku wynik.txt

# c)	Stwórz zestawienie haseł (po jednym w wierszu) zawierających w sobie dwa kolejne znaki, których suma kodów ASCII wynosi 220.

with open('hasla.txt') as file:
    ileparzystych = 0
    ilenieparzystych = 0
    ilepalidromow = 0
    ilekodascii = 0
    tekst = ""
    for line in file:
        line = line.strip()
        odtylu = "".join(reversed(line))
        if(len(line) % 2 == 0):
            ileparzystych += 1
        else:
            ilenieparzystych += 1
        if(odtylu == line):
            ilepalidromow += 1

        for i in range(len(line)):
            try:
                wynikascii = ord(line[i]) + ord(line[i + 1])
                if(ord(line[i]) + ord(line[i+1]) == 220):
                    tekst = line
                    print(tekst)
            except IndexError:
                if(ord(line[i]) == 220):
                    tekst = line
                    print(tekst)


with open('wynik.txt',"w") as wynik:
    wynik.write("Parzyste: "+str(ileparzystych) + "\n")
    wynik.write("Nieparzyste: "+str(ilenieparzystych)+ "\n")
    wynik.write("Palidromow: "+str(ilepalidromow)+ "\n")