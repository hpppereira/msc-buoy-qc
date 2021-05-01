# -*- coding: utf-8 -*-
'''
Compara os dados reprocessados em python com o arquivo Summary (calculado
pela boia) e os do argos (baixados do site)

Henrique P. P. Pereira
LIOc/COPPE/UFRJ

-- Descricao --
Verificar se mesmo com a data baguncada do arquivo Summary
conseguimos coincidir as data utilizando o plot_date, ou 
tentando ler os dados e fazer um 'sort'.

Ultima modificacao: 21/01/2015

#Saida do Python
#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')

#Saida da Axys
#  0        1            2          3        4        5         6        7            8            9         10     11           12       13      14              15  
#YearJulian Date/Zero Crossings/Ave. Ht./Ave. Per./Max Ht./Sig. Wave/Sig. Per./Peak Per.(Tp)/Peak Per.(READ)/HM0/Mean Theta/Sigma Theta/ H1/10 / T.H1/10	/Mean Per.(Tz)

#Saida site (baixado em 08/09/2013)
#  0   1   2   3     4    5    6   7   8
# ano mes dia hora minuto Hs Hmax Tp Dirm

'''

import numpy as np
from matplotlib import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime
import os

# pl.close('all')

# ============================================================================== #
#Carrega os dados


#localizacao (habilite um para processar)

# local = 'Recife/PE' # relatorio
# local1 = 'recife' #nome do arquivo salvo
# latlon = '-8.149 / -34.56' #relatorio
# idargos = '69154'
# idwmo = '31052'

# local = 'Santos/SP'
# local1 = 'santos'
# latlon = '-25.28334 / -44.93334'
# idargos = '69151'
# idwmo = '31051'
# glstr = '8'


# local = 'Florianpolis/SC'
# local1 = 'florianopolis'
# latlon = '-28.50000 / -47.36667'
# idargos = '69150'
# idwmo = '31374'

local = 'Rio Grande/RS'
local1 = 'rio_grande'
latlon = '-31.56667 / -49.86667'
idargos = '69153'
idwmo = '31053'
glstr = '8'

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#Saida do Python
#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')
py = np.loadtxt(pathname + 'triaxys_cp_' + glstr + '_' + local1 + '.out',delimiter=',',skiprows = 0)

datam_py = np.array([datetime.strptime(str(int(py[i,0])), '%Y%m%d%H%M') for i in range(len(py))])


#Saida da Axys
#  0        1            2          3        4        5         6        7            8            9         10     11           12       13      14              15  
#YearJulian Date/Zero Crossings/Ave. Ht./Ave. Per./Max Ht./Sig. Wave/Sig. Per./Peak Per.(Tp)/Peak Per.(READ)/HM0/Mean Theta/Sigma Theta/ H1/10 / T.H1/10	/Mean Per.(Tz)
ax = np.loadtxt(pathname + 'Summary_' + local1 + '.txt',skiprows = 1, usecols = (range(2,18)))
ax_data = np.loadtxt(pathname + 'Summary_' + local1 + '.txt',dtype = str, skiprows = 1, usecols = (0,1))

#Saida site (baixado em 08/09/2013)
#  0   1   2   3     4    5    6   7   8
# ano mes dia hora minuto Hs Hmax Tp Dirm
site = np.loadtxt(pathname + 'pnboia.B' + idargos + '_argos.dat',delimiter=',', skiprows = 1, usecols = (2,3,4,5,6,45,46,47,48))

#carrega a matriz do espectro directional processada pela axys
# do dia 200905090600 - mar bimodal
dirspec = np.loadtxt(pathname + '200912130600.DIRSPEC',skiprows=12)
#nondirspec = np.loadtxt(pathname + '200905090600.NONDIRSPEC',skiprows=9)
#meandir = np.loadtxt(pathname + '200905090600.MEANDIR',skiprows=14)
#sn = np.loadtxt(pathname + 'sn_200905090600.out')

# ============================================================================== #
#Definicao de parametros de onda

#python
hs_py = py[:,1]
h10_py = py[:,2]
hmax_py = py[:,3]
tmed_py = py[:,4]
thmax_py = py[:,5]
hm0_py = py[:,6]
tp_py = py[:,7]
dirtp_py = py[:,8]

