'''
Analise dos dados processados do PNBOIA
pelo LIOc

#Saida do Python
#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')
'''


import numpy as np
from matplotlib import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime
import os
from scipy.stats import norm
import matplotlib.mlab as mlab
import windrose
from windrose import WindroseAxes
import matplotlib.dates as mdates

pl.close('all')

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
# dmag = - 23

# local = 'Florianpolis/SC'
# local1 = 'florianopolis'
# latlon = '-28.50000 / -47.36667'
# idargos = '69150'
# idwmo = '31374'

local = 'Rio Grande/RS'
local1 = 'rio_grande'
latlon = '-31.56667 / -49.86667'
idargos = '69153'
wmo = '31053'
glstr = '8'
dmag = - 16.8

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')
# re = np.loadtxt(pathname + 'triaxys_8_recife.out',delimiter=',') 
sa = np.loadtxt(pathname + 'triaxys_cp_8_santos.out',delimiter=',') 
fl = np.loadtxt(pathname + 'triaxys_cp_8_florianopolis.out',delimiter=',') 
rg = np.loadtxt(pathname + 'triaxys_cp_8_rio_grande.out',delimiter=',')


#Saida do Python
#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')
py = np.loadtxt(pathname + 'triaxys_cp_' + glstr + '_' + local1 + '.out',delimiter=',',skiprows = 0)

#Saida da Axys
#  0        1            2          3        4        5         6        7            8            9         10     11           12       13      14              15  
#YearJulian Date/Zero Crossings/Ave. Ht./Ave. Per./Max Ht./Sig. Wave/Sig. Per./Peak Per.(Tp)/Peak Per.(READ)/HM0/Mean Theta/Sigma Theta/ H1/10 / T.H1/10	/Mean Per.(Tz)
rgax = np.loadtxt(pathname + 'Summary_' + local1 + '.txt',skiprows = 1, usecols = (range(2,18)))
rgax_data = np.loadtxt(pathname + 'Summary_' + local1 + '.txt',dtype = str, skiprows = 1, usecols = (0,1))

#Saida site (baixado em 08/09/2013)
#  0   1   2   3     4    5    6   7   8
# ano mes dia hora minuto Hs Hmax Tp Dirm
site = np.loadtxt(pathname + 'pnboia.B' + idargos + '_argos.dat',delimiter=',', skiprows = 1, usecols = (2,3,4,5,6,45,46,47,48))


#   0     1   2      3   4   5  6   7   8   9  10   11
# datai, lat, lon,  ws, wg, wd, at, pr, wt, hs, tp, dp
dadoscrg = np.loadtxt(pathname + 'argos_opendap_cq_' + local1 + '.out',delimiter=',') #dados sem cq
datatcrg = np.array([datetime.strptime(str(int(dadoscrg[i,0])), '%Y%m%d%H%M') for i in range(len(dadoscrg))])


#carrega a matriz do espectro directional processada pela axys
# do dia 200905090600 - mar bimodal
dirspec = np.loadtxt(pathname + '200905090600.DIRSPEC',skiprows=12)
#dirspec = np.loadtxt(pathname + '200912130600.DIRSPEC',skiprows=12)
#nondirspec = np.loadtxt(pathname + '200905090600.NONDIRSPEC',skiprows=9)
#meandir = np.loadtxt(pathname + '200905090600.MEANDIR',skiprows=14)
#sn = np.loadtxt(pathname + 'sn_200905090600.out')


#correcao da declinacao magnetica 
# re[:,8] = re[:,8] + dmag
# re[:,13] = re[:,13] + dmag
# re[:,16] = re[:,16] + dmag
# re[pl.find(re[:,8] < 0),8] = re[pl.find(re[:,8] < 0),8] + 360
# re[pl.find(re[:,13] < 0),13] = re[pl.find(re[:,13] < 0),13] + 360
# re[pl.find(re[:,16] < 0),16] = re[pl.find(re[:,16] < 0),16] + 360

