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

    # criando um metodo static
    @staticmethod
    def obter_perfis_csv(file):
        perfis = []
        arquivo = open('./csv/' + file, 'r')
        for linha in arquivo:
            try:
                valores = linha.split(',')
                perfis.append(Perfil(*valores))
            except TypeError as error:
                print('Os parametros são invalidos %s' % error)
            finally:
                arquivo.close()
        return perfis

# herdando da class Perfil
class Perfil_vip(Perfil):

    def __init__(self, nome, telefone, empresa, apelido):
        # herdando o construtor de outra class
        super(Perfil_vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def show_dados(self):
        print('nome: %s\ntelefone: %s\nempresa: %s\napelido: %s\ncurtidas: %s\nvalor ganho com curtidas: %s' % (self.nome, self.telefone, self.empresa, self.apelido, self.get_curtidas(), self.obter_creditos()))

    # como a propriedade curtidas é privada precisamos acessar pelo meotodo get_curtidas
    def obter_creditos(self):
        return self.get_curtidas() * 10.0


# perfil = Perfil('Bruno Afonso', 'não informado', 'indra')
# perfil.curtir_perfil()
# perfil.curtir_perfil()
# perfil.curtir_perfil()
# perfil.curtir_perfil()
# print(perfil.get_curtidas())
# perfil.show_dados()
#
# vip = Perfil_vip('Bruno Henrique Afonso', 'não informado', 'indra', 'brunohafonso')
# vip.curtir_perfil()
# vip.curtir_perfil()
# vip.curtir_perfil()
# vip.show_dados()
# print(vip.obter_creditos())
