import os
os.system ("cls")

print("Exemplo de While com texto")

#1 passo - entrada
resposta = input("Deseja calcular a soma de dois números? (sim) ou (nao): ").lower()

while resposta == "sim":
    print("---------------------------------")
    print("Calculando a soma de dois números")
    print("---------------------------------")


    v1 = int(input("Digite um número: "))
    v2 = int(input("Digite um número: "))

    #2 passo - processamento
    resultado = v1 + v2

    #3 pass - saida
    print("O resultado é:",resultado)

    resposta = input("Digite (sim) para reiniciar, e (nao) para encerrar!: ").lower()

else:
    input("Pressione <enter> para encerrar o programa...")    

    



