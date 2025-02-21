#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".

i = 0

while i < 1:
    numero = int(input("Insira um número: "))
    
    if numero < 14:
        print ("Muito baixo!")
    if numero > 21:
        print("Muito alto!")
    if numero >= 15 and numero <= 20:
        print("Obrigado!")
        i = i + 1
        break