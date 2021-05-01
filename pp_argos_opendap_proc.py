# -*- coding: utf-8 -*-
'''
Processamento e controle de qualidade
dos dados transmitidos via satelite
ARGOS

Processa os dados gerados pela rotina
'pp_argos_opendap_concat.py' que gera a seguinte saida:
#   0     1   2   3   4   5   6  7   8   9 
# datai, ws, wg, wd, at, pr, wt, hs, tp, dp

B69008 - recife (lat/lon: -8.149 / -34.56)
B69150 - santos (lat/lon: -25.28334 / -44.93334)
B69152 - florianopolis (lat/lon: -28.50000 / -47.36667)
B69153 - rio_grande (lat/long: -31.56667 / -49.86667)

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

##################################

# local = 'recife'
# lat = -8
# lon = -34
# dmag = -20

# local = 'santos'
# lat = -25
# lon = -44
# dmag = -22

# local = 'florianopolis'
# dmag = -23
# lat = -28
# lon = -47

local = 'rio_grande'
lat = -31
lon = -49
dmag = -17


##################################
pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#   0     1   2      3   4   5  6   7   8   9  10   11
# datai, lat, lon,  ws, wg, wd, at, pr, wt, hs, tp, dp
dados = np.loadtxt(pathname + 'argos_opendap_concat_' + local + '.out',delimiter=',')

print 'Iniciando pre-consistencia e processamento em... ' + local

print 'Retirando dados quando a boia estava fora de posicao...'
#acha posicoes aceitaveis
if local == 'recife':
	n=where((dados[:,1].astype(int)==lat) & (dados[:,2].astype(int)==lon))[0]
	dados = dados[n,:]
elif local == 'santos':
	n=where((dados[:,1].astype(int)==lat) & (dados[:,2].astype(int)==lon))[0]
	dados = dados[n,:]
elif local == 'florianopolis':
    n=where((dados[:,1].astype(int)==lat) & (dados[:,2].astype(int)==lon))[0]
    dados = dados[n,:]
elif local == 'rio_grande':
	n=where((dados[:,1].astype(int)==lat) & (dados[:,2].astype(int)==lon))[0]
	dados = dados[n,:]


print 'Corrigindo a declinacao magneticas da direcao do vento e onda..'
#direcao do vento
dados[:,5] = dados[:,5] + dmag #wd
dados[:,5] = 180 - dados[:,5] #corrige de onde vai para onde vem
dados[pl.find(dados[:,5] < 0),5] = dados[pl.find(dados[:,5] < 0),5] + 360 #wd
dados[pl.find(dados[:,5] > 360),5] = dados[pl.find(dados[:,5] > 360),5] - 360 #wd

#direcao de pico - onda
dados[pl.find(dados[:,11] < 0),11] = np.nan
dados[:,11] = dados[:,11] + dmag #dp
dados[pl.find(dados[:,11] < 0),11] = dados[pl.find(dados[:,11] < 0),11] + 360 #dp

#converte datas para datetime
datat = np.array([datetime.strptime(str(int(dados[i,0])), '%Y%m%d%H%M') for i in range(len(dados))])

# ================================================================================== #  

#cria vetores de flags das series processadas (depende das qtdade de variaveis a serem consistidas + data) 
flagp = np.zeros((len(dados),dados.shape[1]),dtype='|S32')
flagp[:,0] = dados[:,0].astype(int).astype(str) #coloca a data na col 1
flagp[:,1] = dados[:,1] #coloca lat na col 2
flagp[:,2] = dados[:,2] #coloca lon na col 3


# ================================================================================== #  
# Testes de consistencia dos dados processados

#Teste 1 - faixa
#sintaxe: faixa(serie,linf_inst,lmax_inst,lmin_reg,lmax_reg,flag)
print 'Realizando teste de Faixa'
flagp[:,3] = consiste_proc.faixa(dados[:,3],0.1,35,0.2,25,flagp[:,3]) #ws
flagp[:,4] = consiste_proc.faixa(dados[:,4],0.2,35,0.3,25,flagp[:,4]) #wg
flagp[:,5] = consiste_proc.faixa(dados[:,5],0,360,0,360,flagp[:,5]) #wd
flagp[:,6] = consiste_proc.faixa(dados[:,6],0,50,7,40,flagp[:,6]) #at
flagp[:,7] = consiste_proc.faixa(dados[:,7],980,1040,985,1035,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.faixa(dados[:,8],2,50,5,40,flagp[:,8]) #wt
flagp[:,9] = consiste_proc.faixa(dados[:,9],0,20,0.15,7,flagp[:,9]) #hs
flagp[:,10] = consiste_proc.faixa(dados[:,10],1.95,26,3,22,flagp[:,10]) #tp - ndbc09
flagp[:,11] = consiste_proc.faixa(dados[:,11],0,360,0,360,flagp[:,11]) #dp

#Teste 2 - Variabilidade
#sintaxe: variab(serie,lag(hr),lim,flag)
print 'Realizando teste de Variabilidade'
flagp[:,3] = consiste_proc.variab(dados[:,3],1,3,flagp[:,3]) #ws
flagp[:,4] = consiste_proc.variab(dados[:,4],1,10,flagp[:,4]) #wg
flagp[:,5] = consiste_proc.variab(dados[:,5],1,360,flagp[:,5]) #wd
flagp[:,6] = consiste_proc.variab(dados[:,6],1,5,flagp[:,6]) #at
flagp[:,7] = consiste_proc.variab(dados[:,7],1,10,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.variab(dados[:,8],1,5,flagp[:,8]) #wt
flagp[:,9] = consiste_proc.variab(dados[:,9],1,3,flagp[:,9]) #hs
flagp[:,10] = consiste_proc.variab(dados[:,10],1,15,flagp[:,10]) #tp
flagp[:,11] = consiste_proc.variab(dados[:,11],1,360,flagp[:,11]) #dp

#Teste 3 - Consec. iguais
#sintaxe =  iguais(var,nci,flag)
print 'Realizando teste de Consec. Iguais'
flagp[:,3] = consiste_proc.iguais(dados[:,3],3,flagp[:,3]) #ws
flagp[:,4] = consiste_proc.iguais(dados[:,4],3,flagp[:,4]) #wg
flagp[:,5] = consiste_proc.iguais(dados[:,5],10,flagp[:,5]) #wd
flagp[:,6] = consiste_proc.iguais(dados[:,6],3,flagp[:,6]) #at
flagp[:,7] = consiste_proc.iguais(dados[:,7],3,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.iguais(dados[:,8],3,flagp[:,8]) #wt
flagp[:,9] = consiste_proc.iguais(dados[:,9],3,flagp[:,9]) #hs
flagp[:,10] = consiste_proc.iguais(dados[:,10],3,flagp[:,10]) #tp
flagp[:,11] = consiste_proc.iguais(dados[:,11],3,flagp[:,11]) #dp

#Teste 4 - Media e Desvio Padrao
#sintaxe =  iguais(var,per_meddp,mult_dp,flag)
print 'Realizando teste de Media e Desvio Padrao'
flagp[:,3] = consiste_proc.meddp(dados[:,3],100,3,flagp[:,3]) #ws
flagp[:,4] = consiste_proc.meddp(dados[:,4],100,3,flagp[:,4]) #wg
flagp[:,5] = consiste_proc.meddp(dados[:,5],100,10,flagp[:,5]) #wd
flagp[:,6] = consiste_proc.meddp(dados[:,6],100,3,flagp[:,6]) #at
flagp[:,7] = consiste_proc.meddp(dados[:,7],100,3,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.meddp(dados[:,8],50,3,flagp[:,8]) #wt
flagp[:,9] = consiste_proc.meddp(dados[:,9],50,3,flagp[:,9]) #hs
flagp[:,10] = consiste_proc.meddp(dados[:,10],100,3,flagp[:,10]) #tp
flagp[:,11] = consiste_proc.meddp(dados[:,11],100,3,flagp[:,11]) #dp

# ================================================================================== #  
# Coloca nan nos dados reprovados e suspeitos
print 'Colocando nan nos dados reprovados e suspeitos'

#matriz com dados consistentes
dadosc = np.copy(dados)
for c in range(3,flagp.shape[1]):

    for i in range(len(flagp)):
    
        if '4' in flagp[i,c]:
    		
    		dadosc[i,c] = np.nan
        	print ([str(flagp[i,0]) + ' - Reprovado'])

        elif '3' in flagp[i,c]:

        	dadosc[i,c] = np.nan
        	print ([str(flagp[i,0]) + ' - Suspeito'])


#condicoes de consistencias conjuntas
print 'Realizando Consistencia Conjunta de Vento'
# se a velicidade do vento esta com erro (nan), a direcao tambem recebe nan
wsnan = np.where(np.isnan(dadosc[:,3])==True)[0] #acha nan nos dados de vel vento
dadosc[wsnan,4] = np.nan #coloca nan na vel de rajada nas posicoes com nan em ws
dadosc[wsnan,5] = np.nan #coloca nan na direcao do vento nas posicoes com nan em ws

# #se o hs estiver cocom erro (nan) ou menor que 0.25, o hs, tp e dp recebem nan
print 'Realizando Consistencia Conjunta de Ondas'
dadosc[np.where(dados[:,9] < 0.25)[0],9] = np.nan #coloca na nos hs menor que 0.25 (talvez o cq acima ja tenha feito isso)
hsnan = np.where(np.isnan(dadosc[:,9])==True)
dadosc[hsnan,10] = np.nan #coloca nan no periodo de pico
dadosc[hsnan,11] = np.nan #coloca nan na direcao de pico

#consistencia visual
print 'Consistencia Visual'

if local == 'recife':
	pass
    # dadosc[1995:6995,1:] = np.nan
    # dadosc[11411:15932,1:] = np.nan
    # dadosc[11532:15766,1:] = np.nan
elif local == 'florianopolis':
	pass
    # dadosc[2352:4118,1:] = np.nan #florianopolis
elif local == 'santos':
    pass
elif local == 'rio_grande':
    pass

#corrigo com localizacao e declinacao
head = 'date,lat,lon,ws,wg,wd,at,pr,wt,hs,tp,dp'
np.savetxt('out/argos_opendap_' + local + '.out',dados,delimiter=',',fmt=['%i']+11*['%.2f'],header=head)

#salva arquivo consistentes (_cq)
#         0  1   2 3  4  5  6  7  8  9
head = 'date,lat,lon,ws,wg,wd,at,pr,wt,hs,tp,dp'
np.savetxt('out/argos_opendap_cq_' + local + '.out',dadosc,delimiter=',',fmt=['%i']+11*['%.2f'],header=head)
