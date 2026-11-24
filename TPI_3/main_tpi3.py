import biblioteca_tpi3 as b

estudiantes = []

cargados = False
promedios_listos = False

opcion = 0

while opcion != 10:

    b.mostrar_menu()

    dato = input("Ingrese una opción: ")

    if dato == "1" or dato == "2" or dato == "3" or dato == "4" or dato == "5" or dato == "6" or dato == "7" or dato == "8" or dato == "9" or dato == "10":
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
            cargados = True
            promedios_listos = False

        case 3:
            if cargados:
                b.opcion_3(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 4:
            if cargados:
                b.opcion_4(estudiantes)
                promedios_listos = True
            else:
                print("Primero debe cargar los datos.")

        case 5:
            if cargados and promedios_listos:
                b.opcion_5(estudiantes)
            elif not cargados:
                print("Primero debe cargar los datos.")
            else:
                print("Primero debe calcular los promedios.")

        case 6:
            if cargados:
                b.opcion_6(estudiantes)
            else:
                print("Primero debe cargar los datos.")

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
            if cargados:
                b.opcion_9(estudiantes)
            else:
                print("Primero debe cargar los datos.")

        case 10:
            b.opcion_10()

        case _:
            print("Opción inválida.")
