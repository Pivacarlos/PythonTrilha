print("= = = = Desafio 015 = = = =")
km = float(input("Quantos km foram percorridos? "))
diasAlugado = int(input("Por quantos dias o carro foi alugado? "))
print("O valor a ser pago é R$ {:.2f}.".format(km*0.15+diasAlugado*60))