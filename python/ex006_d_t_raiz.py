number = int(input('Digite o numero: '))
print('O dobro de {} é {}'.format(number, number*2))
print('O triplo de {} é {}'.format(number, number*3))
print('A raiz quadrada de {} é {:.2f}'.format(number, number**(1/2)))
'''se quiser, para calculo de raiz quadrada tbm é possivel importar da bliblioteca math
a função sqrt e usa-la da seguinte maneira: .format(sqrt(number))'''