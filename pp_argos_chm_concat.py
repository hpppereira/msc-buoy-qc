'''
Carrega e processa os dados meteorologicos
do PNBOIA baixados do cartao de memoria
Os dados foram cedidos peo CHM

Os arquivos estao em .xls

Dados cedidos pelo PNBOIA


# Cabecalho WKB (teorico)

# col 0 - sensor x Platform ID
# col 1  - sensor x- Longitude
# col 2 - sensor x - Latitude
# col 3 - sensor x - Loc. quality
# col 4 - sensor x - Msg Date
# col 5 - sensor x - Loc. idx
# col 6 - sensor x - Msg
# col 7 - sensor 0 - ???
# col 8 - sensor 1 - ???
# col 9 - sensor 2 - wind speed 1
# col 10 - sensor 3 - wind gust 1
# col 11 - sensor 4 - wind dir 1
# col 12 - sensor 5 - air temp
# col 13 - sensor 6 - relative humidity
# col 14 - sensor 7 - dew point
# col 15 - sensor 8 - pressure
# col 16 - sensor 9 - sst
# col 17 - sensor 10 - buoy heading
# col 18 - sensor 11 - clorofila
# col 19 - sensor 12 - turbidez
# col 20 - sensor 13 - solar rad
# col 21 - sensor 14 - CM velocity 1
# col 22 - sensor 15 - CM direction 1
# col 23 - sensor 16 - CM velocity 2
# col 24 - sensor 17 - CM direction 2
# col 25 - sensor 18 - CM velocity 3
# col 26 - sensor 19 - CM direction 3
# col 27 - sensor 20 - Hs
# col 28 - sensor 21 - Hmax
# col 29 - sensor 22 - Periodo
# col 30 - sensor 23 - Mn dir
# col 31 - sensor 24 - spread
# col 32 - sensor 25 - spare ???
# col 33 - sensor 26 - ???
# col 34 - sensor 27 - ???
# col 35 - sensor 28 - ???
# col 36 - sensor 29 - ???
# col 37 - sensor 30 - ???
# col 38 - sensor 31 - ???
# col 39 - sensor 32 - ???

#matriz de saida

col:   0  1   2  3  4  5  6  7  8 9  10 11 12 13 14 15 16 17
var: date ws wg wd at rh dw pr st bh cl tu sr hs hm tp dp sp

'''

import numpy as np
import pylab as pl
import os
from datetime import datetime
import xlrd
import string


pl.close('all')

# ================================================== #
def lista_xls(pathname):

	''' Lista arquivos com extensao .HNE 
	que estao dentro do diretorio 'pathname' '''

	lista = []
	# Lista arquivos do diretorio atual
	for f in os.listdir(pathname):
		if f.endswith('.xls'):
			lista.append(f)
	lista=np.sort(lista)

	return lista
# ================================================== #

# pl.close('all')

pathname = os.environ['HOME'] + '/Dropbox/lioc/dados/pnboia/argos/chm_boias/'

boias = ['rio_grande','florianopolis','santos','recife']

#numero de sensores no arquvo .xls (sem contar data, msg, ..)
nsens = 31

#array com dados concatenados
#rio grande - rs
data_rs = np.array([])
ws_rs = np.array([])
wg_rs = np.array([])
wd_rs = np.array([])
at_rs = np.array([])
rh_rs = np.array([])
dw_rs = np.array([])
pr_rs = np.array([])
st_rs = np.array([])
bh_rs = np.array([])
cl_rs = np.array([])
tu_rs = np.array([])
sr_rs = np.array([])
hs_rs = np.array([])
hm_rs = np.array([])
tp_rs = np.array([])
dp_rs = np.array([])
sp_rs = np.array([])

#florianopolis - sc
data_sc = np.array([])
ws_sc = np.array([])
wg_sc = np.array([])
wd_sc = np.array([])
at_sc = np.array([])
rh_sc = np.array([])
dw_sc = np.array([])
pr_sc = np.array([])
st_sc = np.array([])
bh_sc = np.array([])
cl_sc = np.array([])
tu_sc = np.array([])
sr_sc = np.array([])
hs_sc = np.array([])
hm_sc = np.array([])
tp_sc = np.array([])
dp_sc = np.array([])
sp_sc = np.array([])

