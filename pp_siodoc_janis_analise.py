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

reload(consiste_proc)
reload(windrose)

pl.close('all')

local = 'arraial_cabo'

print 'Iniciando analise em... ' + local

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#  0  1   2  3  4  5  6  7  8  9 10
#date,ws,wg,wd,at,rh,pr,wt,hs,tp,dp
dados = np.loadtxt(pathname + 'siodoc_janis_' + local + '.out',delimiter=',') #dados sem cq
dadosc = np.loadtxt(pathname + 'siodoc_janis_cq_' + local + '.out',delimiter=',') #dados sem cq

#converte datas para datetime
datat = np.array([datetime.strptime(str(int(dados[i,0])), '%Y%m%d%H%M') for i in range(len(dados))])

#cria nomes com variaveis consistentes
ws1 = dadosc[pl.find(pl.isnan(dadosc[:,1])==False),1]
wg1 = dadosc[pl.find(pl.isnan(dadosc[:,2])==False),2]
wd1 = dadosc[pl.find(pl.isnan(dadosc[:,3])==False),3]
at1 = dadosc[pl.find(pl.isnan(dadosc[:,4])==False),4]
pr1 = dadosc[pl.find(pl.isnan(dadosc[:,5])==False),5]
wt1 = dadosc[pl.find(pl.isnan(dadosc[:,6])==False),6]
hs1 = dadosc[pl.find(pl.isnan(dadosc[:,7])==False),7]
tp1 = dadosc[pl.find(pl.isnan(dadosc[:,8])==False),8]
dp1 = dadosc[pl.find(pl.isnan(dadosc[:,9])==False),9]


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
pl.title('Velocidade do vento')
pl.plot(datat,dados[:,1],'b.',datat,dadosc[:,1],'r.')
pl.ylabel('m/s'), pl.ylim(0,25), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(ws1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(ws1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('m/s'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('m/s'), pl.ylabel('Percentil')

pl.savefig('fig/ws_' + local + '.png')


##########################################################################################
##########################################################################################
#velocidade de rajada vento - wg

#calcula o percentil de 0 a 100
p = []
for i in range(100):
	p.append(np.percentile(wg1,i))

p50 = np.percentile(wg1,50) #percentil 90
p90 = np.percentile(wg1,90) #percentil 90

pl.figure(figsize=(13,8)) #lxh
pl.subplot(211)
pl.title('Velocidade de rajada do vento')
pl.plot(datat,dados[:,2],'b.',datat,dadosc[:,2],'r.')
pl.ylabel('m/s'), pl.ylim(0,25), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(wg1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(wg1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('m/s'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('m/s'), pl.ylabel('Percentil')

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
pl.title('Direcao do vento')
pl.plot(datat,dados[:,3],'b.',datat,dadosc[:,3],'r.')
pl.ylabel('graus'), pl.ylim(0,360), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(wd1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(wd1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('graus'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('graus'), pl.ylabel('Percentil')

pl.savefig('fig/wd_' + local + '.png')


##########################################################################################
##########################################################################################
#velocidade e direcao do vento
#rosa dos ventos

#acha os valores de velocidade idem as de direcao que nao tem nan
ws2 = dadosc[pl.find(isnan(dadosc[:,3])==False),1]
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
plt.savefig('fig/windrose_' + local + '.png', dpi=None, facecolor='w', edgecolor='w',
orientation='portrait', papertype=None, format='png',
transparent=False, bbox_inches=None, pad_inches=0.1)    
plt.close()


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
pl.title('Temperatura do ar')
pl.plot(datat,dados[:,4],'b.',datat,dadosc[:,4],'r.')
pl.ylabel('graus C'), pl.ylim(8,30), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(at1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(at1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('graus C'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('graus C'), pl.ylabel('Percentil')

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
pl.title('Pressao atmosferica')
pl.plot(datat,dados[:,5],'b.',datat,dadosc[:,5],'r.')
pl.ylabel('mBar'), pl.ylim(985,1040), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(pr1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(pr1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('mBar'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('mBar'), pl.ylabel('Percentil')

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
pl.title('Temperatura da agua')
pl.plot(datat,dados[:,6],'b.',datat,dadosc[:,6],'r.')
pl.ylabel('graus C'), pl.ylim(8,35), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(wt1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(wt1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('graus C'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('graus C'), pl.ylabel('Percentil')

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
pl.title('Altura significativa')
pl.plot(datat,dados[:,7],'b.',datat,dadosc[:,7],'r.')
pl.ylabel('metros'), pl.ylim(0,8), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(hs1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(hs1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('metros'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('metros'), pl.ylabel('Percentil')

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
pl.title('Periodo de pico')
pl.plot(datat,dados[:,8],'b.',datat,dadosc[:,8],'r.')
pl.ylabel('segundos'), pl.ylim(2,26), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(tp1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(tp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('segundos'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('segundos'), pl.ylabel('Percentil')

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
pl.title('Direcao de pico')
pl.plot(datat,dados[:,9],'b.',datat,dadosc[:,9],'r.')
pl.ylabel('graus'), pl.ylim(0,360), pl.grid()

pl.subplot(223)
(mu, sigma) = norm.fit(dp1) #ajusta a melhor curva para os dados #media e despad?
n, bins, patches = pl.hist(dp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--',linewidth=3)
pl.title(r'$\mathrm{}\ \mu=%.2f,\ \sigma=%.2f,$' %(mu, sigma))
pl.xlabel('graus'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()

pl.subplot(224)
pl.plot(p,range(100),'bo-',linewidth=2)
pl.plot(p,np.linspace(90,90,100),'r--',linewidth=2)
pl.plot(p,np.linspace(50,50,100),'r--',linewidth=2)
pl.title(r'$\mathrm{} P50=%.2f, \ \ P90=%.2f$' %(p50, p90))
pl.axis('tight'), pl.ylim(0,100), pl.grid()
pl.xlabel('graus'), pl.ylabel('Percentil')

pl.savefig('fig/dp_' + local + '.png')


##########################################################################################
##########################################################################################
#altura e periodo
#rosa de distribuicao conjunta

#o periodo eh o menor vetor de onda (achar os indices de hs e dp referente ao tp)
#acha os valores de altura e periodo na direcoes que nao tem nan
hs2 = dadosc[pl.find(isnan(dadosc[:,8])==False),7]
dp2 = dadosc[pl.find(isnan(dadosc[:,8])==False),9]
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
plt.savefig('fig/conj_hsdp_' + local + '.png', dpi=None, facecolor='w', edgecolor='w',
orientation='portrait', papertype=None, format='png',
transparent=False, bbox_inches=None, pad_inches=0.1)    
plt.close()


##########################################################################################
##########################################################################################
#altura e periodo
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
plt.savefig('fig/conj_tpdp_' + local + '.png', dpi=None, facecolor='w', edgecolor='w',
orientation='portrait', papertype=None, format='png',
transparent=False, bbox_inches=None, pad_inches=0.1)    
plt.close()


pl.show()
