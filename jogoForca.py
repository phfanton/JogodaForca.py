import os
def limparTela():
    os.system("cls")


limparTela()
print('+++++++++  JOGO DA FORCA - by João Nazzari and Pedro Fanton +++++++++ ')

desafiante = input("Desafiante: ")
competidor = input("Competidor: ")

limparTela()
palavraChave = input("Desafiante digite a PALAVRA: ")
dica1 = input("Desafiante digite a PRIMEIRA DICA: ")
dica2 = input("Desafiante digite a SEGUNDA DICA: ")
dica3 = input("Desafiante digite a TERCEIRA DICA: ")
chances = 5
jogadas = 0
letras_jogadas = []
estado_atual = ["*"] * len(palavraChave)   

limparTela()
print(estado_atual)


#FAZER AS OPÇÕES

# (IMPRIMIR AS DICAS)


while chances > 0 and ''.join(estado_atual) != palavraChave:

    letra = input('\n\nDigite uma letra: ')

    while letra in letras_jogadas:
        print('Você já jogou essa letra')
        letra = input('\nTente outra letra: ')

    letras_jogadas.append(letra)
    limparTela()
    
    if letra in palavraChave:
        print('Você acertou uma letra!')
        jogadas = jogadas + 1
        for i in range(len(palavraChave)):
            if letra == palavraChave[i]:
                estado_atual[i] = letra
   
        
    else:
        print('Você errou')
        jogadas = jogadas + 1
        chances = chances - 1
        
    print('Você fez',jogadas,'jogadas')
    print('Restam', chances,'chances')

    print(estado_atual)

    print('Letras já jogadas:')
    for item in letras_jogadas:
        print(item, end=' ')

if chances == 0:
    print('\n\nFORCA! \nSuas tentativas acabaram!')
    print(desafiante,'ganhou')
else:
    print('\n\nPARABÉNS VOCÊ SAIU VIVO!')
    print(desafiante,'perdeu')

print('A palavra era:',palavraChave)

#CRIAR O ARQUIVO DE ARMAZENAMENTO
#PREVENÇÃO DE BUGS


#CRIAR GIT

