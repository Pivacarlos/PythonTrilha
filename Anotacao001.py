print("= = = =Anotaçao 001 = = = =")
nome = input("Qual é o seu nome? ")
# Centralizando o texto
print("Prazer em te conhecer {:^20}!".format(nome))
# Alinhando o texto a direita
print("Prazer em te conhecer {:>20}!".format(nome))
# Alinhando o texto a esquerda
print("Prazer em te conhecer {:<20}!".format(nome))
# Centralizando o texto e preenchendo os espaços com o caractere =
print("Prazer em te conhecer {:=^20}!".format(nome))
# Alinhando o texto a esquerda e preenchendo os espaços com o caractere =
print("Prazer em te conhecer {:=<20}!".format(nome))
# Alinhando o texto a direita e preenchendo os espaços com o caractere =
print("Prazer em te conhecer {:=>20}!".format(nome))

