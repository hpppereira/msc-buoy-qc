# -*- coding: utf-8 -*-

'''Programa Principal para consistencia de dados ###

cria perturbacoes nas series temporais
utiliza uma serie de heave, pitch e roll simuladas

#Obs: Para ver os dados de entrada
#verificar o help de cada funcao:

#EX: criaperturbacao.spikes?
'''

# ================================================================================ #
## Importa bibliotecas

import pylab as pl
import numpy as np
import scipy as sp
import copy as cp
import os

import criaperturb
import consiste_bruto

reload(criaperturb)
reload(consiste_bruto)

pl.close('all')

# ================================================================================ #
## Diretorio dos arquivos

#diretorio dos arquivos simulados
pathname = os.environ['HOME'] + '/Dropbox/lioc/dados/pnboia/triaxys/rio_grande/HNE/'

#caracteristicas das ondas simuladas:
#Hs = 2.5 m
#Tp = 12 seg
#Dp = 45 graus

# ================================================================================ #
## Carrega arquivos de dados

#onda
tempo,eta,etax,etay = np.loadtxt(pathname + '200905010000.HNE',skiprows=11,unpack=True)

#variavel sem perturbacoes
#vet = cp.copy(eta)


# ================================================================================ #
## Parametros de entrada para cada teste (verificar descricao da rot criaperturb.py)

#comprimento do vetor
param2hne = 1000

#gaps
param1 = [100,25,600,50,1000,40]

#spikes
param2 = [50,2,3,150,4,-4,400,4,-4,550,1,4,800,4,5,1000,1,-3.5]

#consec. iguais
param3 = [5,30,300,40,500,30,200,60,745,50,1000,100]

#consec. nulos
param4 = [100,20,400,40,800,100]

#media deslocada
param5 = [500,524,2]

#variabilidade temporal
param6 = [100,5,300,-4,500,3,800,3,1100,4]

#atraso (coloca zeros no final da serie)
param7 = [100,1,200,5,400,10,600,50,800,200]


# ================================================================================ #
## Cria perturbacoes

#obs: Se o 't1' estiver habilitado, nao pode escolher pontos acima do comprimento da 
#serie escolhida no t1

#variavel com perturbacoes
#vetp = cp.copy(eta)

#perturbacoes em series separadas

#* para criar as perturbacoes na mesma serie,
#modificar os dados de saida para 'vetp'

vet1 = criaperturb.t1(eta,param1) #gap
vet2 = criaperturb.t2(eta,param2) #spike
vet3 = criaperturb.t3(eta,param3)
vet4 = criaperturb.t4(eta,param4)
vet5 = criaperturb.t5(eta,param5)
vet6 = criaperturb.t6(eta,param6)
vet7 = criaperturb.t7(eta,param7)

# Variavel perturbada, que sera inteporlada
# veti = cp.copy(vetp)

# ================================================================================ #
## Testes de CQ dos dados brutos

#sintaxe: [flag] ou [flag,vetc] = consistencia.teste(serie_perturbada,vetor_flags)

# flag = str()

# flag = consiste_bmo_bruto.t1(vetp,10,flag)
# flag, vetc = consiste_bmo_bruto.t2(vetp,np.mean(eta),np.std(eta),10,4,2,flag)
# flag = consiste_bmo_bruto.t3(vetp,flag)
# flag = consiste_bmo_bruto.t4(vetp,flag)
# flag = consiste_bmo_bruto.t5(vetp,5,flag)
# flag = consiste_bmo_bruto.t6(vetp,5,flag)
# flag = consiste_bmo_bruto.t7(vetp,-3,3,flag)
# flag = consiste_bmo_bruto.t8(vetp,4,np.std(vet),flag)


# ================================================================================ #
## Parametros dos vetores

# #media - vetor cons
# med = np.zeros(len(vet))
# med[:] = np.mean(np.isnan(vet))

# #media - vetor perturb
# medp = np.zeros(len(vetp))
# medp[:] = np.mean(np.isnan(vetp))

# #media - vetor consistente
# medc = np.zeros(len(vetc))
# medc[:] = np.mean(np.isnan(vetc))


# ================================================================================ #
## Graficos das series perturbadas

# pl.subplot(311)
# pl.plot(vet,'b-')
# pl.plot(med,'--r')
# pl.title('Elevacao - Simulada')
# pl.ylabel('metros')
# pl.axis('tight')
# pl.xticks([])

# pl.subplot(312)
# pl.plot(vetp,'b-')
# pl.plot(medp,'--r')
# pl.title('Elevacao - Perturbada')
# pl.ylabel('metros')
# pl.axis('tight')
# pl.xticks([])

# pl.subplot(313)
# pl.plot(vetc,'b-')
# pl.plot(medc,'--r')
# pl.title('Elevacao - Interpolada')
# pl.xlabel('tempo (s)')
# pl.ylabel('metros')
# pl.axis('tight')

# ================================================================================ #
#plotagens das series perturbadas

pl.figure()
pl.subplot(3,2,1)
pl.plot(vet1)
pl.title('Lacuna')
pl.axis('tight')
pl.grid()
pl.xticks(visible=False)

pl.subplot(3,2,2)
pl.plot(vet2)
pl.title('Faixa/Spike')
pl.axis('tight')
pl.grid()
pl.xticks(visible=False)

pl.subplot(3,2,3)
pl.plot(vet3)
pl.title('Iguais')
pl.ylabel('Elevacao (m)')
pl.axis('tight')
pl.grid()
pl.xticks(visible=False)

pl.subplot(3,2,4)
pl.plot(vet5)
pl.title('Media deslocada')
pl.axis('tight')
pl.grid()
pl.xticks(visible=False)

pl.subplot(3,2,5)
pl.plot(vet6)
pl.title('Variabilidade')
pl.xlabel('Tempo (s)')
pl.axis('tight')
pl.grid()
pl.xticks(visible=False)

pl.subplot(3,2,6)
pl.plot(vet7)
pl.title('Atraso/Nulos')
pl.xlabel('Tempo (s)')
pl.axis('tight')
pl.grid()
pl.xticks(visible=False)


# pl.savefig('perturb.png')

pl.show()