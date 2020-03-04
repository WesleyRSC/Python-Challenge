import re

valor = 'readme'
i = 1
j=1
lista=[]
lista2=[]
while i < 910:
    if i == 2:
        arquivos = open('channel/' + numero[1] + '.txt').read()
        lista.insert(int(lista.pop(0)), int(numero[1]))
    else:
        arquivos = open('channel/' + valor + '.txt').read()
    print(arquivos)
    rex = re.compile('[0-9]+')
    numero = rex.findall(arquivos)
    blocos = ""
    teste = numero[0]
    lista.append(int(teste))

    if numero:
        valor = teste
        str(valor)
    print(i)
    i = i + 1
    if i == 909:
        continue

print(lista)
listaaux =lista.copy()

lista.sort()

print('\n\n',lista)

for x in lista:


    lista2.append(int(x))


print('\n\n',lista2)

for t in zip(listaaux,lista2):
    print(t)


#valor='29'
#while j < 910:
#    #if i == 2:
#     #   arquivos = open('channel/' + numero[1] + '.txt').read()
#      #  lista2.insert(int(lista2.pop(0)), numero[1])
#    #else:
#    arquivos = open('channel/' + valor + '.txt').read()
#    print(arquivos)
#    rex = re.compile('[0-9]+')
#    numero = rex.findall(arquivos)
#    blocos = ""
#    teste = numero[0]
#    lista2.append(teste)
#
#    if numero:
#        valor = teste
#        str(valor)
#    else:
#        valor=input("Digite qualquer coisa:")
#    print(j)
#    j = j + 1
#    if j == 909:
#        continue
#print("\n\n", lista2)
#