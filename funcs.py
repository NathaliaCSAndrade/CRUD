# UMC- Universidade de Mogi das Cruzes
# Engenharia de Software/ADS - Software Básico
# Sarah Êmily Cruz Bianchin - Nathalia Cristiny da Silva Andrade
# Funções usadas no código final
# Bibliotecas
from tabulate import tabulate
import os
# Cores
FIM= '\033[0m' # Reset
AC= '\033[1;94m' # Azul Claro
VERN='\033[1;31m' # Vermelho Negrito
VER='\033[31m' # Apenas vermelho
AN='\033[1;34m' # Azul Negrito
TIT= "GESTÃO DE ADEGA" # Título do app
BC=(f"{AC}{'='}{FIM}") # Coloração da linha
linha= (BC) * (len(TIT) + 40) # Linhas de separação título
line= (BC) * 101 # Linhas de separação de tabela
# Função para verificar a existência do arquivo .txt e abrir
def abrir(D1):
    caminho = "dados.txt"
    if os.path.exists(caminho):
        L1= []
        with open(caminho, 'r', encoding="utf-8") as Dados:
            for i in Dados:
                L1.append(i.rstrip() .split(","))
        for i in L1:
            D1[i[0]]=[i[1],i[2],i[3],i[4],i[5]]
        return D1
    else:
        print("Arquivo não encontrado:", caminho)
# Função para salvar .txt
def salve(dict):
    caminho = "dados.txt"
    with open(caminho, 'w', encoding="utf-8") as Dados:
        for chave,dados in dict.items():
            Dados.write (f"{chave},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]}\n")
# Função para título
def tit():
    print (f'''
{linha}
{AC}{'|'}{FIM}{' '*19}{TIT}{' '*19}{AC}{'|'}{FIM}
{linha}''')
# Função para criação do menu
def menu():
    print (f'''
{linha}
{AN}[1]{FIM} Cadastrar novo produto
{AN}[2]{FIM} Listar produtos
{AN}[3]{FIM} Atualizar lista de produtos
{AN}[4]{FIM} Excluir produto
{AN}[5]{FIM} Pesquisar produto
{AN}[0]{FIM} Encerrar programa
{linha}''')
# Função para validar escolha no menu
def opt():
    while True:
        entrada= input("Entre com a opção desejada: ")
        if entrada in ["1","2","3","4","5","0"]:
            return entrada
        else:
            print (f"{VERN}OPÇÃO INVÁLIDA!{FIM}")
            print (f"{VER}Escolha apenas entre as opções fornecidas{FIM}")
            input("Pessione Enter para tentar novamente!")
            os.system ("cls")
            tit()
            menu()
# Função para Tabela
def lista():    
    cabecalhos=["ID", "Categoria", "Nome", "Preço de custo (R$)", "Preço de venda (R$)", "Quantidade"]
    caminho = "dados.txt"
    L1= []
    with open(caminho, 'r', encoding="utf-8") as Dados:
        for i in Dados:
            L1.append(i.rstrip() .split(","))
    print (line)
    print(tabulate( L1, headers=cabecalhos, tablefmt="double.grid"))
    print (line)
# Função para abrir o txt como lista
def open_lista():    
    caminho = "dados.txt"
    L1= []
    with open(caminho, 'r', encoding="utf-8") as Dados:
        for i in Dados:
            L1.append(i.rstrip() .split(","))
    return L1
