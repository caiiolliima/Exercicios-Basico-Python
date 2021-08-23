n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2

print('A soma entre {} e {} resulta no valor de {}'.format(n1, n2, s))

n = input('Digite algo: ')
print(type(n), n.isascii(), n.isalpha(), n.isdigit(), n.isalnum(), n.isnumeric(), n.isdecimal(), n.isidentifier(),
      n.isprintable(), n.istitle(), n.isupper(), n.isspace())