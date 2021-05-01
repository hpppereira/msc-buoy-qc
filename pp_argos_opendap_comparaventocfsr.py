'''
Comparacao dos dados de vento da boia com o CFSR

Periodo de comparacao: Julho/2013
Boia de Rio Grande
'''

import numpy as np
import pylab as pl
import os
import datetime


name = 'riogrande_pnboiacfsr_201307'
#   0     1   2      3   4   5  6   7   8   9  10   11
# datai, lat, lon,  ws, wg, wd, at, pr, wt, hs, tp, dp
pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'
dadosc = np.loadtxt(pathname + 'argos_opendap_cq_' + 'rio_grande' + '.out',delimiter=',') #dados sem cq

#converte datas para datetime
datatc = np.array([datetime.datetime.strptime(str(int(dadosc[i,0])), '%Y%m%d%H%M') for i in range(len(dadosc))])

#vento
pathnamecfsr = os.environ['HOME'] + '/Dropbox/cfsr/'
u = np.loadtxt(pathnamecfsr + 'uCFSR_RioGrande_201307.txt')
v = np.loadtxt(pathnamecfsr + 'vCFSR_RioGrande_201307.txt')

#cria data
startime = datetime.datetime(2013,07,01,00,00)
datatcfsr = np.array([startime + datetime.timedelta(hours=x) for x in xrange(744)])

ws = np.sqrt(u**2 + v**2);
wd = np.arctan2(v,u) * 180 / np.pi; #vento de onde vem
wd[pl.find(wd<0)] = wd[pl.find(wd<0)] + 360;
wd[pl.find(wd>=360)] = wd[pl.find(wd>=360)] - 360;


pl.figure()
pl.subplot(211)
pl.plot(datatc,dadosc[:,3],'ob',label='PNBOIA')
pl.plot(datatcfsr,ws,'or',label='CFSR')
pl.xlim(datatcfsr[0],datatcfsr[-1])
pl.xticks(visible=False)
pl.legend(ncol=2)
pl.grid()
pl.ylabel(r'$Vel.\ Vento\ (m/s)$')
pl.subplot(212)
pl.plot(datatc,dadosc[:,5],'ob')
pl.plot(datatcfsr,wd,'or')
pl.xlim(datatcfsr[0],datatcfsr[-1])
pl.grid()
pl.yticks([0,45,90,135,180,225,270,315,360])
pl.ylim(0,360)
pl.ylabel(r'$Dir.\ Vento\ $'+u'(\u00b0)')





#seleciona mes de jul 2013 nos dados da boia

ini = pl.find(np.array(datatc).astype(str)=='2013-07-01 01:00:00')
fim = pl.find(np.array(datatc).astype(str)=='2013-07-31 23:00:00')

wsb = dadosc[ini:fim,3]
wdb = dadosc[ini:fim,5]
datam_py = datatc[ini:fim]


#################################################################
#acha no modelo apenas as datas que tem dados (deixa o vetor do modelo do mesmo comprimento do dado)

nest = np.zeros(len(wsb)) #vetor de zeros do tamanho dos dados
datam_pystr = datam_py.astype(str)
datam_ww3str = datatcfsr.astype(str)
 

for idata in range(len(datam_pystr)):
    nest[idata] = np.where(datam_ww3str == datam_pystr[idata])[0]

# stop

nest = nest.astype(int)
ws = ws[nest]
wd = wd[nest]
datam_ww3 = datatcfsr[nest]

#seleciona valor sem nan
aux = np.where( (np.isnan(wsb)==False) & (np.isnan(wdb)==False) )[0]

ws = ws[aux]; hs = ws
wd = wd[aux] ; tp = wd
wsb = wsb[aux] ; hs_mod = wsb
wdb = wdb[aux] ; tp_mod = wdb



### BIAS ###
#hs
bias_hs = np.mean(hs_mod - hs)
#tp
bias_tp = np.mean(tp_mod - tp)
 
### ERMS ###
#hs
rmse_hs = np.sqrt( pl.sum( (hs_mod - hs) ** 2 ) / len(hs) )
#tp
rmse_tp = np.sqrt( pl.sum( (tp_mod - tp) ** 2 ) / len(tp) )
 
