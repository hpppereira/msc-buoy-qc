'''
Plotagem da localizacao das boias
'''


import pylab as pl
import numpy as np
import os
from mpl_toolkits.basemap import Basemap, shiftgrid, interp
import mpl_toolkits.basemap


pl.close('all')


pathname = os.environ['HOME'] + '/Dropbox/tese/rot/out/'

#  0  1   2  3  4  5  6  7  8  9
#date,ws,wg,wd,at,pr,wt,hs,tp,dp
#consistentes
sa = np.loadtxt(pathname + 'argos_opendap_cq_santos.out',delimiter=',') 
fl = np.loadtxt(pathname + 'argos_opendap_cq_florianopolis.out',delimiter=',') 
rg = np.loadtxt(pathname + 'argos_opendap_cq_rio_grande.out',delimiter=',') 

#brutos
# sa = np.loadtxt(pathname + 'argos_opendap_concat_santos.out',delimiter=',') 
# fl = np.loadtxt(pathname + 'argos_opendap_concat_florianopolis.out',delimiter=',') 
# rg = np.loadtxt(pathname + 'argos_opendap_concat_rio_grande.out',delimiter=',') 


pl.figure()
lat0=-34
lat1=-21
lon0=-53
lon1=-41

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
#pl.plot(sa[:,2],sa[:,1],'sb',markersize=9,alpha=0.5,label='Santos')
#pl.plot(fl[:,2],fl[:,1],'.r',markersize=19,alpha=0.5,label='Florianopolis')
#pl.plot(rg[:,2],rg[:,1],'^g',markersize=9,alpha=0.5,label='Rio Grande')

pl.plot(-44.933,-25.283,'sb',markersize=10,label='Santos')
pl.plot(-47.366,-28.500,'or',markersize=10,label='Florianopolis')
pl.plot(-49.866,-31.566,'^g',markersize=10,label='Rio Grande')


pl.legend(loc=4,fontsize=11)

pl.show()