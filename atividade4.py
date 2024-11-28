import os
import csv
import re

arquivo = "cadastro.csv"

def menu():
    print("MENU")
    print("1) Cadastrar")
    print("2) Listar")
    print("3) Atualizar")
    print("4) Deletar")
    print("5) Sair")

def cadastrar():
    if not os.path.isfile(arquivo):
        with open(arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv: 
            escritor = csv.writer(arquivo_csv) 
            escritor.writerow(["Nome", "Email", "Telefone"])
            funcCad ()    
    else:
        funcCad ()

def listar():
    with open(arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv: 
        ler = csv.reader(arquivo_csv) 
        for id, linha in enumerate(ler, start=1): 
            print(f"{id}) {linha}")

def atualizar():
    listar()
    id_escolhido = int(input("Digite o ID que deseja editar: "))
    linhas = []
    with open(arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for id, linha in enumerate(leitor, start=1):
            if id == id_escolhido:
                print(f"Dados atuais: Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}")
                nome = input("Digite o novo nome (deixe em branco para não alterar): ")
                email = input("Digite o novo e-mail (deixe em branco para não alterar): ")
                telefone = input("Digite o novo telefone (deixe em branco para não alterar): ")
                if nome:
                    linha[0] = nome
                if email:
                    linha[1] = email
                if telefone:
                    linha[2] = telefone
            linhas.append(linha)

    with open(arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(linhas)
    print("Dados atualizados com sucesso!")
    listar()


def deletar():
    listar()
    id_escolhido = int(input("Digite o ID que deseja deletar: "))
    linhas = []
    with open(arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for id, linha in enumerate(leitor, start=1):
            if id != id_escolhido:
                linhas.append(linha)
            else:
                print(f"Dados a serem deletados: Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}")
                confirmacao = input("Tem certeza que deseja deletar esses dados? (s/n): ")
                if confirmacao.lower() != 's':
                    linhas.append(linha)
                    print("Operação cancelada.")
                    return
    with open(arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(linhas)
    print("Dados deletados com sucesso!")
    listar()

def main():
    while True:
        menu()
        opcao = input("Opção (1-5): ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            print("Fim do Programa")
            break
        else:
            print("Opção inválida!")

def funcCad ():
    while True:
            nome = input("Digite o nome: ")
            if nome == "":
                print("O campo não pode estar vazio")
                continue

            while True:
                email = input ("Digite o e-mail: ")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email): 
                    print("O campo e-mail deve conter um e-mail válido.") 
                    continue
                if email == "":
                    print("O campo não pode estar vazio")
                    continue
                break

            while True:
                telefone = input ("Digite o telefone: ")
                if telefone == "":
                    print("O campo não pode estar vazio")
                    continue
                if not telefone.isnumeric(): 
                    print("O campo telefone deve conter apenas números.") 
                    continue
                break
        
            with open(arquivo, mode='a', newline='', encoding='utf-8') as arquivo_csv: 
                escritor = csv.writer(arquivo_csv) 
                escritor.writerow([nome, email, telefone]) 
                print("Usuário Cadastrado com sucesso")
                break
            
    listar()

if __name__ == "__main__":
    main()

