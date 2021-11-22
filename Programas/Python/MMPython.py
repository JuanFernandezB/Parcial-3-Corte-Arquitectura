
#David Zarate
#10 Noviembre
#Programa multiplicacion de matrices en python
#Se ingresa la dimension de la matriz (NXN) por argumento

#Para ejecutar : python3 nombre.py (dimension)
#                time python3 pythonMM.py 100

#Nombre archivo : pythonMM.py

import sys
import time
import numpy

#Se ingresa dimension de la matriz
N = int(sys.argv[1])

#Se crean las matrices (NxN) con numpy inicializados aleatoriamente

matA = numpy.random.uniform(low=0.75, high=1.25, size=(N,N))
matB = numpy.random.uniform(low=0.75, high=1.25, size=(N,N))
matC = numpy.zeros([N,N])

#Se crea la funcion para imprimir la matriz
def imprimirMatriz(matriz, T):
  for i in range(T):
    for j in range(T):
      print(round(matriz[i][j], 3), end=' ')
    print("\n")

def multiplicacionMatrices(matrizA, matrizB, T):
  matrizC = numpy.zeros([T,T])
  for i in range(T):
    for j in range(T):
      for k in range(T):
        matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

  return matrizC

'''
imprimirMatriz(matA, N)
print("==================================\n")
imprimirMatriz(matB, N)
print("==================================\n")
'''

inicio = time.time()
matC = multiplicacionMatrices(matA, matB, N)
final = time.time()
print(final-inicio)

#imprimirMatriz(matC, N)