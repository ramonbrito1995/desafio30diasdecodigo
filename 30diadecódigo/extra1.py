#exemplo 1
lista = list()
v = int(input("Numero vezes: "))
x = [lista.append(int(input("Qual o elemento ?"))) for i in range(v)]
print(lista)

#exemplo 2
nomes = list()
v = int(input("Quantos nomes você ques add? "))
lista =[nomes.append(input("Diga o nome: ")) for i in range(v)]
print(nomes)

for i in range(v):
    nome = input("Diga o nome: ")
    nomes.append(nome)

#exemplo 3
lista_1 = [1,2,4,5]
lista_2 = [2,4,5,6]
x = [print(f"o índice {i} da lista 1 == ao índice {x} da lista 2.") for i in range(len(lista_1)) for x in range(len(lista_2)) if lista_1[i] == lista_2[x]]


for i in range(len(lista_1)):
    for x in range(len(lista_2)):
        if lista_1[i] == lista_2[x]:
            print("Há elemento igual")
            print(f"o índice {i} da lista 1 == ao índice {x} da lista 2.")
        