#axys
hm0_ax = ax[:,10]
tp_ax = ax[:,8] #qual periodo usar?
tmed_ax = ax[:,15]
th10_ax = ax[:,14]
dirtp_ax = ax[:,11]
hmax_ax = ax[:,5]
hs_ax = ax[:,6]
h10_ax = ax[:,13]

#site
hs_st = site[:,5]
hmax_st = site[:,6]
tp_st = site[:,7]
dirm_st = site[:,8]

# ========================================================================== #
#Correcao dos dados (para facilitar na visualizacao dos graficos
#*pois tem valores de hs de 1200 no site)

hs_st[(np.where(hs_st>30))] = np.nan

# ========================================================================== #

#Graficos

# #hm0 
# pl.figure()
# pl.plot_date(datam_py,hm0_py,'bo')
# pl.plot_date(datam_ax,hm0_ax,'go',alpha=0.5)
# pl.title('Hm0 - Rio_Grande_do_Sul')
# pl.ylabel('metros')
# pl.legend(('python','axys'))

# #hs
# pl.figure()
# pl.plot_date(datam_py,hs_py,'bo')
# pl.plot_date(datam_ax,hs_ax,'go',alpha=0.6)
# pl.plot_date(datam_st,hs_st,'ro',alpha=0.5)
# pl.title('Hs - Rio_Grande_do_Sul')
# pl.ylabel('meters')
# pl.legend(('python','axys','site'))

# #h 1/10
# pl.figure()
# pl.plot_date(datam_py,h10_py,'bo')
# pl.plot_date(datam_ax,h10_ax,'go',alpha=0.5)
# pl.title('H 1/10 - Rio_Grande_do_Sul')
# pl.ylabel('metros')
# pl.legend(('python','axys'))

# #hmax
# pl.figure()
# pl.plot_date(datam_py,hmax_py,'bo')
# pl.plot_date(datam_ax,hmax_ax,'go',alpha=0.6)
# pl.plot_date(datam_st,hmax_st,'ro',alpha=0.5)
# pl.ylabel('metros')
# pl.title('Hmax - Rio_Grande_do_Sul')
# pl.legend(('python','axys','site'))

# #tp
# pl.figure()
# pl.plot_date(datam_py,tp_py,'bo')
# pl.plot_date(datam_ax,tp_ax,'go',alpha=0.6)
# pl.plot_date(datam_st,tp_st,'ro',alpha=0.5)
# pl.ylabel('segundos')
# pl.title('Tp - Rio_Grande_do_Sul')
# pl.legend(('python','axys','site'))

# #tmed
# pl.figure()
# pl.plot_date(datam_py,tmed_py,'bo')
# pl.plot_date(datam_ax,tmed_ax,'go',alpha=0.5)
# pl.title('tmed')
# pl.legend(('python','axys'))

# #t hmax
# pl.figure()
# pl.plot_date(datam_py,thmax_py,'bo')
# pl.plot_date(datam_ax,th10_ax,'go',alpha=0.6)
# pl.title('t hmax')
# pl.legend(('python','axys'))

# #dirtp
# pl.figure()
# pl.plot_date(datam_py,dirtp_py,'bo')
# pl.plot_date(datam_ax,dirtp_ax,'go',alpha=0.6)
# pl.plot_date(datam_st,dirm_st,'ro',alpha=0.5)
# pl.title('Dirtp - Rio_Grande_do_Sul')
# pl.ylabel('graus')
# pl.legend(('python','axys','site'))

#subplot do periodo de dez 09
# pl.figure()
# pl.subplot(3,1,1)
# pl.plot_date(datam_py,hs_py,'b.')
# pl.plot_date(datam_ax,hs_ax,'g.') #,alpha=0.6)
# pl.plot_date(datam_st,hs_st,'r.',alpha=0.5)
# pl.axis([datam_py[0],datam_py[-1],0,10])
# pl.title(local)
# pl.ylabel('Hs - metros')
# pl.legend(('lioc','axys','site'))
# # pl.xticks(rotation=70)
# pl.subplot(3,1,2)
# pl.plot_date(datam_py,tp_py,'b.')
# pl.plot_date(datam_ax,tp_ax,'g.',alpha=0.6)
# pl.plot_date(datam_st,tp_st,'r.',alpha=0.5)
# pl.axis([datam_py[0],datam_py[-1],0,20])
# pl.ylabel('Tp - segundos')
# # pl.legend(('lioc','axys','site'))
# pl.subplot(3,1,3)
# pl.plot_date(datam_py,dirtp_py,'b.')
# pl.plot_date(datam_ax,dirtp_ax,'g.',alpha=0.6)
# pl.plot_date(datam_st,dirm_st,'r.',alpha=0.5)
# pl.axis([datam_py[0],datam_py[-1],0,360])
# pl.ylabel('Dp - graus')
# # pl.legend(('lioc','axys','site'))

