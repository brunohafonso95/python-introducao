# configurando cacarcteres especiais
# -*- coding: UTF-8 -*-
import re

def cadastrar(nomes):
    print('Digite o nome')
    nome = input()
    nomes.append(nome)

def listar_nomes_cadastrados(nomes):
    print('lista de nomes')
    for nome in nomes:
        print(nome)

def filtrar_lista_nome(nomes):
    texto_filtro = input('Digite o texto do filtro')
    print('lista de nomes filtrada')
    for nome in nomes:
        results = re.findall('\w+' + texto_filtro + '\w+', nome)
        for result in results:
            print(result)

def deletar(nomes):
    registro = input('digite o elemento a remover\n')
    nomes.remove(registro)

def terminar():
    print('programa finalizado!')

def menu():
    nomes = []
    escolha = ''
    while escolha != '0':
        print('Digite 1 para cadastrar, Digite 2 para listar os nomes cadastrados, Digite 3 para filtrar os nomes cadastrados, Digite 4 para remover um elemento cadastrado,  0 para terminar')
        escolha = input()
        
        if(escolha == '1'):
            cadastrar(nomes)
        elif(escolha == '2'):
            listar_nomes_cadastrados(nomes)
        elif(escolha == '3'):
            filtrar_lista_nome(nomes)
        elif(escolha == '4'):
            deletar(nomes)
        else:    
            terminar()

menu()