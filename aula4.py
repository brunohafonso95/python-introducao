# trabalhando com funções
convite =  'Bruno Afonso'
parte1 = convite[0:4]
parte2 = convite[6:11]
print('%s %s' % (parte1, parte2))

# conseguindo o length de uma string
print(len(parte1))

# definindo uma função com um parametro
def invite_name_generator(name):
    posicao_final = len(name)
    posicao_inicial = posicao_final - 4
    parte1 = name[0:4]
    parte2 = convite[posicao_inicial: posicao_final]
    return '%s %s' % (parte1, parte2)

formated_invite_name = invite_name_generator('Bruno Afonso')
print(formated_invite_name)

