# -*- coding: utf-8 -*-
'''
Analise dos dados brutos e processados
com controle de qualidade dos dados
baixados pelo opendap do site do goos/brasil
- saltambiental

dados - dados sem constrole de qualidade
dados_cq - dados com controle de qualidade

formato:
#   0     1   2   3   4   5   6  7   8   9   10
# datai, ws, wg, wd, at, rh, pr, wt, hs, tp, dp

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
from mpl_toolkits.basemap import Basemap, shiftgrid, interp
import mpl_toolkits.basemap
import matplotlib.pyplot as plt
import pandas.tools.rplot as rplot

reload(consiste_proc)
reload(windrose)

pl.close('all')

############################################################

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

# local = 'recife'
# local = 'santos'
# local = 'florianopolis'
local = 'rio_grande'

############################################################

print 'Realizando analise em... ' + local


#   0     1   2      3   4   5  6   7   8   9  10   11
# datai, lat, lon,  ws, wg, wd, at, pr, wt, hs, tp, dp
dados = np.loadtxt(pathname + 'argos_opendap_' + local + '.out',delimiter=',') #dados sem cq
dadosc = np.loadtxt(pathname + 'argos_opendap_cq_' + local + '.out',delimiter=',') #dados sem cq


#converte datas para datetime
datat = np.array([datetime.strptime(str(int(dados[i,0])), '%Y%m%d%H%M') for i in range(len(dados))])
datatc = np.array([datetime.strptime(str(int(dadosc[i,0])), '%Y%m%d%H%M') for i in range(len(dadosc))])

#cria nomes com variaveis consistentes
ws1 = dadosc[pl.find(pl.isnan(dadosc[:,3])==False),3]
wg1 = dadosc[pl.find(pl.isnan(dadosc[:,4])==False),4]
wd1 = dadosc[pl.find(pl.isnan(dadosc[:,5])==False),5]
at1 = dadosc[pl.find(pl.isnan(dadosc[:,6])==False),6]
pr1 = dadosc[pl.find(pl.isnan(dadosc[:,7])==False),7]
wt1 = dadosc[pl.find(pl.isnan(dadosc[:,8])==False),8]
hs1 = dadosc[pl.find(pl.isnan(dadosc[:,9])==False),9]
tp1 = dadosc[pl.find(pl.isnan(dadosc[:,10])==False),10]
dp1 = dadosc[pl.find(pl.isnan(dadosc[:,11])==False),11]

#dados sem consistencia
ws1b = dadosc[pl.find(pl.isnan(dados[:,3])==False),3]
wg1b = dadosc[pl.find(pl.isnan(dados[:,4])==False),4]
wd1b = dadosc[pl.find(pl.isnan(dados[:,5])==False),5]
at1b = dadosc[pl.find(pl.isnan(dados[:,6])==False),6]
pr1b = dadosc[pl.find(pl.isnan(dados[:,7])==False),7]
wt1b = dadosc[pl.find(pl.isnan(dados[:,8])==False),8]
hs1b = dadosc[pl.find(pl.isnan(dados[:,9])==False),9]
tp1b = dadosc[pl.find(pl.isnan(dados[:,10])==False),10]
dp1b = dadosc[pl.find(pl.isnan(dados[:,11])==False),11]

##########################################################################################
##########################################################################################

pl.figure()
lat0=-35
lat1=-5
lon0=-55
lon1=-30

map = Basemap(llcrnrlat=lat0,urcrnrlat=lat1,\
    llcrnrlon=lon0,urcrnrlon=lon1,\
    rsphere=(5378137.00,6356752.3142),\
    resolution='h',area_thresh=1000.,projection='cyl',\
    # lat_1=-35,lon_1=-35,lat_0=-5,lon_0=-50
    )

map.drawmeridians(np.arange(round(lon0),round(lon1),2),labels=[0,0,0,1],linewidth=0.3,fontsize=7)
map.drawparallels(np.arange(round(lat0),round(lat1),2),labels=[1,0,0,0],linewidth=0.3,fontsize=7)
map.fillcontinents(color='grey')
map.drawcoastlines(color='white',linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.drawstates(linewidth=0.2)

# pl.plot(dados[:,2],dados[:,1],'.b')
pl.plot(dadosc[:,2],dadosc[:,1],'or')

#faz isso para rodas os graficos, pois foi feito sem a latlon
# dados = dados[:,2:]
# dadosc = dadosc[:,2:]


##########################################################################################
##########################################################################################
#velocidade do vento - ws

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(ws1,i))

p50 = np.percentile(ws1,50) #percentil 90
p90 = np.percentile(ws1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Velocidade\ do\ Vento$')
pl.plot(datat,dados[:,3],'b.',datatc,dadosc[:,3],'r.')
pl.ylabel(r'$m/s$'), pl.ylim(-0.4,25), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(ws1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(ws1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(r'$m/s$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(r'$m/s$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/ws_' + local + '.png')

##########################################################################################
##########################################################################################
#velocidade de rajada do vento - wg

#calcula o percentil de 0 a 100
p = []
for i in range(100):
    p.append(np.percentile(wg1,i))

p50 = np.percentile(wg1,50) #percentil 90
p90 = np.percentile(wg1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Velocidade\ de\ Rajada$')
pl.plot(datat,dados[:,4],'b.',datatc,dadosc[:,4],'r.')
pl.ylabel(r'$m/s$'), pl.ylim(-0.4,25), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(wg1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(wg1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(r'$m/s$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(r'$m/s$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/wg_' + local + '.png')


##########################################################################################
##########################################################################################
#direcao do vento - wd

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(wd1,i))

p50 = np.percentile(wd1,50) #percentil 90
p90 = np.percentile(wd1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Direc\c{}\~ao\ do\ Vento$')
pl.plot(datat,dados[:,5],'b.',datatc,dadosc[:,5],'r.')
pl.yticks([0,45,90,135,180,225,270,315,360])
pl.ylabel(u'\u00b0'), pl.ylim(0,360), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(wd1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(wd1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(u'\u00b0'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(u'\u00b0'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/wd_' + local + '.png')


##########################################################################################
##########################################################################################
#temperatura do ar - at

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(at1,i))

p50 = np.percentile(at1,50) #percentil 90
p90 = np.percentile(at1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Temperatura\ do\ Ar$')
pl.plot(datat,dados[:,6],'b.',datatc,dadosc[:,6],'r.')
pl.ylabel(u'\u00b0 $C$'), pl.ylim(8,30), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(at1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(at1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(u'\u00b0 $C$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(u'\u00b0 $C$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/at_' + local + '.png')

###################################################################################
##########################################################################################
#pressao atmosferica - pr

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(pr1,i))

p50 = np.percentile(pr1,50) #percentil 90
p90 = np.percentile(pr1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Pressa\~o\ Atmosfe\'rica$')
pl.plot(datat,dados[:,7],'b.',datatc,dadosc[:,7],'r.')
pl.ylabel(r'$mBar$'), pl.ylim(985,1040), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(pr1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(pr1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(r'$mBar$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(r'$mBar$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/bp_' + local + '.png')


###################################################################################
##########################################################################################
#temperatura da agua - wt

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(wt1,i))

p50 = np.percentile(wt1,50) #percentil 90
p90 = np.percentile(wt1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Temperatura\ da\ A\'gua$')
pl.plot(datat,dados[:,8],'b.',datatc,dadosc[:,8],'r.')
pl.ylabel(u'\u00b0 $C$'), pl.ylim(8,35), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(wt1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(wt1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(u'\u00b0 $C$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(u'\u00b0 $C$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/wt_' + local + '.png')


###################################################################################
##########################################################################################
#altura significativa - hs

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(hs1,i))

p50 = np.percentile(hs1,50) #percentil 90
p90 = np.percentile(hs1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Altura\ significativa$')
pl.plot(datat,dados[:,9],'b.',datatc,dadosc[:,9],'r.')
pl.ylabel(r'$m$'), pl.ylim(0,8), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(hs1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(hs1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(r'$m$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(r'$m$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/hs_' + local + '.png')

##################################################################################
#########################################################################################
#periodo de pico - tp

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(tp1,i))

p50 = np.percentile(tp1,50) #percentil 90
p90 = np.percentile(tp1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r"$Periodo\ de\ Pico$")
pl.plot(datat,dados[:,10],'b.',datatc,dadosc[:,10],'r.')
pl.ylabel(r'$s$'), pl.ylim(2,26), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(tp1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(tp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(r'$s$'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(r'$s$'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/tp_' + local + '.png')


##################################################################################
#########################################################################################
#direcao de pico - dp

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(dp1,i))

p50 = np.percentile(dp1,50) #percentil 90
p90 = np.percentile(dp1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title(r'$Direc\c{}a\~o\ de\ Pico$')
pl.plot(datat,dados[:,11],'b.',datatc,dadosc[:,11],'r.')
pl.yticks([0,45,90,135,180,225,270,315,360])
pl.ylabel(u'\u00b0'), pl.ylim(0,360), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(dp1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(dp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
# l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f$' %(mu, sigma))
pl.xlabel(u'\u00b0'), pl.ylabel(r'$Probabilidade$')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel(u'\u00b0'), pl.ylabel(r'$Percentil$')

pl.savefig('fig/dp_' + local + '.png')


##########################################################################################
##########################################################################################
#altura e direcao
#rosa de distribuicao conjunta

#o periodo eh o menor vetor de onda (achar os indices de hs e dp referente ao tp)
#acha os valores de altura e direcao na periodo que nao tem nan
hs2 = dadosc[pl.find(isnan(dadosc[:,10])==False),9]
dp2 = dadosc[pl.find(isnan(dadosc[:,10])==False),11]
tp2 = tp1

# windrose
def new_axes():
    fig = plt.figure(figsize=(10, 8), dpi=80, frameon=False)
    rect = [0.1, 0.1, 0.6, 0.8]
    ax = WindroseAxes(fig, rect, axisbg='w')
    fig.add_axes(ax)
    return ax

def set_legend(ax):
    l = ax.legend(loc="center right",borderaxespad=-10.8)
    # l.get_frame().set_fill(False) #transparent legend
    plt.setp(l.get_texts(), fontsize=10,weight='bold')
    

#windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(dp2, hs2, normed=True, bins=7, opening=0.8, edgecolor='white',nsector=8)
ax.grid(True,linewidth=1.5,linestyle='dotted')
set_legend(ax)

plt.savefig('fig/rosa_hsdp_' + local + '.png', dpi=None, facecolor='w', edgecolor='w',
orientation='portrait', papertype=None, format='png',
transparent=False, bbox_inches=None, pad_inches=0.1)    
plt.close()


##########################################################################################
##########################################################################################
#periodo e direcao
#rosa de distribuicao conjunta


# windrose
def new_axes():
    fig = plt.figure(figsize=(10, 8), dpi=80, frameon=False)
    rect = [0.1, 0.1, 0.6, 0.8]
    ax = WindroseAxes(fig, rect, axisbg='w')
    fig.add_axes(ax)
    return ax

def set_legend(ax):
    l = ax.legend(loc="center right",borderaxespad=-10.8)
    # l.get_frame().set_fill(False) #transparent legend
    plt.setp(l.get_texts(), fontsize=10,weight='bold')
    

#windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(dp2, tp2, normed=True, bins=7, opening=0.8, edgecolor='white',nsector=8)
ax.grid(True,linewidth=1.5,linestyle='dotted')
set_legend(ax)
plt.savefig('fig/rosa_tpdp_' + local + '.png', dpi=None, facecolor='w', edgecolor='w',
orientation='portrait', papertype=None, format='png',
transparent=False, bbox_inches=None, pad_inches=0.1)    
plt.close()



##########################################################################################
##########################################################################################
#velocidade e direcao do vento
#rosa dos ventos

#acha os valores de velocidade idem as de direcao que nao tem nan
ws2 = dadosc[pl.find(isnan(dadosc[:,5])==False),3]
wd2 = wd1

# windrose
def new_axes():
    fig = plt.figure(figsize=(10, 8), dpi=80, frameon=False)
    rect = [0.1, 0.1, 0.6, 0.8]
    ax = WindroseAxes(fig, rect, axisbg='w')
    fig.add_axes(ax)
    return ax

def set_legend(ax):
    l = ax.legend(loc="center right",borderaxespad=-10.8)
    # l.get_frame().set_fill(False) #transparent legend
    plt.setp(l.get_texts(), fontsize=10,weight='bold')
    

#windrose like a stacked histogram with normed (displayed in percent) results
ax = new_axes()
ax.bar(wd2, ws2, normed=True, bins=7, opening=0.8, edgecolor='white',nsector=8)
ax.grid(True,linewidth=1.5,linestyle='dotted')
set_legend(ax)
plt.savefig('fig/rosa_vento' + local + '.png', dpi=None, facecolor='w', edgecolor='w',
orientation='portrait', papertype=None, format='png',
transparent=False, bbox_inches=None, pad_inches=0.1)    
plt.close()


##########################################################################################
##########################################################################################
#relacao onda/vento

aux = np.where((np.isnan(dadosc[:,3])==False) & (np.isnan(dadosc[:,9])==False))[0]


pl.figure()
poly_params = np.polyfit(dadosc[aux,3],dadosc[aux,9], 2)    # Fit the data with a 3rd degree polynomial
poly_3 = np.poly1d(poly_params)      # Construct the polynomial
xPoly = dadosc[aux,3]  # Generate 100 x-coordinates from 0 to max(x)
yPoly = poly_3(xPoly)
pl.plot(dadosc[aux,3],dadosc[aux,9], 'b.',np.sort(xPoly),np.sort(yPoly), '-r',linewidth=4)
pl.xlim(0,18); pl.ylim(0,8)
pl.xlabel(r'$Velocidade\ do\ Vento\ (m/s)$')
pl.ylabel(r'$Altura\ Significativa\ (m)$')
pl.grid()


pl.show()
