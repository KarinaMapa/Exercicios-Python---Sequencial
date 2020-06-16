area = float(input('Qual tamanho da área ser pintada em m²? '))
lata = 80
cobertura = 54
from math import ceil
quant = area/cobertura
valor = ceil(quant)*80
print('Você precisará de {} latas de tintas, valor total R$ {:.2f}'.format(ceil(quant),valor))