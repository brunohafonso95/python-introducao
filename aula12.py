# -*- coding: UTF-8 -*-
from aula10 import Perfil, Perfil_vip

perfis = Perfil.obter_perfis_csv('dados.csv')
for perf in perfis:
    print(perf.nome)
