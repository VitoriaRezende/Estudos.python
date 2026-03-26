# Modulos O QUE S MODULOS SÃO BIBLIOTECAS DE FUNÇÕES PRONTAS PARA USAR, QUE PODEM SER IMPORTADAS PARA O SEU PROJETO.
# EXEMPLO DE COMO IMPORTAR UM MODULO:
import math
# AGORA PODEMOS USAR AS FUNÇÕES DO MODULO MATH, COMO POR EXEMPLO A FUNÇÃO SQRT PARA CALCULAR A RAIZ QUADRADA DE UM NÚMERO:
num = 16
raiz = math.sqrt(num)
print("A raiz quadrada de {} é {}".format(num, raiz))
# OUTRO EXEMPLO DE MODULO É O RANDOM, QUE PERMITE GERAR NÚMEROS ALEATÓRIOS:
import random
num_aleatorio = random.randint(1, 100)
print("O número aleatório gerado é {}".format(num_aleatorio))
# EXISTEM MUITOS MODULOS DISPONÍVEIS, COMO O OS PARA INTERAGIR COM O SISTEMA OPERACIONAL, O SYS PARA INTERAGIR COM O INTERPRETADOR, O TIME PARA TRABALHAR COM TEMPO, ENTRE OUTROS. VOCÊ PODE IMPORTAR APENAS AS FUNÇÕES QUE PRECISA DE UM MODULO, USANDO A SINTAXE "FROM MODULO IMPORT FUNÇÃO":
#FROM SERVE PARA IMPORTAR APENAS UMA FUNÇÃO DE UM MODULO, AO INVÉS DE IMPORTAR O MODULO INTEIRO. POR EXEMPLO, SE VOCÊ QUISER IMPORTAR APENAS A FUNÇÃO SQRT DO MODULO MATH, VOCÊ PODE FAZER O SEGUINTE:
#COMO SABER QUAIS FUNÇÕES ESTÃO DISPONÍVEIS EM UM MODULO? VOCÊ PODE CONSULTAR A DOCUMENTAÇÃO DO MODULO, OU USAR A FUNÇÃO DIR PARA LISTAR AS FUNÇÕES DISPONÍVEIS EM UM MODULO:
import math
print(dir(math))
#ALGUMAS FUNÇÕES DO MODULO MATH SÃO: sqrt, sin, cos, tan, log, exp, entre outras. VOCÊ PODE USAR ESSAS FUNÇÕES PARA REALIZAR CÁLCULOS MATEMÁTICOS DE FORMA SIMPLES E EFICIENTE. POR EXEMPLO, PARA CALCULAR O SENO DE UM ÂNGULO, VOCÊ PODE USAR A FUNÇÃO SIN DO MODULO MATH:
import math
angulo = 30
seno = math.sin(math.radians(angulo))
print("O seno de {} graus é {}".format(angulo, seno))
#VOCÊ TAMBÉM PODE IMPORTAR UM MODULO E DAR UM NOME DIFERENTE PARA ELE, USANDO A SINTAXE "IMPORT MODULO AS NOME":
#IMPORT SERVE PARA IMPORTAR UM MODULO INTEIRO, ENQUANTO FROM SERVE PARA IMPORTAR APENAS UMA FUNÇÃO DE UM MODULO. QUANDO VOCÊ IMPORTA UM MODULO, VOCÊ PODE USAR AS FUNÇÕES DO MODULO USANDO A SINTAXE "MODULO.FUNÇÃO". QUANDO VOCÊ IMPORTA APENAS UMA FUNÇÃO DE UM MODULO, VOCÊ PODE USAR A FUNÇÃO DIRETAMENTE, SEM PRECISAR USAR O NOME DO MODULO. POR EXEMPLO, SE VOCÊ IMPORTAR APENAS A FUNÇÃO SQRT DO MODULO MATH, VOCÊ PODE USAR A FUNÇÃO SQRT DIRETAMENTE, SEM PRECISAR USAR O NOME DO MODULO: 
#?------------------------------------------------- 