dmag = -22
sa[:,8] = sa[:,8] + dmag
sa[:,13] = sa[:,13] + dmag
sa[:,16] = sa[:,16] + dmag
sa[pl.find(sa[:,8] < 0),8] = sa[pl.find(sa[:,8] < 0),8] + 360
sa[pl.find(sa[:,13] < 0),13] = sa[pl.find(sa[:,13] < 0),13] + 360
sa[pl.find(sa[:,16] < 0),16] = sa[pl.find(sa[:,16] < 0),16] + 360

dmag = -23
fl[:,8] = fl[:,8] + dmag
fl[:,13] = fl[:,13] + dmag
fl[:,16] = fl[:,16] + dmag
fl[pl.find(fl[:,8] < 0),8] = fl[pl.find(fl[:,8] < 0),8] + 360
fl[pl.find(fl[:,13] < 0),13] = fl[pl.find(fl[:,13] < 0),13] + 360
fl[pl.find(fl[:,16] < 0),16] = fl[pl.find(fl[:,16] < 0),16] + 360

dmag = -17
rg[:,8] = rg[:,8] + dmag
rg[:,13] = rg[:,13] + dmag
rg[:,16] = rg[:,16] + dmag
rgax[:,11] = rgax[:,11] + dmag
rg[pl.find(rg[:,8] < 0),8] = rg[pl.find(rg[:,8] < 0),8] + 360
rg[pl.find(rg[:,13] < 0),13] = rg[pl.find(rg[:,13] < 0),13] + 360
rg[pl.find(rg[:,16] < 0),16] = rg[pl.find(rg[:,16] < 0),16] + 360
rgax[pl.find(rgax[:,11] < 0),11] = rgax[pl.find(rgax[:,11] < 0),11] + 360

#datas
# dre = np.array([datetime.strptime(str(int(re[i,0])), '%Y%m%d%H%M') for i in range(len(re))])
dsa = np.array([datetime.strptime(str(int(sa[i,0])), '%Y%m%d%H%M') for i in range(len(sa))])
dfl = np.array([datetime.strptime(str(int(fl[i,0])), '%Y%m%d%H%M') for i in range(len(fl))])
drg = np.array([datetime.strptime(str(int(rg[i,0])), '%Y%m%d%H%M') for i in range(len(rg))])
drgax = np.array([datetime.strptime(rgax_data[i,0]+'-'+rgax_data[i,1], '%Y/%m/%d-%H:%M') for i in range(len(rgax))])

#retira os valores com nan
# re1 = re[pl.find(pl.isnan(re[:,1])==False),:]
sa1 = sa[pl.find(pl.isnan(sa[:,1])==False),:]
fl1 = fl[pl.find(pl.isnan(fl[:,1])==False),:]
rg1 = rg[pl.find(pl.isnan(rg[:,1])==False),:]


####################################################################################
####################################################################################
#comparacao da serie temporal da axys (summary) e lioc

#janela para plotagem com as 3 medicoes
a1 = datetime(2012,8,19,1,0)
a2 = datetime(2012,9,30,1,0)
ms = 9 #markersize


pl.figure()
pl.subplot(311)
pl.plot(drgax,rgax[:,6],'b.',markersize=ms,label='axys')
pl.plot(drg,rg[:,6],'r.',markersize=ms,label='cq')
pl.plot(datatcrg,dadoscrg[:,9],'g.',markersize=ms,label='goos')
pl.legend(loc=9,fontsize=12,ncol=3)
pl.xticks(visible=False)
pl.ylabel(r'$Hs\ (m)$')
pl.ylim(-0.2,7)
pl.xlim(a1,a2)
pl.grid()
pl.subplot(312)
pl.plot(drgax,rgax[:,7],'b.',markersize=ms)
pl.plot(drg,rg[:,7],'r.',markersize=ms)
pl.plot(datatcrg,dadoscrg[:,10],'g.',markersize=ms)
pl.xticks(visible=False)
pl.ylabel(r'$Tp\ (s)$')
pl.ylim(2,18)
pl.xlim(a1,a2)
pl.grid()
pl.subplot(313)
pl.plot(drgax,rgax[:,11],'b.',markersize=ms)
pl.plot(drg,rg[:,8],'r.',markersize=ms)
pl.plot(datatcrg,dadoscrg[:,11],'g.',markersize=ms)
pl.axis('tight')
pl.xticks(visible=True)
pl.ylabel(r'$Dp\ $'+u'(\u00b0)')
pl.yticks([0,45,90,135,180,225,270,315,360])
pl.grid()
pl.xlim(a1,a2)

