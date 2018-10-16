# encapsulamento

class Perfil(object):
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        # encapsulando o atributo
        self.__curtidas = 0

    def show_dados(self):
        print('nome: %s\ntelefone: %s\nempresa: %s\ncurtidas: %s' % (self.nome, self.telefone, self.empresa, self.__curtidas))

    def curtir_perfil(self):
        self.__curtidas += 1

    def get_curtidas(self):
        return self.__curtidas


perfil = Perfil('Bruno Afonso', 'não informado', 'indra')
perfil.curtir_perfil()
print(perfil.get_curtidas())
perfil.show_dados()
