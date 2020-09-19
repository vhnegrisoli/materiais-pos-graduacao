# -*- coding: utf-8 -*-

import csv
import glob
import sys

import mincemeat
from stopwords import allStopWords

caminho_arquivos = "C:\\Users\\Lord_Negrisoli\\Desktop\\Faculdade\\Pós-Graduação\\Repositórios\\06 - Processamento Paralelo e Distribuído de Dados\\Contagem de Palavras Map Reduce\\textos\\*"

arquivos = glob.glob(caminho_arquivos)

def conteudo_arquivos(arquivo):
    arquivo_leitura = open(arquivo)
    try:
        return arquivo_leitura.read()
    finally:
        arquivo_leitura.close()

fonte = dict((arquivo, conteudo_arquivos(arquivo)) for arquivo in arquivos)

def mapfn(k, v):
    print('map {}'.format(k))
    for line in v.splitlines():
        for word in line.split():
            if (word not in allStopWords):
                yield word, 1

def reducefn(k, v):
    print('Reduce {}'.format(k))
    return sum(v)

s = mincemeat.Server()
s.datasource = fonte
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password = "123456")

w = csv.writer(open("resultados/results.csv", "w"))
for k, v in results.items():
    w.writerow([k, v])