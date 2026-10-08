class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        return (self.nota1 + self.nota2) / 2
    def situacao(self):
        media = self.media()
        if media >= 6:
            return "Aprovado"
        elif media >= 4:
            return "Recuperação"
        else:
            return "Reprovado"
    def descrever(self):
            return f"{self.nome:<16}{self.nota1:<7}{self.nota2:<7}{self.media():<8}{self.situacao():<14}"
estudantes = []

def cadastrar():
    nome = input("Nome do estudante: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    
    estudantes.append(Estudante(nome, nota1, nota2))
    print("Estudante cadastrado.")

def listar():
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado")
        return

    print(f"\n{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}")
    for estudante in estudantes:
        print(estudante.descrever())

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

    