#plotagem do erro (ax-cq ; ax-goos ; cq-goos)

# pl.figure()
# pl.subplot(311)
# pl.plot(drgax,rgax[:,6],'b.',markersize=ms,label='axys')
# pl.plot(drg,rg[:,6],'r.',markersize=ms,label='cq')
# pl.plot(datatcrg,dadoscrg[:,9],'g.',markersize=ms,label='goos')
# pl.legend(loc=1,fontsize=12)
# pl.xticks(visible=False)
# pl.ylabel(r'$Hs\ (m)$')
# pl.ylim(-0.2,7)
# pl.xlim(a1,a2)
# pl.grid()
# pl.subplot(312)
# pl.plot(drgax,rgax[:,7],'b.',markersize=ms)
# pl.plot(drg,rg[:,7],'r.',markersize=ms)
# pl.plot(datatcrg,dadoscrg[:,10],'g.',markersize=ms)
# pl.xticks(visible=False)
# pl.ylabel(r'$Tp\ (s)$')
# pl.ylim(2,18)
# pl.xlim(a1,a2)
# pl.grid()
# pl.subplot(313)
# pl.plot(drgax,rgax[:,11],'b.',markersize=ms)
# pl.plot(drg,rg[:,8],'r.',markersize=ms)
# pl.plot(datatcrg,dadoscrg[:,11],'g.',markersize=ms)
# pl.axis('tight')
# pl.xticks(visible=True)
# pl.ylabel(r'$Dp\ $'+u'(\u00b0)')
# pl.yticks([0,45,90,135,180,225,270,315,360])
# pl.grid()
# pl.xlim(a1,a2)




####################################################################################
####################################################################################
#relacao de freakwave


