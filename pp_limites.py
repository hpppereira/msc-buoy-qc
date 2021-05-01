# -*- coding: utf-8 -*-
'''
Programa principal para criar limites de perturbacoes

Henrique P. P. Pereira
LIOc-COPPE/UFRJ

-- Descricao -- 
Carrega variavel de elevacao
1 - Limite de spike
2 - Limite de variabilidade temporal

Serites avaliadas:
1 - Heave simulada (geraonda.m)
2 - Heave BMOs PNBOIA

Ultima modificacao: 21/01/2015
'''

import numpy as np
import pylab as pl
import os
import glob
import crialimites

reload(crialimites)

# pl.close('all')

#======================================================================#
## Carrega dados

# -------------------------------------------------------------------- #

#parametros para as figuras
fontsizefig = 18

#diretorio de ondas estao os dados

#simulados
#pathname = os.environ['HOME'] + '/Dropbox/tese/cq/dados/simulados/geraonda/'

#boias
local1 = 'rio_grande'
local2 = 'florianopolis'
local3 = 'santos'
local4 = 'recife'

# -------------------------------------------------------------------- #

pathname1 = os.environ['HOME'] + '/Documents/pnboia/' + local1 + '/hne_' + local1 + '/'
pathname2 = os.environ['HOME'] + '/Documents/pnboia/' + local2 + '/hne_' + local2 + '/'
pathname3 = os.environ['HOME'] + '/Documents/pnboia/' + local3 + '/hne_' + local3 + '/'
pathname4 = os.environ['HOME'] + '/Documents/pnboia/' + local4 + '/hne_' + local4 + '/'

# -------------------------------------------------------------------- #
## Simulados

for loc in range(1,5):

	pathname = eval('pathname' + str(loc))

	lista = []

	# Lista arquivos do diretorio atual
	for f in os.listdir(pathname):
	    if f.endswith('.HNE'):
	        lista.append(f)
	lista=np.array(sorted(lista))

	#arquivo inicial e final a serem processados
	arqp = np.arange(len(lista))

	eta = np.zeros((1024,arqp.shape[0]))

	cont = -1 #contador da variavel eta
	for j in arqp:

		cont += 1

		#diretorio com arquivo de dados
		arqdir = pathname + lista[j]

		print str(arqdir) + ' -- ' + str(cont)

		dados = np.loadtxt(arqdir,skiprows=10,usecols=([1]))

		if len(dados) > 1024:

			#matriz com cada serie de elevacao
			eta[:,cont] = dados[0:len(eta)]

		else:

			print '### Valor inconsistente - Comprimento do vetor < 1024 pontos ###'

	print 'Numero de Arquivos Processados: ' + str(eta.shape[1])

	#chama subrotinas para criar limite de spike (Meta=Multiplicador do desvio padrao e Leta=limite para spike
	Meta, Leta = crialimites.limspike(eta)

	#calcula limite de range (Lr)
	lim_faixa_inf, lim_faixa_sup = crialimites.limrange(eta)

	#salva variaveis
	if loc == 1:
		Meta1 = Meta
		Leta1 = Leta
	elif loc == 2:
		Meta2 = Meta
		Leta2 = Leta
	elif loc == 3:
		Meta3 = Meta
		Leta3 = Leta
	elif loc == 4:
		Meta4 = Meta
		Leta4 = Leta

#Figuras

pl.figure()
pl.subplot(221)
pl.hist(Meta1[pl.find(pl.isnan(Meta1)==False)],200,color='b',label=local1)
pl.axis([-5,5,0,1400000])
# pl.xlabel('M',fontsize=fontsizelabel)
pl.ylabel('Num. Ocorrências',fontsize=fontsizefig)
pl.legend()
pl.subplot(222)
pl.hist(Meta2[pl.find(pl.isnan(Meta2)==False)],200,color='r',label=local2)
pl.axis([-5,5,0,950000])
# pl.xlabel('M',fontsize=fontsizefig)
pl.legend()
pl.subplot(223)
pl.hist(Meta3[pl.find(pl.isnan(Meta3)==False)],200,color='g',label=local3)
pl.axis([-5,5,0,950000])
pl.xlabel('M',fontsize=fontsizefig)
pl.ylabel('Num. Ocorrencias',fontsize=fontsizefig)
pl.legend()
pl.subplot(224)
pl.hist(Meta4[pl.find(pl.isnan(Meta4)==False)],200,color='y',label=local4)
pl.axis([-5,5,0,1100000])
pl.xlabel('M',fontsize=fontsizefig)
pl.legend()
pl.suptitle('Multiplicador do Desvio Padrao para serie de Heave',fontsize=fontsizefig)

# pl.figure()
# pl.hist(Leta,100)
# pl.title('Limite para elevacao (M * std)')
# pl.xlabel('M * std(eta)')
# pl.ylabel('N ocorrencias')
# pl.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/lim_eta.png')

pl.show()
