from modules.funkce import *

if __name__ == '__main__':
    vycistit_obrazovku()
    print('')

    print('  Zadejte levou stranu rovnice: ')
    levaStrana  = input('  ')
    levaStrana  = levaStrana.replace(' ', '')
    levaStrana  = levaStrana.split('+')

    print('  Zadejte pravou stranu rovnice: ')
    pravaStrana = input('  ')
    pravaStrana = pravaStrana.replace(' ', '')
    pravaStrana = pravaStrana.split('+')
    rovnice     = levaStrana + pravaStrana

    vstupniLatka  = input('\n  Zadejte sloučeninu na vstupu: ')
    vystupniLatka = input('  Zadejte sloučeninu na výstupu: ')
    poziceVstup   = rovnice.index(vstupniLatka)
    poziceVystup  = rovnice.index(vystupniLatka)
    hodnotaVstup  = ziskat_molarni_hmotnost(rovnice[poziceVstup])
    hodnotaVystup = ziskat_molarni_hmotnost(rovnice[poziceVystup])

    print(f'\n  Kolik máme gramů vstupní látky?')

    gramuVstupu    = hodnotaVstup
    gramuVystupu   = hodnotaVystup
    vysledekVstup  = int(input('  '))
    vysledekVystup = vysledekVstup * gramuVystupu / gramuVstupu

    vykreslit_trojclenku(gramuVstupu, gramuVystupu, vysledekVstup, vysledekVystup, vstupniLatka, vystupniLatka)

    print(f'\n  Výsledek je {vysledekVystup} g.')

    # print(f'\nRovnice: {rovnice}')
    # print(f'Levá strana: {levaStrana}')
    # print(f'Pravá strana: {pravaStrana}')
    # print(f'Pozice vstupu: {poziceVstup}')
    # print(f'Pozice vstupu: {poziceVystup}')
    # print(f'Hodnota vstupu: {hodnotaVstup}')
    # print(f'Hodnota vstupu: {hodnotaVystup}')

    input()
