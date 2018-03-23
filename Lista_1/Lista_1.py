import numpy as np
import sys
import ipdb
import time

# parametros do algoritmo
quantidade_numeros = 100000
limite_inferior = 0
limite_superior = quantidade_numeros*10
gap_percentage = 10 #max value for this is 100

lista_de_valores = list(
    np.linspace(limite_inferior, limite_superior, num=quantidade_numeros, endpoint=False, dtype=int)
    )

vetor_de_indice = [i*gap_percentage for i in range(quantidade_numeros//gap_percentage)]
vetor_de_indice.append(quantidade_numeros-1)

def busca_binaria(lista, valor):
    posicao = -1
    if lista:
        l = 0
        r = len(lista)-1
        mid = (l+r)//2
        if(l<r):
            if(lista[mid] == valor):
                posicao = mid
            elif (lista[mid] < valor):
                posicao = mid + 1 + busca_binaria(lista[mid+1:], valor)
            else:
                posicao = l + busca_binaria(lista[:mid], valor)
        elif lista[0] == valor:
            posicao = 0
    return posicao

# Busca sequencial no indice da lista 
def busca_no_indice(indice, lista, valor):
    indice_fim = len(indice)-1
    encontrou_maior = False #flag
    posicao = -1
    
    if indice and lista:
        if lista[indice[0]] <= valor and lista[indice[indice_fim]] > valor:
            for i in range (indice_fim+1):
                if (not encontrou_maior) and lista[indice[i]] > valor:
                    posicao_relativa = busca_binaria(lista[indice[(i-1)]:indice[i]], valor)
                    if not(posicao_relativa == -1):
                        posicao = indice[i-1] + posicao_relativa
                    encontrou_maior = True
        elif lista[indice[indice_fim]] == valor:
            posicao = indice[indice_fim]

    return posicao


def main():
    n = input('Digite o valor que deseja procurar no vetor: \n')
    start = time.time()
    value = int(n)
    posicao = busca_no_indice(vetor_de_indice, lista_de_valores, value)
    if posicao >= 0:
        pass
        print "O valor esta localizado na posicao: ", posicao
    else:
        pass
        print "valor nao encontrado"

    end = time.time()
    print(end - start)

def performance():
    start = time.time()
    for n in lista_de_valores:
        value = int(n)
        posicao = busca_no_indice(vetor_de_indice, lista_de_valores, value)
        if posicao >= 0:
            pass
        else:
            pass

    end = time.time()
    print("Tempo de resposta: ", end - start)

if __name__ == '__main__':
    n = int(input('0 - Performance Automatica\n1 - Busca Manual: \n'))
    
    if n:
        main()
    else:
        performance()
