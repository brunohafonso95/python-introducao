# não há criação explicita de variaveis de python, então uma variavel
# só para a existir após ter um valor atribuido a mesma.

convites, convites_ano_passado = 12, 20
print(convites,'\n',convites_ano_passado)

# tipo long (usamos L no final no valor atribuido)
salario = 10.000

# tipo complexo (usamos j no final no valor atribuido)
salario_chefe = 2700.00j

# string
aspas_duplas = "string com aspas duplas"
aspas_simples = 'string com aspas simples'

# operador slice
nome = 'Bruno Henrique Afonso'
primeiro_nome = nome[0:5]
print(primeiro_nome)

# template string
print('Ola %s, seu salario: %s' % (primeiro_nome, salario))


