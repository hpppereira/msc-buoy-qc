'''
Pos processamento dos dados meteorologicos 
do PNBOIA cedidos pelo CHM

Os dado de entrada dessa rotina sao gerados pela saida
da rotina 'pp_argos_chm_concat.py'

Ex de dado de entrada:
col:  0    1   2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
var: date ws wg wd at rh dw pr wt bh cl tu sr hs hm tp dp sp

A saida dos dados eh utilizada na rotina pp_argos_chm_analysis.py

Ex de saida dos dados submetidos a consistencia
#         0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
# dados = ws wg wd at rh dw pr st bh cl tu sr hs hm tp dp sp

#           0   1  2 3   4 5   6  7 8  9  10 11 
# dados = date bh ws wg wd at rh pr Wt hs tp dp



'''

import os
import numpy as np
from datetime import datetime
import pylab as pl
import consiste_proc
from scipy.stats import norm
import matplotlib.mlab as mlab

reload(consiste_proc)

#pl.close('all')

#escolha a boia a ser processada ('rio_grande', 'santos', 
boia = 'rio_grande'

#caminho dos arquivos
pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/argos/'

#carrega dados
dados = np.loadtxt(pathname + 'argos_chm_' + boia + '.out',delimiter=',')

data = np.array([datetime.strptime(str(int(dados[i,0])), '%Y%m%d%H%M') for i in range(len(dados))])

#data em numero inteiro
datastr = data.astype(str)
datai = np.array([datastr[i][0:4]+datastr[i][5:7]+datastr[i][8:10]+datastr[i][11:13].zfill(2)+'00' for i in range(len(datastr))])
datai = datai.astype(int)

# data = np.array([datetime(int(mat[i,0][0:4]),int(mat[i,0][5:7]),int(mat[i,0][8:10]),int(mat[i,1][0:2])) for i in range(len(mat))])

dados = dados[:,1:]

#         0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
# dados = ws wg wd at rh dw pr st bh cl tu sr hs hm tp dp sp

#numero de parametros processados
npa = 17

# ================================================================================== #  

#cria vetores de flags das series processadas (depende das qtdade de variaveis a serem consistidas + data) 
flagp = np.zeros((len(dados),npa+1),dtype='|S32')
flagp[:,0] = data.astype(str)

# ================================================================================== #  
# Testes de consistencia dos dados processados

