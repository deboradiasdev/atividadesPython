#Crie um loop for para iterar sobre cada elemento da lista e printe cada nome
nomes = ['Abelardo', 'Aluisio', 'Adalberto', 'Anastacio', 'Ubirajara']

for nome in nomes :
    print(nome)

#Faça o mesmo exercício acima utilizando o loop while
while len(nomes) > 0:
    print(nomes.pop(0))