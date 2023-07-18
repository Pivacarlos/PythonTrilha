print("= = = =Anotaçao 002 = = = =")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1+n2
menos = n1-n2
vezes = n1*n2
divisao = n1/n2
exponecial = n1**n2
divisaoInteira = n1//n2
print ("A soma é igual a {}.\nA subtração é igual a {}.\nA multiplicação é igual a {}.\nA divisão é igual a {:.3f}.\nA exponenciação é igual a {}.\nA divisão inteira é igual a {}.".format(soma, menos, vezes, divisao, exponecial, divisaoInteira))
