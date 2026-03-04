# UMC- Universidade de Mogi das Cruzes
# Engenharia de Software/ADS - Software Básico
# Sarah Êmily Cruz Bianchin - Nathalia Cristiny da Silva Andrade
# Importando funções do arquivo (funcs.py)
import funcs as fc
import os
# TXT
D1= {}
fc.abrir(D1)
fc.salve(D1)
# Menu
while True:
    os.system("cls")
    # Título
    fc.tit()
    fc.menu()
    opt= fc.opt()
    if opt=="1":
        os.system("cls")
        fc.cadastro(D1)
    elif opt=="2":
        os.system("cls")
        fc.listar(D1)
    elif opt=="3":
        os.system("cls")
        fc.atualizar(D1)
    elif opt=="4":
        os.system("cls")
        fc.excluir(D1)
    elif opt=="5":
        os.system("cls")
        fc.pesquisar()
    elif opt=="0":
        os.system("cls")
        print("Encerrando o programa...")
        break
