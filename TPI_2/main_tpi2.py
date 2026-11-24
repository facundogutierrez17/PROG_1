import biblioteca_tpi2 as b

# Inicialización de la lista de diccionarios

estudiantes = []

cargados = False
promedios_listos = False

opcion = 0


# =========================
# MENU PRINCIPAL
# =========================

while opcion != 8:

    b.mostrar_menu()

    dato = input("Ingrese una opción: ")

    if len(dato) == 1 and dato >= "1" and dato <= "8":
        opcion = int(dato)
    else:
        opcion = 0

    match opcion:

        case 1:
            estudiantes = b.opcion_1()

            cargados = True
            promedios_listos = False

        case 2:
            if cargados:

                b.opcion_2(estudiantes)

            else:
                print("Primero debe cargar los datos.")

        case 3:
            if cargados:

                b.opcion_3(estudiantes)

                promedios_listos = True

            else:
                print("Primero debe cargar los datos.")

        case 4:
            if cargados and promedios_listos:

                b.opcion_4(estudiantes)

            elif not cargados:
                print("Primero debe cargar los datos.")

            else:
                print("Primero debe calcular los promedios.")

        case 5:
            if cargados:

                b.opcion_5(estudiantes)

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
            if cargados:

                b.opcion_7(estudiantes)

            else:
                print("Primero debe cargar los datos.")

        case 8:
            b.opcion_8()

        case _:
            print("Opción inválida.")
