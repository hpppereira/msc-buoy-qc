'''
Processamento de todos os dados
do SIODOC (janis) enviados pelo candela
no dia:

Para processar os dados baixados do site,
utilizar a rotina:
pp_siodoc_site_proc.py
'''

import os
import numpy as np
import pylab as pl
from datetime import datetime

pl.close('all')

pathname = os.environ['HOME'] + '/Dropbox/siodoc/dados/proc/'

local = 'arraial_cabo'

print 'Iniciando concatenacao em... ' + local

dd = np.loadtxt(pathname + 'janis_data.dat') #siodoc

#decinacao mag (-23 graus)
#Obs: os dados de direcao das ondas e do vento
#	  sao corrigidos abaixo
dmag = -23

#data com datetime
#siodoc
datat = np.array([datetime(int(dd[i,2]),int(dd[i,1]),int(dd[i,0]),int(dd[i,3])) for i in range(len(dd))])
datastr = datat.astype(str)

#data em numero inteiro
datai = np.array([datastr[i][0:4]+datastr[i][5:7]+datastr[i][8:10]+datastr[i][11:13].zfill(2)+'00' for i in range(len(datastr))])
datai = datai.astype(int)

#define variaveis

bp = dd[:,6] #pressao atm
at = dd[:,7] #temp ar
hm0 = dd[:,27] #hm0
hm0a = dd[:,28] #hm0 swell
hm0b = dd[:,29] #hm0 sea
hmax = dd[:,30] #hmax (onda individual)
dp = dd[:,38] + dmag #dp
dpa = dd[:,39] + dmag #dp swell
dpb = dd[:,40] + dmag #dp sea
spr = dd[:,50] + dmag #espalhamento ang em torno de tp
thhf = dd[:,51] + dmag #direcao media de alta freq
thmax = dd[:,52] #periodo da onda maxima
thtp = dd[:,53] + dmag #direcao da onda no Tp (idem dp?)
tm01 = dd[:,54] #periodo medio (m0/m1)
tm02 = dd[:,55] #periodo medio (sqrt(m0/m1))
tm02a = dd[:,56] #periodo medio (swell)
tp = dd[:,57] #periodo de pico
wt = dd[:,58] #temp agua sup
wd = dd[:,66] + dmag #dir vento
wg = dd[:,67] #int de rajada do vento
ws = dd[:,68] #int do vento

#corrige valores que ficaram menor que zero

dp[np.where(dp < 0)] = dp[np.where(dp < 0)] + 360
dpa[np.where(dpa < 0)] = dpa[np.where(dpa < 0)] + 360
thtp[np.where(thtp < 0)] = thtp[np.where(thtp < 0)] + 360
wd[np.where(wd < 0)] = wd[np.where(wd < 0)] + 360

dados = np.array([datai,ws,wg,wd,at,bp,wt,hm0,tp,dp]).T

# #salva os dados
head = 'date,ws,wg,wd,at,bp,wt,hs,tp,dp'
np.savetxt('out/siodoc_janis_'+local+'.out',dados,delimiter=',',fmt=['%i']+9*['%.2f'],header=head)


# #figuras
# pl.figure()
# pl.title('Altura Significativa')
# pl.plot(datat,hm0,'bo')

# pl.figure()
# pl.title('Periodo de Pico')
# pl.plot(datat,tp,'bo')

# pl.figure()
# pl.title('Direcao de Pico e Vento')
# pl.plot(datat,thhf,'bo',datat,wd,'go')
# pl.legend(['dp','wd'])

# pl.show()