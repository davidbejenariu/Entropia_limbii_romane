import string
import math

def read():
    reader = open("data/total.txt", "r", encoding='utf-8')
    text = reader.read()
    text = text.replace('ţ', 'ț')
    text = text.replace('ş', 'ș')
    text = text.replace('é', '')
    #string in care memoram caractere neobisnuite
    str = "0123456789“”йд’µ…‘†à„–·éí✓ç»áó¡→ã±áäéá¾¼é½©°'²''³''ä¹';■öä×¬«§¥÷⋅≥≤−∆↓↑•βúαü"
    for c in str:
        text = text.replace(c,'')
    #eliminam punctuatia obisnuita
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace('\n', ' ').replace('—','').replace('  ', ' ')
    #eliminam caractere white space
    text = text.replace('\uf0b7', '')
    text = text.replace('\uf0a7', '')
    text = text.replace('\uf0d8', '')
    text = text.replace('\uf02d', '')
    text = text.replace('\u2008', '')
    text = text.replace('\uf8eb', '')
    text = text.replace('\uf8ec', '')
    text = text.replace('\uf8ed', '')
    text = text.replace('\uf8f6', '')
    text = text.replace('\uf8f7', '')
    text = text.replace('\uf8f8', '')
    text = text.replace('\x83', '')
    text = text.replace('\t', '')
    text = text.lower()
    return text

def countInstances(k, text):

    #k reprezinta lungimea secventelor dupa care calculam entropia
    #d - dictionar in care memoram cuvintele si aparitiile
    d = {}
    l = len(text)
    for i in range(0, l - k + 1):
        s = text[ i : i+k ]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    #print("intrati:", d.items(), sep = '\n')
    return d

def computeEntropy(k, text):

    dict = countInstances(k, text)
    totalWords = sum(dict.values())
    H = 0 # entropia
    for s in dict:
        P = dict[s] / totalWords #calculam probabilitatea unui cuvant
        H -= P * math.log(P,2)
    return H

text = read()
listCount = text.split(" ")
totalLen = len(text) - text.count(" ")
print("Lungimea medie a unui cuvant: " + str(totalLen / len(listCount)))
Hprev = 0
F = 0
for i in range(1,7):
    H = computeEntropy(i, text)
    print('H' + str(i) + " = " + str(H))
    F = H - Hprev
    print('F' + str(i) + " = " + str(F))
    print()
    Hprev = H
