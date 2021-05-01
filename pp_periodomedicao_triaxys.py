'''
Grafico com periodos de medicoes das boias

dados de entrada: ano, mes, dia, hora
*matriz de parametros calculados
'''

import numpy as np
from datetime import datetime
import os
import matplotlib.pylab as pl

pl.close('all')

#carrega arquivos 'lista'

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#  0  1   2  3  4  5  6  7  8  9 10
re = np.loadtxt(pathname + 'triaxys_8_recife.out',delimiter=',') 
sa = np.loadtxt(pathname + 'triaxys_8_florianopolis.out',delimiter=',') 
fl = np.loadtxt(pathname + 'triaxys_8_santos.out',delimiter=',') 
rg = np.loadtxt(pathname + 'triaxys_8_rio_grande.out',delimiter=',') 

#datas
dre = np.array([datetime.strptime(str(int(re[i,0])), '%Y%m%d%H%M') for i in range(len(re))])
dsa = np.array([datetime.strptime(str(int(sa[i,0])), '%Y%m%d%H%M') for i in range(len(sa))])
dfl = np.array([datetime.strptime(str(int(fl[i,0])), '%Y%m%d%H%M') for i in range(len(fl))])
drg = np.array([datetime.strptime(str(int(rg[i,0])), '%Y%m%d%H%M') for i in range(len(rg))])

#valores para plotagem
vre = np.linspace(4,4,len(re))
vsa = np.linspace(3,3,len(sa))
vfl = np.linspace(2,2,len(fl))
vrg = np.linspace(1,1,len(rg))

pl.figure(); pl.hold('on')
# pl.title('Periodo medicao das boias meteo-oceanograficas - PNBOIA',fontsize=18)
pl.plot(dre,vre,'y.',markersize=25)
pl.plot(dsa,vsa,'g.',markersize=25)
pl.plot(dfl,vfl,'r.',markersize=25)
pl.plot(drg,vrg,'b.',markersize=25)

pl.xticks(rotation=20,fontsize=18)
pl.yticks(visible=False)
pl.xlabel('Data',fontsize=18)
pl.legend(['Recife','Santos','Florianopolis','Rio Grande'],loc=0,fontsize=18)
pl.ylim([0,5])
pl.grid('on')
pl.hold('off')

#xlim([731217  734139]); ylim([0 6]); grid();

pl.show()
