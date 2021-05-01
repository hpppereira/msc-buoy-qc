# -*- coding: utf-8 -*-
##Programa que cria perturbacoes

#------------------------------------------------------------#
### IMPORTA BIBLIOTECAS

import numpy as np
import copy as cp


#------------------------------------------------------------#
### GERA GAPS - LACUNAS COM NAN ###

def t1(vet,param):
    '''
    ### GERA SEGMENTOS COM GAPS (NAN) ###

    Dados de entrada:
    vet1 = vetor com serie temporal original (ex: tar,ur..)
    param = vetor com posicao, tamanho do segmento do gap
    param: col 1 - posicao inicial da perturbacao
           col 2 - tamanho do segmento
           col 3,4,5.... repete col 1 e 2

    Dados de saida:
    vet1 = vetor perturbado com gaps (lacunas de nan)
    '''

    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)

    #le o vetor com os parametros para criar as perturbacoes
    for i in range(0,len(param),2):

        #posicao inicial da perturbacao
        a=param[i]
        #tamanho do segmento
        b=param[i+1]

        #vetor com valores consecutivos nulos
        vet1[a:a+b]=np.nan

    return vet1

    
#------------------------------------------------------------#
### GERA SPIKES ###

def t2(vet,param):

    '''
    ### GERA SPIKES ###

    Dados de entrada:
    vet  = vetor com serie temporal original (ex: temp. do ar, umidade rel.)
    param = vetor com caracteristicas dos spikes a serem criados
    param: col 1 - posicao inicial do spike
           col 2 - numero de pontos do spike
           col 3 - valor determinado para spike
           col 5,6,7.... repete col 1 a 3

    Dados de saida:
    vet1 = vetor perturbado com spikes
    '''
    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)

    #le o vetor de parametros para criar spike com incremento de 4 (4 parametros para definir um spike)
    for i in range(0,len(param),3):

        a=param[i] #posicao do spike
        b=param[i+1] #numero de spikes a partir da posicao 'a'
        c=param[i+2] #multiplicador

        #cria spike com valor determinado
        vet1[a:a+b]=c
    
    #retorna vetor com spikes
    return vet1

#------------------------------------------------------------#
### GERA VALORES CONSECUTIVOS IGUAIS ###

def t3(vet,param):

    '''
    ### GERA VALORES CONSECUTIVOS IGUAIS ###

    Dados de entrada:
    vet = vetor com serie temporal original (ex: tar,ur..)
    param = vetor com posicao e quantidade dos valores consecutivos
    param: col 1 - posicao inicial da perturbacao
           col 2 - tamanho do segmento com valores consecutivos iguais
           col 3,4,5,6.... repete col 1 e 2

    Dados de saida:
    vet1 = vetor perturbado com valores consecutivos iguais
    Obs: Os valores vão repetir o valor da posicao inicial da perturbacao
    '''

    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)
    
    #le o vetor com os parametros para criar as perturbacoes
    for i in range(0,len(param),2):

        #posicao inicial da perturbacao
        a=param[i]
        #comprimento da perturbacao
        b=param[i+1]

        #cria valores consecutivos iguais ao valor inicial da perturbacao
        vet1[a:a+b]=vet1[a]

    #retorna vetor com valores consecutivos iguais
    return vet1

#------------------------------------------------------------#
### GERA SEGMENTOS COM VALORES CONSECUTIVOS NULOS ###

def t4(vet,param):
    '''
    ### GERA SEGMENTOS COM VALORES CONSECUTIVOS NULOS ###

    Dados de entrada:
    vet1 = vetor com serie temporal original (ex: tar,ur..)
    param = vetor com posicao, tamanho do segmento com valores nulos
    param: col 1 - posicao inicial da perturbacao
           col 2 - tamanho do segmento
           col 3,4,5.... repete col 1 e 2

    Dados de saida:
    vet1 = vetor perturbado com valores consecutivos nulos
    '''

    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)

    #le o vetor com os parametros para criar as perturbacoes
    for i in range(0,len(param),2):

        #posicao inicial da perturbacao
        a=param[i]
        #tamanho do segmento
        b=param[i+1]

        #vetor com valores consecutivos nulos
        vet1[a:a+b]=0

    return vet1

#------------------------------------------------------------#
### GERA SEGMENTOS COM A MEDIA DESLOCADA ###

def t5(vet,param):

    '''
    ### GERA SEGMENTOS COM A MEDIA DESLOCADA ###

    Dados de entrada:
    vet = vetor com serie temporal original (ex: tar,ur..)
    param = vetor com posicao, tamanho do segmento e valor do deslocamento
    param: col 1 - posicao inicial da perturbacao
           col 2 - tamanho do segmento
           col 3 - valor da media da serie deslocada
           col 4,5,6.... repete col 1 a 3

    Dados de saida:
    vet1 = vetor perturbado com valores consecutivos iguais
    '''

    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)
    
    #le o vetor com os parametros para criar as perturbacoes
    for i in range(0,len(param),3):

        #posicao inicial da perturbacao
        a=param[i]
        #tamanho do segmento
        b=param[i+1]
        #valor que a media sera deslocada
        c=param[i+2]

        #vetor com a media dos segmentos deslocada
        vet1[a:a+b]=vet1[a:a+b]+c

    return vet1

#------------------------------------------------------------#
### GERA GRANDES GRADIENTES ENTRE VALORES CONSECUTIVOS ###

def t6(vet,param):

    '''
    ### GERA GRANDES GRADIENTES ENTRE VALORES CONSECUTIVOS ###

    Dados de entrada:
    vet = vetor com serie temporal original (ex: tar,ur..)
    param = vetor com posicao e multiplicador do valor a ser criado
    param: col 1 - posicao da perturbacao
           col 2 - multiplicador
           col 3,4,5.... repete col 1 e 2

    Dados de saida:
    vet1 = vetor perturbado com alto gradiente
    Obs: Atencao com series de direcao para passar de 0 e 360
    '''

    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)
    
    #le o vetor com os parametros para criar as perturbacoes
    for i in range(0,len(param),2):

        #posicao da perturbacao
        a=param[i]
        #multiplicados da serie real
        b=param[i+1]

        #cria vetor com alto gradiente com base no valor anterior
        vet1[a]=vet1[a-1]*b

    return vet1

#------------------------------------------------------------#
### GERA ATRASO NA SERIE COLOCANDO ZEROS NO FINAL DA SERIE ###

def t7(vet,param):

    '''
    ### GERA ATRASO NA SERIE COLOCANDO ZEROS NO FINAL DA SERIE ###

    Dados de entrada:
    vet = vetor com serie temporal original (ex: tar,ur..)
    param = vetor com posicao e tempo do atraso
    param: col 1 - posicao inicial do atraso
           col 2 - tempo do atraso
           col 3,4,5,6.... repete col 1
           
    Dados de saida:
    vet1 = vetor perturbado com atrasos
    Obs: O tamanho do atraso nao pode ser igual ou maior que a posicao
    '''

    #copia serie original para ser perturbada
    vet1 = cp.copy(vet)
    
    #le o vetor com os parametros para criar as perturbacoes
    c=0
    for i in range(0,len(param),2):

        #posicao da perturbacao
        a=param[i]
        #tempo do atraso
        b=param[i+1]

        #cria vetor de atraso
        vet1[a:-1-b]=vet1[a+b:-1]

        #conta atraso total
        c=c+b

    #coloca zeros no final do vetor na quantidade de elementos totais do atraso = 'c'
    vet1[-c:-1]=0
    vet1[-1]=0

    return vet1




