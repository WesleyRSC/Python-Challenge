import urllib.request
import re

valor='12345'
i=0
while i<400:
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+ valor) as response:
        html = response.read()
        print(i)
        print(html)
        rex = re.compile('[0-9]+')
        numero = rex.findall(html.decode("utf-8"))
        #teste=numero[0]

        if numero:
            valor = numero[0]
        else :
            valor=input("Digita ai o novo numero: ")
        i=i+1


#RESPOSTA PEAK