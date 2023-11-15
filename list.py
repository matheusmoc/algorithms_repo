#antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#com listas
notas = [7.9, 9.7, 8.2]

#criando listas
lista = list()  
lista = []
lista = [24, 'Matheus', 3.14159, True]
lista_de_listas = [10, [1, 2, 3]]


#Indexação e slices
lista = [24, 'Matheus', 3.14159, False]
print(lista[2])
print(lista[-1])

print(lista[0:3])
print(lista[3:])
print(lista[0:3:2]) #Pula de dois em dois 


#percorrendo listas
for elemento in lista:
    print(elemento)

#percorrendo listas utilizando indices
print('Comprimento: ', len(lista))
for i in range(len(lista)):
    print(i)




lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:
    if item % 2 == 0:
        if item < 0:
            lista_final.append(-2*item)
        else:
            lista_final.append(2*item)
    else:
        if item < 0:
            lista_final.append(-item)
        else:
            lista_final.append(item)
print(lista_final)