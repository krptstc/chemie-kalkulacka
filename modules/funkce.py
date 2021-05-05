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

def ziskat_stranu():
    strana = input()
    strana = strana.replace(' ', '')
    strana = strana.split('+')
    return strana

def vypocitat_trojclenku(trojclenka):
    return trojclenka[2] * trojclenka[1] / trojclenka[0]

def vykreslit_trojclenku(trojclenka, vstupLatka, vystupLatka):
    rowA1 = f'{trojclenka[0]} g {vstupLatka}'
    rowA2 = f'{trojclenka[1]} g {vystupLatka}'
    rowB1 = f'{trojclenka[2]} g {vstupLatka}'
    rowB2 = f'x g {vystupLatka}'

    print('')
    print(f'{rowA1} ... {rowA2}')
    print(f'{rowB1} ... {rowB2}')
    print('\nx = ?')
    print(f'x = {trojclenka[2]} * {trojclenka[1]} / {trojclenka[0]}')
    print(f'x = {vypocitat_trojclenku(trojclenka)}')
