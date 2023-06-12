#ESTRUCTURAS DISCRETAS I

def menu_inicial():
    # Captura de la opcion
    try:
        opc = int(input("""
[1] Calcular las Combinaciones n de r elementos  
[2] Hallar Número de Disposiciones de Letras en un Texto
[3] Calcular Combinaciones de N Objetos 
[4] Lanzamiento de Monedas 
[5] Salir
>>> """))   
        if opc not in [1,2,3,4,5]:
            print(">>> No se ha seleccionado una opción válida")
            menu_inicial()
            return

    except Exception:
        print(">>> No se ha seleccionado una opción válida")
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
            pass

""" Resolucion de ejercicios """

def ejercicio_1():
    # Calcular las combinaciones de n en r elementos
    try:
        print(">>> Ingrese los valores a trabajar (cumpliendo la condición 0 <= r <= n)...")
        n = int(input(">>> Ingrese el valor de n: "))
        r = int(input(">>> Ingrese el valor de r: "))
        if (0 <= r  and  r <= n):
            comb = factorial(n) / (factorial(n-r) * factorial(r))
            print(f">>> La combinatoria de {r} de {n} elementos es de {comb}!")
            menu_inicial()
        else:
            print(">>> No ha ingresado correctamente los valores...")
            ejercicio_1()
    except:
        print(">>> Los valores de 'r' y 'n' tienen que ser numeros enteros...")

def ejercicio_2():
  texto = input(">>> Ingrese una palabra: ")
  if not " " in texto:
    texto = texto.upper()
    texto = "".join(c for c in texto if c.isalpha())
    frecuencias = {}
    for letra in texto:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    n = len(texto)
    n_factorial = factorial(n)
    denominador = 1
    for valor in frecuencias.values():
        denominador *= factorial(valor)
    print(f">>> El valor de las disposiciones de las letras en {texto} es de {n_factorial // denominador}...")
    menu_inicial()
  else:
      print(">>> Solo puede ingresar una palabra...")
      menu_inicial()

def ejercicio_3():
    try:
        n = int(input("Ingrese el valor de n: "))
        r = int(input("Ingrese el valor de r: "))
        # Función que calcula el número de combinaciones con repetición
        nr_factorial = factorial(n+r-1)
        r_factorial = factorial(r)
        n_factorial = factorial(n-1)
        print(f">>> El valor de la combinacion con repeticion de n = {n} y r = {r} es {nr_factorial // (r_factorial * n_factorial)}...")
        menu_inicial()
    except:
        print(">>> Ingrese valores enteros...")
        menu_inicial()

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

#Menu para Ejercicios 4 y 5
def ejercicios_4_5():
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