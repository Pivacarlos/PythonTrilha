import random
num = random.randint(0, 5)
print ("O computador pensou em um número entre 0 e 5. Tente adivinhar!")
if num == int(input("Qual número o computador pensou? ")):
    print ("Parabéns! Você acertou!")
else:
    print ("Que pena! Você errou!")