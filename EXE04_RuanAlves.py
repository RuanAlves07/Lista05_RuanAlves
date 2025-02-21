#Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.

convites = []
i = 0

while i < 5:
        nomes_convites = input("Informe o nome das pessoas convidadas: ")
        convites.append(nomes_convites)
        print("{} foi adicionado(a) com sucesso no convite!".format(convites))
        continuação = input("Deseja convidar outra pessoa? (S/N)")
        if continuação == "n":
            print("Os seguintes membros foram convidados: {}".format(convites))
            break
        elif continuação != "s":
              print("Insira uma resposta valida!")
                


print ("Ruan Augusto Alves")

