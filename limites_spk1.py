#verifica limites de spikes



# ================================================================================== #
## Realiza o teste de spike para todas as series consistentes

#criar limites de testes    

mult_spike_eta = zeros((1024,cc)) #multiplicador do desvio padrao para o teste de spike - elevacao
mult_spike_dspx = zeros((1024,cc)) #multiplicador do desvio padrao para o teste de spike - dspx
mult_spike_dspy = zeros((1024,cc)) #multiplicador do desvio padrao para o teste de spike - dspy

for c in range(cc):

    for i in range(len(eta_mat_cons)):

        #multiplicador do despad para eta, dspx e dspy
        mult_spike_eta[i,c] = ( eta_mat_cons[i,c] - mean(eta_mat_cons[:,c]) ) / std(eta_mat_cons[:,c])
        mult_spike_dspx[i,c] = ( dspx_mat_cons[i,c] - mean(dspx_mat_cons[:,c]) ) / std(dspx_mat_cons[:,c])
        mult_spike_dspy[i,c] = ( dspy_mat_cons[i,c] - mean(dspy_mat_cons[:,c]) ) / std(dspy_mat_cons[:,c])


#deixa o limite de spike em uma coluna (para fazer o histograma)
mult_spike_eta = reshape(mult_spike_eta,[size(mult_spike_eta),1])
mult_spike_dspx = reshape(mult_spike_dspx,[size(mult_spike_dspx),1])
mult_spike_dspy = reshape(mult_spike_dspy,[size(mult_spike_dspy),1])


# figure()
# hist(mult_spike_eta,100)
# pl.title('Multiplicador do desvio padrao')
# pl.xlabel('M')
# pl.ylabel('N ocorrencias')
# axis([-4,4,0,1000000])
# savefig(os.environ['HOME'] + '/Dropbox/tese/doc/latex/figuras/meta_rs.png')

# pl.show()

