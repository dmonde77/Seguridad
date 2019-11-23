from vigenere import IC, Media, decryptQuadgram

criptograma = "AZESMYGZBUOLLBSVKLAZBPYCYDVZKLZCOBTYQZWPRGLOYIXCDSYWIMXDXGUYEQKIGHLQMVSMZABLXMPMEUGDLABPIYODWVZMCDCFGJXHCTURTDWWUYDHCAOMLKKLYAFDVHJCOHLBPMDSYWKLDTCWXGXDBVYGYSOUZMDCOJULGDBAOPDTCOGZTKSKGBPROUGJRNBLTRLAVLYCPMMVTRCNMVTKFBRHYBPBOWIGZMOZVCCNPPTYWLOUZCZADBBMPKOUIYCFYKKCWZLVXYCZVNALLRSSAQEQKJOMYDCWGPLTXHXCGHCAGBPLYKGCYC"

#criptograma = "DAZFISFSPAVQLSNPXYSZWXALCDAFGQUISMTPHZGAMKTTFTCCFXKFCRGGLPFETZMMMZOZDEADWVZWMWKVGQSOHQSVHPWFKLSLEASEPWHMJEGKPURVSXJXVBWVPOSDETEQTXOBZIKWCXLWNUOVJMJCLLOEOFAZENVMJILOWZEKAZEJAQDILSWWESGUGKTZGQZVRMNWTQSEOTKTKPBSTAMQVERMJEGLJQRTLGFJYGSPTZPGTACMOECBXSESCIYGUFPKVILLTWDKSZODFWFWEAAPQTFSTQIRGMPMELRYELHQSVWBAWMOSDELHMUZGPGYEKZUKWTAMZJMLSEVJQTGLAWVOVVXHKWQILIEUYSZWXAHHUSZOGMUZQCIMVZUVWIFJJHPWVXFSETZEDF"

print("Criptograma: {}\n".format(criptograma))

ICsMedios = []

for i in range(1, 18):

    m = []
    c = 0

    print("Múltiplo de {}:".format(i))

    for n in range(i):
        m.append(list())

    for c in range(criptograma.__len__()):
        arrayEnUso = m[c % i]
        arrayEnUso.append(criptograma[c])

    ICs = []
    for c in range(m.__len__()):

        # Une la lista en una string
        line = "".join(m[c])

        # Obtenemos el IC para esta linea
        IClinea = IC(line)
        print("L{}: {}".format(c+1, line))
        ICs.append(IClinea)

    ICmedio = Media(ICs)
    ICsMedios.append(ICmedio)
    print("IC medio: {}".format(ICmedio))
    print()

ICprobable = max(ICsMedios)
longitudProbable = ICsMedios.index(ICprobable) + 1
print("La clave más probable es de longitud {} , con un IC de {}".format(longitudProbable, ICprobable))

print("Probando claves de longitud {}".format(longitudProbable))

decryptQuadgram(criptograma, longitudProbable)

