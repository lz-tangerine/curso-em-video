salary = float(input('Digite o valor do salário R$: '))
increase = salary + (15 * salary / 100)
print('O salário de R$ {} com 15% de aumento, fica R$ {:.2f}!'.format(salary, increase))
