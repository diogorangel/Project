import advinhacao
import forca

def escolhe_jogo():

    print("*****************************************")
    Nome = input("Qual é o seu nome? ")
    print(f"Bem vindo {Nome}, Nós temos dois jogos, (1) é da advinhacao e o outro (2)é da forca")
    print("*****************************************")

    Jogos = int(input("Escolha um jogo: "))
    if Jogos == 1:
        print("Jogar Advinhacao")
        advinhacao.jogar()

    elif Jogos == 2:
        print("Jogar forca")
        #forca.jogar_forca()
        forca.jogar()
if __name__ =="__main__":
    escolhe_jogo()