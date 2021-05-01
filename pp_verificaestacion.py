#Verifica a estacionaridade para dados da axys analisando 1024 pontos
#Freq. am = 1.28 Hz - 0.78 s, Num. am = 1382 pontos = 17 min

#testar 1024 pontos  = 800 seg = 13.3 min

#carrega 3 arquivos (S, NE e L)

import numpy as np
import os
import proc_onda
import pylab as plt

plt.close('all')

pathname = os.environ['HOME'] + '/Dropbox/tese/cq/dados/axys/rs/hne/'

#Sul (Hs = 6, Dp = 145)
s = np.loadtxt(pathname + '200912130300.HNE',skiprows = 11)

#Nordeste (Hs = 2.6, Dp = 45)
n = np.loadtxt(pathname + '200912200900.HNE',skiprows = 11)

#Leste (Hs = 1,0, Dp = 108)
l = np.loadtxt(pathname + '200912291600.HNE',skiprows = 11)


#prcessamento dos dados de onda no dom da freq.
gl = 32
han = 1
h = 180

nlag = len(s) - 1024

#parametros de onda (hm0, tp, dp)

ps = []
pn = []
pl = []

#varia os pontos a serem coletados
for i in range(nlag):

	sai_ondafreq, k, aannx, aanny, aanxny, a1, b1, diraz = proc_onda.onda_freq(s[i:i+1024,0],s[i:i+1024,1],s[i:i+1024,2],s[i:i+1024,3],gl,han,h)
	ps.append(sai_ondafreq)

	sai_ondafreq, k, aannx, aanny, aanxny, a1, b1, diraz = proc_onda.onda_freq(n[i:i+1024,0],n[i:i+1024,1],n[i:i+1024,2],n[i:i+1024,3],gl,han,h)
	pn.append(sai_ondafreq)

	sai_ondafreq, k, aannx, aanny, aanxny, a1, b1, diraz = proc_onda.onda_freq(l[i:i+1024,0],l[i:i+1024,1],l[i:i+1024,2],l[i:i+1024,3],gl,han,h)
	pl.append(sai_ondafreq)

ps = np.array(ps)
pn = np.array(pn)
pl = np.array(pl)

hss = np.zeros(nlag) ; hss[:] = 6.1
hsn = np.zeros(nlag) ; hsn[:] = 2.9
hsl = np.zeros(nlag) ; hsl[:] = 1.1

plt.figure()
plt.subplot(211)
plt.plot(s[:,1])
plt.title('Elevacao - Hm0 = 6,1 m, Dp = 151 graus')
plt.ylabel('metros')
plt.axis('tight')
plt.subplot(212)
plt.plot(ps[:,0],'.'), plt.hold('on')
plt.plot(hss,'r--')
plt.title('Altura significativa')
plt.xlabel('lag')
plt.ylabel('metros')
plt.axis('tight')
plt.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/hm0_mov1.png')

plt.figure()
plt.subplot(211)
plt.plot(n[:,1])
plt.title('Elevacao - Hm0 = 2.9 m, Dp = 48 graus')
plt.ylabel('metros')
plt.axis('tight')
plt.subplot(212)
plt.plot(pn[:,0],'.'), plt.hold('on')
plt.plot(hsn,'r--')
plt.title('Altura significativa')
plt.xlabel('lag')
plt.ylabel('metros')
plt.axis('tight')
plt.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/hm0_mov2.png')

plt.figure()
plt.subplot(211)
plt.plot(l[:,1])
plt.title('Elevacao - Hm0 = 1.1 m, Dp = 113 graus')
plt.ylabel('metros')
plt.axis('tight')
plt.subplot(212)
plt.plot(pl[:,0],'.'), plt.hold('on')
plt.plot(hsl,'r--')
plt.title('Altura significativa')
plt.xlabel('lag')
plt.ylabel('metros')
plt.axis('tight')
plt.savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/hm0_mov3.png')

plt.show()