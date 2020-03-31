width = float(input('Digite a largura da parede: '))
height = float(input('Digite a altura da parede: '))
area = width * height
paint = area / 2
print('Sua parede tem dimensão de {} x {} e sua área é de {:.2f}m².'.format(width, height, area))
print('Você precisará de {:.2f} litros de tinta, para pintar essa parede.'.format(paint))
