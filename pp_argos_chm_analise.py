'''
pp_argos_chm_analysis.py
'''


## plotagem ##

param = ['WIND SPEED',
		 'WIND GRUST',
		 'WIND DIR',
		 'AIR TEMP',
		 'REL HUMID',
		 'DEW POINT',
		 'PRESSURE',
		 'SST',
		 'BUOY HEAD',
		 'CLR-A',
		 'TURBID',
		 'SOLAR RAD',
		 'Hs',
		 'Hmax',
		 'Tp',
		 'SPREAD']


#         0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
# dadosc = ws wg wd at rh dw pr st bh cl tu sr hs hm tp dp sp

ws = dadosc[pl.find(pl.isnan(dadosc[:,0])==False),0]
wg = dadosc[pl.find(pl.isnan(dadosc[:,1])==False),1]



ll = 0
tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

pl.figure() #figsize=(12,12))
pl.subplot(211)
pl.plot(data,dadosc[:,0],'.b')
pl.plot(data,dadosc[:,1],'.r')
pl.subplot(212)


pl.figure()
# the histogram of the data
n, bins, patches = pl.hist(ws1,20,normed=1,histtype='stepfilled',color='b',alpha=1)
#ajusta a melhor curva para os dados
(mu, sigma) = norm.fit(ws1)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'b--', linewidth=2)

n, bins, patches = pl.hist(wg,20,normed=1,histtype='stepfilled',color='r',alpha=0.5)
#ajusta a melhor curva para os dados
(mu, sigma) = norm.fit(wg)
y = mlab.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--', linewidth=2)

pl.axis('tight')



# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,1])==False),1],50,histtype='stepfilled',color='r',alpha=0.5)



# ll = 1
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 2
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')


# ll = 3
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 4
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 5
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 6
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 7
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 8
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 9
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 10
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 11
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 12
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 13
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 14
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 15
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')

# ll = 16
# tt = param[ll]

# pl.figure()
# pl.title(tt)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight')
# pl.legend()

# pl.figure()
# pl.subplot(211)
# pl.plot(data,dados[:,ll],'bo',label='bruto')
# pl.title(tt), pl.legend()
# pl.axis('tight')
# pl.subplot(212)
# pl.plot(data,dadosc[:,ll],'ro',label='cons')
# pl.axis('tight'), pl.legend()

# pl.figure()
# pl.hist(dadosc[pl.find(pl.isnan(dadosc[:,ll])==False),ll],50,color='b')
# pl.title(tt)
# pl.axis('tight')



pl.show()