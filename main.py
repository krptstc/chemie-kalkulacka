from modules.funkce import *

if __name__ == '__main__':
    vycistit_obrazovku()

    print('Zadejte levou stranu rovnice: ')
    levaStrana = ziskat_stranu()
    print('Zadejte pravou stranu rovnice: ')
    pravaStrana = ziskat_stranu()

    rovnice = levaStrana + pravaStrana
    for sloucenina in rovnice:
        sloucenina.replace(' ', '')

    vstupniLatka  = input('\nZadejte sloučeninu na vstupu: ')
    vstupniLatka.replace(' ', '')
    vystupniLatka = input('Zadejte sloučeninu na výstupu: ')
    vystupniLatka.replace(' ', '')
    poziceVstup   = rovnice.index(vstupniLatka)
    poziceVystup  = rovnice.index(vystupniLatka)
    hodnotaVstup  = 0
    hodnotaVystup = 0

    if rovnice[poziceVstup][0].isnumeric():
        bezCisel = []
        for c in rovnice[poziceVstup]:
            if not c.isnumeric():
                bezCisel.append(c)

        hodnotaVstup  = ziskat_molarni_hmotnost(bezCisel)
        hodnotaVstup *= int(rovnice[poziceVstup][0])
    else:
        hodnotaVstup  = ziskat_molarni_hmotnost(rovnice[poziceVstup])

    if rovnice[poziceVystup][0].isnumeric():
        bezCisel = []
        for c in rovnice[poziceVystup]:
            if not c.isnumeric():
                bezCisel.append(c)

        hodnotaVystup  = ziskat_molarni_hmotnost(bezCisel)
        hodnotaVystup *= int(rovnice[poziceVystup][0])
    else:
        hodnotaVystup  = ziskat_molarni_hmotnost(rovnice[poziceVystup])

    print(f'\nKolik máme gramů vstupní látky?')

    gramuVstupu    = hodnotaVstup
    gramuVystupu   = hodnotaVystup
    vysledekVstup  = int(input())

    trojclenka = [
        hodnotaVstup, hodnotaVystup, vysledekVstup
    ]

    vysledekVystup = vypocitat_trojclenku(trojclenka)
    vykreslit_trojclenku(trojclenka, vstupniLatka, vystupniLatka)

    print(f'\nVýsledek je {vysledekVystup} g.')

    input()
