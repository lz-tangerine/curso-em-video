product = float(input('Qual o valor do produto? R$ '))
discount = product - (5 * product) / 100
print('O produto que custava R$ {} vai passar a custar R$ {:.2f} com 5% de desconto!'.format(product, discount))