'''
Processamento e controle de qualidade dos dados
de ondas do PNBOIA baixados pelo site do GOOS/BRASIL

Site:
Ex de arquivo: 'pnboia.B69151_argos.dat'

69154 - recife
69151 - santos
69150 - florianopolis
69153 - rio grande

Realiza a consistencia dos dados processados (consiste_proc.py)

#Boia da baia de guanabara - o formato esta diferente
# argos = np.loadtxt(pathname + 'pnboia.B69009_argos.dat' ,delimiter=',', skiprows = 1, usecols = (2,3,4,5,6,41,42,43,44,45))

'''

import numpy as np
import pylab as pl
import os
from datetime import datetime

pl.close('all')

arq = 'pnboia.B69153_argos.dat'
# arq_lioc = 'argos_rio_grande'

pathname = os.environ['HOME'] + '/Dropbox/lioc/dados/pnboia/argos/goos/'
# pathname_lioc = os.environ['HOME'] + '/Dropbox/tese/rot/out/argos/'

# ============================================================================= #

#         0   1   2   3     4      5    6    7   8   9   10  11  12  13  14  15  16  17  18  19  20  21    22  23   24
# goos = ano mes dia hora minuto, lon, lat, bat, ws, wg, wd, at, rh, dw, pr, wt, hd, cl, tu, sr, Hs, Hmax, Tp, Dirm, Df
goos = np.loadtxt(pathname + arq ,delimiter=',', skiprows = 1, usecols = (2,3,4,5,6,7,8,10,27,28,29,30,31,32,33,34,35,36,37,38,45,46,47,48,49))

data = []
for i in range(len(goos)):
	data.append(datetime(int(goos[i,0]),int(goos[i,1]),int(goos[i,2]),int(goos[i,3]),int(goos[i,4])))

#deixa os valores com -99999 (erro) com nan
for i in range(goos.shape[1]):
	goos[np.where(goos[:,i] == -99999),i] = np.nan

#define variaveis
lon, lat, bat, ws, wg, wd, at, rh, dw, pr, wt, hd, cl, tu, sr, hs, hmax, tp, dm, df = goos[:,[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]].T


# Fazer aqui a consitencia dos dados



# ============================================================================= #

#          0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
# lioc = data ws wg wd at rh dw pr st bh cl tu sr hs hm tp dp sp
#lioc = np.loadtxt(pathname_lioc + arq_lioc + '.out',delimiter=',')
#data_li = np.array([datetime.strptime(str(int(lioc[i,0])), '%Y%m%d%H%M') for i in range(len(lioc))])
# lioc = dados[:,1:]


#pl.figure()
#pl.plot(data_go,ws)
#pl.plot(data_li,lioc[:,1])
#pl.show()

# pl.figure()
# pl.plot(datat,hs,'ob')
# # pl.plot(datat,hmax,'or')

# hs_goos = hs

# pl.show()