#rio grande - rs
data_sp = np.array([])
ws_sp = np.array([])
wg_sp = np.array([])
wd_sp = np.array([])
at_sp = np.array([])
rh_sp = np.array([])
dw_sp = np.array([])
pr_sp = np.array([])
st_sp = np.array([])
bh_sp = np.array([])
cl_sp = np.array([])
tu_sp = np.array([])
sr_sp = np.array([])
hs_sp = np.array([])
hm_sp = np.array([])
tp_sp = np.array([])
dp_sp = np.array([])
sp_sp = np.array([])

#rio grande - rs
data_pe = np.array([])
ws_pe = np.array([])
wg_pe = np.array([])
wd_pe = np.array([])
at_pe = np.array([])
rh_pe = np.array([])
dw_pe = np.array([])
pr_pe = np.array([])
st_pe = np.array([])
bh_pe = np.array([])
cl_pe = np.array([])
tu_pe = np.array([])
sr_pe = np.array([])
hs_pe = np.array([])
hm_pe = np.array([])
tp_pe = np.array([])
dp_pe = np.array([])
sp_pe = np.array([])


#loop para variar as boias
for boia in boias:

	pathname_boia = pathname + boia + '/'

	lista = lista_xls(pathname_boia)

	#loop para processar cada arquivo .xls
	for arquivos in range(len(lista)):

		#cria um novo arquivo de data para cada arquivo
		datat = []

		# arquivo processado
		arq = lista[arquivos]

		#Open an Excel workbook 
		workbook = xlrd.open_workbook(pathname_boia + arq)

		#imprime nome das planilhas
		print pathname_boia + ' -- ' + str(workbook.sheet_names())

		#seleciona planilha por indice (pode ser por nome tbm)
		sheet_0 = workbook.sheet_by_index(0) #anemometro

		#pega os valores das celulas selecionadas
		meteo_all = np.array([[sheet_0.cell_value(r,c) for r in range(0,sheet_0.nrows)] for c in range(0,sheet_0.ncols)]).T

		cabec = meteo_all[0,:]
		meteo = meteo_all[1:,:]

		# coloca NAN no lugar dos dados invalidos (strings) que tem no meio
		# das series, p.ex ('E3', ...)
		for c in range(meteo.shape[1]):

			for l in range(meteo.shape[0]):

				if meteo[l,c].isalnum() == True:

					meteo[l,c] = np.nan

				elif meteo[l,c] == '':

					meteo[l,c] = np.nan


		#carrega data, ex: 2012/04/30 00:18:51
		if  'Msg Date' in cabec:
			ind_data = int(np.where(cabec == 'Msg Date')[0])
			tipo_msg = 1
			print 'MENSAGEM ARGOS - TIPO ' + str(tipo_msg)

		elif 'Loc. date' in cabec:
			ind_data = int(np.where(cabec == 'Loc. date')[0])
			tipo_msg = 2
			print 'MENSAGEM: ' + str(tipo_msg)

		#acha os indices dos sensores da matriz
		ind_ws = int(np.where(cabec == 'SENSOR 02')[0]) # wind speed
		ind_wg = int(np.where(cabec == 'SENSOR 03')[0]) # wind gust
		ind_wd = int(np.where(cabec == 'SENSOR 04')[0]) # wind direction
		ind_at = int(np.where(cabec == 'SENSOR 05')[0]) # wind direction
		ind_rh = int(np.where(cabec == 'SENSOR 06')[0]) # air temp
		ind_dw = int(np.where(cabec == 'SENSOR 07')[0]) # dew point
		ind_pr = int(np.where(cabec == 'SENSOR 08')[0]) # pressure
		ind_st = int(np.where(cabec == 'SENSOR 09')[0]) # sst
		ind_bh = int(np.where(cabec == 'SENSOR 10')[0]) # buoy heading
		ind_cl = int(np.where(cabec == 'SENSOR 11')[0]) # clorofila a
		ind_tu = int(np.where(cabec == 'SENSOR 12')[0]) # turbidez
		ind_sr = int(np.where(cabec == 'SENSOR 13')[0]) # solar rad
		ind_hs = int(np.where(cabec == 'SENSOR 20')[0]) # hs
		ind_hm = int(np.where(cabec == 'SENSOR 21')[0]) # hmax
		ind_tp = int(np.where(cabec == 'SENSOR 22')[0]) # period
		ind_dp = int(np.where(cabec == 'SENSOR 23')[0]) # mean dir
		ind_sp = int(np.where(cabec == 'SENSOR 24')[0]) # spread

		#pega o vetor da variavel (retira o cabecalho - linha 0)
		data_arq = meteo[:,ind_data]

		#indice com dados que tem valores de data (retira os dados faltando)
		indv = np.where(data_arq <> 'nan')[0]

		#vetor de datas (sem os nan)
		data = data_arq[indv]

		ws_str = meteo[indv,ind_ws]
		wg_str = meteo[indv,ind_wg]
		wd_str = meteo[indv,ind_wd]
		at_str = meteo[indv,ind_at]
		rh_str = meteo[indv,ind_rh]
		dw_str = meteo[indv,ind_dw]
		pr_str = meteo[indv,ind_pr]
		pr_str = meteo[indv,ind_pr]
		st_str = meteo[indv,ind_st]
		bh_str = meteo[indv,ind_bh]
		cl_str = meteo[indv,ind_cl]
		tu_str = meteo[indv,ind_tu]
		sr_str = meteo[indv,ind_sr]
		hs_str = meteo[indv,ind_hs]
		hm_str = meteo[indv,ind_hm]
		tp_str = meteo[indv,ind_tp]
		dp_str = meteo[indv,ind_dp]
		sp_str = meteo[indv,ind_sp]

		#passa as variaveis dos sensores para float
		ws = ws_str.astype(float)
		wg = wg_str.astype(float)
		wd = wd_str.astype(float)
		at = at_str.astype(float)
		rh = rh_str.astype(float)
		dw = dw_str.astype(float)
		pr = pr_str.astype(float)
		st = st_str.astype(float)
		bh = bh_str.astype(float)
		cl = cl_str.astype(float)
		tu = tu_str.astype(float)
		sr = sr_str.astype(float)
		hs = hs_str.astype(float)
		hm = hm_str.astype(float)
		tp = tp_str.astype(float)
		dp = dp_str.astype(float)
		sp = sp_str.astype(float)

		#cria vetor de datas com datetime
		for i in range(len(data)):
			datat.append(datetime(int(data[i][0:4]),int(data[i][5:7]),int(data[i][8:10]),int(data[i][11:13])))

		#concatena os arquivos
		if boia == 'rio_grande':
			data_rs = np.concatenate((data_rs,datat))
			ws_rs = np.concatenate((ws_rs,ws))
			wg_rs = np.concatenate((wg_rs,wg))
			wd_rs = np.concatenate((wd_rs,wd))
			at_rs = np.concatenate((at_rs,at))
			rh_rs = np.concatenate((rh_rs,rh))
			dw_rs = np.concatenate((dw_rs,dw))
			pr_rs = np.concatenate((pr_rs,pr))
			st_rs = np.concatenate((st_rs,st))
			bh_rs = np.concatenate((bh_rs,bh))
			cl_rs = np.concatenate((cl_rs,cl))
			tu_rs = np.concatenate((tu_rs,tu))
			sr_rs = np.concatenate((sr_rs,sr))
			hs_rs = np.concatenate((hs_rs,hs))
			hm_rs = np.concatenate((hm_rs,hm))
			tp_rs = np.concatenate((tp_rs,tp))
			dp_rs = np.concatenate((dp_rs,dp))
			sp_rs = np.concatenate((sp_rs,sp))

		elif boia == 'florianopolis':
			data_sc = np.concatenate((data_sc,datat))
			ws_sc = np.concatenate((ws_sc,ws))
			wg_sc = np.concatenate((wg_sc,wg))
			wd_sc = np.concatenate((wd_sc,wd))
			at_sc = np.concatenate((at_sc,at))
			rh_sc = np.concatenate((rh_sc,rh))
			dw_sc = np.concatenate((dw_sc,dw))
			pr_sc = np.concatenate((pr_sc,pr))
			st_sc = np.concatenate((st_sc,st))
			bh_sc = np.concatenate((bh_sc,bh))
			cl_sc = np.concatenate((cl_sc,cl))
			tu_sc = np.concatenate((tu_sc,tu))
			sr_sc = np.concatenate((sr_sc,sr))
			hs_sc = np.concatenate((hs_sc,hs))
			hm_sc = np.concatenate((hm_sc,hm))
			tp_sc = np.concatenate((tp_sc,tp))
			dp_sc = np.concatenate((dp_sc,dp))
			sp_sc = np.concatenate((sp_sc,sp))

		elif boia == 'santos':
			data_sp = np.concatenate((data_sp,datat))
			ws_sp = np.concatenate((ws_sp,ws))
			wg_sp = np.concatenate((wg_sp,wg))
			wd_sp = np.concatenate((wd_sp,wd))
			at_sp = np.concatenate((at_sp,at))
			rh_sp = np.concatenate((rh_sp,rh))
			dw_sp = np.concatenate((dw_sp,dw))
			pr_sp = np.concatenate((pr_sp,pr))
			st_sp = np.concatenate((st_sp,st))
			bh_sp = np.concatenate((bh_sp,bh))
			cl_sp = np.concatenate((cl_sp,cl))
			tu_sp = np.concatenate((tu_sp,tu))
			sr_sp = np.concatenate((sr_sp,sr))
			hs_sp = np.concatenate((hs_sp,hs))
			hm_sp = np.concatenate((hm_sp,hm))
			tp_sp = np.concatenate((tp_sp,tp))
			dp_sp = np.concatenate((dp_sp,dp))
			sp_sp = np.concatenate((sp_sp,sp))

		elif boia == 'recife':
			data_pe = np.concatenate((data_pe,datat))
			ws_pe = np.concatenate((ws_pe,ws))
			wg_pe = np.concatenate((wg_pe,wg))
			wd_pe = np.concatenate((wd_pe,wd))
			at_pe = np.concatenate((at_pe,at))
			rh_pe = np.concatenate((rh_pe,rh))
			dw_pe = np.concatenate((dw_pe,dw))
			pr_pe = np.concatenate((pr_pe,pr))
			st_pe = np.concatenate((st_pe,st))
			bh_pe = np.concatenate((bh_pe,bh))
			cl_pe = np.concatenate((cl_pe,cl))
			tu_pe = np.concatenate((tu_pe,tu))
			sr_pe = np.concatenate((sr_pe,sr))
			hs_pe = np.concatenate((hs_pe,hs))
			hm_pe = np.concatenate((hm_pe,hm))
			tp_pe = np.concatenate((tp_pe,tp))
			dp_pe = np.concatenate((dp_pe,dp))
			sp_pe = np.concatenate((sp_pe,sp))





