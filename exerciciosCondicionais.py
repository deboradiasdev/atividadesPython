# Faça um programa que peça dois números e imprima o maior deles.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2 :
    print(f'O maior número é: {numero1}')
else:
    print(f'O maior número é: {numero2}')

# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('Digite um número: '))

if valor > 0 :
    print('Valor positivo')
else :
    print('Valor negativo')

# Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = input('Digite uma letra: ')

if letra == 'F' :
    print('Feminino')
elif letra == 'M' :
    print('Masculino')
else :
    print('Sexo Inválido')

# Crie um código em linguagem Python que peça o nome do usuário por meio da função input (). Se o nome for "Ultima", imprima "Bem-vindo, você é um(a) exclenete aluno(a)". Caso contrário, imprima "Bom dia, NOME". (Substitua o NOME pelo nome do usuário).
nome = input('Digite seu nome: ')

if nome == 'Ultima' :
    print('Bem-vindo, você é um(a) exclenete aluno(a)')
else :
    print('Bom dia, ' + nome)

# Escrever um programa em Python para ler um número inteiro e informar se ele é divisível por 5.
numeroInt = int(input('Digite um número inteiro: '))

if numeroInt % 5 == 0 :
    print('Número divisivel por 5')
else :
    print('Número não divisivel por 5')

# Escreva um programa Python para verificar se uma letra do Alfabeto(Abecedário) é uma vogal ou consoante.
vogais = ['a', 'e', 'i', 'o', 'u']

letra = input('Digite uma letra: ')

if letra in vogais :
    print('É uma vogal')
else :
    print("É uma consoante")