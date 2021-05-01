'''
Grafico com periodos de medicoes das boias

dados de entrada: ano, mes, dia, hora
*matriz de parametros calculados
'''

import numpy as np
from datetime import datetime
import os
import matplotlib.pylab as pl

# pl.close('all')

#carrega arquivos 'lista'

pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'
#pathname = 'C:/Users/hp/Dropbox/tese (1)/rot/out/'
#---------------------------------------------------------------------------
#carrega dados sem cq
#  0  1   2  3  4  5  6  7  8  9 10
#date,ws,wg,wd,at,rh,pr,wt,hs,tp,dp
#sa = np.loadtxt(pathname + 'argos_opendap_santos.out',delimiter=',') 
#fl = np.loadtxt(pathname + 'argos_opendap_florianopolis.out',delimiter=',') 
rg = np.loadtxt(pathname + 'argos_opendap_rio_grande.out',delimiter=',') 

#---------------------------------------------------------------------------
#carrega dados com cq

#  0  1   2  3  4  5  6  7  8  9 10
#date,ws,wg,wd,at,rh,pr,wt,hs,tp,dp
#sac = np.loadtxt(pathname + 'argos_opendap_cq_santos.out',delimiter=',') 
#flc = np.loadtxt(pathname + 'argos_opendap_cq_florianopolis.out',delimiter=',') 
rgc = np.loadtxt(pathname + 'argos_opendap_cq_rio_grande.out',delimiter=',') 

#consistencia manual
# rec[1995:6995,1:] = np.nan ; rec[11411:15932,1:] = np.nan #recife
# flc[2352:4118,1:] = np.nan #florianopolis

#plotar apenas os dados consistentes
#sac = sac[pl.find(np.isnan(sac[:,1])==False),:]
#flc = flc[pl.find(np.isnan(flc[:,1])==False),:]
rgc = rgc[pl.find(np.isnan(rgc[:,1])==False),:]

#---------------------------------------------------------------------------
#carrega dados brutos da triaxys
saw = np.loadtxt(pathname + 'triaxys_cp_8_santos.out',delimiter=',') 
flw = np.loadtxt(pathname + 'triaxys_cp_8_florianopolis.out',delimiter=',') 
rgw = np.loadtxt(pathname + 'triaxys_cp_8_rio_grande.out',delimiter=',') 

#plotar apenas os dados consistentes
# rew = rew[pl.find(np.isnan(rew[:,1])==False),:]
saw = saw[pl.find(np.isnan(saw[:,1])==False),:]
flw = flw[pl.find(np.isnan(flw[:,1])==False),:]
rgw = rgw[pl.find(np.isnan(rgw[:,1])==False),:]

#---------------------------------------------------------------------------
#datas

#dados processados sem cq
#dsa = np.array([datetime.strptime(str(int(sa[i,0])), '%Y%m%d%H%M') for i in range(len(sa))])
#dfl = np.array([datetime.strptime(str(int(fl[i,0])), '%Y%m%d%H%M') for i in range(len(fl))])
#drg = np.array([datetime.strptime(str(int(rg[i,0])), '%Y%m%d%H%M') for i in range(len(rg))])

#dados processados sem cq
#dsac = np.array([datetime.strptime(str(int(sac[i,0])), '%Y%m%d%H%M') for i in range(len(sac))])
#dflc = np.array([datetime.strptime(str(int(flc[i,0])), '%Y%m%d%H%M') for i in range(len(flc))])
drgc = np.array([datetime.strptime(str(int(rgc[i,0])), '%Y%m%d%H%M') for i in range(len(rgc))])

#datas triaxys
dsaw = np.array([datetime.strptime(str(int(saw[i,0])), '%Y%m%d%H%M') for i in range(len(saw))])
dflw = np.array([datetime.strptime(str(int(flw[i,0])), '%Y%m%d%H%M') for i in range(len(flw))])
drgw = np.array([datetime.strptime(str(int(rgw[i,0])), '%Y%m%d%H%M') for i in range(len(rgw))])

#valores para plotagem

#processados sem cq
#vsa = np.linspace(3,3,len(sa))
#vfl = np.linspace(2,2,len(fl))
#vrg = np.linspace(1,1,len(rg))

#processados com cq
#vsac = np.linspace(3,3,len(sac))
#vflc = np.linspace(2,2,len(flc))
vrgc = np.linspace(1,1,len(rgc))


#valores para plotagem - triaxys
vsaw = np.linspace(2.75,2.75,len(saw))
vflw = np.linspace(1.75,1.75,len(flw))
vrgw = np.linspace(0.75,0.75,len(rgw))


pl.figure(); pl.hold('on')
# pl.title('Periodo medicao das boias meteo-oceanograficas - PNBOIA',fontsize=18)
# pl.plot(dre,vre,'b.',markersize=35)
# pl.plot(drec,vrec,'k.',markersize=20)
# pl.plot(drew,vrew,'b.',markersize=20,label='Recife')

#pl.plot(dsa,vsa,'b.',markersize=35)
#pl.plot(dsac,vsac,'k.',markersize=17)
pl.plot(dsaw,vsaw,'b.',markersize=16,label=r'$Santos$')

#pl.plot(dfl,vfl,'r.',markersize=35)
#pl.plot(dflc,vflc,'k.',markersize=17)
pl.plot(dflw,vflw,'r.',markersize=16,label=r'$Floriano\'polis$')

#pl.plot(drg,vrg,'g.',markersize=35)
pl.plot(drgc,vrgc,'g.',markersize=40)
pl.plot(drgw,vrgw,'g.',markersize=16,label=r'$Rio\ Grande$')

pl.xticks(rotation=0,fontsize=14)
pl.yticks(visible=False)
pl.legend(loc=0,fontsize=18)
pl.ylim([0.25,3.5])
pl.grid('on')
pl.hold('off')

#xlim([731217  734139]); ylim([0 6]); grid();

pl.show()
