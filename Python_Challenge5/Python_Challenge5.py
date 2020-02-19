
import pickle
import urllib.request

html = pickle.load(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print(html)
for line in html:
    print("".join([k * v for k, v in line]))

    #REVER ISSO AQUI

    #Resposta Channel