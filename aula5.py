# para capturar entrada de dados no teclado usamos a função input
nome = input('qual o seu nome ?')
print(nome)

# entrada de dados são sempre tratadas como string
# para calculos matematicos é necessario converter a entrada de dados para in ou float

num1 = input('digite um numero:\n')
num2 = input('digite outro numero:\n')
print(int(num1) + int(num2))