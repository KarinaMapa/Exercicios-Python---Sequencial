count = 1
soma = 0
lista = []
while count <=4:
    x = float(input('Digite a nota do %s bimestre: '%(count)))
    count +=1
    lista.append(x)
print(lista)
for i in lista:
    soma += i
media = soma/len(lista)
print('A média é %s' %(media))