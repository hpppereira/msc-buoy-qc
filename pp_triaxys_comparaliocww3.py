# -*- coding: utf-8 -*-
'''
Compara os dados da triaxys processado pelo lioc e 
resultado do ww3

Ultima modificacao: 09/05/2015

#Saida do Python
#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')

#Saida WW3
# 0   1   2    3   4   5   6  7   8
#ano,mes,dia,hora,min,hs,tp,dp,spread
'''

import numpy as np
from matplotlib import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from datetime import datetime
import os

plt.close('all')

local = 'Santos/SP'
local1 = 'santos'
latlon = '-25.28334 / -44.93334'
idargos = '69151'
idwmo = '31051'
glstr = '8'
dmag = -23

name = 'santos_pnboiaww3_201307_'

#triaxys_8_santos_jul13

#Saida do lioc
#         0   1   2   3    4     5    6   7   8     9       10       11   12   13   14    15   16   17    18   19
#header='data,hs,h10,hmax,tmed,thmax,hm0, tp, dp, sigma1p, sigma2p, hm01, tp1, dp1, hm02, tp2, dp2, gam, gam1, gam2')
py = np.loadtxt(os.environ['HOME'] + '/Dropbox/tese/rot/out/' + 'triaxys_cp_' + glstr + '_' + local1 + '.out',delimiter=',',skiprows = 0)

#python
datam_py = []
for i in range(len(py)):
	datam_py.append(datetime(int(str(py[i,0])[0:4]),int(str(py[i,0])[4:6]),int(str(py[i,0])[6:8]),int(str(py[i,0])[8:10])))
datam_py = np.array(datam_py)

#seleciona mes de jul 2013 nos dados da boia
ini = pl.find(np.array(datam_py).astype(str)=='2013-07-01 01:00:00')
fim = pl.find(np.array(datam_py).astype(str)=='2013-07-31 23:00:00')
py = py[ini:fim,:]
datam_py = datam_py[ini:fim]

############ ww3 ################
# 0   1   2    3   4   5  6  7   8
#ano,mes,dia,hora,min,hs,tp,dp,spread
ww3 = np.loadtxt(os.environ['HOME'] + '/Dropbox/tese/rot/out/ww3_santos_201207.txt')
# ww3 = np.loadtxt(os.environ['HOME'] + '/Dropbox/ww3vale/Geral/TU/hindcast/201302/grade_atl/santos.txt')


datam_ww3 = []
for i in range(len(ww3)):
	datam_ww3.append(datetime(int(ww3[i,0]), int(ww3[i,1]), int(ww3[i,2]), int(ww3[i,3]) ))
datam_ww3 = np.array(datam_ww3)



#################################################################
#acha no modelo apenas as datas que tem dados (deixa o vetor do modelo do mesmo comprimento do dado)

nest = np.zeros(len(py)) #vetor de zeros do tamanho dos dados
datam_pystr = datam_py.astype(str)
datam_ww3str = datam_ww3.astype(str)
 
for idata in range(len(datam_pystr)):
    nest[idata] = np.where(datam_ww3str == datam_pystr[idata])[0]
 
nest = nest.astype(int)
 
ww3 = ww3[nest]
datam_ww3 = datam_ww3[nest]
 


###########################################################################
#realiza estatisticas (bias, rmse, si, corr)

#seleciona valor sem nan
aux = pl.find(pl.isnan(py[:,6])==False)

hs = py[aux,6]
tp = py[aux,7]
dp = py[aux,8]
hs_mod = ww3[aux,5]
tp_mod = ww3[aux,6]
dp_mod = ww3[aux,7]


### BIAS ###
#hs
bias_hs = np.mean(hs_mod - hs)
#tp
bias_tp = np.mean(tp_mod - tp)
#dp
bias_dp = np.mean(dp_mod - dp)
 
### ERMS ###
#hs
rmse_hs = np.sqrt( pl.sum( (hs_mod - hs) ** 2 ) / len(hs) )
#tp
rmse_tp = np.sqrt( pl.sum( (tp_mod - tp) ** 2 ) / len(tp) )
#hs
rmse_dp = np.sqrt( pl.sum( (dp_mod - dp) ** 2 ) / len(dp) )
 
### SI ###
#hs
si_hs = rmse_hs / np.mean(hs)
#tp
si_tp = rmse_tp / np.mean(tp)
#dp
si_dp = rmse_dp / np.mean(dp)
 
 
### Correlacao ###
#hs
corr_hs = np.corrcoef(hs_mod,hs)[0,1]
#tp
corr_tp = np.corrcoef(tp_mod,tp)[0,1]
#dp
corr_dp = np.corrcoef(dp_mod,dp)[0,1]
 
### media boia ###
mean_adcp_hs = np.mean(hs)
mean_adcp_tp = np.mean(tp)
mean_adcp_dp = np.mean(dp)
### media modelo ###
mean_mod_hs = np.mean(hs_mod)
mean_mod_tp = np.mean(tp_mod)
mean_mod_dp = np.mean(dp_mod)
 
### maximo boia ###
max_adcp_hs = np.max(hs)
max_adcp_tp = np.max(tp)
max_adcp_dp = np.max(dp)
### maximo modelo ###
max_mod_hs = np.max(hs_mod)
max_mod_tp = np.max(tp_mod)
max_mod_dp = np.max(dp_mod)
 
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
 
