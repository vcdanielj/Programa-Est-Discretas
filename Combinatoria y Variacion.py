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


#FUNCIONES RESOLUCIÓN EJERCICIOS

def ejercicio_1():
    pass

def ejercicio_2():
    pass

def ejercicio_3():
    pass

def ejercicio_4():
    pass

def ejercicio_5():
    pass

def ejercicios_4_5():
    #Menu para Ejercicios 4 y 5
    try:
        opc = int(input("""
[1] Una Moneda es Lanzada 10 veces
    ¿Cuantos Resultados Tienen Exactamente 3 Caras?
    ¿Cuantos Resultados Tienen a lo Sumo 3 Caras?

[2] Hallar las Distribuciones en las que se Reparten 10 Monedas Idénticas entre 3 Niños
    Si no hay Restricciones
    Si cada Niño Recibe como Mínimo una Moneda
    Si el Niño Mayor Recibe como Mínimo dos Monedas

[3] Regresar
"""))   
        if opc not in [1,2,3]:
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
            ejercicio_4()
        case 2:
            ejercicio_5()
        case 3:
            menu_inicial()
