n1 = int(input('Digite um número: '))
a = n1 + 1
b = n1 - 1
print("O sucessor do número {} é {}!".format(n1, a))
print('O antecessor do número {} é {}!'.format(n1, b))

#Código corrigido pelo professor.

n = int(input('Digite um número: '))
print('O sucessor do número {} é {}, e seu antecessor é {}'.format(n, (n+1), (n-1)))