estat1 = np.zeros((3,5))
estat1[0,0] = np.mean(hs)
estat1[1,0] = np.mean(tp)
estat1[2,0] = np.mean(dp)
estat1[0,1] = np.std(hs)
estat1[1,1] = np.std(tp)
estat1[2,1] = np.std(dp)
estat1[0,2] = np.min(hs)
estat1[1,2] = np.min(tp)
estat1[2,2] = np.min(dp)
estat1[0,3] = np.percentile(hs,90)
estat1[1,3] = np.percentile(tp,90)
estat1[2,3] = np.percentile(dp,90)
estat1[0,4] = np.max(hs)
estat1[1,4] = np.max(tp)
estat1[2,4] = np.max(dp)
 
#estatistica 2 (hs, tp, dp) estat_modelo.csv
# Hs  | Med | DesPad | Min | P90 | Max
# Tp  | Med | DesPad | Min | P90 | Max
# Dp  | Med | DesPad | Min | P90 | Max
 
estat2 = np.zeros((3,5))
estat2[0,0] = np.mean(hs_mod)
estat2[1,0] = np.mean(tp_mod)
estat2[2,0] = np.mean(dp_mod)
estat2[0,1] = np.std(hs_mod)
estat2[1,1] = np.std(tp_mod)
estat2[2,1] = np.std(dp_mod)
estat2[0,2] = np.min(hs_mod)
estat2[1,2] = np.min(tp_mod)
estat2[2,2] = np.min(dp_mod)
estat2[0,3] = np.percentile(hs_mod,90)
estat2[1,3] = np.percentile(tp_mod,90)
estat2[2,3] = np.percentile(dp_mod,90)
estat2[0,4] = np.max(hs_mod)
estat2[1,4] = np.max(tp_mod)
estat2[2,4] = np.max(dp_mod)
# perc90[0,1] = np.percentile(hs_mod,90)
# perc90[1,1] = np.percentile(tp_mod,90)
# perc90[2,1] = np.percentile(dp_mod,90)
 
est=np.zeros((6,4))
est[0,0]=bias_hs
est[1,0]=bias_tp
est[2,0]=bias_dp
est[3,0]=mean_adcp_hs
est[4,0]=mean_adcp_tp
est[5,0]=mean_adcp_dp
est[0,1]=rmse_hs
est[1,1]=rmse_tp
est[2,1]=rmse_dp
est[3,1]=mean_mod_hs
est[4,1]=mean_mod_tp
est[5,1]=mean_mod_dp
est[0,2]=si_hs
est[1,2]=si_tp
est[2,2]=si_dp
est[3,2]=max_adcp_hs
est[4,2]=max_adcp_tp
est[5,2]=max_adcp_dp
est[0,3]=corr_hs
est[1,3]=corr_tp
est[2,3]=corr_dp
est[3,3]=max_mod_hs
est[4,3]=max_mod_tp
est[5,3]=max_mod_dp

#np.savetxt('out/' + name + 'estat_validacao.csv',est,delimiter=",",fmt='%2.2f')
#np.savetxt('out/' + name + 'estat_dados.csv',estat1,delimiter=",",fmt='%2.2f')
#np.savetxt('out/' + name + 'estat_modelo.csv',estat2,delimiter=",",fmt='%2.2f')
 
# # scatter plot
# xi=hs
# y=hs_mod
# coefficients = np.polyfit(xi, y, 1)
# polynomial = np.poly1d(coefficients)
# ys = polynomial(xi)
# pl.figure()
# pl.subplot(3,1,1)
# pl.plot(xi, y, '.')
# pl.plot(xi, ys, 'r--')
# pl.plot(range(0,7),range(0,7),'k')
# pl.grid()
# pl.xlabel('Hs (m) medido')
# pl.ylabel('Hs (m) modelado')
 
# xi=tp
# y=tp_mod
# coefficients = np.polyfit(xi, y, 1)
# polynomial = np.poly1d(coefficients)
# ys = polynomial(xi)
# pl.subplot(3,1,2)
# pl.plot(xi, y, '.')
# pl.plot(xi, ys, 'r--')
# pl.plot(range(0,21),range(0,21),'k')
# pl.grid()
# pl.xlabel('Tp (s) medido')
# pl.ylabel('Tp (s) modelado')
 
# xi=dp
# y=dp_mod
# coefficients = np.polyfit(xi, y, 1)
# polynomial = np.poly1d(coefficients)
# ys = polynomial(xi)
# pl.subplot(3,1,3)
# pl.plot(xi, y, '.')
# pl.plot(xi, ys, 'r--')
# pl.plot(range(0,250),range(0,250),'k')
# pl.xlim(0,250)
# pl.ylim(0,250)
# #pl.axis('equal')
# pl.grid()
# pl.xlabel('Dp (graus) medido')
# pl.ylabel('Dp (graus) modelado')
# pl.show()












plt.figure()
plt.subplot(311)
plt.plot(datam_py,py[:,6],'b')
plt.plot(datam_ww3,ww3[:,5],'r')
plt.legend(['PNBOIA','WW3'])
plt.ylabel(r'$Hs\ (m)$'), pl.grid()
plt.xlim(datam_ww3[0],datam_ww3[-1])
plt.xticks(visible=False)
plt.subplot(312)
plt.plot(datam_py,py[:,7],'b.')
plt.plot(datam_ww3,ww3[:,6],'r.')
plt.ylabel(r'$Tp\ (s)$'), pl.grid()
plt.xlim(datam_ww3[0],datam_ww3[-1])
plt.xticks(visible=False)
plt.subplot(313)
plt.plot(datam_py,py[:,8]+dmag,'b.')
plt.plot(datam_ww3,ww3[:,7],'r.')
plt.ylabel(r'$Dp\ $' + u'(\u00b0)'), pl.grid()
plt.axis('tight')
plt.yticks([0,45,90,135,180,225,270,315,360])
plt.xlim(datam_ww3[0],datam_ww3[-1])
    
pl.show()
# plt.show()