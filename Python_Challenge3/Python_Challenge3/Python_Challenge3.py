import re
p = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
arquivo=open('Teste.txt')
texto=arquivo.read()
resposta = p.findall(texto)
print(resposta)

#RESPOSTA LINKEDLIST