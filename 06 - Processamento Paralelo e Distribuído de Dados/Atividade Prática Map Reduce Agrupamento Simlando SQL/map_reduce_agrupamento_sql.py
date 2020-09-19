# -*- coding: utf-8 -*-

import csv
import glob
import sys
import mincemeat

arquivos = glob.glob("joins\\*")

# print(arquivos)


def conteudo_arquivos(arquivo):
    arquivo_leitura = open(arquivo)
    try:
        return arquivo_leitura.read()
    finally:
        arquivo_leitura.close()


fonte = dict((arquivo, conteudo_arquivos(arquivo)) for arquivo in arquivos)


def mapfn(k, v):
    print('map {}'.format(k))
    print(k)
    for line in v.splitlines():
        splitted = line.split(';')
        if (k == 'joins\\2.2-vendas.csv'):
            yield splitted[0], 'Vendas' + ':' + splitted[5]
        if (k == 'joins\\2.2-filiais.csv'):
            yield splitted[0], 'Filial' + ':' + splitted[1]


def reducefn(k, v):
    # print('reduce ' + k)
    return v


s = mincemeat.Server()
s.datasource = fonte
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="123456")

w = csv.writer(open("resultados/results.csv", "w"))
for k, v in results.items():
    w.writerow([k, v])