#faz figura da relacao hmax/hs
pl.figure()
rfw = rg[:,3] / rg[:,1]
rfw1 = rg1[:,3] / rg1[:,1]
p95 = np.percentile(rfw1,95)
(mu, sigma) = norm.fit(rfw1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(rfw1,30,facecolor='blue',alpha=0.75)
pl.plot([2.1,2.1],[0,1900],'r--',linewidth=2)
# y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ Max=%.2f,\ Min=%.2f,\ \mu=%.2f, \sigma=%.2f,\ P98=%.2f$' %(rfw1.max(), rfw1.min(), mu, sigma, p95 ))
pl.xlabel(r'$Hmax/Hs$'), pl.ylabel(r'$Nu\'mero\ de\ ocorre\^ncias$')
pl.axis('tight'), pl.grid()
pl.xlim(1.2,2.5)

#acha ondas com hs > que 3 m e relacao hmax/hs> 2.1
indfw = np.where((rg[:,1]>3.5) & (rfw>2.1))[0] #indices das freawaves
numfw = len(indfw) #numero de freakwaves
datafw = drg[indfw] #datas com a freakwaves
#hsfw, hmaxfw, tpfw, dpfw = rg[indfw,[1,3,7,8]].T

pl.show()

####################################################################################
####################################################################################
#propagacao das ondas

a1rg = pl.find(drg==datetime(2012,3,23,1,0))
a2rg = pl.find(drg==datetime(2012,4,03,1,0))
a1fl = pl.find(dfl==datetime(2012,3,23,1,0))
a2fl = pl.find(dfl==datetime(2012,4,03,1,0))
a1sa = pl.find(dsa==datetime(2012,3,23,1,0))
a2sa = pl.find(dsa==datetime(2012,4,03,1,0))

pl.figure()
a=5
pl.subplot(311)
pl.plot(dsa[a1sa:a2sa],sa[a1sa:a2sa,6],'k-o', markersize=a)
pl.plot(dfl[a1fl:a2fl],fl[a1fl:a2fl,6],'r-d', markersize=a)
pl.plot(drg[a1rg:a2rg],rg[a1rg:a2rg,6],'c-*', markersize=a)
pl.xticks(visible=False)
pl.ylabel(r'$Hm0\ (m)$')
pl.grid()
pl.legend([r'$Santos$',r'$Florianpo\'lis$',r'$Rio\ Grande$'],fontsize=10,loc=1)
pl.subplot(312)
pl.plot(dsa[a1sa:a2sa],sa[a1sa:a2sa,7],'ko', markersize=a)
pl.plot(dfl[a1fl:a2fl],fl[a1fl:a2fl,7],'rd', markersize=a)
pl.plot(drg[a1rg:a2rg],rg[a1rg:a2rg,7],'c*', markersize=a)
pl.xticks(visible=False)
pl.ylabel(r'$Tp\ (s)$')
pl.grid()
pl.subplot(313)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
pl.plot(dsa[a1sa:a2sa],sa[a1sa:a2sa,8],'ko', markersize=a)
pl.plot(dfl[a1fl:a2fl],fl[a1fl:a2fl,8],'rd', markersize=a)
pl.plot(drg[a1rg:a2rg],rg[a1rg:a2rg,8],'c*', markersize=a)
pl.yticks([0,45,90,135,180,225,270,315,360])
pl.xticks(rotation=15)
pl.ylabel(r'$Dp\ $'+u'(\u00b0)')
pl.grid()
#plt.gcf().autofmt_xdate()



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
hm0_ax = rgax[:,10]
tp_ax = rgax[:,8] #qual periodo usar?
tmed_ax = rgax[:,15]
th10_ax = rgax[:,14]
dirtp_ax = rgax[:,11]
hmax_ax = rgax[:,5]
hs_ax = rgax[:,6]
h10_ax = rgax[:,13]

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
plt.xlabel(r'$Freque\^ncia (Hz)$',fontsize=14), plt.ylabel(r'$Direc\c{}a\~o\ (graus)$',fontsize=14)
cbar = plt.colorbar(format='%.2f')
cbar.set_label(r'$m^{2}/Hz$',size=14)
plt.ylim(0,360)

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





####################################################################################
####################################################################################



#######################################################################
#figura de particionamento espectral - ww3br

#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')



# #escolhe o limite da plotagem
# lfi = pl.find(py[:,0]==200905010000)
# lfs = pl.find(py[:,0]==200905312300)

# # lfi = 0
# # lfs = len(py) - 1

# pl.figure()
# pl.title(local)
# pl.subplot(3,1,1)
# pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,11],'go') #hm01
# pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,14],'ro') #hm02
# pl.axis([datam_py[lfi],datam_py[lfs],0,np.nanmax(py[lfi:lfs,6])])
# pl.xticks(visible=False)
# pl.grid()
# pl.ylabel('Hs - metros')
# pl.legend(['$swell$','$windsea$'],loc=0)

# pl.subplot(3,1,2)
# pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,12],'go',label='Tp1') #hm01
# pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,15],'ro',label='Tp2') #hm02
# pl.axis([datam_py[lfi],datam_py[lfs],0,20])
# pl.xticks(visible=False)
# pl.grid()
# pl.ylabel('Tp - seg')

# pl.subplot(3,1,3)
# pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,13],'go',label='Tp1') #hm01
# pl.plot_date(datam_py[lfi:lfs],py[lfi:lfs,16],'ro',label='Tp2') #hm02
# pl.axis([datam_py[lfi],datam_py[lfs],0,360])
# pl.grid()
# pl.ylabel('Dp - graus')


####################################################################################
####################################################################################













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

#esbeltez de onda (Hm0/Tp2)

# pl.figure()

# pl.subplot(221)
# fw = re[:,6] / re[:,7]**2
# fw = fw[pl.find(np.isnan(fw)==False)]
# (mu, sigma) = norm.fit(fw) #media e dp vel
# n, bins, patches = pl.hist(fw,25,normed=1,facecolor='blue',alpha=0.75)
# y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'k--',linewidth=3)
# pl.title(r'$\mathrm{}\ Recife\ -\ Esbeltez: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.ylabel('Probabilidade')
# pl.axis('tight'), pl.axis('tight'), pl.grid()
# # pl.xlim(1.2,2.5)

# pl.subplot(222)
# fw = sa[:,6] / sa[:,7]**2
# fw = fw[pl.find(np.isnan(fw)==False)]
# (mu, sigma) = norm.fit(fw) #media e dp vel
# n, bins, patches = pl.hist(fw,25,normed=1,facecolor='blue',alpha=0.75)
# y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'k--',linewidth=3)
# pl.title(r'$\mathrm{}\ Santos\ -\ Esbeltez: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.axis('tight'), pl.axis('tight'), pl.grid()
# # pl.xlim(1.2,2.5)

# pl.subplot(223)
# fw = fl[:,6] / fl[:,7]**2
# fw = fw[pl.find(np.isnan(fw)==False)]
# (mu, sigma) = norm.fit(fw) #media e dp vel
# n, bins, patches = pl.hist(fw,25,normed=1,facecolor='blue',alpha=0.75)
# y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'k--',linewidth=3)
# pl.title(r'$\mathrm{}\ Florianpolis\ -\ Esbeltez: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.ylabel('Probabilidade')
# pl.xlabel('Hm0/Tp2')
# pl.axis('tight'), pl.axis('tight'), pl.grid()
# # pl.xlim(1.2,2.5)

# pl.subplot(224)
# fw = rg[:,6] / rg[:,7]**2
# fw = fw[pl.find(np.isnan(fw)==False)]
# (mu, sigma) = norm.fit(fw) #media e dp vel
# n, bins, patches = pl.hist(fw,25,normed=1,facecolor='blue',alpha=0.75)
# y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'k--',linewidth=3)
# pl.title(r'$\mathrm{}\ Rio\ Grande\ -\ Esbeltez: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.axis('tight'), pl.axis('tight'), pl.grid()
# # pl.xlim(1.2,2.5)
# pl.xlabel('Hm0/Tp2')


####################################################################################
####################################################################################
#recife
#conjunta hm0 tp

# windrose
# def new_axes():
#     fig = plt.figure(figsize=(10, 8), dpi=80, frameon=False)
#     rect = [0.1, 0.1, 0.6, 0.8]
#     ax = WindroseAxes(fig, rect, axisbg='w')
#     fig.add_axes(ax)
#     return ax

# def set_legend(ax):
#     l = ax.legend(loc="center right",borderaxespad=-10.8)
#     # l.get_frame().set_fill(False) #transparent legend
#     plt.setp(l.get_texts(), fontsize=10,weight='bold')
    

# #windrose like a stacked histogram with normed (displayed in percent) results
# ax = new_axes()
# ax.bar(re[:,8], re[:,6], normed=True, bins=7, opening=0.8, edgecolor='white',nsector=8)
# ax.grid(True,linewidth=1.5,linestyle='dotted')
# set_legend(ax)
# plt.savefig('fig/triaxys_hsdp_' + local1 + '.png', dpi=None, facecolor='w', edgecolor='w',
# orientation='portrait', papertype=None, format='png',
# transparent=False, bbox_inches=None, pad_inches=0.1)    
# plt.close()

# #periodo de pico

# # windrose
# def new_axes():
#     fig = plt.figure(figsize=(10, 8), dpi=80, frameon=False)
#     rect = [0.1, 0.1, 0.6, 0.8]
#     ax = WindroseAxes(fig, rect, axisbg='w')
#     fig.add_axes(ax)
#     return ax

# def set_legend(ax):
#     l = ax.legend(loc="center right",borderaxespad=-10.8)
#     # l.get_frame().set_fill(False) #transparent legend
#     plt.setp(l.get_texts(), fontsize=10,weight='bold')
    

# #windrose like a stacked histogram with normed (displayed in percent) results
# ax = new_axes()
# ax.bar(re[:,8], re[:,7], normed=True, bins=7, opening=0.8, edgecolor='white',nsector=8)
# ax.grid(True,linewidth=1.5,linestyle='dotted')
# set_legend(ax)
# plt.savefig('fig/triaxys_tpdp_' + local1 + '.png', dpi=None, facecolor='w', edgecolor='w',
# orientation='portrait', papertype=None, format='png',
# transparent=False, bbox_inches=None, pad_inches=0.1)    
# plt.close()









pl.show()
