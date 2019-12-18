import math
import sys

#f = open("/home/diego/PycharmProjects/Seguridad/ejercicio11-entropia/file", "rb")
#f = open("/home/diego/PycharmProjects/Seguridad/ejercicio11-entropia/randomChar", "rb")
#f = open("/home/diego/Downloads/ply-3.11.tar.gz", "rb")
#f = open("/home/diego/Documents/id_rsa.pub", "rb")

f = open(sys.argv[1], "rb")

bytesArr = []
while True:
    ventana = f.read(1)
    if not ventana:
        break
    bytesArr.append(ventana)

f.close()

print(bytesArr)

fileSize = bytesArr.__len__()
print("Tamaño en bytes: {}".format(fileSize))

frecuencias = []

for b in range(256):
    ocurrencias = 0
    for bite in bytesArr:
        if bite == b.to_bytes(1, byteorder="big"):
            ocurrencias += 1
    frecuencias.append(ocurrencias / fileSize)
print("Frecuencias de cada byte: {}".format(frecuencias))


entropia = 0.0
for freq in frecuencias:
    if freq > 0:
        entropia = entropia + freq * math.log(freq, 2)
entropia = -entropia
print("Entropía: {}".format(entropia))

### Histogram by Ken Hartman www.KennethGHartman.com

import numpy as np
import matplotlib.pyplot as plt

ind = np.arange(len(frecuencias))  # the x locations for the groups
width = 1.00        # the width of the bars

fig = plt.figure(figsize=(11,5),dpi=100)
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, frecuencias, width)
ax.set_autoscalex_on(False)
ax.set_xlim([0,frecuencias.__len__()])

ax.set_ylabel("Frecuencia")
ax.set_xlabel("Byte")
plt.show()