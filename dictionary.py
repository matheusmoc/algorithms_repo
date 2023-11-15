dicionario = {}
dicionario = dict()

dicionario = { 'nome' : 'Matheus', 'idade' : '24', 'altura' : 1.77  }
print(dicionario)
dicionario['idade']

dicionario['dev'] = True
print(dicionario)

dicionario['altura'] = 1.80
print(dicionario)

for var in dicionario: 
    print(var) #index

for index in dicionario: 
    print(index, dicionario[index]) #index and value

print('peso' in dicionario) #verificar se a index existe