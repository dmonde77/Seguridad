cripto   = "REEELQWSVKLPFXWJAUEGWDFJDOWFYCVBJYYZNXRHTBNYNBKIUUUZKQVJVBWHLFWTCPFGOQIOTQJIGQIYZSRZUOFSKPNPRORIJTNXYZUXJDWYRQEAKWUCXZURRPWMFFGTADNPNXWXJUISRZWWZSRCEZUTPPWONBWWRUEQUGRMCUVZYXRSRDROFGNNREJZZCNHTQUQEHWLPLJCYQWHKC"

# Diccionarios
AB = {
    "A" : "N",
    "B" : "O",
    "C" : "P",
    "D" : "Q",
    "E" : "R",
    "F" : "S",
    "G" : "T",
    "H" : "U",
    "I" : "V",
    "J" : "W",
    "K" : "X",
    "L" : "Y",
    "M" : "Z",
}

CD = {
    "A" : "Z",
    "B" : "N",
    "C" : "O",
    "D" : "P",
    "E" : "Q",
    "F" : "R",
    "G" : "S",
    "H" : "T",
    "I" : "U",
    "J" : "V",
    "K" : "W",
    "L" : "X",
    "M" : "Y",
}

EF = {
    "A" : "Y",
    "B" : "Z",
    "C" : "N",
    "D" : "O",
    "E" : "P",
    "F" : "Q",
    "G" : "R",
    "H" : "S",
    "I" : "T",
    "J" : "U",
    "K" : "V",
    "L" : "W",
    "M" : "X",
}

GH = {
    "A" : "X",
    "B" : "Y",
    "C" : "Z",
    "D" : "N",
    "E" : "O",
    "F" : "P",
    "G" : "Q",
    "H" : "R",
    "I" : "S",
    "J" : "T",
    "K" : "U",
    "L" : "V",
    "M" : "W",
}

IJ = {
    "A" : "W",
    "B" : "X",
    "C" : "Y",
    "D" : "Z",
    "E" : "N",
    "F" : "O",
    "G" : "P",
    "H" : "Q",
    "I" : "R",
    "J" : "S",
    "K" : "T",
    "L" : "U",
    "M" : "V",
}

KL = {
    "A" : "V",
    "B" : "W",
    "C" : "Z",
    "D" : "Y",
    "E" : "Z",
    "F" : "N",
    "G" : "O",
    "H" : "P",
    "I" : "Q",
    "J" : "R",
    "K" : "S",
    "L" : "T",
    "M" : "U",
}

MN = {
    "A" : "U",
    "B" : "V",
    "C" : "W",
    "D" : "X",
    "E" : "Y",
    "F" : "Z",
    "G" : "N",
    "H" : "O",
    "I" : "P",
    "J" : "Q",
    "K" : "R",
    "L" : "S",
    "M" : "T",
}

OP = {
    "A" : "T",
    "B" : "U",
    "C" : "V",
    "D" : "W",
    "E" : "X",
    "F" : "Y",
    "G" : "Z",
    "H" : "N",
    "I" : "O",
    "J" : "P",
    "K" : "Q",
    "L" : "R",
    "M" : "S",
}

QR = {
    "A" : "S",
    "B" : "T",
    "C" : "U",
    "D" : "V",
    "E" : "W",
    "F" : "X",
    "G" : "Y",
    "H" : "Z",
    "I" : "N",
    "J" : "O",
    "K" : "P",
    "L" : "Q",
    "M" : "R",
}

ST = {
    "A" : "R",
    "B" : "S",
    "C" : "T",
    "D" : "U",
    "E" : "V",
    "F" : "W",
    "G" : "X",
    "H" : "Y",
    "I" : "Z",
    "J" : "N",
    "K" : "O",
    "L" : "P",
    "M" : "Q",
}

UV = {
    "A" : "Q",
    "B" : "R",
    "C" : "S",
    "D" : "T",
    "E" : "U",
    "F" : "V",
    "G" : "W",
    "H" : "X",
    "I" : "Y",
    "J" : "Z",
    "K" : "N",
    "L" : "O",
    "M" : "P",
}

WX = {
    "A" : "P",
    "B" : "Q",
    "C" : "R",
    "D" : "S",
    "E" : "T",
    "F" : "U",
    "G" : "V",
    "H" : "W",
    "I" : "X",
    "J" : "Y",
    "K" : "Z",
    "L" : "N",
    "M" : "O",
}

YZ = {
    "A" : "O",
    "B" : "P",
    "C" : "Q",
    "D" : "R",
    "E" : "S",
    "F" : "T",
    "G" : "U",
    "H" : "V",
    "I" : "W",
    "J" : "X",
    "K" : "Y",
    "L" : "Z",
    "M" : "N",
}


diccionarios = [AB, CD, EF, GH, IJ, KL, MN, OP, QR, ST, UV, WX, YZ]

#clave = S  U   I  C  I  D  I  O
#dic   = ST UV  IJ CD IJ CD IJ OP
clave = (9, 10, 4, 1, 4, 1, 4, 7)

index = 0

mensaje = ""
for letra in cripto:
    # Obtenemos el diccionario a usar
    itemKey = clave[index]
    if index < len(clave)-1:
        index += 1
    else:
        index = 0

    dic = diccionarios[itemKey]

    # Primera parte del alfabeto
    if letra in dic.keys():
        mensaje += dic.get(letra)

    # Segunda parte del alfabeto, la letra estará entre los valores del diccionario
    else:
        mensaje += next(key for key, value in dic.items() if value == letra)


print("Mensaje: {}".format(mensaje))

