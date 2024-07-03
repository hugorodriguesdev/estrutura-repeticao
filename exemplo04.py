import os
os.system ("cls")

print("Exemplo de While ultilizando continue")

contador = 0

while contador < 6:
    contador = contador + 1

    if contador == 3:
        continue

    print(contador)
