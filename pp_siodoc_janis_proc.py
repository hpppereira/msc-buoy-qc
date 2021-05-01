# -*- coding: utf-8 -*-
'''
Processamento e controle de qualidade
dos dados da boia janis de arraial do cabo

Processa os dados gerados pela rotina
'pp_siodoc_janis_concat.py' que gera a seguinte saida:
#   0     1   2   3   4   5   6  7   8   9 
# datai, ws, wg, wd, at, pr, wt, hs, tp, dp

B69008 - recife
B69150 - santos
B69152 - florianopolis
B69153 - rio_grande

'''

import os
import numpy as np
import pylab as pl
from datetime import datetime
import consiste_proc
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy import * 
import os
import windrose
from windrose import WindroseAxes

reload(consiste_proc)
reload(windrose)

pl.close('all')

local = 'arraial_cabo'

print 'Iniciando processamento em... ' + local


pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#  0  1   2  3  4 5  6  7  8  9
#date,ws,wg,wd,at,pr,wt,hs,tp,dp
dados = np.loadtxt(pathname + 'siodoc_janis_' + local + '.out',delimiter=',')

#converte datas para datetime
datat = np.array([datetime.strptime(str(int(dados[i,0])), '%Y%m%d%H%M') for i in range(len(dados))])

#numero de parametros processados
npa = 9

print 'Iniciando processamento em ... ' + local

# ================================================================================== #  

#cria vetores de flags das series processadas (depende das qtdade de variaveis a serem consistidas + data) 
flagp = np.zeros((len(dados),npa+1),dtype='|S32')
flagp[:,0] = dados[:,0].astype(int).astype(str)

# ================================================================================== #  
# Testes de consistencia dos dados processados

#Teste 1 - faixa
#sintaxe: faixa(serie,linf_inst,lmax_inst,lmin_reg,lmax_reg,flag)
print 'Realizando teste de Faixa'
flagp[:,1] = consiste_proc.faixa(dados[:,1],0.1,35,0.2,25,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.faixa(dados[:,2],0.1,35,0.3,25,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.faixa(dados[:,3],0,360,0,360,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.faixa(dados[:,4],0,40,6,30,flagp[:,4]) #at
flagp[:,5] = consiste_proc.faixa(dados[:,5],980,1040,985,1035,flagp[:,5]) #pr
flagp[:,6] = consiste_proc.faixa(dados[:,6],10,35,13,30,flagp[:,6]) #wt
flagp[:,7] = consiste_proc.faixa(dados[:,7],0,20,0.15,7,flagp[:,7]) #hs
flagp[:,8] = consiste_proc.faixa(dados[:,8],1.95,26,3,22,flagp[:,8]) #tp - ndbc09
flagp[:,9] = consiste_proc.faixa(dados[:,9],0,360,0,360,flagp[:,9]) #dp

#Teste 2 - Variabilidade
#sintaxe: variab(serie,lag(hr),lim,flag)
print 'Realizando teste de Variabilidade'
flagp[:,1] = consiste_proc.variab(dados[:,1],1,10,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.variab(dados[:,2],1,10,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.variab(dados[:,3],1,360,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.variab(dados[:,4],1,5,flagp[:,4]) #at
flagp[:,5] = consiste_proc.variab(dados[:,5],1,10,flagp[:,5]) #pr
flagp[:,6] = consiste_proc.variab(dados[:,6],1,5,flagp[:,6]) #wt
flagp[:,7] = consiste_proc.variab(dados[:,7],1,3,flagp[:,7]) #hs
flagp[:,8] = consiste_proc.variab(dados[:,8],1,15,flagp[:,8]) #tp
flagp[:,9] = consiste_proc.variab(dados[:,9],1,360,flagp[:,9]) #dp

#Teste 3 - Consec. iguais
#sintaxe =  iguais(var,nci,flag)
print 'Realizando teste de Consec. Iguais'
flagp[:,1] = consiste_proc.iguais(dados[:,1],3,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.iguais(dados[:,2],3,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.iguais(dados[:,3],3,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.iguais(dados[:,4],3,flagp[:,4]) #at
flagp[:,5] = consiste_proc.iguais(dados[:,5],3,flagp[:,5]) #pr
flagp[:,6] = consiste_proc.iguais(dados[:,6],3,flagp[:,6]) #wt
flagp[:,7] = consiste_proc.iguais(dados[:,7],3,flagp[:,7]) #hs
flagp[:,8] = consiste_proc.iguais(dados[:,8],3,flagp[:,8]) #tp
flagp[:,9] = consiste_proc.iguais(dados[:,9],3,flagp[:,9]) #dp

#Teste 4 - Media e Desvio Padrao
#sintaxe =  iguais(var,per_meddp,mult_dp,flag)
print 'Realizando teste de Media e Desvio Padrao'
flagp[:,1] = consiste_proc.meddp(dados[:,1],100,3,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.meddp(dados[:,2],100,3,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.meddp(dados[:,3],100,3,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.meddp(dados[:,4],100,3,flagp[:,4]) #at
flagp[:,5] = consiste_proc.meddp(dados[:,5],100,3,flagp[:,5]) #pr
flagp[:,6] = consiste_proc.meddp(dados[:,6],50,3,flagp[:,6]) #wt
flagp[:,7] = consiste_proc.meddp(dados[:,7],50,3,flagp[:,7]) #hs
flagp[:,8] = consiste_proc.meddp(dados[:,8],100,3,flagp[:,8]) #tp
flagp[:,9] = consiste_proc.meddp(dados[:,9],100,3,flagp[:,9]) #dp

# ================================================================================== #  
# Coloca nan nos dados reprovados e suspeitos
print 'Colocando nan nos dados reprovados e suspeitos'

#matriz com dados consistentes
dadosc = np.copy(dados)
for c in range(1,flagp.shape[1]):

    for i in range(len(flagp)):
    
        if '4' in flagp[i,c]:
    		
    		dadosc[i,c] = np.nan
        	print ([str(flagp[i,0]) + ' - Reprovado'])

        elif '3' in flagp[i,c]:

        	dadosc[i,c] = np.nan
        	print ([str(flagp[i,0]) + ' - Suspeito'])


#condicoes de consistencias conjuntas
print 'Consistencia conjunta'

#se a velicidade do vento esta com erro (nan), a direcao tambem recebe nan
wsnan = np.where(np.isnan(dadosc[:,1])==True)[0] #acha nan nos dados de vel vento
dadosc[wsnan,2] = np.nan #coloca nan na vel de rajada nas posicoes com nan em ws
dadosc[wsnan,3] = np.nan #coloca nan na direcao do vento nas posicoes com nan em ws

#se o hs estiver cocom erro (nan) ou menor que 0.25, o hs, tp e dp recebem nan
dadosc[np.where(dados[:,7] < 0.25)[0],7] = np.nan #coloca na nos hs menor que 0.25 (talvez o cq acima ja tenha feito isso)
hsnan = np.where(np.isnan(dadosc[:,7])==True)
dadosc[hsnan,8] = np.nan #coloca nan no periodo de pico
dadosc[hsnan,9] = np.nan #coloca nan na direcao de pico

#salva arquivo consistentes (_cq)
#         0  1   2 3  4  5  6  7  8  9
head = 'date,ws,wg,wd,at,pr,wt,hs,tp,dp'
np.savetxt('out/siodoc_janis_cq_' + local + '.out',dadosc,delimiter=',',fmt=['%i']+9*['%.2f'],header=head)
