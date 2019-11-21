import re

cripto   = "REEELQWSVKLPFXWJAUEGWDFJDOWFYCVBJYYZNXRHTBNYNBKIUUUZKQVJVBWHLFWTCPFGOQIOTQJIGQIYZSRZUOFSKPNPRORIJTNXYZUXJDWYRQEAKWUCXZURRPWMFFGTADNPNXWXJUISRZWWZSRCEZUTPPWONBWWRUEQUGRMCUVZYXRSRDROFGNNREJZZCNHTQUQEHWLPLJCYQWHKC"
palabraConocida  = "CALENTAMIENTO"

# Recorremos la palabra que sabemos que aparece
# en el mensaje viendo si sus letras pertenecen al
# primer grupo (A-M) o al segundo (N-Z)

def partesDic(str, invertido=False):
    ndic = ""
    for c in str:
        if ord(c) >= 65 and ord(c) <= 77:
            ndic += "1" if invertido == False else "0"
        else:
            ndic += "0" if invertido == False else "1"

    return ndic

# Invierte la palabra conocida para que coincida con alguna posicion del criptograma
partesPalConocida = partesDic(palabraConocida, invertido=True)
partesCripto = partesDic(cripto)
print("Partes del diccionario usadas en palabra conocida: {}".format(partesPalConocida))
print("Partes del diccionario usadas en el criptograma: {}".format(partesCripto))

x = re.search(".{}.".format(partesPalConocida), partesCripto)
if x is None:
    print("No se ha encotrado ninguna palabra conocida")
    exit()

print("Se ha encontrado la palabra conocida: {}".format(x))