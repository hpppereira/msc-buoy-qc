'''
Programa principal para comparar
os dados de ondas enviados pelo sistema argos
e do processado pelo lioc
'''

import os
import numpy as np
import pylab as pl
from datetime import datetime

pl.close('all')

local = 'rio_grande'

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#  0   1  2   3     4    5    6  7  8    9       10    11   12  13   14  15  16
#data,hs,h10,hmax,tmed,thmax,hm0,tp,dp,sigma1p,sigma2p,hm01,tp1,dp1,hm02,tp2,dp2
lioc = np.loadtxt(pathname + 'triaxys_8_' + local + '.out',delimiter=',')

#   0     1     2    3   4   5   6  7   8   9   10  11 
# datai, lat, lon,  ws, wg, wd, at, pr, wt, hs, tp, dp
argos = np.loadtxt(pathname + 'argos_opendap_' + local + '.out',delimiter=',')

#converte datas para datetime
data_li = np.array([datetime.strptime(str(int(lioc[i,0])), '%Y%m%d%H%M') for i in range(len(lioc))])
data_ar = np.array([datetime.strptime(str(int(argos[i,0])), '%Y%m%d%H%M') for i in range(len(argos))])

pl.figure()
pl.plot(data_li,lioc[:,8]-17,'bo')
pl.plot(data_ar,argos[:,11],'ro')

pl.show()