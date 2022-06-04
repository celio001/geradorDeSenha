import random

class GerarSenhas():

    def __init__(self):
        self.caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?0123456789'
        self.numero = int()
        self.quantidade = int()

    def Iniciar(self):
        self.menu()
        self.pedirQuantidade()
        self.fazerSenhas()
        self.final()

    def menu(self):
        print('\nBem vindo ao seu Gerador de senhas')

    def pedirQuantidade(self):
        self.numero = input('\nQuantidade de senhas a serem geradas: ')
        self.numero = int(self.numero)
        self.quantidade = input('Comprimento da sua senha: ')
        self.quantidade = int(self.quantidade)

    def fazerSenhas(self):
        print('\nAqui estão suas senhas: \n')
        for self.pwb in range (self.numero):
            self.senha = ''
            for self.c in range (self.quantidade):
                self.senha += random.choice(self.caracteres)
            print(self.senha)

    def final(self):
        self.resposta  = input('\nDeseja voltar ao inicio\n 1- Sim \n 2- Não\n')
        self.resposta = int(self.resposta)
        while self.resposta >= 3 or self.resposta <= 0:
            print('Escolha 1 ou 2 para proceguir')
            return self.final()
        if self.resposta == 1:
            self.Iniciar()
        elif self.resposta == 2:
            print('Obrigado por usar meu codigo')


senha = GerarSenhas()
senha.Iniciar()