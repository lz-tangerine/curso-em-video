cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipo = (cat_oposto ** 2) + (cat_adjacente ** 2)
calc_hipo = hipo ** (1/2)
print('O valor da hipotenusa é de {:.2f}'.format(calc_hipo))
# pode-se tbm importar da biblioteca math a funcão hypot e usa-la para fazer o calculo
# hipo = math.hypot(cat_oposto, cat_adjacente)
