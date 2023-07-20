salario = float(input('Digite o salário do funcionário: R$'))
if salario <= 1250:
    novoSalario = salario + (salario * 1.15)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novoSalario))
else:
    novoSalario = salario + (salario * 1.10)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novoSalario))