import math 
print("= = = =Desafio 018 = = = =")
angulo = float(input("Digite o valor do ângulo: "))
print ("O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}.".format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))