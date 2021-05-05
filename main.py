from modules.funkce       import *
from modules.molhmotnosti import *

if __name__ == '__main__':
    zvolenaSloucenina = input("Zadejte sloučeninu: ")
    prvkySlouceniny   = ziskat_prvky(zvolenaSloucenina)
    print("\nPrvky této sloučeniny:")
    print(prvkySlouceniny)