pl.figure()
pl.subplot(411)
pl.title('WIND SPEED/GUST')
pl.plot(data_rs,wg_rs,'yo',label='rs')
pl.plot(data_rs,ws_rs,'bo',label='rs')
pl.legend()

pl.subplot(412)
pl.plot(data_sc,wg_sc,'yo',label='sc')
pl.plot(data_sc,ws_sc,'ro',label='sc')
pl.legend()

pl.subplot(413)
pl.plot(data_sp,wg_sp,'yo',label='sp')
pl.plot(data_sp,ws_sp,'go',label='sp')
pl.legend()

pl.subplot(414)
pl.plot(data_pe,wg_pe,'yo',label='pe')
pl.plot(data_pe,ws_pe,'ko',label='pe')
pl.legend()


# pl.figure()
# pl.plot(datat,ws,'ob',label='ws1')
# pl.plot(datat,wg,'or',label='wg1')
# pl.legend()

# pl.figure()
# pl.plot(datat,wd,'og',label='wd1')
# pl.plot(datat,bh,'ok',label='bh')
# pl.legend()

# pl.figure()
# pl.plot(datat,at,'ob',label='at')
# pl.plot(datat,st,'or',label='sst')
# pl.legend()

# pl.figure()
# pl.plot(datat,rh,'ob',label='rh')
# pl.legend()

