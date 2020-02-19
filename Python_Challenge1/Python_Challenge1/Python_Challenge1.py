#from string import maketrans
frase = "map"
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = frase.maketrans(intab, outtab)
print (frase.translate(trantab))

#RESPOSTA OCR