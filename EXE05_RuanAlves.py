#Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".

advinha = 50
tentativa = 0



while tentativa != 50:
    numero = int(input("Advinhe o numero que estou pensando: "))

    if numero <= 49:
        print("Numero está abaixo do que estou pensando!")
        tentativa = tentativa + 1
    
    elif numero >= 51:
        print("Numero está a cima do que estou pensando!")
        tentativa = tentativa + 1
    if numero == 50:
        tentativa = tentativa + 1
        print("Parabens! Você acertou o numero em {} tentativas!".format(tentativa))
        break


