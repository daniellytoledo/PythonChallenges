galera = list()
dado = list()
tmaior = tmenor = 0
for c in range(0,3):
    dado.append(str(input("NOME: ")))
    dado.append(int(input("IDADE: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        tmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tmenor += 1
print(f'Temos {tmaior} maior(es) de idade e {tmenor} menor(es) de idade.')
