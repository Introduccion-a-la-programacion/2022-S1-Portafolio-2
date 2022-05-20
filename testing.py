import Portafolio2;
import pytest;

p = Portafolio2

def test_invertirVector_1():
    assert p.invertirVector([50, 25, 89]) == [89, 25, 50]
    
def test_invertirVector_2():
    assert p.invertirVector([10]) == [10]
    
#########################################################################    
    
def test_diagonalInversa_1():
    assert p.diagonalInversa([[50, 25, 89], [2, 8, 9], [57, 32, 71]]) == [57, 8, 89]
    
def test_diagonalInversa_2():
    assert isinstance(str(p.diagonalInversa([[50, 25, 89, 10], [2, 8, 9, 4], [57, 32, 71, 11]])), str) == isinstance('Error: La matriz debe ser de tamaño de columnas impar',str)
    
#########################################################################    
    
def test_formarMatrizTriangularSuperior_1():
    assert p.formarMatrizTriangularSuperior(3) ==  [[1, 1, 1], [0, 1, 1], [0, 0, 1]]

def test_formarMatrizTriangularSuperior_2():
    assert p.formarMatrizTriangularSuperior(5) == [[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]    
    
#########################################################################    

def test_ordenarMatriz_1():
    assert p.ordenarMatriz([[50, 25, 89], [2, 8, 9], [57, 32, 71]]) == [[2, 8, 9], [50, 25, 89], [57, 32, 71]]
