import numpy as np
import sys


# Gera valores aleatorios
def valor_aleatorio():
    valor = np.random.randint(0, 1000)
    return valor

# Gera um vetor de tamanho 1001  com valores inteiros aleatorios > 10000
lista_de_valores = np.linspace(0, 10000, num=101, endpoint=False, dtype=int)
print (lista_de_valores)

# Converte a lista de valores aleatorios para array numpy
vetor = np.asarray(lista_de_valores)

# Gera uma lista de valores para servir como base para o intervalo do vetor_de_index
lista_de_index = []
for index in range(101):
    lista_de_index.append(index)

# Cria o vetor de index com um intervalo de 10
vetor_de_index = [index for index in lista_de_index if index % 10 == 0]
print (vetor_de_index)

# Faz a indexacao do vetor
print(vetor[np.array(vetor_de_index)])


def busca_binaria(array, valor):
    l = 0
    r = len(array)-1
    mid = (l+r)/2

    while(l < r):
        if(array[mid] == valor):
            return mid
        elif (array[mid] < valor):
            return mid + 1 + busca_binaria(array[mid+1:], valor)
        else:
            return busca_binaria(array[:mid], valor)

    if (array[mid] != valor):
        print "valor nao encontrado"
        return -1

    return mid


def main():
    n = input('Digite o valor que deseja procurar no vetor: \n')
    value = int(n)

    print "O valor esta localizado na posicao: ", busca_binaria(vetor_de_index, value)


if __name__ == '__main__':
    main()