# Função para opção 1
def cadastro(D1):
    while True:
        os.system("cls")
        print (f"{AC}Lembre-se que o ID para um novo produto deve ser diferente dos ID's já existentes, sendo ele com 4 digitos numéricos (ex:0007).{FIM}")
        ID= input("Digite o ID para o novo produto: ")
        os.system("cls")
        if ID in D1 or len(ID)<4 or not ID.isdigit():
            print (f"{VERN}ID INVÁLIDO!{FIM}")
            print (f"{VER}Insira um novo ID.{FIM}")
            input("Pressione Enter para tentar novamente!")
            os.system("cls")
        else:
            while True:
                cat = input("Digite a categoria do produto: ").strip()
                os.system("cls")
                if not cat:
                    print(f"{VERN}CATEGORIA INVÁLIDA!{FIM}")
                    print(f"{VER}Digite um valor não vazio.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
                else:
                    break
            while True:
                nm = input("Digite o nome do produto: ").strip()
                os.system("cls")
                if not nm:
                    print(f"{VERN}NOME INVÁLIDO!{FIM}")
                    print(f"{VER}Digite um nome não vazio.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
                else:
                    break
            while True:
                try:
                    ct= float(input("Digite o custo do produto: "))
                    os.system("cls")
                    break
                except ValueError:
                    print (f"{VERN}VALOR INVÁLIDO!{FIM}")
                    print (f"{VER}Digite um valor numérico.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
            while True:
                try:
                    pv= float(input(f"Digite o preço de venda do produto: "))
                    os.system("cls")
                    break
                except ValueError:
                    print (f"{VERN}VALOR INVÁLIDO!{FIM}")
                    print (f"{VER}Digite um valor numérico.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
            while True:
                try:
                    q= int(input("Digite a quantidade de produtos disponiveis no estoque: "))
                    os.system("cls")
                    break
                except ValueError:
                    print (f"{VERN}QUANTIDADE INVÁLIDA!{FIM}")
                    print (f"{VER}Digite um valor numérico.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
            D1[ID]=[cat,nm,ct,pv,q]
            salve(D1)
            print (f"{AC}Item registrado!{FIM}")
            opt= input ("Pressione Enter para adicionar outro produto ou A para voltar ao menu inicial. ")
            if opt in ["A", "a"]:
                break
            else:
                continue
# Função para a opção 2
def listar(D1):
    lista()
    input("\nPressione Enter para voltar ao menu...")
# Função para a opção 3
def atualizar(D1):
    while True:
        os.system("cls")
        lista()
        ID=input("\nInforme o ID do produto que deseja atualizar: ")
        if ID in D1:
            os.system("cls")
            print ("Verifique o produto informado:\n")
            print (line)
            print (f"{ID:<10}{D1[ID][0]:<15}{D1[ID][1]:>15}{D1[ID][2]:>15}{D1[ID][3]:>15}{D1[ID][4]:>15}")
            print (line)
            input ("Pressione Enter para continuar...")
            os.system("cls")
            cat= input("Informe a nova categoria do produto (ou Enter para manter): ") or D1[ID][0]
            os.system("cls")
            nm= input("Informe o novo nome do produto (ou Enter para manter): ") or D1[ID][1]
            os.system("cls")
            while True:
                    try:
                        ct= float(input("Informe o novo custo do produto (ou Enter para manter): ") or D1[ID][2])
                        os.system("cls")
                        break
                    except ValueError:
                        print (f"{VERN}VALOR INVÁLIDO!{FIM}")
                        print (f"{VER}Digite um valor numérico.{FIM}")
                        input("Pressione Enter para tentar novamente!")
                        os.system("cls")
            while True:
                try:
                    pv= float(input(f"Digite o preço de venda do produto (ou Enter para manter): ") or D1[ID][3])
                    os.system("cls")
                    break
                except ValueError:
                    print (f"{VERN}VALOR INVÁLIDO!{FIM}")
                    print (f"{VER}Digite um valor numérico.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
            while True:
                try:
                    q= int(input("Digite a quantidade de produtos disponiveis no estoque (ou Enter para manter): ") or D1[ID][4])
                    os.system("cls")
                    break
                except ValueError:
                    print (f"{VERN}QUANTIDADE INVÁLIDA!{FIM}")
                    print (f"{VER}Digite um valor numérico.{FIM}")
                    input("Pressione Enter para tentar novamente!")
                    os.system("cls")
            D1[ID]=[cat,nm,ct,pv,q]
            salve(D1)
            print (f"{AC}Atualizado com sucesso!{FIM}")
            opt= input ("Pressione Enter para atualizar outro produto ou A para voltar ao menu inicial...")
            if opt in ["A", "a"]:
                break
        else:
            print (f"{VERN}ID NÃO ENCONTRADO!{FIM}")
            optt= input ("Pressione Enter para tentar novamente ou A para voltar ao menu inicial...")
            if optt in ["A", "a"]:
                break
# Função para a opção 4
def excluir(D1):
    while True:
        os.system("cls")
        lista()
        ID=input("\nInforme o ID do produto que deseja excluir: ")
        if ID in D1:
            os.system("cls")
            print ("Verifique o produto informado:\n")
            print (line)
            print (f"{ID:<10}{D1[ID][0]:<15}{D1[ID][1]:>15}{D1[ID][2]:>15}{D1[ID][3]:>15}{D1[ID][4]:>15}")
            print (line)
            opt= input ("Pressione X para excluir ou O para cancelar ação...")
            if opt in ["X","x"]:
                del D1[ID]
                salve(D1)
                os.system("cls")
                print (f"{AC}Excluído com sucesso!{FIM}")
                oopt= input ("Pressione Enter para excluir outro produto ou A para voltar ao menu inicial...")
                if oopt in ["A", "a"]:
                    break
            else:
                os.system("cls")
                print (f"{AC}Ação cancelada com sucesso!{FIM}")
                oppt= input ("Pressione Enter para tentar novamente ou A para voltar ao menu inicial...")
                if oppt in ["A", "a"]:
                    break
        else:
            print (f"{VERN}ID NÃO ENCONTRADO!{FIM}")
            optt= input ("Pressione Enter para tentar novamente ou A para voltar ao menu inicial...")
            if optt in ["A", "a"]:
                break
# Função para a opção 5
def pesquisar():
    while True:
        os.system("cls")
        L1 = []
        nm = input("Informe o nome do produto a ser pesquisado: ")
        print(line)
        for i in open_lista():
            if nm.lower() in i[2].lower():
                L1.append(i)
        if L1:
            for item in L1:
                print (f"{item[0]:<15}{item[1]:<20}{item[2]:<20}{item[3]:>15}{item[4]:>15}{item[5]:>15}")
        else:
            print(f"{VERN}PRODUTO NÃO ENCONTRADO!{FIM}")
        print(line)
        oppt = input("\nPressione Enter para pesquisar novo produto ou A para voltar ao menu inicial...")
        if oppt in ["A", "a"]:
            break