from math import sqrt
num = 25
raiz = sqrt(num)
print("A raiz quadrada de {} é {}".format(num, raiz))
# VOCÊ TAMBÉM PODE IMPORTAR UM MODULO E DAR UM NOME DIFERENTE PARA ELE, USANDO A SINTAXE "IMPORT MODULO AS NOME":
import math as m
num = 9
raiz = m.sqrt(num)
print("A raiz quadrada de {} é {}".format(num, raiz))  
#?------------------------------------------------- 
#Manipulação de sistema e arquivos
import os
import sys
#?------------------------------------------------- 
#EXEMPLO DE COMO USAR O MODULO OS PARA INTERAGIR COM O SISTEMA OPERACIONAL:
#LISTAR OS ARQUIVOS E PASTAS DO DIRETÓRIO ATUAL
print(os.listdir())
#CRIAR UMA NOVA PASTA
os.mkdir("nova_pasta")
#RENOMEAR A PASTA
os.rename("nova_pasta", "pasta_renomeada")
#REMOVER A PASTA
os.rmdir("pasta_renomeada")
#?-------------------------------------------------
#EXEMPLO DE COMO USAR O MODULO SYS PARA INTERAGIR COM O INTERPRETADOR:
#EXIBIR OS ARGUMENTOS DE LINHA DE COMANDO
print(sys.argv)
#EXIBIR O NOME DO INTERPRETADOR
print(sys.executable)
#EXIBIR A VERSÃO DO PYTHON
print(sys.version)
#?-------------------------------------------------
#COMO USAR O MODULO TIME PARA TRABALHAR COM TEMPO:
import time
#EXIBIR O TEMPO ATUAL EM SEGUNDOS DESDE 1 DE JANEIRO DE 1970
print(time.time())
#PAUSAR A EXECUÇÃO DO PROGRAMA POR 2 SEGUNDOS
time.sleep(2)
print("2 segundos se passaram")
#EXIBIR A HORA ATUAL
print(time.ctime())
#?-------------------------------------------------
#Datas
import datetime
#EXIBIR A DATA E HORA ATUAL
print(datetime.datetime.now())
#EXIBIR APENAS A DATA ATUAL
print(datetime.date.today())
#EXIBIR APENAS A HORA ATUAL
print(datetime.datetime.now().time())
#?-------------------------------------------------
#MATEMÁTICA
import math
#EXIBIR O VALOR DE PI
print(math.pi)
#EXIBIR O VALOR DE E
print(math.e)
#EXIBIR O VALOR DE FATORIAL DE 5
print(math.factorial(5))
import random
#GERAR UM NÚMERO ALEATÓRIO ENTRE 1 E 10
print(random.randint(1, 10))
#ESCOLHER UM ELEMENTO ALEATÓRIO DE UMA LISTA
lista = ['maçã', 'banana', 'laranja']
print(random.choice(lista))
#?-------------------------------------------------
#JSON
import json
#CONVERTER UM DICIONÁRIO PARA JSON
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
json_string = json.dumps(dicionario)
print(json_string)
#CONVERTER UMA STRING JSON PARA DICIONÁRIO
json_string = '{"nome": "Maria", "idade": 25, "cidade": "Rio de Janeiro"}'
dicionario = json.loads(json_string)
print(dicionario)  
#?-------------------------------------------------     
#Requisições HTTP (muito usado em API)
import requests
#FAZER UMA REQUISIÇÃO GET PARA UM SITE
response = requests.get("https://www.google.com")
print(response.status_code)
#FAZER UMA REQUISIÇÃO POST PARA UM SITE
data = {"username": "user", "password": "pass"}
response = requests.post("https://httpbin.org/post", data=data)
print(response.status_code) 

#?-------------------------------------------------
#Trabalhar com listas e contagens
from collections import Counter
#CONTAR A FREQUÊNCIA DE ELEMENTOS EM UMA LISTA
lista = ['maçã', 'banana', 'laranja', 'maçã',
            'banana', 'maçã']
contador = Counter(lista)
print(contador)
#OBTER OS 2 ELEMENTOS MAIS COMUNS
mais_comuns = contador.most_common(2)
print(mais_comuns)
#?-------------------------------------------------
#Expressões regulares (validação)
import re
#VALIDAR SE UM E-MAIL É VÁLIDO
email = "joao@example.com"
padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(padrao, email):
    print("E-mail válido")
else:
    print("E-mail inválido")
 #?-------------------------------------------------
 #Manipulação de dados (TOP pra mercado)
import pandas as pd
#CRIAR UM DATAFRAME A PARTIR DE UM DICIONÁRIO
dados = {"nome": ["João", "Maria", "Pedro"],
         "idade": [30, 25, 35],
         "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]}
df = pd.DataFrame(dados)
print(df)
#EXIBIR AS PRIMEIRAS LINHAS DO DATAFRAME
print(df.head())
#EXIBIR AS INFORMAÇÕES DO DATAFRAME
print(df.info())    

 #?-------------------------------------------------
 
 #Criar APIs (backend)
from flask import Flask, jsonify
app = Flask(__name__)   
#CRIAR UMA ROTA PARA A API
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})
#INICIAR O SERVIDOR DA API
if __name__ == '__main__':
    app.run(debug=True) 
    
 #?-------------------------------------------------
 
 #Trabalhar com arquivos
import os
#CRIAR UM NOVO ARQUIVO E ESCREVER DADOS NELE
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, este é um arquivo de exemplo.")
#LER O CONTEÚDO DE UM ARQUIVO
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
#RENOMEAR UM ARQUIVO
os.rename("arquivo.txt", "novo_arquivo.txt")
#?-------------------------------------------------

