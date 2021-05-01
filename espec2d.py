'''
Prepara matriz para a plotagem
do espectro direcional de ondas

1- cria matriz de freqXdir de nxm pontos
2- com a energia de cada frequencia do espec 1D,
distribuir essa energia ao longo das direcoes de
cada frequencia definido pela direcao media mais
o espalhamento (sigma1 ou sigma2)
3- Plotar a matriz do espectro direcional
'''

import numpy as np
import matplotlib as mpl
# def mat2d(freq,en,spr):

# freq = np.double(freq)
# en = np.double(en)

# #cria vetor de direcao
# fr = np.linspace(0,max(freq),25)
# di = np.linspace(0,360,24)

dire = np.double(np.linspace(0,360,len(freq)))
freq = np.double(freq)

[freqs,dires] = np.meshgrid(freq,dire)

energs = mpl.mlab.griddata(freq,dire,sn[:,1],freqs,dires,interp='nn') #a interp linear e a nn ficaram praticamente iguais
