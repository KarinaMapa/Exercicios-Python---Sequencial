lata18 = 80
lata36 = 25
area18 = 6*18
area36 = 6*3.6

area = float(input('Qual a área total a ser pintada (m²)? '))

from math import ceil
area_total18 = ceil(area/area18)
area_total36 = ceil(area/area36)
print('Se você optar por comprar apenas latas de 18 l irá precisar de {} latas e o valor total gasto será de R$ {:.2f}'.format(area_total18,(area_total18*80)))
print('Se optar por galões de 3,6 l precisará de {} galões e o valor total será de R$ {:.2f}'.format(area_total36,(area_total36*25)))

otimizando1 = area//area18
resto = area%area18
otimizando2 = ceil(resto/area36)
otimizado =(otimizando1*80)+(otimizando2*25)

print('Se optar por mesclar as opções precisará de ', end=' ')
if (area_total18*80) > otimizado:
    melhor = otimizado
    print('{} latas de 18 l e {} galões de 3,6 l.Já o custo total será de {:.2f}'.format(otimizando1, otimizando2, ((otimizando1*80)+(otimizando2*25))))
else:
    melhor = (area_total18*80)
    print('{} latas de 18 l e o custo total será de R$ {:.2f}'.format(area_total18, melhor))