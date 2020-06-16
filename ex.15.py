salario = float(input('Salário/hora: R$ '))
horas = int(input('Número de horas trabalhadas/mês: '))

salario_bruto = salario*horas
print('Salário bruto: R$ {:.2f}'.format(salario_bruto))

ir = salario_bruto*0.11
print('IR (11%): R$ {:.2f}'.format(ir))

inss = salario_bruto*0.08
print('INSS (8%): R$ {:.2f}'.format(inss))

sindicato = salario_bruto*0.05
print('Sindicato (5%): R$ {:.2f}'.format(sindicato))

salario_liquido = salario_bruto-ir-inss-sindicato
print('Salário Líquido: R$ {:.2f}'.format(salario_liquido))


