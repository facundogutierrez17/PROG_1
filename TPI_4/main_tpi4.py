import biblioteca_tpi4 as b

estudiantes = []

cargados = False
promedios_listos = False

opcion = 0

while opcion != 12:

    b.mostrar_menu()

    dato = input("Ingrese una opción: ")

    if b.es_entero(dato):
        opcion = int(dato)
    else:
        opcion = 0

    match opcion:

        case 1:
            estudiantes = b.opcion_1()

            if len(estudiantes) > 0:
                cargados = True
                promedios_listos = False
            else:
                cargados = False
                promedios_listos = False

        case 2:
            estudiantes = b.opcion_2()

            if len(estudiantes) > 0:
                cargados = True
                promedios_listos = False
            else:
                cargados = False
                promedios_listos = False

        case 3:
            if cargados:
                b.opcion_3(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 4:
            if cargados:
                b.opcion_4(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 5:
            if cargados:
                b.opcion_5(estudiantes)
                promedios_listos = True
            else:
                print("Primero debe cargar los datos.")

        case 6:
            if cargados and promedios_listos:
                b.opcion_6(estudiantes)
            elif not cargados:
                print("Primero debe cargar los datos.")
            else:
                print("Primero debe calcular los promedios.")

        case 7:
            if cargados and promedios_listos:
                b.opcion_7(estudiantes)
            elif not cargados:
                print("Primero debe cargar los datos.")
            else:
                print("Primero debe calcular los promedios.")

        case 8:
            if cargados:
                b.opcion_8(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 9:
            if cargados and promedios_listos:
                b.opcion_9(estudiantes)
            elif not cargados:
                print("Primero debe cargar los datos.")
            else:
                print("Primero debe calcular los promedios.")

        case 10:
            if cargados:
                b.opcion_10(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 11:
            if cargados:
                b.opcion_11(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 12:
            b.opcion_12()

        case _:
            print("Opción inválida.")
