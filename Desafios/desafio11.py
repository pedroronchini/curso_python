altura = float(input('Digite a altura da parede em metros:  '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2

print('Sua parede tem dimensão de {:.2f} x {:.2f} e sua área é de {}m²'.format(altura, largura, area))
print('Para pintar essa parede você precisara de {}L de tinta'.format(tinta))
