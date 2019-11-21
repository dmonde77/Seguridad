

def extraerColumnas(path):
    final = ""
    for i in range(0, 100):
        for line in open(path, "r"):
            try:
                if line[i] is "\n":
                    pass
                else:
                    final += line[i]
            except IndexError:
                pass
    return final

def descifrar(s):
    resultado = ""

    T = [["",  "7", "1", "3", "4", "9", "8", "2", "6", "5", "0"],
         ["",  "A", "T",  "", "O", "N", "E",  "", "S", "I", "R"],
         ["3", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M"],
         ["2", "P", "Q", "U", "V", "W", "X", "Y", "Z", ".", "/"]]

    s = iter(s)
    for c in s:
        if c in [T[2][0], T[3][0]]:
            i = [T[2][0], T[3][0]].index(c)
            n = T[2 + i][T[0].index(s.__next__())]
            resultado += " " if n == "/" else n
        else:
            resultado += T[1][T[0].index(c)]

    return resultado



criptograma = extraerColumnas("/home/diego/PycharmProjects/Seguridad/ejercicio3-CBdoble/dataCB")
print("Criptograma: {}".format(criptograma))

mensaje = descifrar(criptograma)
print("Mensaje: {}".format(mensaje))

