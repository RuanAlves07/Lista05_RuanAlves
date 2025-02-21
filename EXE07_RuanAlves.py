#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.

lista_numeros = []
i = 0 

while i < 1:
    numero = int(input("Insira um valor: (0 para finalizar) "))

    if numero in lista_numeros:
        lista_numeros.index(numero)
        print("Já inserido! Porfavor, inserir outro valor.")
        lista_numeros.remove(numero)
    if numero == 0:
        print("Numeros inseridos: {}".format(lista_numeros))
        break
    else:
        lista_numeros.append(numero)

print ("Ruan Augusto Alves")
