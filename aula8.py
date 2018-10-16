# orientação a objeto
# -*- coding: UTF-8 -*-

# sintaxe de uma classe
# sintaxe old style class Perfil():
# intaxe new style
class Perfil(object):
    'Classe padrão para perfis de usuários'
    # construtor da class
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
    # metodo da class
    def show_dados(self):
        print('nome: %s\ntelefone: %s\nempresa: %s' % (self.nome, self.telefone, self.empresa))

# instanciando uma class
perfil = Perfil('Bruno Afonso', 'não informado', 'indra')
# acessando o atributo de uma class
perfil.show_dados()

# instanciando uma class com parametros nomeados
perfil2 = Perfil(telefone='não informado', empresa='indra', nome='Bruno Henrique Afonso')
perfil2.show_dados()
print(type(perfil2))

