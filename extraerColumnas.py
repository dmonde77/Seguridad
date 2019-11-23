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
