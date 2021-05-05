from modules.funkce       import *

if __name__ == '__main__':
    zvolenaSloucenina = input("Zadejte sloučeninu: ")
    prvkySlouceniny   = ziskat_prvky(zvolenaSloucenina)
    molarniHmotnost   = ziskat_molarni_hmotnost(zvolenaSloucenina)
    print('\nPrvky této sloučeniny:')
    print(prvkySlouceniny)
    print(f'Molární hmotnost sloučeniny: {molarniHmotnost} g/mol')
