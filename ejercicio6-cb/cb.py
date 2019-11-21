
def descifrar(s):
    resultado = ""

    T = [["",  "6", "1", "9", "7", "4", "3", "5", "0", "2", "8"],
            ["",  "A", "T",  "", "O", "N", "E",  "", "S", "I", "R"],
            ["9", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M"],
            ["5", "P", "Q", "U", "V", "W", "X", "Y", "Z", ".", "/"]]

    s = iter(s)
    for c in s:
        if c in [T[2][0], T[3][0]]:
            i = [T[2][0], T[3][0]].index(c)
            n = T[2 + i][T[0].index(s.__next__())]
            resultado += " " if n == "/" else n
        else:
            resultado += T[1][T[0].index(c)]

    return resultado


criptograma = "39258915961875899358696829258993589829258475739123417058912491593416585558791937583458927499830580358913926968658594658986429730169124589935899235058982925856380746058917418658926589679896658617982916"
print("Criptograma: {}".format(criptograma))

mensaje = descifrar(criptograma)
print("Mensaje: {}".format(mensaje))