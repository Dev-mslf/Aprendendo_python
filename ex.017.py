#017 Leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
catOposto = float(input('valor do cateto oposto:'))
catAdjacente= float(input('valor do cateto adjacente:'))
hipotenusa = (catAdjacente**2)+(catOposto**2)**(1/2)
print('Nesse triângulo retângulo, a hipotenusa vale', hipotenusa)
