#ESTRUCTURAS DISCRETAS I

def menu_inicial():

    try:
        opc = int(input("""
[1] Calcular las Combinaciones k de n elementos  
[2] Hallar Número de Disposiciones de Letras en un Texto
[3] Calcular Combinaciones de N Objetos 
[4] Lanzamiento de Monedas 
[5] Salir
"""))   
        if opc not in [1,2,3,4,5]:
            print("No se ha seleccionado una opción válida")
            menu_inicial()
            return

    except Exception:
        print("No se ha seleccionado una opción válida")
        menu_inicial()
        return
    
    #Ejecución Opciones del Menú

    match opc:
        case 1:
            ejercicio_1()
        case 2:
            ejercicio_2()
        case 3:
            ejercicio_3()
        case 4:
            ejercicios_4_5()
        case 5:
            quit()

#FUNCIONES RESOLUCIÓN EJERCICIOS

def ejercicio_1():
    pass

def ejercicio_2():
    pass

def ejercicio_3():
    pass

def ejercicio_4():
    print("""Una Moneda es Lanzada 10 veces
¿Cuantos Resultados Tienen Exactamente 3 Caras?""")
    n = 10
    r = 3

    nCr = factorial(n)/(factorial(r)*factorial(n-r))

    print(f"Existen un total de {nCr} resultados que tienen exactamente 3 caras")
    x = input()
    print("¿Cuantos Resultados Tienen a lo Sumo 3 Caras?")

    r = 3

    nCr = 0

    for i in range(0, r+1):
        nCr += factorial(n)/(factorial(i)*factorial(n-i))
    
    print(f"Existen un total de {nCr} resultados que tienen como máximo 3 caras")
    x = input()

    ejercicios_4_5()

def ejercicio_5():
    print("""¿De Cúantas Formas es Posible Distribuir 10 Monedas Idénticas entre 5 Niños?
Sin Restricciones:""")
     
    r = 5
    n = 10 + r - 1
    r = 10

    nCr = factorial(n)/(factorial(r)*factorial(n-r))

    print(f"Existen un total de {nCr} formas posibles de distribuir 10 monedas idénticas entre 5 niños cuando no hay restricciones")

    x = input()

    print("Cuando cada Niño Tiene Mínimo una Moneda:")
     
    r = 5
    n = 5 + r - 1
    r = 5

    nCr = factorial(n)/(factorial(r)*factorial(n-r))

    print(f"Existen un total de {nCr} formas posibles de distribuir 10 monedas idénticas entre 5 niños cuando cada niño tiene mínimo una moneda")

    x = input()

    print("Cuando el Niño Mayor Recibe al Menos 2 Monedas:")
     
    r = 5
    n = 8 + r - 1
    r = 8

    nCr = factorial(n)/(factorial(r)*factorial(n-r))

    print(f"Existen un total de {nCr} formas posibles de distribuir 10 monedas idénticas entre 5 niños cuando el Niño Mayor Recibe al Menos 2 Monedas")
    
    x = input()

    ejercicios_4_5()

def ejercicios_4_5():
    #Menu para Ejercicios 4 y 5
    try:
        opc = int(input("""
[1] Una Moneda es Lanzada 10 veces
    ¿Cuantos Resultados Tienen Exactamente 3 Caras?
    ¿Cuantos Resultados Tienen a lo Sumo 3 Caras?

[2] Hallar las Distribuciones en las que se Reparten 10 Monedas Idénticas entre 5 Niños
    Si no hay Restricciones
    Si cada Niño Recibe como Mínimo una Moneda
    Si el Niño Mayor Recibe como Mínimo dos Monedas

[3] Regresar
"""))   
        if opc not in [1,2,3]:
            print("No se ha seleccionado una opción válida")
            ejercicios_4_5()
            return

    except Exception:
        print("No se ha seleccionado una opción válida")
        ejercicios_4_5()
        return
    
    #Ejecución Opciones del Menú

    match opc:
        case 1:
            ejercicio_4()
        case 2:
            ejercicio_5()
        case 3:
            menu_inicial()

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    return fact


menu_inicial()