# pl.figure()
# pl.plot(datat,dw,'or',label='dwp')
# pl.legend()

# pl.figure()
# pl.plot(datat,pr,'ob',label='pr')
# pl.legend

# pl.figure()
# pl.plot(datat,hs,'ob',label='hs')
# pl.plot(datat,hm,'or',label='hmax')
# pl.legend


#salva variaveis na tabela
# cria arquivos para salvar

#retira as datas repetidas
rs,indices_rs = np.unique(data_rs, return_index=True)
sc,indices_sc = np.unique(data_sc, return_index=True)
sp,indices_sp = np.unique(data_sp, return_index=True)
pe,indices_pe = np.unique(data_pe, return_index=True)

#modelo - data em AAAAMMDDHHMMSS
data_rs = data_rs.astype(str)
data_rs = np.array([data_rs[i][0:4]+data_rs[i][5:7]+data_rs[i][8:10]+data_rs[i][11:13].zfill(2)+'00' for i in range(len(data_rs))])
data_rs = data_rs.astype(int)

data_sc = data_sc.astype(str)
data_sc = np.array([data_sc[i][0:4]+data_sc[i][5:7]+data_sc[i][8:10]+data_sc[i][11:13].zfill(2)+'00' for i in range(len(data_sc))])
data_sc = data_sc.astype(int)

