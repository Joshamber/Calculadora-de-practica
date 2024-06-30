#se importa la libreria de matematicas
import math

#Definimos las operaciones como la suma. resta, multiplicacion y otras

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        return "Error: Raíz cuadrada de un número negativo"
    return math.sqrt(a)

def ecuacion_primero_grado(a, b):
    if a == 0:
        return "No hay solución" if b != 0 else "Infinitas soluciones"
    return -b / a

def ecuacion_segundo_grado(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)

#aqui desarrollamos la calculadora definiendo su comportamiento y programacion de la misma

def calculadora():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Ecuación de primer grado")
    print("8. Ecuación de segundo grado")
    
    while True:
        try:
            operacion = int(input("Ingrese el número de la operación (1/2/3/4/5/6/7/8): "))
            if operacion in [1, 2, 3, 4, 5, 6, 7, 8]:
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Por favor, ingrese un número.")

    if operacion in [1, 2, 3, 4, 5]:
        while True:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Por favor, ingrese números válidos.")
    
        if operacion == 1:
            print(f"Resultado: {suma(num1, num2)}")
        elif operacion == 2:
            print(f"Resultado: {resta(num1, num2)}")
        elif operacion == 3:
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif operacion == 4:
            print(f"Resultado: {division(num1, num2)}")
        elif operacion == 5:
            print(f"Resultado: {potencia(num1, num2)}")

    elif operacion == 6:
        while True:
            try:
                num = float(input("Ingrese el número: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        print(f"Resultado: {raiz(num)}")

    elif operacion == 7:
        while True:
            try:
                a = float(input("Ingrese el coeficiente a (de ax + b = 0): "))
                b = float(input("Ingrese el coeficiente b (de ax + b = 0): "))
                break
            except ValueError:
                print("Por favor, ingrese números válidos.")
        
        print(f"Resultado: {ecuacion_primero_grado(a, b)}")

    elif operacion == 8:
        while True:
            try:
                a = float(input("Ingrese el coeficiente a (de ax^2 + bx + c = 0): "))
                b = float(input("Ingrese el coeficiente b (de ax^2 + bx + c = 0): "))
                c = float(input("Ingrese el coeficiente c (de ax^2 + bx + c = 0): "))
                break
            except ValueError:
                print("Por favor, ingrese números válidos.")
        
        resultado = ecuacion_segundo_grado(a, b, c)
        if isinstance(resultado, tuple):
            print(f"Las soluciones son: x1 = {resultado[0]}, x2 = {resultado[1]}")
        else:
            print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()