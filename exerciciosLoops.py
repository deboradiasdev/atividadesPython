#Crie um loop for para iterar sobre cada elemento da lista e printe cada nome
nomes = ['Abelardo', 'Aluisio', 'Adalberto', 'Anastacio', 'Ubirajara']

for nome in nomes :
    print(nome)

#Faça o mesmo exercício acima utilizando o loop while
while len(nomes) > 0 :
    print(nomes.pop(0))

#Crie uma função que recebe a lista de nomes como parâmetro e passe por algum dos loops criados acima
def imprimir_nomes(lista) :
    for nome in lista :
        print(nome)

imprimir_nomes(nomes)

#Utilize o loop do exercício 1 ou 2 e printe somente os nomes que começam com letra “A”

for nome in nomes:
    if nome[0] == 'A':
        print(nome)