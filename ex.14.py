peso_permitido = 50
peso = float(input('Quantos quilos você pescou hoje? '))
excesso = peso - peso_permitido
if excesso <=0:
    excesso *= (-1)
    print('Olá, hoje você não pescou nenhuma quantidade excedente. Tenha um ótimo dia!')
else:
    multa = 4 * excesso
    print('Olá, hoje você pescou %s quilos excedentes e deverá pagar uma multa de %s reais.'%(excesso,multa))
