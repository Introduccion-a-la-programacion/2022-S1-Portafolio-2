# 2022 S1 Portafolio #2

El archivo debe llamarse **Portafolio2.py**, además respetar el nombre de las funciones que más adelante se describen
Recordar hacer las validaciones de cada una de las restricciones

## invertirVector(vector)
Dado un parámetro **vector** diferente a vacio, la función debe revertir el orden de los valores del vector
No utilizar funciones como **reverse** o similares

```python
>>>invertirVector([50, 25, 89])
[89, 25, 50]
>>>invertirVector([10])
[10]
```

## diagonalInversa(matriz)
Dado una matriz **cuadrada**, devolver el vector de la diagonal forma, la matriz debe tener un número impar de filas y columnas

```python
>>>diagonalInversa([[50, 25, 89], [2, 8, 9], [57, 32, 71]])
[57, 8, 89]
>>>diagonalInversa([[50, 25, 89, 10], [2, 8, 9, 4], [57, 32, 71, 11]])
'Error: La matriz debe ser de tamaño de columnas impar'
```
## formarMatrizTriangularSuperior(tamano)
- Dado un parámetro llamado **tamano**, este determinará las dimensiones de una matriz cuadrada que este sea una triangular superior. 
- Una matriz triangular superior, es aquella que apartir de su diagonal estará compuesta por el valor de 1, y debajo de la diagonal estará lleno de ceros

```python
>>>formarMatrizTriangularSuperior(3)
[[1, 1, 1], [0, 1, 1], [0, 0, 1]]

>>>formarMatrizTriangularSuperior(5)
[[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]

```

## ordenarMatriz(matriz)
- Dado una matriz diferente a vacio y mayor tamaño 2, ordenar sus vectores haciendo uso de cualquier técnica de ordenamiento.
- Para ordenarlos, tomar en cuenta el primer valor del indice cero de cada vector para su ordenamiento

```python
>>>ordenarMatriz([[50, 25, 89], [2, 8, 9], [57, 32, 71]])
[[2, 8, 9], [50, 25, 89], [57, 32, 71]]

```
