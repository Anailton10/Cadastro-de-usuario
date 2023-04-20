from colorama import Fore
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

class Cadastro:
    def __init__(self, pessoa):
        self.ficha = dict()
        self.salvar = list()
        self.pessoa = pessoa

    def armazenar(self):
        self.ficha['Nome'] = self.pessoa.nome
        self.ficha['Idade'] = self.pessoa.idade
        self.salvar.append(self.ficha.copy())
        self.ficha.clear()
        print(Fore.GREEN + 'Usuário Adicionado com sucesso!!' + Fore.RESET)





