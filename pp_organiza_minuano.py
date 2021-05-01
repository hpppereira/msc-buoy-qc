# -*- coding: utf-8 -*-

#Processamento dos dados meteorologicos da boia
#minuano, no rio grande do sul

#versao para carregar os dados (comentado)

# ================================================================================== #
#Importa bibliotecas

from numpy import *
from pylab import *
import os
#import consiste_bmo_proc
#import lim_consistencia
#import graficos_minuano
import carrega_minuano
import data_minuano
from datetime import datetime

reload(carrega_minuano)
#funcao reload atualiza alteracoes nos modulos
#reload(consiste_bmo_proc)
#reload(lim_consistencia)
#reload(graficos_minuano)
#reload(data_minuano)

#close('all')
    

# ================================================================================== #
#Carrega os dados meteo-oceanograficos da boia MINUANO

#caminho com o nome dos arquivos da boia minuano
pathname1 = os.environ['HOME'] + '/Dropbox/tese/cq/dados/minuano/1_Dados_da_Minuano_de_240502_a_130104/'
pathname2 = os.environ['HOME'] + '/Dropbox/tese/cq/dados/minuano/2_Dados_da_Minuano_de_220104_a_171004/'


# ================================================================================== #
#Lista arquivos .CSV que estao dentro do diretorio 'pathname'

#cria lista com o nome dos arquivos
lista1 = carrega_minuano.lista_csv(pathname1)
lista2 = carrega_minuano.lista_csv(pathname2)

#chama funcao para carregar arquivos da boia minuano 
dados_minuano1 = carrega_minuano.dados_csv(pathname1,lista1)
dados_minuano2 = carrega_minuano.dados_csv(pathname2,lista2)

#                   0      1    2   3  4   5   6   7   8   9  10 11  12   13   14  15
##dados_minuano = data,hora_min,at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr
dados_minuano = concatenate((dados_minuano1,dados_minuano2))


# ================================================================================== #
#Chama funcao para criar data (utiliza funcao 'datetime')

datam,ano,mes,dia,hora,minuto = data_minuano.data(dados_minuano)


# ================================================================================== #
# Deixa a matriz 'dados_minuano' em ordem crescente

#acha os indices para ordem crescente
datam_aux = argsort(datam)

#deixa a data em ordem crescente
datam = array(datam)[datam_aux]

#matriz de data em ordem crescente
ano = array(ano)[datam_aux]
mes = array(mes)[datam_aux]
dia = array(dia)[datam_aux]
hora = array(hora)[datam_aux]

data = array([ano,mes,dia,hora]).T

#deixa os dados em ordem crescente
dados_minuano = concatenate((data,dados_minuano[datam_aux,:]),axis=1)
dados_minuano = dados_minuano[:,[0,1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19]]


##                  0  1    2   3   4  5  6  7    8   9   10 11  12 13 14    15    16 17   
##dados_minuano = ano,mes,dia,hora,at,rh,ws1,ws2,wg1,wg2,wd1,wd2,wt,bp,sigw,sigp,maxw,sr

#Cria vetor de datas igual da boia axys
lista_arq= array([ [str(int(dados_minuano[i,0])) + str(int(dados_minuano[i,1])).zfill(2) + str(int(dados_minuano[i,2])).zfill(2) +
              str(int(dados_minuano[i,3])).zfill(2) + '00' ]  for i in range(len(dados_minuano)) ])
              

#deixa em ordem crescente
lista_arq = lista_arq[datam_aux]


# ================================================================================== #
#Tabela para salvar dados
#savetxt('saida_minuano.txt',dados_minuano,fmt='%5.2f')