# #Teste 1 - faixa
flagp[:,1] = consiste_proc.faixa(dados[:,0],0.25,30,0.5,15,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.faixa(dados[:,1],0.25,40,0.5,25,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.faixa(dados[:,2],0,360,0,360,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.faixa(dados[:,3],0,40,10,30,flagp[:,4]) #at
flagp[:,5] = consiste_proc.faixa(dados[:,4],25,102,40,100,flagp[:,5]) #rh
# flagp[:,6] = consiste_proc.faixa(dados[:,5],0,40,10,30,flagp[:,6]) #dw
flagp[:,7] = consiste_proc.faixa(dados[:,6],900,1100,950,1050,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.faixa(dados[:,7],12,38,15,35,flagp[:,8]) #st
flagp[:,9] = consiste_proc.faixa(dados[:,8],0,360,0,360,flagp[:,9]) #bh
# flagp[:,10] = consiste_proc.faixa(dados[:,9],???,flagp[:,10]) #cl
# flagp[:,11] = consiste_proc.faixa(dados[:,10],???,flagp[:,11]) #tu
# flagp[:,12] = consiste_proc.faixa(dados[:,11],0,1500,10,1450,flagp[:,12]) #sr
flagp[:,13] = consiste_proc.faixa(dados[:,12],0,20,0.25,8,flagp[:,13]) #hs
# flagp[:,14] = consiste_proc.faixa(dados[:,13],0,35,0.5,20,flagp[:,14]) #hm
flagp[:,15] = consiste_proc.faixa(dados[:,14],3,30,4,18,flagp[:,15]) #tp
flagp[:,16] = consiste_proc.faixa(dados[:,15],0,360,0,360,flagp[:,16]) #dp
# flagp[:,17] = consiste_proc.faixa(dados[:,16],0,360,0,360,flagp[:,17]) #sp

# #Teste 1 - Variabilidade
flagp[:,1] = consiste_proc.variab(dados[:,0],1,5,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.variab(dados[:,1],1,5,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.variab(dados[:,2],1,5,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.variab(dados[:,3],1,5,flagp[:,4]) #at
flagp[:,5] = consiste_proc.variab(dados[:,4],1,5,flagp[:,5]) #rh
# flagp[:,6] = consiste_proc.variab(dados[:,5],1,5,flagp[:,6]) #dw
flagp[:,7] = consiste_proc.variab(dados[:,6],1,5,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.variab(dados[:,7],1,5,flagp[:,8]) #st
flagp[:,9] = consiste_proc.variab(dados[:,8],1,5,flagp[:,9]) #bh
# flagp[:,10] = consiste_proc.variab(dados[:,9],???,flagp[:,10]) #cl
# flagp[:,11] = consiste_proc.variab(dados[:,10],???,flagp[:,11]) #tu
# flagp[:,12] = consiste_proc.variab(dados[:,11],1,5,flagp[:,12]) #sr
flagp[:,13] = consiste_proc.variab(dados[:,12],1,5,flagp[:,13]) #hs
# flagp[:,14] = consiste_proc.variab(dados[:,13],1,5,flagp[:,14]) #hm
flagp[:,15] = consiste_proc.variab(dados[:,14],1,5,flagp[:,15]) #tp
flagp[:,16] = consiste_proc.variab(dados[:,15],1,5,flagp[:,16]) #dp
# flagp[:,17] = consiste_proc.variab(dados[:,16],1,5,flagp[:,17]) #sp

# #Teste 1 - Consec. iguais
flagp[:,1] = consiste_proc.iguais(dados[:,0],5,flagp[:,1]) #ws
flagp[:,2] = consiste_proc.iguais(dados[:,1],5,flagp[:,2]) #wg
flagp[:,3] = consiste_proc.iguais(dados[:,2],5,flagp[:,3]) #wd
flagp[:,4] = consiste_proc.iguais(dados[:,3],5,flagp[:,4]) #at
flagp[:,5] = consiste_proc.iguais(dados[:,4],5,flagp[:,5]) #rh
# flagp[:,6] = consiste_proc.iguais(dados[:,5],5,flagp[:,6]) #dw
flagp[:,7] = consiste_proc.iguais(dados[:,6],5,flagp[:,7]) #pr
flagp[:,8] = consiste_proc.iguais(dados[:,7],5,flagp[:,8]) #st
flagp[:,9] = consiste_proc.iguais(dados[:,8],5,flagp[:,9]) #bh
# flagp[:,10] = consiste_proc.iguais(dados[:,9],???,flagp[:,10]) #cl
# flagp[:,11] = consiste_proc.iguais(dados[:,10],???,flagp[:,11]) #tu
# flagp[:,12] = consiste_proc.iguais(dados[:,11],5,flagp[:,12]) #sr
flagp[:,13] = consiste_proc.iguais(dados[:,12],5,flagp[:,13]) #hs
# flagp[:,14] = consiste_proc.iguais(dados[:,13],5,flagp[:,14]) #hm
flagp[:,15] = consiste_proc.iguais(dados[:,14],5,flagp[:,15]) #tp
flagp[:,16] = consiste_proc.iguais(dados[:,15],5,flagp[:,16]) #dp
# flagp[:,17] = consiste_proc.iguais(dados[:,16],5,flagp[:,17]) #sp


# ================================================================================== #  
# Coloca nan nos dados reprovados e suspeitos

#### *** verificar coluna de data

#matriz com dados consistentes
dadosc = np.copy(dados)

for c in range(1,flagp.shape[1]):

    for i in range(len(flagp)):

        if '4' in flagp[i,c] or '3' in flagp[i,c]:

        	print (['Arquivo: ' + str(flagp[i,0]) + ' -- Reprovado'])

        	dadosc[i,c-1] = np.nan


#         0  1   2 3  4   5 6  7  8  9  10
# dados = bh ws wg wd at rh pr Wt hs tp dp
dadosc = dadosc[:,[8,0,1,2,3,4,5,6,7,12,14,15]]

#salva arquivo de dados consistentes
arqc = np.concatenate(([datai],dadosc.T)).T

#           0   1  2 3   4 5   6  7 8  9  10 11 
# dados = date bh ws wg wd at rh pr Wt hs tp dp
head = 'date,bh,ws,wg,wd,at,rh,pr,wt,hs,tp,dp'

np.savetxt('out/argos/argos_chm_' + boia + '_lioc.out',arqc,delimiter=',',fmt='%s',header=head)

