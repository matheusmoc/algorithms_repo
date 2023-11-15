# ABS retorna o valor absoluto de um número. 
# O argumento pode ser um inteiro, um número de ponto flutuante ou um objeto implementando __abs__() .

def printTwoElements( arr, size):
    for i in range(size):
        # ele verifica se o elemento atual já foi encontrado e se é é positivo
        if arr[abs(arr[i])-1] > 0:
            # Ele faz isso verificando se o valor no índice abs(arr[i])-1 é positivo. 
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            # Se for positivo, significa que este elemento ainda não foi encontrado, então ele nega o valor nesse índice
        else:
            # Se o valor em arr[abs(arr[i])-1] for negativo, isso significa que o elemento atual já foi encontrado antes. 
            # Nesse caso, ele imprime o elemento repetido.
            print("The repeating element is", abs(arr[i]))
             
    for i in range(size):
        if arr[i]>0:
            print("and the missing element is", i + 1)
 
# Driver program to test above function */
arr = [7, 3, 4, 5, 5, 6, 2]
n = len(arr)
printTwoElements(arr, n)

# No entanto se aparecer um número que já foi negado, ou seja, colocado como negativo, ao se repetir isso será depurado.

# Na segunda parte do código, ele percorre a matriz novamente.
# Se um valor no índice i é positivo, isso significa que o índice i + 1 não estava presente na matriz original (porque não foi negado). 
# Então, ele identifica esse índice como o elemento ausente.
