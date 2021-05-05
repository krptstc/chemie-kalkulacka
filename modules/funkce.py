import os

from modules.molhmotnosti import *

def vycistit_obrazovku():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def ziskat_prvky(sloucenina):
    prvky = []
    momentalniPrvek = ''
    for pismeno in sloucenina:
        if pismeno.isupper():
            if len(momentalniPrvek) != 0:
                prvky.append(momentalniPrvek)
            momentalniPrvek = ''
            momentalniPrvek += pismeno
        elif pismeno.isnumeric():
            for i in range(int(pismeno)):
                prvky.append(momentalniPrvek)
            momentalniPrvek = ''
        else:
            momentalniPrvek += pismeno
    if not pismeno.isnumeric():
        prvky.append(momentalniPrvek)
    return prvky

def ziskat_molarni_hmotnost(sloucenina):
    vysledek = 0
    prvky    = ziskat_prvky(sloucenina)
    for prvek in prvky:
        vysledek += molarniHmotnost[prvek]
    return vysledek

def vykreslit_trojclenku(vstupA, vstupB, vystupA, vystupB, vstupLatka, vystupLatka):
    print('')
    print(f'  {vstupA} g {vstupLatka} ... {vystupA} g {vystupLatka}')
    print(f'  {vstupB} g {vstupLatka} ... x g {vystupLatka}')
    print('\n  x = ?')
    print(f'  x = {vstupB} * {vystupA} / {vstupA}')
    print(f'  x = {vstupB * vystupA / vstupA}')
