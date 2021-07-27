from typing import Text
import random
def jogar():
    print("*****************************************")
    Nome = input("Qual é o seu nome? ")
    print(f"Bem vindo {Nome}, ao jogo de Advinhação")
    print("*****************************************")
    print()

    # NumeroSecreto
    # 0.0
    Numero_secreto = random.randrange(1, 100)
    Try = 0
    Points = 100

    print("Escolha o Nível de Dificuldade")
    print("(1) Fácil, (2) Médio ou (3) Difícil")

    Level = int(input("Digite o Nível: "))
    if Level == 1:
        Try = 20
    elif Level == 2:
        Try = 10
    else:
        Try = 5
    # while Rodada <= Try:
    for Rodada in range(1, Try + 1):
        print(f"Tentativa {format(Rodada)} de {Try}.")

        # print(Rodada, "Tentativa de",Try)
        if Try == 1:
            lastchance = Text(input(f"ÚLTIMA TENTATIVA {Nome}, você está preparado? Responda com Sim, Não. "))
            lastchance == lastchance.upper()
            print(lastchance, "!", "É a Hora da verdade.")
            # if Try == Yes:
        elif Try == 0:
            print("Acabaram as suas tentativas")
        Numero_usuario = str(input("Digite um numero entre 1 a 100!: "))
        print("Você digitou:", Numero_usuario)

        Numero_usuario = int(Numero_usuario)
        Acertou = Numero_secreto == Numero_usuario
        Maior = Numero_secreto > Numero_usuario
        Menor = Numero_secreto < Numero_usuario
        if Numero_usuario < 1 or Numero_usuario > 100:
            print("Você deve digitar um número entre 1 a 100")
            continue

        # if Numero_usuario == Numero_secreto:
        if Acertou:
            print(f"Você acertou, o número secreto é {format(Numero_secreto)} e você fez {Points} pontos!")
            # Break - Saí do Laço
            break
        else:
            LostPoints = abs(Numero_secreto - Numero_usuario)
            Points = Points - LostPoints
            # if Numero_usuario > Numero_secreto:
            if Maior:
                print("Você errou! O seu numero foi maior que o numero secreto")
                print(f"O numero secreto é {Numero_secreto} e seus pontos são {Points}!")


            # if Numero_usuario < Numero_secreto:
            # elif Numero_usuario < Numero_secreto:
            elif Menor:
                print("Você errou! O seu numero foi menor que o numero secreto")
                print(f"O numero secreto é {Numero_secreto} e você tem {Points}")
                # Sum

        # Rodada = Rodada + 1
        # print("Você errou")
    print("Fim do Jogo")
#condição para jogar
if __name__ =="__main__":
    jogar()