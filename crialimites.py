'''
Cria limites para testes de CQ

-- Funcoes --
a) limspikes - cria limites de multiplicador do desvio
padrao para o teste de spike

b) limrange = cria limtes maximos e minimos

Ultima modificacao: 21/01/2015
'''

import numpy as np

#======================================================================#
## cria limites para testes de CQ

def limspike(mat_series):

	#media e desvio padrao para cada serie
	med = np.mean(mat_series,axis=0)
	dp = np.std(mat_series,axis=0)

	#multiplicador do desvio padrao e limites
	mult_despad = np.zeros((1024,len(med)))
	lim_spike = np.zeros((1024,len(med)))

	for i in range(len(med)):

		#multiplicador do desvio padrao
		mult_despad[:,i] = ( mat_series[:,i] - med[i] ) / dp[i]

		#limites de spike para elevacao
		lim_spike[:,i] = mult_despad[:,i] * dp[i]
	
	mult_despad = np.reshape(mult_despad,[np.size(mult_despad),1])
	lim_spike = np.reshape(lim_spike,[np.size(lim_spike),1])
	
	return mult_despad, lim_spike

def limrange(mat_series):

	lim_faixa_inf = np.min(abs(mat_series),axis=0)
	lim_faixa_sup = np.max(abs(mat_series),axis=0)

	return lim_faixa_inf, lim_faixa_sup