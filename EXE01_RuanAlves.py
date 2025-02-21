#Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.

i = 0

while True:
    numero = int(input("Insira o número digitado "))
    i += numero

    if i > 50:
        print("O total é: {}".format(i))
        break


print ("Ruan Augusto Alves")