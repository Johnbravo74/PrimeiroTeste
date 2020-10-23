# COMPARAÇÃO DAS TRANSFERÊNCIAS MUNICIPAIS - RN
"""Este programinha articula análise comparativa das transferências via bb arrecadação
Bibliografia: https://www.youtube.com/watch?v=lJjR906426o&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
"""

import os
from typing import Any

"""FUNÇÃO DE LIMPEZA DE TELA"""
def cls():
    os.system("cls")

cls()
print("\n")
print("TRANSFERÊNCIAS DO TESOURO NACIONAL")
print("FONTE: BANCO DO BRASIL")
print("COMPETÊNCIA: 07/2020")
print("Observação: o arquivo de banco de dados contendo as informações das transferências devem ser digitados no NOTEPAD++" + "\n"
      "Passo 1: copiar os dados individualmente do bbarrecadação;" + "\n"
      "Passo 2: colar no arquivo NOTEPAD;" + "\n"
      "Passo 3: digitar as teclas CRTL A e depois CRTL J." + "\n")

arquivo = input("Especifique o caminho do arquivo a ser analisado (ex: C:\\Users\\Base.txt): ")
print("\n")

print("Município                            FPM           FEP       ITR            ICS            ANP            CFM            FUS            IPM        ISS/STN            CID         FUNDEB            SNA            AFM")
# Abre o arquivo para análise
with open(arquivo, 'r', encoding="utf-8") as fp:
#with open('C:\\Users\\jpereira\\OneDrive\\2020\\INOVATION\\bbarrecada\\Base_072020', 'r', encoding="utf-8") as fp:
    for line in fp:
        j = 0  # type: Any
        credito = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
        while line[j] != "-":
            j += 1
        mun = line[0:j - 1]

        j+=1
        while line[j] != "\n":
            z = 0
            j += 1
            if line[j] == "\t" and line[j - 4:j] == "DATA":
                z = j
                while line[z - 1] != line[z - 2]:
                    z -= 1
                fonte = line[z:j - 5]

                while line[j - 13:j] != "CREDITO FUNDO":
                    j += 1
                z = 0
                j += 4
                while line[j] != "C":
                    j += 1
                    z += 1

                if fonte == "FPM - FUNDO DE PARTICIPACAO DOS MUNICIPIOS":
                    credito[0] = line[j - z:j - 1]
                elif fonte == "FEP - FUNDO ESPECIAL DO PETROLEO":
                    credito[1] = line[j - z:j - 1]
                elif fonte == "ITORIAL RURAL":
                    credito[2] = line[j - z:j - 1]
                elif fonte == "ICS - ICMS ESTADUAL":
                    credito[3] = line[j - z:j - 1]
                elif fonte == "ANP - ROYALTIES DA ANP":
                    credito[4] = line[j - z:j - 1]
                elif fonte == "CFM - DEPARTAMENTO NACIONAL DE PRODUCAO MINERAL":
                    credito[5] = line[j - z:j - 1]
                elif fonte == "FUS - FUNDO SAUDE":
                    credito[6] = line[j - z:j - 1]
                elif fonte == "IPM - IPI EXPORTACAO - COTA MUNICIPIO":
                    credito[7] = line[j - z:j - 1]
                elif fonte == " - IMPOSTO SOBRE SERVICO - STN CONVENIO":
                    credito[8] = line[j - z:j - 1]
                elif fonte == "CID - CIDE-CONTRIB. INTERVENCAO DOMINIO ECONOMICO":
                    credito[9] = line[j - z:j - 1]
                elif fonte == "FUNDEB - FNDO MANUT DES EDUC BASICA E VLRIZ PROF EDUC":
                    credito[10] = line[j - z:j - 1]
                elif fonte == "SNA - SIMPLES NACIONAL":
                    credito[11] = line[j - z:j - 1]
                elif fonte == "AFM - APOIO FINANCEIRO AOS MUNICIPIOS":
                    credito[12] = line[j - z:j - 1]

        print("{0:<25}".format(mun) + "{0:>15}".format(credito[0]) + "{0:>14}".format(credito[1]) + "{0:>10}".format(
            credito[2]) + "{0:>15}".format(credito[3]) + "{0:>15}".format(credito[4]) + "{0:>15}".format(
            credito[5]) + "{0:>15}".format(credito[6]) + "{0:>15}".format(credito[7]) + "{0:>15}".format(
            credito[8]) + "{0:>15}".format(credito[9]) + "{0:>15}".format(credito[10]) + "{0:>15}".format(
            credito[11]) + "{0:>15}".format(credito[12]))
        j += 1
fp.close()
print("_____________________________________")
print("Desenvolvido por: João Evangelista")
sair = input("Deseja sair do sistema? Digite 1 para Sim: ")

