# -*- coding: UTF-8 -*-
from aula10 import Perfil, Perfil_vip

perfis = []
arquivo = open('./csv/dados.csv', 'r')
for linha in arquivo:
    colunas = linha.split(',')
    if(colunas[0] == '1'):
        perfil = Perfil(colunas[1], colunas[2], colunas[3])
        perfis.append(perfil)
    else:
        perfil = Perfil_vip(colunas[1], colunas[2], colunas[3], colunas[4])
        perfis.append(perfil)


for perfil in perfis:
    print(perfil.nome)
