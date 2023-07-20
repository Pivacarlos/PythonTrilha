reta1 = int(input("Digite o comprimento da primeira reta: "))
reta2 = int(input("Digite o comprimento da segunda reta: "))
reta3 = int(input("Digite o comprimento da terceira reta: "))
if (reta1 + reta2) >= reta3 and (reta3 + reta1) >= reta2 and (reta3 + reta2) >= reta1:
    print("É possível formar um triângulo com essas retas!")
else: 
    print("Não é possível formar um triângulo com essas retas!")
