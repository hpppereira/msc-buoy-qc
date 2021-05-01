# -*- coding: utf-8 -*-
'''
Comparacao das 4 boias
** Faz graficos 2x2 com as 4 boias
Analise dos dados brutos e processados
com controle de qualidade dos dados
baixados pelo opendap do site do goos/brasil
- saltambiental

dados - dados sem constrole de qualidade
dados_cq - dados com controle de qualidade

formato:
#   0     1   2   3   4   5   6  7   8   9 
# datai, ws, wg, wd, at, pr, wt, hs, tp, dp

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

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#  0  1   2  3  4  5  6  7  8  9
#date,ws,wg,wd,at,pr,wt,hs,tp,dp
re = np.loadtxt(pathname + 'argos_opendap_cq_recife.out',delimiter=',') 
sa = np.loadtxt(pathname + 'argos_opendap_cq_santos.out',delimiter=',') 
fl = np.loadtxt(pathname + 'argos_opendap_cq_florianopolis.out',delimiter=',') 
rg = np.loadtxt(pathname + 'argos_opendap_cq_rio_grande.out',delimiter=',') 

#datas
dre = np.array([datetime.strptime(str(int(re[i,0])), '%Y%m%d%H%M') for i in range(len(re))])
dsa = np.array([datetime.strptime(str(int(sa[i,0])), '%Y%m%d%H%M') for i in range(len(sa))])
dfl = np.array([datetime.strptime(str(int(fl[i,0])), '%Y%m%d%H%M') for i in range(len(fl))])
drg = np.array([datetime.strptime(str(int(rg[i,0])), '%Y%m%d%H%M') for i in range(len(rg))])

#consistencia visual
re[1995:6995,1:] = np.nan ; re[11411:15932,1:] = np.nan
fl[2352:4118,1:] = np.nan #florianopolis


# #  0  1   2  3  4  5  6  7  8  9
# #date,ws,wg,wd,at,pr,wt,hs,tp,dp
# dados = np.loadtxt(pathname + 'argos_opendap_' + local + '.out',delimiter=',') #dados sem cq
# dadosc = np.loadtxt(pathname + 'argos_opendap_cq_' + local + '.out',delimiter=',') #dados sem cq

# #converte datas para datetime
# datat = np.array([datetime.strptime(str(int(dados[i,0])), '%Y%m%d%H%M') for i in range(len(dados))])

# #cria nomes com variaveis consistentes
# ws1 = dadosc[pl.find(pl.isnan(dadosc[:,1])==False),1]
# wg1 = dadosc[pl.find(pl.isnan(dadosc[:,2])==False),2]
# wd1 = dadosc[pl.find(pl.isnan(dadosc[:,3])==False),3]
# at1 = dadosc[pl.find(pl.isnan(dadosc[:,4])==False),4]
# pr1 = dadosc[pl.find(pl.isnan(dadosc[:,5])==False),5]
# wt1 = dadosc[pl.find(pl.isnan(dadosc[:,6])==False),6]
# hs1 = dadosc[pl.find(pl.isnan(dadosc[:,7])==False),7]
# tp1 = dadosc[pl.find(pl.isnan(dadosc[:,8])==False),8]
# dp1 = dadosc[pl.find(pl.isnan(dadosc[:,9])==False),9]


##########################################################################################
##########################################################################################
#1 - velocidade e rajada do vento - ws

#recife

pl.figure(figsize=(13,10)) #lxh

#retira os nan
ws1 = np.diff(re[pl.find(pl.isnan(re[:,1])==False),1])
wg1 = np.diff(re[pl.find(pl.isnan(re[:,2])==False),2])

p90ws = np.percentile(ws1,90) #percentil 90
p90wg = np.percentile(wg1,90) #percentil 90

pl.subplot(221)

(mu, sigma) = norm.fit(ws1) #media e dp vel
(mu1, sigma1) = norm.fit(wg1) #med e dp rajada

n, bins, patches = pl.hist(ws1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wg1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Recife\ -\ Vel: \mu=%.1f,\ \sigma=%.1f / Raj: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.xlim(0,25), pl.grid()

#santos

#retira os nan
ws1 = np.diff(sa[pl.find(pl.isnan(sa[:,1])==False),1])
wg1 = np.diff(sa[pl.find(pl.isnan(sa[:,2])==False),2])

p90ws = np.percentile(ws1,90) #percentil 90
p90wg = np.percentile(wg1,90) #percentil 90

pl.subplot(222)

(mu, sigma) = norm.fit(ws1) #media e dp vel
(mu1, sigma1) = norm.fit(wg1) #med e dp rajada

n, bins, patches = pl.hist(ws1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wg1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Santos\ -\ Vel: \mu=%.1f,\ \sigma=%.1f / Raj: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.axis('tight'), pl.xlim(0,25), pl.grid(),
pl.legend(['Vel. Vento','Raj. Vento'])

#florianopolis

#retira os nan
ws1 = np.diff(fl[pl.find(pl.isnan(fl[:,1])==False),1])
wg1 = np.diff(fl[pl.find(pl.isnan(fl[:,2])==False),2])

p90ws = np.percentile(ws1,90) #percentil 90
p90wg = np.percentile(wg1,90) #percentil 90

pl.subplot(223)

(mu, sigma) = norm.fit(ws1) #media e dp vel
(mu1, sigma1) = norm.fit(wg1) #med e dp rajada

n, bins, patches = pl.hist(ws1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wg1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Florianopolis\ -\ Vel: \mu=%.1f,\ \sigma=%.1f / Raj: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.xlabel('m/s'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.xlim(0,25), pl.grid(),


#rio grande

#retira os nan
ws1 = np.diff(rg[pl.find(pl.isnan(rg[:,1])==False),1])
wg1 = np.diff(rg[pl.find(pl.isnan(rg[:,2])==False),2])

p90ws = np.percentile(ws1,90) #percentil 90
p90wg = np.percentile(wg1,90) #percentil 90

pl.subplot(224)

(mu, sigma) = norm.fit(ws1) #media e dp vel
(mu1, sigma1) = norm.fit(wg1) #med e dp rajada

n, bins, patches = pl.hist(ws1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wg1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Rio\ Grande\ -\ Vel: \mu=%.1f,\ \sigma=%.1f / Raj: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.xlabel('m/s')
pl.axis('tight'), pl.xlim(0,25), pl.grid()

pl.savefig('fig/hist_wswg.png')

##########################################################################################
##########################################################################################
#2 - temperatura do ar e da agua

#recife

pl.figure(figsize=(13,10)) #lxh

#retira os nan
at1 = np.diff(re[pl.find(pl.isnan(re[:,4])==False),4])
wt1 = np.diff(re[pl.find(pl.isnan(re[:,6])==False),6])

p90at = np.percentile(at1,90) #percentil 90
p90wt = np.percentile(wt1,90) #percentil 90

pl.subplot(221)

(mu, sigma) = norm.fit(at1) #media e dp vel
(mu1, sigma1) = norm.fit(wt1) #med e dp rajada

n, bins, patches = pl.hist(at1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wt1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Recife\ -\ Ar: \mu=%.1f,\ \sigma=%.1f / Agua: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(5,35)

#santos

#retira os nan
at1 = np.diff(sa[pl.find(pl.isnan(sa[:,4])==False),4])
wt1 = np.diff(sa[pl.find(pl.isnan(sa[:,6])==False),6])

p90ws = np.percentile(at1,90) #percentil 90
p90wg = np.percentile(wt1,90) #percentil 90

pl.subplot(222)

(mu, sigma) = norm.fit(at1) #media e dp vel
(mu1, sigma1) = norm.fit(wt1) #med e dp rajada

n, bins, patches = pl.hist(at1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wt1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Santos\ -\ Ar: \mu=%.1f,\ \sigma=%.1f / Agua: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.axis('tight'), pl.grid()
pl.xlim(5,35)

pl.legend(['Temp. Ar','Temp. Agua'],loc=0)

#florianopolis

#retira os nan
at1 = np.diff(fl[pl.find(pl.isnan(fl[:,4])==False),4])
wt1 = np.diff(fl[pl.find(pl.isnan(fl[:,6])==False),6])

p90ws = np.percentile(at1,90) #percentil 90
p90wg = np.percentile(wt1,90) #percentil 90

pl.subplot(223)

(mu, sigma) = norm.fit(at1) #media e dp vel
(mu1, sigma1) = norm.fit(wt1) #med e dp rajada

n, bins, patches = pl.hist(at1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wt1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Florianopolis\ -\ Ar: \mu=%.1f,\ \sigma=%.1f / Agua: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.xlabel('graus C'), pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(5,35)


#rio grande

#retira os nan
at1 = np.diff(rg[pl.find(pl.isnan(rg[:,4])==False),4])
wt1 = np.diff(rg[pl.find(pl.isnan(rg[:,6])==False),6])

p90ws = np.percentile(at1,90) #percentil 90
p90wg = np.percentile(wt1,90) #percentil 90

pl.subplot(224)

(mu, sigma) = norm.fit(at1) #media e dp vel
(mu1, sigma1) = norm.fit(wt1) #med e dp rajada

n, bins, patches = pl.hist(at1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

n, bins, patches = pl.hist(wt1,25,normed=1,facecolor='red',alpha=0.75)
y = mlab.normpdf( bins, mu1, sigma1)
l = pl.plot(bins, y, 'r--',linewidth=3)

pl.title(r'$\mathrm{}\ Rio\ Grande\ -\ Ar: \mu=%.1f,\ \sigma=%.1f / Agua: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma, mu1, sigma1))
pl.xlabel('graus C')
pl.axis('tight'), pl.grid()
pl.xlim(5,35)

pl.savefig('fig/hist_atwt.png')

##########################################################################################
##########################################################################################
#3 - pressao atmosferica

#recife

pl.figure(figsize=(13,10)) #lxh

#retira os nan
pr1 = np.diff(re[pl.find(pl.isnan(re[:,5])==False),5])

p90pr = np.percentile(pr1,90) #percentil 90

pl.subplot(221)

(mu, sigma) = norm.fit(pr1) #media e dp vel

n, bins, patches = pl.hist(pr1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Recife\ -\ Pressao\ atm.: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(990,1035)

#santos

#retira os nan
pr1 = np.diff(sa[pl.find(pl.isnan(sa[:,5])==False),5])

p90pr = np.percentile(pr1,90) #percentil 90

pl.subplot(222)

(mu, sigma) = norm.fit(pr1) #media e dp vel

n, bins, patches = pl.hist(pr1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Santos\ -\ Pressao\ atm.: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(990,1035)

#florianopolis

#retira os nan
pr1 = np.diff(fl[pl.find(pl.isnan(fl[:,5])==False),5])

p90pr = np.percentile(pr1,90) #percentil 90

pl.subplot(223)

(mu, sigma) = norm.fit(pr1) #media e dp vel

n, bins, patches = pl.hist(pr1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Florianopolis\ -\ Pressao\ atm.: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlabel('hPa')
pl.xlim(990,1035)


#rio grande

#retira os nan
pr1 = np.diff(rg[pl.find(pl.isnan(rg[:,5])==False),5])

p90pr = np.percentile(pr1,90) #percentil 90

pl.subplot(224)

(mu, sigma) = norm.fit(pr1) #media e dp vel

n, bins, patches = pl.hist(pr1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Rio\ Grande\ -\ Pressao\ atm.: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.axis('tight'), pl.grid()
pl.xlim(990,1035)
pl.xlabel('hPa')

pl.savefig('fig/hist_bp.png')

##########################################################################################
##########################################################################################
#4 - Altura sig

pl.figure(figsize=(13,10)) #lxh

#recife

#retira os nan
hs1 = np.diff(re[pl.find(pl.isnan(re[:,7])==False),7])

p90hs = np.percentile(hs1,90) #percentil 90

pl.subplot(221)

(mu, sigma) = norm.fit(hs1) #media e dp vel

n, bins, patches = pl.hist(hs1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Recife\ -\ Hs: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(0.25,6)

#santos

#retira os nan
hs1 = np.diff(sa[pl.find(pl.isnan(sa[:,7])==False),7])

p90hs = np.percentile(hs1,90) #percentil 90

pl.subplot(222)

(mu, sigma) = norm.fit(hs1) #media e dp vel

n, bins, patches = pl.hist(hs1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Santos\ -\ Hs: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(0.25,6)

#florianopolis

#retira os nan
hs1 = np.diff(fl[pl.find(pl.isnan(fl[:,7])==False),7])

p90hs = np.percentile(hs1,90) #percentil 90

pl.subplot(223)

(mu, sigma) = norm.fit(hs1) #media e dp vel

n, bins, patches = pl.hist(hs1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Florianopolis\ -\ Hs: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlabel('metros')
pl.xlim(0.25,6)

#rio grande

#retira os nan
hs1 = np.diff(rg[pl.find(pl.isnan(rg[:,7])==False),7])

p90hs = np.percentile(hs1,90) #percentil 90

pl.subplot(224)

(mu, sigma) = norm.fit(hs1) #media e dp vel

n, bins, patches = pl.hist(hs1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Rio\ Grande\ -\ Hs: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
# pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlabel('metros')
pl.xlim(0.25,6)

pl.savefig('fig/hist_hs.png')

##########################################################################################
##########################################################################################
#5 - Periodo de pico

pl.figure(figsize=(13,10)) #lxh

#recife

#retira os nan
tp1 = np.diff(re[pl.find(pl.isnan(re[:,8])==False),8])

p90tp = np.percentile(tp1,90) #percentil 90

pl.subplot(221)

(mu, sigma) = norm.fit(tp1) #media e dp vel

n, bins, patches = pl.hist(tp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Recife\ -\ Tp: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(3,22)

#santos

#retira os nan
tp1 = np.diff(sa[pl.find(pl.isnan(sa[:,8])==False),8])

p90tp = np.percentile(tp1,90) #percentil 90

pl.subplot(222)

(mu, sigma) = norm.fit(tp1) #media e dp vel

n, bins, patches = pl.hist(tp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Santos\ -\ Tp: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.axis('tight'), pl.grid()
pl.xlim(3,22)

#florianopolis

#retira os nan
tp1 = np.diff(fl[pl.find(pl.isnan(fl[:,8])==False),8])

p90tp = np.percentile(tp1,90) #percentil 90

pl.subplot(223)

(mu, sigma) = norm.fit(tp1) #media e dp vel

n, bins, patches = pl.hist(tp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Florianopolis\ -\ Tp: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.ylabel('Probabilidade')
pl.axis('tight'), pl.grid()
pl.xlim(3,22)
pl.xlabel('segundos')

#rio grande

#retira os nan
tp1 = np.diff(rg[pl.find(pl.isnan(rg[:,8])==False),8])

p90tp = np.percentile(tp1,90) #percentil 90

pl.subplot(224)

(mu, sigma) = norm.fit(tp1) #media e dp vel

n, bins, patches = pl.hist(tp1,25,normed=1,facecolor='green',alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'g--',linewidth=3)

pl.title(r'$\mathrm{}\ Rio Grande\ -\ Tp: \mu=%.1f,\ \sigma=%.1f$' %(mu, sigma))
pl.axis('tight'), pl.grid()
pl.xlim(3,22)
pl.xlabel('segundos')






pl.show()