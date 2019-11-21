criptograma = "UJPDNAAJMNERNCWJVODNDWLXWOURLCXKNURLXYJAJRVYNMRAUJANDWRORLJLRXWMNERNCWJVKJSXDWPXKRNAWXLXVDWRBCJNWM"

print("Criptograma: " + criptograma)


for d in range(1,26):
    mensaje = ""
    for c in range(len(criptograma)):
        letra = criptograma[c]
        mensaje += chr((ord(letra) + d - 65) % 26 + 65)

    print("Desplazamiento {}\t: {}".format(str(d), mensaje))
