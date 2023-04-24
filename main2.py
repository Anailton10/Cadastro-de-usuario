from system import Pessoa
from system import Cadastro
p1 = Pessoa()
c1 = Cadastro(p1)
lista = list()
resp = 1
while resp != 2:
    nome = str(input('Nome: '))
    idade = str(input('Idade: '))
    if idade.isnumeric():
        idade = int(idade)
    else:
        print('ERRO...DIGITE APENAS NUMERO')
    p1 = Pessoa(nome, idade)
    c1 = Cadastro(p1)
    c1.armazenar()
    lista.append(c1.salvar.copy())
    print('[ 1 ] PARA CONTINUAR.\n[ 2 ] PARA PARAR.')
    try:
        resp = int(input('Escolha uma Opção:'))
    except:
        print('ERRO!!')
        print('OPÇÃO INVÀLIDA, DIGITE NOVAMENTE.')

for i in lista:
    for k, x in enumerate(i):
        print(f'Nome:{x["Nome"]}\nIdade:{x["Idade"]}')
        print('-' * 20)
