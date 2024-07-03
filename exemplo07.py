import os
os.system ("cls")

print("exibindo intervalos dos números")

#1 passo - entrada dos números
primeiro_numero = int(input("Digite o primeiro número da sua ordem: "))
segundo_numero = int(input("Digite o número final da sua ordem: "))

#2 passo - processando a ordem dos números
if primeiro_numero < segundo_numero:
    while primeiro_numero < segundo_numero:
     primeiro_numero = primeiro_numero + 1
     print("Número:",primeiro_numero)
    

else:
   while segundo_numero < primeiro_numero:
      segundo_numero = segundo_numero + 1
      print("Número:",segundo_numero)    

input("Pressione <ENTER> para encerrar...")          

