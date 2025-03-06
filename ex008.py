medida = float(input('Digite uma distancia em metros: '))
dam = medida / 10
hm = medida / 100
km = medida / 1000
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A distancia de {}m é igual a:\n {}dam \n {}hm \n {}km \n {}dm \n {}cm \n {}mm'.format(medida, dam, hm, km, dm, cm, mm))