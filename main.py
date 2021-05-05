from modules.funkce import *

if __name__ == '__main__':
    vycistit_obrazovku()

    print('Zadejte levou stranu rovnice: ')
    levaStrana = ziskat_stranu()
    print('Zadejte pravou stranu rovnice: ')
    pravaStrana = ziskat_stranu()

    rovnice = levaStrana + pravaStrana

    vstupniLatka  = input('\nZadejte sloučeninu na vstupu: ')
    vystupniLatka = input('Zadejte sloučeninu na výstupu: ')
    poziceVstup   = rovnice.index(vstupniLatka)
    poziceVystup  = rovnice.index(vystupniLatka)
    hodnotaVstup  = ziskat_molarni_hmotnost(rovnice[poziceVstup])
    hodnotaVystup = ziskat_molarni_hmotnost(rovnice[poziceVystup])

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
