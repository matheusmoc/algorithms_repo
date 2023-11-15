#Métodos de lista
lista = [1, 3, 12, 8, 2]

#sort
lista.sort(reverse=True)
print(lista)

#sort
lista.sort()
print(lista)

#append 
print(lista)
lista.append(3)
print('depois do append', lista)

#insert
lista.insert(2, 10) #indice #elemento
print('depois do insert', lista)

#extend 
lista2 = ['maçã', 'banana', 1000]
lista.extend(lista2)
print('depois do extend', lista)

#pop
lista.pop(0)
print('depois do pop', lista)

#remove
lista.remove('maçã')
print('depois do remove', lista)

#count
print('depois do count', lista.count('banana'))

#index
print("depois do index", lista.index(12)) #qual índice o valor está

#functions
lista = [1, 2, 3]

print(sum(lista))
print(min(lista))
print(max(lista))
