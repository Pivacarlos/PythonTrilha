nome = str(input('Digite o nome da sua cidade: ')).strip()
print ('Sua cidade começa com Santo? {}'.format(nome.split()[0].upper() == 'SANTO'))