data_sp = data_sp.astype(str)
data_sp = np.array([data_sp[i][0:4]+data_sp[i][5:7]+data_sp[i][8:10]+data_sp[i][11:13].zfill(2)+'00' for i in range(len(data_sp))])
data_sp = data_sp.astype(int)

data_pe = data_pe.astype(str)
data_pe = np.array([data_pe[i][0:4]+data_pe[i][5:7]+data_pe[i][8:10]+data_pe[i][11:13].zfill(2)+'00' for i in range(len(data_pe))])
data_pe = data_pe.astype(int)

mat_rs = zip(data_rs.astype(str)[indices_rs],ws_rs[indices_rs],wg_rs[indices_rs],wd_rs[indices_rs],
	at_rs[indices_rs],rh_rs[indices_rs],dw_rs[indices_rs],pr_rs[indices_rs],st_rs[indices_rs],
	bh_rs[indices_rs],cl_rs[indices_rs],tu_rs[indices_rs],sr_rs[indices_rs],hs_rs[indices_rs],
	hm_rs[indices_rs],tp_rs[indices_rs],dp_rs[indices_rs],sp_rs[indices_rs])

mat_sc = zip(data_sc.astype(str)[indices_sc],ws_sc[indices_sc],wg_sc[indices_sc],wd_sc[indices_sc],
	at_sc[indices_sc],rh_sc[indices_sc],dw_sc[indices_sc],pr_sc[indices_sc],st_sc[indices_sc],
	bh_sc[indices_sc],cl_sc[indices_sc],tu_sc[indices_sc],sr_sc[indices_sc],hs_sc[indices_sc],
	hm_sc[indices_sc],tp_sc[indices_sc],dp_sc[indices_sc],sp_sc[indices_sc])

mat_sp = zip(data_sp.astype(str)[indices_sp],ws_sp[indices_sp],wg_sp[indices_sp],wd_sp[indices_sp],
	at_sp[indices_sp],rh_sp[indices_sp],dw_sp[indices_sp],pr_sp[indices_sp],st_sp[indices_sp],
	bh_sp[indices_sp],cl_sp[indices_sp],tu_sp[indices_sp],sr_sp[indices_sp],hs_sp[indices_sp],
	hm_sp[indices_sp],tp_sp[indices_sp],dp_sp[indices_sp],sp_sp[indices_sp])

mat_pe = zip(data_pe.astype(str)[indices_pe],ws_pe[indices_pe],wg_pe[indices_pe],wd_pe[indices_pe],
	at_pe[indices_pe],rh_pe[indices_pe],dw_pe[indices_pe],pr_pe[indices_pe],st_pe[indices_pe],
	bh_pe[indices_pe],cl_pe[indices_pe],tu_pe[indices_pe],sr_pe[indices_pe],hs_pe[indices_pe],
	hm_pe[indices_pe],tp_pe[indices_pe],dp_pe[indices_pe],sp_pe[indices_pe])

head = 'date,ws,wg,wd,at,rh,dw,pr,st,bh,cl,tu,sr,hs,hm,tp,dp,sp'
# 																	   0    1   2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
np.savetxt('out/argos/argos_chm_rio_grande.out',mat_rs,delimiter=',',fmt='%s',header=head)
np.savetxt('out/argos/argos_chm_florianopolis.out',mat_sc,delimiter=',',fmt='%s',header=head)
np.savetxt('out/argos/argos_chm_santos.out',mat_sp,delimiter=',',fmt='%s',header=head)
np.savetxt('out/argos/argos_chm_recife.out',mat_pe,delimiter=',',fmt='%s',header=head)

# # 	
pl.show()