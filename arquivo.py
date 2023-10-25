import csv
import pandas as pd

with open("advertising.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print()
        else:
            print()
        print()

tabela = pd.read_csv("advertising.csv", sep=",")
print(tabela)

print(tabela["Radio"].sum())

while True:
    print("1 - Somar total TV")
    print("2 - Somar total Radio")
    print("3 - Somar total Jornal")
    print("4 - Somar total Vendas")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("O total de vendas da tv foram: ", tabela["TV"].sum())
    elif opcao == 2:
        print("O total de vendas do radio foram: ", tabela["Radio"].sum())
    elif opcao == 3:
        print("O total de vendas do jornal foram", tabela["Jornal"].sum())
    elif opcao == 4:
        print("O total de vendas foram", tabela["Vendas"].sum())
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Escolha inválida")