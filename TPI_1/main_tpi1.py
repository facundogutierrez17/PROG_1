import biblioteca_tpi1 as b

calificaciones = [[0] * 5 for i in range(30)]

nombres = [""] * 30
generos = [""] * 30
legajos = [0] * 30
promedios = [0.0] * 30

cargados = False
promedios_listos = False

opcion = 0

while opcion != 8:

    b.mostrar_menu()

    dato = input("Ingrese una opción: ")

    if len(dato) == 1 and dato >= "1" and dato <= "8":
        opcion = int(dato)
    else:
        opcion = 0

    match opcion:

        case 1:
            b.cargar_datos(calificaciones, nombres,
                            generos, legajos)

            cargados = True
            promedios_listos = False

            print("Datos cargados correctamente.")

        case 2:
            if cargados:

                b.mostrar_todos(calificaciones, nombres,
                                generos, legajos,
                                promedios, False)

            else:
                print("Primero debe cargar los datos.")

        case 3:
            if cargados:

                promedios = b.calcular_promedios(calificaciones)

                promedios_listos = True

                print("Promedios calculados correctamente.")

            else:
                print("Primero debe cargar los datos.")

        case 4:
            if cargados and promedios_listos:

                b.ordenar_datos(calificaciones, nombres,
                                generos, legajos,
                                promedios, "DESC")

                b.mostrar_todos(calificaciones, nombres,
                                generos, legajos,
                                promedios, True)

            else:
                    print("Primero debe cargar los datos y calcular los promedios.")

        case 5:
            if cargados:

                b.mostrar_materias(calificaciones)

            else:
                print("Primero debe cargar los datos.")

        case 6:
            if cargados and promedios_listos:

                b.buscar_y_mostrar(legajos, calificaciones,
                                       nombres, generos, promedios)

            else:
                print("Primero debe cargar los datos y calcular los promedios.")

        case 7:
            if cargados:

                materia = input("Ingrese el número de materia (1-5): ")

                while not b.validar_materia(materia):
                    print("Error: ingrese un número entre 1 y 5.")
                    materia = input("Ingrese el número de materia (1-5): ")

                contador = b.contar_calificaciones(
                    calificaciones, int(materia))

                print("\nREPETICIONES DE CALIFICACIONES")

                for i in range(len(contador)):
                    print("Nota", i + 1, ":", contador[i])

            else:
                print("Primero debe cargar los datos.")

        case 8:
            print("Saliendo del programa...")

        case _:
            print("Opción inválida.")