### SI ###
#hs
si_hs = rmse_hs / np.mean(hs)
#tp
si_tp = rmse_tp / np.mean(tp)
 
 
### Correlacao ###
#hs
corr_hs = np.corrcoef(hs_mod,hs)[0,1]
#tp
corr_tp = np.corrcoef(tp_mod,tp)[0,1]
 
### media boia ###
mean_adcp_hs = np.mean(hs)
mean_adcp_tp = np.mean(tp)
### media modelo ###
mean_mod_hs = np.mean(hs_mod)
mean_mod_tp = np.mean(tp_mod)
 
### maximo boia ###
max_adcp_hs = np.max(hs)
max_adcp_tp = np.max(tp)
### maximo modelo ###
max_mod_hs = np.max(hs_mod)
max_mod_tp = np.max(tp_mod)
 
# estatistica (matriz est)
# ---------------------------------------------
# Hs | BIAS   | RMSE    | SI      | CORR
# Tp | BIAS   | RMSE    | SI      | CORR
# Dp | BIAS   | RMSE    | SI      | CORR
# Hs | Med Obs| Med Mod | Max Obs | Max Mod
# Tp | Med Obs| Med Mod | Max Obs | Max Mod
# Dp | Med Obs| Med Mod | Max Obs | Max Mod
 
#estatistica 1 (hs, tp, dp) estat_dados.csv
# Hs  | Med | DesPad | Min | P90 | Max
# Tp  | Med | DesPad | Min | P90 | Max
# Dp  | Med | DesPad | Min | P90 | Max
 
estat1 = np.zeros((2,5))
estat1[0,0] = np.mean(hs)
estat1[1,0] = np.mean(tp)
estat1[0,1] = np.std(hs)
estat1[1,1] = np.std(tp)
estat1[0,2] = np.min(hs)
estat1[1,2] = np.min(tp)
estat1[0,3] = np.percentile(hs,90)
estat1[1,3] = np.percentile(tp,90)
estat1[0,4] = np.max(hs)
estat1[1,4] = np.max(tp)
 
#estatistica 2 (hs, tp, dp) estat_modelo.csv
# Hs  | Med | DesPad | Min | P90 | Max
# Tp  | Med | DesPad | Min | P90 | Max
# Dp  | Med | DesPad | Min | P90 | Max
 
estat2 = np.zeros((2,5))
estat2[0,0] = np.mean(hs_mod)
estat2[1,0] = np.mean(tp_mod)
estat2[0,1] = np.std(hs_mod)
estat2[1,1] = np.std(tp_mod)
estat2[0,2] = np.min(hs_mod)
estat2[1,2] = np.min(tp_mod)
estat2[0,3] = np.percentile(hs_mod,90)
estat2[1,3] = np.percentile(tp_mod,90)
estat2[0,4] = np.max(hs_mod)
estat2[1,4] = np.max(tp_mod)
# perc90[0,1] = np.percentile(hs_mod,90)
# perc90[1,1] = np.percentile(tp_mod,90)
# perc90[2,1] = np.percentile(dp_mod,90)
 
est=np.zeros((5,4))
est[0,0]=bias_hs
est[1,0]=bias_tp
est[3,0]=mean_adcp_hs
est[4,0]=mean_adcp_tp
est[0,1]=rmse_hs
est[1,1]=rmse_tp
est[3,1]=mean_mod_hs
est[4,1]=mean_mod_tp
est[0,2]=si_hs
est[1,2]=si_tp
est[3,2]=max_adcp_hs
est[4,2]=max_adcp_tp
est[0,3]=corr_hs
est[1,3]=corr_tp
est[3,3]=max_mod_hs
est[4,3]=max_mod_tp

np.savetxt('out/' + name + 'estat_validacao.csv',est,delimiter=",",fmt='%2.2f')
np.savetxt('out/' + name + 'estat_dados.csv',estat1,delimiter=",",fmt='%2.2f')
np.savetxt('out/' + name + 'estat_modelo.csv',estat2,delimiter=",",fmt='%2.2f')
 

pl.show()