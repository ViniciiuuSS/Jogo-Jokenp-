from random import randint
from time import sleep
print("\033[1;33;44m-=-" * 54)
jo = ("\033[1;31;44m Jogo do Jokenpô")
print(jo.center(170))
print("\033[1;33;44m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------

itens = ("Pedra", "Papel", "Tesoura")
comp = randint(0,2)
jogador = int(input("""\033[7;40mEscolha uma posição: 
[0] Pedra
[1] Papel
[2] Tesoura
>>>:"""))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
print("Computador jogou {}".format(itens[comp]))
print("Jogador jogou {}".format(itens[jogador]))
if( comp == 0):
    if (jogador == 0):
        print("EMPATE")
    elif (jogador == 1):
        print("JOGADOR VENCE")
    elif (jogador == 2):
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif (comp == 1):
    if (jogador == 0):
        print("COMPUTADOR VENCE")
    elif (jogador == 1):
        print("EMPATE")
    elif (jogador == 2):
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif (comp == 2):
    if (jogador == 0):
        print("JOGADOR VENCE")
    elif(jogador == 1):
        print("COMPUTADOR VENCE")
    elif(jogador == 2):
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")