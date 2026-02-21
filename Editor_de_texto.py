def menu():
    print("O que você quer fazer?")
    print("Modificar um caractere (1)")
    print("Verificar o tamanho da frase (2)")
    print("Contar quantas vezes um caractere apareceu (3)")
    print("Verificar quando um caractere aparece (4)")
    print("Sair (5)")

frase = input("Digite uma frase: ")

while True:

    menu()
    resposta = int(input("Resposta: "))

    match resposta:
        case 1:
            caractereSubsituido = input("Digite o caractere a ser substituido: ")
            caractereSubstituto = input("Digite o caractere a ser o substituto: ")

            print(frase)
            print(frase.replace(caractereSubsituido, caractereSubstituto))

        case 2:
            tamanho = len(frase)
            print(tamanho)

        case 3:
            caractere = input("Escolha um caractere: ")

            if caractere in frase:
                print(frase)
                quantidade = frase.count(caractere)
                print(quantidade)

        case 4:
            caractere = input("Escolha um caractere: ")

            posicao = frase.find(caractere)
            print(posicao)

        case 5:
            break

        case _:

            print("Insira uma opção válida!!!")