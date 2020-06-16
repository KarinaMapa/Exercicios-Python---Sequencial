h = float(input('Qual sua altura? '))
sexo = str(input('Qual seu sexo? [M/F] ')).upper()
if sexo == 'M':
    peso = (72.7*h)-58
    print('Seu peso ideal é %s' %(peso))
else:
    peso = (62.1*h)-44.7
    print('Seu peso ideal é %s' %(peso))
