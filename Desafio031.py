distancia = float(input('Qual é a distância da sua viagem? '))
if distancia >= 200:
    print ('Valor dessa viagem é de R${:.2f}'.format(distancia * 0.45))
else:
    print ('Valor dessa viagem é de R${:.2f}'.format(distancia * 0.5))