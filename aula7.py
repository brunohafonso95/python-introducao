# trabalhando com expressões regulares
# importando lib para expressões regulares
import re

# busca uma correspondencia na string informada
result = re.match('[A-Z-a-z]y', 'Python')
# group retorna a correspondencia da regex
print(result.group())

results = re.findall('[A-Za-z]y[A-Za-z]+', 'Python ou jython')
results = re.findall('\wy\w+', 'Python ou jython')
print(results)
