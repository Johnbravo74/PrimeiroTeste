# COMPARAÇÃO DAS TRANSFERÊNCIAS MUNICIPAIS - RN
"""Este programinha verifica informações empresariais junto ao SINTEGRA
Bibliografia: CURSO COMPLETO DE PYTHON - https://www.youtube.com/watch?v=lJjR906426o&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
"""

import os
from typing import Any

"""FUNÇÃO DE LIMPEZA DE TELA"""
def cls():
    os.system("cls")

cls()
print("\n")
print("ANALISANDO OS CASOS OMISSOS")
print("FONTE: SINTEGRA/SET")
print("COMPETÊNCIA: 2019")

arquivo = input("Especifique o caminho do arquivo a ser analisado (ex: C:\\Users\\jpereira\\OneDrive\\2020\\IPM\\omissos2019): ")
mostrar = input("Mostrar somente as empresas ativas? Digite 1 para Sim: ")
if mostrar == "1":
    arquivo1 = input(
        "Especifique o caminho do segundo arquivo a ser analisado (ex: C:\\Users\\jpereira\\OneDrive\\2020\\IPM\\banco): ")
    print("IE             CNPJ                   SITUAÇÃO CNAE_P         EMAIL                                        RAZÃO SOCIAL                                                                           TIPO DE CONTRIBUINTE        CONTADOR")
else:
    print(
        "IE             CNPJ                   SITUAÇÃO CNAE_P         EMAIL                                        RAZÃO SOCIAL ")

cont = 0
# Abre o arquivo para análise
with open(arquivo, 'r', encoding="utf-8") as fp:
    for line in fp:
        array = ["", "", "", "", "", "", "", "", "", ""]
        array[0] = line[0:12]      # IE
        array[1] = line[23:41]     # CNPJ
        j = 57
        while line[j] != "\t":
            j += 1
        array[4] = line[57:j]
        j += 3
        if line[j: j + 19] == "atividade_principal":
            j += 19
            while line[j - 4:j] != "code":
                j += 1
            j += 3
            array[5] = line[j:j + 10]
            j += 10

        while line[j] != "\n":
            j += 1
            if line[j - 8:j] == "situacao" and line[j - 9] != "_":
                array[2] = line[j + 3:j + 8]        # Situação cadastral
                break
            if line[j - 5:j] == "email":
                z = 0
                while line[j] != ",":
                    j += 1
                    z += 1
                array[3] = line[j - z + 3:j - 1]         # email

        # Abre o segundo arquivo para análise
        with open(arquivo1, 'r', encoding="utf-8") as fp1:
            indicador = 0          # Serve somente entrar no loop
            for line1 in fp1:
                """teste = "joao evangelista evan"
                pos = teste.find_all("evan")"""     # REFERÊNCIA: https://www.it-swarm.dev/pt/python/localizar-todas-ocorrencias-de-uma-substring-em-python/970303130/
                if indicador == 0:
                    j = 31
                    if array[0] == line1[19:j]:
                        while line1[j] != "\n":
                            while line1[j - 17:j] != "Tipo Contribuinte":
                                j += 1
                            z = j + 1
                            while line1[z] != " ":
                                z += 1
                            array[6] = line1[j:z]

                            while line1[j - 18:j] != "Situação Cadastral":
                                j += 1
                            z = j + 1
                            while line1[z] != " ":
                                z += 1
                            array[8] = line1[j + 1:z]

                            if array[8] == "ATIVO":
                                cont += 1

                            zi = len(array[8]) + 36
                            zf = len(array[8]) + 46
                            array[9] = ""
                            if line1[j + zi + 2] == "/":
                                array[9] = line1[j + zi:j + zf]

                            while line1[j - 8:j] != "Contador":
                                j += 1
                            if line1[j + 1:j + 5] == "Nome":
                                z = j + 6
                                j += 1
                                while line1[j - 3:j] != "(s)":
                                    j += 1
                                    if line1[j] == "\n":
                                        array[7] = line1[z:j]
                                        break
                                    else:
                                        array[7] = line1[z:j - 17]
                            else:
                                array[7] = "Não definido"

                            if array[2] == "ATIVA" and mostrar == "1":
                                print(
                                    "{0:<15}".format(array[0]) + "{0:>15}".format(array[1]) + "{0:>10}".format(
                                        array[2]) + "    " + "{0:<15}".format(array[5]) + "{0:<45}".format(array[3]) + "{0:<100}".format(
                                        array[4]) + "{0:<15}".format(
                                        array[6]) + "{0:<55}".format(
                                        array[7]) + "{0:>15}".format(array[8]) + "{0:>15}".format(array[9]))
                                indicador = 1
                                break
                            elif mostrar != "1":
                                print(
                                    "{0:<15}".format(array[0]) + "{0:>15}".format(array[1]) + "{0:>10}".format(
                                        array[2]) + "    " + "{0:<15}".format(array[5]) + "{0:<45}".format(array[3]) + "{0:<100}".format(
                                        array[4]))
                                indicador = 1
                                break
print("\nRESUMO DOS DADOS")
print("Número de empresas ativas: ", cont)
print("_____________________________________")
print("Desenvolvido por: João Evangelista")
sair = input("Tecle  qualque tecla para sair do sistema? ")