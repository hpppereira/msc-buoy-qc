#Verifica freakwaves

import numpy as np
import pylab as pl
import os

pl.close('all')

loc = 'rio_grande'
#carrega parametros de onda

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

hs1, hmax1 = np.loadtxt(pathname + 'triaxys_cp_8_' + loc + '.out', usecols=(1,3), delimiter=',', unpack=True)

#calcula relacao para classificar freakwave (Hmax/Hs > 2.1)
rfw1 = hmax1 / hs1

#retira os valores com nan
rfw = rfw1[np.where(np.isnan(rfw1)==False)]
hs = hs1[np.where(np.isnan(hs1)==False)]
hmax = hmax1[np.where(np.isnan(hmax1)==False)]

nfw = len(np.where(rfw>=2.1)[0]) #numero de ondas com relacao hmax/hs > 2.1
pfw = float(nfw)/len(rfw) * 100 #porcentagem de frakwaves

#plotagem

pl.figure()
pl.hist(rfw,50)
pl.plot(np.linspace(2.1,2.1,2),np.linspace(0,1500,2),linewidth=3) #limite de 2,1 
pl.title('Relacao de Freak-Wave (Ochi)')
pl.xlabel('Hmax / Hs')
pl.ylabel('Numero de ocorrencias')
pl.grid()
pl.axis('tight')

pl.show()

