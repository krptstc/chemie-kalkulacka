from modules.molhmotnosti import *

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
