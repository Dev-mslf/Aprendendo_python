#011 - leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.
largura = float(input('Informe a largura em metros: '))
altura = float(input('Informe a altura em metros: '))
area = largura*altura
print('A área da parede é de {:.0f} m², então será necessário {:.0f} litros para pintá-la.'.format(area, area/2))
