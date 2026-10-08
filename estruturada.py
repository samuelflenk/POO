nomes = []
notas1 = []
notas2 = []

def cadastrar():
    nome = input("Digite o nome do estudante: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))

    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)

    print("Estudante cadastrado.")

def calcular_media(indice):
    return (notas1[indice] + notas2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)

    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Em recuperação"
    else:
        return "Reprovado"

def listar():
    if len(nomes) == 0:
        print("Nenhum estudante cadastrado")
        return

    print(f"\n{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")

    for i in range(len(nomes)):
        print(f"{nomes[i]:<16}{notas1[i]:<7}{notas2[i]:<7}{calcular_media(i):<8}{situacao(i):<14}")

cadastrar()
listar()
def menu():
    while True:
        print("\n1 - Cadastrar estudante\n2- Listar estudante\n0 - Sair do sistema")
        opcao = input("Digite uma opção: ")

        if(opcao == "1"):
            cadastrar()
        elif(opcao == "2"):
            listar()
        else:
            print("Voce saiu")
            break

menu()
