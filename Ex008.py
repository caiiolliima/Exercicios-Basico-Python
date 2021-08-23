n1 = int(input('Digite um valor: '))
a = n1 * 100
b = n1 * 1000
print('O valor {} em centimetros é {}!'.format(n1, a))
print('O valor {} em milimetros é {}!'. format(n1, b))


#Código corrigido pelo professor
#Medidas também se usa FLOAT e não INT.

medida = float(input('Digite um valor: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))