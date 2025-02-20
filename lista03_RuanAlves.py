#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.

total = 0
i = 0

while i < 5:
    numero = int(input("Insira um numero: "))
    pergunta = input("Deseja inserir outro número? (S/N) ")
    i += 1

    if pergunta == "s":
        total += numero
    else:
        total += numero
        break

print("Total deu: {}".format(total))

print ("Ruan Augusto Alves")


