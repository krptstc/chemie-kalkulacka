def ziskat_prvky(sloucenina):
    prvky = []
    momentalniPrvek = ''
    for pismeno in sloucenina:
        if pismeno.isupper():
            if len(momentalniPrvek) != 0:
                prvky.append(momentalniPrvek)
            momentalniPrvek = ''
        momentalniPrvek += pismeno
    prvky.append(momentalniPrvek)
    return prvky