#######################################################################
#figura de particionamento espectral - ww3br

#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')

#escolhe o limite da plotagem
lfi = pl.find(py[:,0]==200905010000)
lfs = pl.find(py[:,0]==200905312300)

# lfi = 0
# lfs = len(py) - 1

pl.figure()
pl.title(local)
pl.subplot(3,1,1)
pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,11],'go') #hm01
pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,14],'ro') #hm02
pl.axis([datam_py[lfi],datam_py[lfs],0,np.nanmax(py[lfi:lfs,6])])
pl.xticks(visible=False)
pl.grid()
pl.ylabel('Hs - metros')
pl.legend(['$swell$','$windsea$'],loc=0)

pl.subplot(3,1,2)
pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,12],'go',label='Tp1') #hm01
pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,15],'ro',label='Tp2') #hm02
pl.axis([datam_py[lfi],datam_py[lfs],0,20])
pl.xticks(visible=False)
pl.grid()
pl.ylabel('Tp - seg')

pl.subplot(3,1,3)
pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,13],'go',label='Tp1') #hm01
pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,16],'ro',label='Tp2') #hm02
pl.axis([datam_py[lfi],datam_py[lfs],0,360])
pl.grid()
pl.ylabel('Dp - graus')


##########################################################################
#matriz do espectro direcional processado pela axys
#arquivo .DIRSPEC

# #espec 1d
# plt.figure()
# pl.subplot(211)
# plt.plot(meandir[:,0],meandir[:,1],'b')
# plt.plot(sn[:,0],sn[:,1],'r')
# plt.legend(['axys','lioc'])
# plt.grid()
# plt.ylabel('m2/Hz')

# #dirmedia +- spread
# plt.subplot(212)
# plt.plot(meandir[:,0],meandir[:,2],'-b')
# plt.plot(meandir[:,0],meandir[:,2] + meandir[:,3] / 2 ,'--b')
# plt.plot(meandir[:,0],meandir[:,2] + (meandir[:,3] / 2 * -1) ,'--b')
# plt.plot(sn[:,0],sn[:,2],'-r')
# plt.plot(sn[:,0],sn[:,2] + sn[:,3] / 2 ,'--r') #spread
# plt.plot(sn[:,0],sn[:,2] + (sn[:,3] / 2 * -1) ,'--r') #spread
# plt.ylim(0,360)
# plt.grid()
# plt.ylabel('graus')

#axys
#matriz de 129 freq e 128 direcoes
[freqs,dires] = np.meshgrid(np.linspace(0.06,0.445,129),np.linspace(0,360,121),sparse=False,copy=False)

#corrige declinacao mag??

plt.figure()
cs = plt.contourf(freqs,dires,dirspec.T,shading='flat',cmap=plt.cm.jet,levels=np.linspace(dirspec.min(),dirspec.max(),20)) #,vmin=np.nanmin(s2d),vmax=np.nanmax(s2d))
plt.xlabel('Freq. (Hz)'), plt.ylabel('graus')
plt.colorbar(label=u'm2/Hz')
plt.ylim(0,345)

#lioc
# [freqs,dires] = np.meshgrid(np.linspace(0,max(sn[:,0]),100),np.linspace(0,360,100),sparse=False,copy=False)
# en = sn[:,1] * np.real(sn[:,3])

#interpola a energia
# sp2 = mpl.mlab.griddata(sn[:,0],sn[:,2],en/max(sn[:,3]),freqs,dires,interp='nn') #a interp linear e a nn ficaram praticamente iguais

#coloca zeros no lugar de nan
# sp2.data[np.where(np.isnan(sp2.data)==True)] = 0

# plt.subplot(224)
# cs = plt.contourf(freqs,dires,sp2.data,shading='flat',cmap=plt.cm.jet,levels=np.arange(0,np.nanmax(sp2.data),0.25),vmin=np.nanmin(sp2.data),vmax=np.nanmax(sp2.data))
# plt.xlabel('Freq. (Hz)'), plt.ylabel('graus')
# plt.colorbar()





pl.show()