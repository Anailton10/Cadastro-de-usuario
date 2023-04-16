pessoa = dict()
ficha = list()
resp = 's'
while resp != 'n':
    pessoa['nome'] = str(input('Nome:'))
    pessoa['idade'] = int(input('Idade:'))
    ficha.append(pessoa.copy())
    for k, v in enumerate(ficha):
        print(f'{k}:{v}')
    resp = input('Quer continuar?')
