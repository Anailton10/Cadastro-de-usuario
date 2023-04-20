from system import Pessoa
from system import Cadastro
p1 = Pessoa()
c1 = Cadastro(p1)
lista = list()
resp = 's'
while resp != 'n':
    nome = input('Nome: ')
    idade = input('Idade: ')
    p1 = Pessoa(nome, idade)
    c1 = Cadastro(p1)
    c1.armazenar()
    lista.append(c1.salvar.copy())
    resp = str(input('Deseja continuar? '))

for i in lista:
    for k, x in enumerate(i):
        print(f'Nome:{x["Nome"]}\nIdade:{x["Idade"]}')
        print('-' * 20)
