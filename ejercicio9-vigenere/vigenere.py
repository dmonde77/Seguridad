import collections
from random import randint
from string import ascii_uppercase
from ngram_score import ngram_score


def IC(string):
    N            = len(string)
    freqs        = collections.Counter(string)
    alphabet     = map(chr, range(ord('A'), ord('Z') + 1))
    freqsum      = 0.0

    for letter in alphabet:
        freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

    IC = freqsum / ( N*(N-1) )

    return IC

def Media(lst):
    return sum(lst) / len(lst)



def decrypt(input, key):
    result = ""
    for i in range(0, len(input)):
        indexInKey = i % len(key)
        caracter = (ord(input[i]) - ord(key[indexInKey]) + 65)

        if caracter < 65:
            caracter += 26

        result += chr(caracter)
    return result


def decryptQuadgram(input, longitudClave):
    key = ""
    for i in range(longitudClave):
        key += chr(65 + randint(0, 25))
    print("Clave aleatoria inicial: ", key)

    ngram = ngram_score("/home/diego/PycharmProjects/Seguridad/ejercicio9-vigenere/spanish_monograms.txt")
    fitness = ngram.score(decrypt(input, key))
    print("Fitness inicial: ", fitness)

    encontrado = False
    indexClave = 0
    while not encontrado:
        bestFitness = float("-inf")
        bestKey = ""

        # Generamos una derivación de la clave
        childrenKeys = computeChildren(key, indexClave)
        indexClave = (indexClave + 1) % longitudClave

        for childKey in childrenKeys:
            childScore = ngram.score(decrypt(input, childKey))
            if childScore > bestFitness:
                bestFitness = childScore
                bestKey = childKey

        if bestFitness-1 <= fitness:
            encontrado = True
        else:
            fitness = bestFitness
            key = bestKey
            print("Clave: {}  Fitness: {}".format(key, fitness))

    print("Clave definitiva: {}".format(key))
    print("Mensaje: {}".format(decrypt(input, key)))

def computeChildren(keyString, indexToModify):
    children = []
    for letter in ascii_uppercase:
        child = list(keyString)
        child[indexToModify] = letter
        children.append("".join(child))
    return children

