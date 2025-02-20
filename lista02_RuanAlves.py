#Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem “ O último número que você digitou foi um [número] " e pare o programa.

i = 0

while i < 5:
    numero =  int(input("Insira um numero: "))
    i += 1
print("Ultimo numero é: {}".format(numero))




