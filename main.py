from modules.funkce import *

if __name__ == '__main__':
    vycistit_obrazovku()
    print('Zadejte levou stranu rovnice: ')
    levaStrana = input()
    levaStrana = levaStrana.replace(' ', '')
    print('Zadejte pravou stranu rovnice: ')
    pravaStrana = input()
    pravaStrana = pravaStrana.replace(' ', '')

    print(f'\nLevá strana: {levaStrana}')
    print(f'\nPravá strana: {pravaStrana}')
