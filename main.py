pessoa = dict()
ficha = list()
resp = 's'
while resp != 'n':
    pessoa['nome'] = str(input('Nome:')).strip().title()
    pessoa['idade'] = int(input('Idade:'))
    ficha.append(pessoa.copy())
    for k, v in enumerate(ficha):
        print(f'Nome:{v["nome"]}\nIdade:{v["idade"]} anos')
        print('=' * 20)
    resp = input('Quer continuar?')
