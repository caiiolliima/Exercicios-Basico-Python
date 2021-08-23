n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
a = (n1 + n2)/2
print('A média final é {:.2f}!'.format(a))

#Código corrigido pelo professor

#Números quebrados se usa tipo float e não int.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
a = (n1 + n2) / 2
print('A média final é {:.2f}.'.format(a))