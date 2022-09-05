import json
import numpy as np
from dolar import ValorDoDolar


abrir = open("dados.json") # Open = abrir arquivo

dados = json.load(abrir)   #json.load = transformar o arquivo json para objeto python
listdados = dados["notas"] # transformar o objeto de dict para list

#dolar.py
dolar = ValorDoDolar()
dolar.consulta()

#Criar as variaveis cnpj e valor para cada nota fiscal
cnpj = listdados[0]['cnpjFornecedor']
valor = listdados[0]['valor']
useless = "R$ "  # Remover "a parte string" do valor para obter somento valor bruto(número)                 "tratamento de variavel"
virgula = ","    # Remover  "," para substituir por "." devido a gramática python.                          "tratamento de variavel"
valorDecimal = 0 # valor incial para evitar lixo de memória
cnpjSalvos = []  #vetor

for i in listdados:
    if cnpj != i['cnpjFornecedor']:  # acessando cada cnpjFornecedor da lista
        cnpj = i['cnpjFornecedor']
        valorDecimal = 0
        if cnpj not in cnpjSalvos:                              #adiciona cnpj no vetor
            cnpjSalvos.append(cnpj)
            for j in listdados:                                     #soma cada valor de um cnpj
                if cnpj == j['cnpjFornecedor']:                
                    valor = j['valor']                            # para cada cnpj individual da lista somar os valores
                    for i in range(0,len(useless)):               #tratamento de variavel
                        valor =valor.replace(useless[i],"")       #tratamento de variavel
                    for i in range(0,len(virgula)):               #tratamento de variavel
                        valor =valor.replace(virgula[i],".")      #tratamento de variavel
                        valorDecimal += float(valor)              #valorDecimal = valorDecimal + float(valor)
            print("O valor total das notas do fornecedor", cnpj, "é R$", round(valorDecimal,2), "ou US$", round(valorDecimal/float(dolar.valorapi),2), "na cotação atual do dólar de R$" , dolar.valorapi)
