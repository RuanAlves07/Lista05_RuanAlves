#Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem “ O último número que você digitou foi um [número] " e pare o programa.

i = 0

while True:
    numero = input (int(input("Insira um numero: ")))
    i += 1
    if i == 5:
        print ("Resultado deu: {}".format(numero))
        break


