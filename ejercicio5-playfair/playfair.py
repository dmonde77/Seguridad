import re

criptograma = "IKFNABBIRAGVFPIBIKVOWQVCRVXVUGEWVOBVBFIVQCBSNACPVCUNVBPNEYQCQTABWTCOHCHSUGICYGAQVIHSNQPOCIQTRSVQIHIKDADVQSIKEVVYSIBYBIIHABCEWIHIARORYVBSCORHVOISIKVHIHCEVPBY"
key = "VAEVICTIS"
mensaje = ""

def generarMatriz(k):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matriz = []

    for c in k.upper():
        if c not in matriz and c in alfabeto:
              matriz.append(c)

    for c in alfabeto:
        if c not in matriz:
            matriz.append(c)

    return matriz


matriz = generarMatriz(key)

for c1, c2 in re.findall("..", criptograma):
    fil1, col1 = divmod(matriz.index(c1), 5)
    fil2, col2 = divmod(matriz.index(c2), 5)

    if fil1 == fil2:
        mensaje += matriz[fil1*5+(col1-1)%5]
        mensaje += matriz[fil2*5+(col2-1)%5]
    elif col1 == col2:
        mensaje += matriz[((fil1-1)%5)*5+col1]
        mensaje += matriz[((fil2-1)%5)*5+col2]
    else:
        mensaje += matriz[fil1*5+col2]
        mensaje += matriz[fil2*5+col1]

print("Mensaje: {}".format(mensaje))

