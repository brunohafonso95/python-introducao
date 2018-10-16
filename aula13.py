# -*- coding: UTF-8 -*-
from aula10 import Perfil, Perfil_vip

try:
    perfis = Perfil.obter_perfis_csv('dados.csv')
    for perfil in perfis:
        print(perfil.nome)
except IOError as error:
    print('O arquivo não existe. %s' % error)

