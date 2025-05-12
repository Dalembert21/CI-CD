from practica import saludar

def test_saludo_correcto():
    assert saludar() == "Hola esta es mi primera practica de CI/CD"

def test_saludo_incorrecto():
    #comparar si tienen el mismo dato
    assert saludar() == "Hola mundooooooooo"

def test_saludo_no_vacio():
    assert saludar() != ""

def test_saludo_contenido():
    assert "CI/CD" in saludar()
