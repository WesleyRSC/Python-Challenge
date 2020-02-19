from collections import Counter

arquivo = open('teste.txt')
texto=arquivo.read()
c=Counter(texto)
print(c.most_common())
arquivo.close()

#RESPOSTA EQUALITY