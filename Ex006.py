n1 = int(input('Digite um valor: '))
a = n1 * 2
b = n1 * 3
c = n1 ** (1/2)
print('O dobro do número {} é {}!'.format(n1, a))
print('O triplo do número {} é {}!'.format(n1, b))
print('A raiz quadrada do número {} é {:.2f}!'.format(n1, c))

#Código corrigido pelo professor

n = int(input('Digite um número: '))
print('O dobro de {} vale {}. O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))

print('O dobro de {} vale {}. O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))