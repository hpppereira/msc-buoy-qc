'''
calcula parametros de onda (hs e hm0) em funcao
da quantidade e duracao da perturbacao

para a perturbacao na serie, serao colocados valores nulos
'''

import numpy as np
import pylab as pl
import scipy as sp
import os
import copy as cp

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

import proconda
import espec

reload(proconda)

pl.close('all')

#Hs=6,2, Tp= , Dp=130 - Onda com maior Hs
dados = np.loadtxt(os.environ['HOME'] + '/Dropbox/lioc/dados/pnboia/triaxys/rio_grande/HNE/200912130600.HNE',
	    skiprows = 11)

t = dados[:,0] - dados[0,0]
eta = dados[:,1]


# ------------------------------------------------- #
#calcula parametros de onda para a serie normal
#param =  [Hs,H10,Hmax,Tmed,THmax]

#parametros de onda no tempo
etat = proconda.ondat(t,eta,200)

#parametros de onda na frequencia
etaf = espec.espec1(eta,328,1.28)
hm0 = 4.01 * sp.sqrt(sum(etaf[:,1]) * (etaf[0,0]))

# ------------------------------------------------- #

#cria serie perturbada
etap = cp.copy(eta)
#etap1 = cp.copy(eta)

#numero de perturbacoes
npt = 50

#duracao da perturbacao
dpt = 50

#posicoes aleatorias das perturbacoes
#*verificar se a a quantidade e numero de perturbacoes nao ultrapassa 1024 pontos (por isso 900)
pos = sp.rand(npt) * 900
pos = [int(pos[i]) for i in range(len(pos))]


#matriz com parametros calculados (tempo e frequencia)
#lin=duracao da perturb ; col=num de perturb
paramt = np.zeros((dpt,npt))
paramf = np.zeros((dpt,npt))

# ------------------------------------------------- #
#gera perturbacoes e calcula os parametros

#indices das perturbacoes
a = []

etap1 = []
etafp1 = []
hm01 = []
#varia o numero de perturbacoes
for j in range(npt):

	#posicoes das perturbacoes
	a.append(pos[j])

	#retorna o eta ao valor normal
	etap = cp.copy(eta)

	for i in range(dpt):

		#gera perturacoes
		#etap[pa[j]+i] = 0
		etap[np.array(a)+i] = 0

		#Hs
		etatp = proconda.ondat(t,etap,200)
		paramt[i,j] = etatp[0]

		#Hm0
		etafp = espec.espec1(etap,328,1.28)
		paramf[i,j] = 4.01 * sp.sqrt(sum(etafp[:,1]) * (etafp[0,0]))

		#pl.figure()
		#pl.plot(etap)
		#pl.show()
	etap1.append(etap)
	etafp1.append(etafp[:,1])
	hm01.append(4.01 * np.sqrt(sum(etafp[:,1]) * etafp[0,0]))

etap1 = np.array(etap1)
etafp1 = np.array(etafp1)

# ------------------------------------------------- #

#series temporais e espectro

pl.figure()
pl.subplot(211)
pl.plot(eta)
pl.title('Elevacao - consistente')
pl.xlabel('Tempo (s)')
pl.ylabel('metros')
pl.axis('tight')
pl.subplot(212)
pl.plot(etaf[:,0],etaf[:,1])
pl.xlabel('Frequencia (Hz)')
pl.ylabel('m^2/Hz')
pl.axis('tight')
# pl.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/seriespec_etac.png')


pl.figure()
pl.subplot(211)
pl.plot(etap)
pl.title('Elevacao - perturbada')
pl.xlabel('Tempo (s)')
pl.ylabel('metros')
pl.axis('tight')
pl.subplot(212)
pl.plot(etafp[:,0],etafp[:,1])
pl.xlabel('Frequencia (Hz)')
pl.ylabel('m^2/Hz')
pl.axis('tight')
# pl.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/seriespec_etap.png')


# ------------------------------------------------- #

#grafico 3d

x = range(npt)
y = range(dpt)
X, Y = np.meshgrid(x, y)

fig = pl.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, paramf, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.hold(True)
#ax.plot(X,Y,hm0 - (np.ones(50) * hm0 * 0.1), k--)
ax.view_init(15,45)
#ax.set_title('Variacao de Hm0 para quantidade e duracao de perturbacoes')
ax.set_xlabel(r'$Quantidade$')
ax.set_ylabel(r'$Durac\c{}a\~o\ (s)$')
ax.set_zlabel(r'$Hm0\ (m)$')
# pl.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/perturb_hm0_3d.png')


#plotagem dos limites por perturbacao

limeta = [hm0 - (hm0 * 0.2) for i in range(dpt)]

pl.figure()
pl.subplot(211)
pl.title('Altura Significativa (Hm0)')
pl.plot(paramf[:,range(0,50,10)])
pl.legend(('1','10','20','30','40','50'))
pl.plot(range(dpt),limeta,'k--')
pl.xlabel('Duracao da perturbacao')
pl.ylabel('metros')
pl.subplot(212)
pl.plot(paramf.T[:,range(0,50,10)])
pl.legend(('1','10','20','30','40','50'))
pl.plot(range(dpt),limeta,'k--')
pl.xlabel('Quantidade de perturbacoes')
pl.ylabel('m')
# pl.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/perturb_hm0.png')


pl.figure()
pl.subplot(4,2,1)
pl.plot(t,eta)
pl.ylim(-5.5,5.5)
pl.ylabel('m')
pl.axis('tight')
pl.subplot(4,2,2)
pl.plot(etaf[:,0],etaf[:,1])
pl.xlim(0,0.4)
pl.text(0.25,120,'Hm0 = %.1f m' %(hm0))
pl.ylabel(r'$m^{2}/Hz$')


pl.subplot(4,2,3)
pl.plot(t,etap1[3,:])
pl.ylim(-5.5,5.5)
pl.ylabel('m')
pl.axis('tight')
pl.subplot(4,2,4)
pl.plot(etaf[:,0],etafp1[3,:])
pl.xlim(0,0.4)
pl.text(0.25,100,'Hm0 = %.1f m' %(hm01[3]))
pl.ylabel(r'$m^{2}/Hz$')


pl.subplot(4,2,5)
pl.plot(t,etap1[10,:])
pl.ylim(-5.5,5.5)
pl.ylabel('m')
pl.axis('tight')
pl.subplot(4,2,6)
pl.plot(etaf[:,0],etafp1[10,:])
pl.xlim(0,0.4)
pl.text(0.25,50,'Hm0 = %.1f m' %(hm01[10]))
pl.ylabel(r'$m^{2}/Hz$')


pl.subplot(4,2,7)
pl.plot(t,etap1[49,:])
pl.ylim(-5.5,5.5)
pl.ylabel('m')
pl.xlabel('Tempo (s)')
pl.axis('tight')
pl.subplot(4,2,8)
pl.plot(etaf[:,0],etafp1[49,:])
pl.xlim(0,0.4)
pl.xlabel('Freq. (Hz)')
pl.text(0.25,30,'Hm0 = %.1f m' %(hm01[49]))
pl.ylabel(r'$m^{2}/Hz$')


pl.show()
