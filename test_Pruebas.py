import pytest 
from Pruebas import suma,resta,multiplicacion,division

def test_suma():
    assert suma(-2,-3) == -5
    print("La función suma trabaja correctamente")

def test_suma2():
    assert suma(51,6) == 57
    print("La función suma trabaja correctamente")
    
def test_resta():
    assert resta(2,-3) == 5
    print ("La funcion resta trabaja correctamente")
    
def test_resta2():
    assert resta (-2,2) == -4
    print ("La funcion resta trabaja correctamente")

def test_multiplicacion():
    assert multiplicacion (2,-3) == -6
    print ("La función multiplicacion trabaja correctamente")

def test_multiplicacion2():
    assert multiplicacion (-5,-5) == 25
    print ("La función multiplicacion trabaja correctamente")
    
def test_division():
    assert division (2,0) == None
    print ("La función division trabaja correctamente")
    
def test_division2():
    assert division (-4,2) == -2
    print ("La función division trabaja correctamente")
    
def test_division3():
    assert division (-8,-4) == 2
    print ("La función division trabaja correctamente")
    
    
