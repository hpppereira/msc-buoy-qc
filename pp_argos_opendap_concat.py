'''
Concatena dados das boias do PNBOIA
baixados pelo openDAP. Seleciona
apenas os dados que serao utilizados na tese

Cria 1 arquivo para boia que estiver sendo processada,
contendo:
#   0     1   2   3   4   5   6  7   8   9 
# datai, ws, wg, wd, at, bp, wt, hs, tp, dp

B69008 - recife (lat/lon: -8.149 / -34.56)
B69150 - santos (lat/lon: -25.28334 / -44.93334)
B69152 - florianopolis (lat/lon: -28.50000 / -47.36667)
B69153 - rio_grande (lat/long: -31.56667 / -49.86667)

Baixados do site do GOOS/BRASIL - SaltAmbiental
site: goosbrasil.saltambiental
'''

import numpy as np
import pylab as pl
import os
import netCDF4 as nc
from matplotlib import dates

pl.close('all')

###############################################################################

pathname = os.environ['HOME'] + '/Dropbox/lioc/dados/pnboia/argos/opendap/'

#escolher uma boia
# local = 'recife'
# argosname = 'B69007_argos.nc' 

# local = 'santos'
# argosname = 'B69150_argos.nc' 

local = 'florianopolis'
argosname = 'B69152_argos.nc' 

# local = 'rio_grande'
# argosname = 'B69153_argos.nc' 

###############################################################################


print 'Iniciando concatenacao em... ' + local

#opendap
buoy = nc.Dataset(pathname + argosname)

#lista o nome das variaveis
for v in buoy.variables:
	print v

#define variaveis
time = buoy.variables['time'][:]
lat = buoy.variables['latitude'][:]
lon = buoy.variables['longitude'][:]
avg_radiation = buoy.variables['avg_radiation'][:]
rel_humid = buoy.variables['rel_humid'][:]
wave_period = buoy.variables['wave_period'][:]
cm_dir1 = buoy.variables['cm_dir1'][:]
temp_air = buoy.variables['temp_air'][:]
wave_dir = buoy.variables['wave_dir'][:]
battery = buoy.variables['battery'][:]
wind_dir1 = buoy.variables['wind_dir1'][:]
cm_int1 = buoy.variables['cm_int1'][:]
cm_int3 = buoy.variables['cm_int3'][:]
cm_int2 = buoy.variables['cm_int2'][:]
wave_hs = buoy.variables['wave_hs'][:]
sst = buoy.variables['sst'][:]
wind_gust1_f2 = buoy.variables['wind_gust1_f2'][:]
pressure = buoy.variables['pressure'][:]
wave_h_max = buoy.variables['wave_h_max'][:]
wind_dir1_f2 = buoy.variables['wind_dir1_f2'][:]
dew_point = buoy.variables['dew_point'][:]
avg_wind_int1_f2 = buoy.variables['avg_wind_int1_f2'][:]
cm_dir3 = buoy.variables['cm_dir3'][:]
cm_dir2 = buoy.variables['cm_dir2'][:]
longitude = buoy.variables['longitude'][:]
avg_wind_int1 = buoy.variables['avg_wind_int1'][:]
avg_wind_int2 = buoy.variables['avg_wind_int2'][:]
wind_gust2 = buoy.variables['wind_gust2'][:]
avg_dir2 = buoy.variables['avg_dir2'][:]
wind_gust1 = buoy.variables['wind_gust1'][:]

#converte as data para datetime
datat = np.array(dates.num2date(time))
datastr = datat.astype(str)

#data em numero inteiro
datai = np.array([datastr[i][0:4]+datastr[i][5:7]+datastr[i][8:10]+\
	datastr[i][11:13].zfill(2)+'00' for i in range(len(datastr))])
datai = datai.astype(int)

#concatena os dados

#   0     1     2    3   4   5   6  7   8   9   10  11 
# datai, lat, lon,  ws, wg, wd, at, pr, wt, hs, tp, dp

#cria array de dados
dados = np.array(zip(datai,lat,lon,avg_wind_int1_f2,wind_gust1_f2,wind_dir1_f2,temp_air,
	pressure,sst,wave_hs,wave_period,wave_dir))

#retira os valores repetidos
#acha os indices
indaux = np.unique(datai,return_index=True)[1]
dados = dados[indaux,:]
datat = datat[indaux]

#habilitar essa parte do codigo para uma visualizacao rapida dos dados

#deixa os valores com -99999 (erro) com nan
for i in range(dados.shape[1]):
	dados[np.where(dados[:,i] == -99999),i] = np.nan

tt = ['datai','lat','lon','ws','wg','wd','at','bp','wt','hs','tp','dp']

#plotagem das variaveis
for i in range(dados.shape[1]):
	pl.figure()
	pl.plot(datat,dados[:,i])
	pl.title(tt[i])

pl.show()

#salva os dados
head = 'date,lat,lon,ws,wg,wd,at,bp,wt,hs,tp,dp'
np.savetxt('out/argos_opendap_concat_'+local+'.out',dados,delimiter=',',fmt=['%i']+11*['%.2f'],header=head)

