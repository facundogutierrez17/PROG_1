# ==================================================
# FUNCIONES DE VALIDACION
# ==================================================

def validar_nombre(nombre: str) -> bool:
    """
    Entrada: recibe el nombre del estudiante (str).
    Proceso: verifica que contenga solamente letras y espacios.
    Salida: devuelve True si es válido o False si no lo es.
    """

    if len(nombre) == 0:
        return False

    for caracter in nombre:
        if not (("a" <= caracter.lower() <= "z") or
                caracter in "áéíóúÁÉÍÓÚñÑ "):
            return False

    return True


def validar_genero(genero: str) -> bool:
    """
    Entrada: recibe el género del estudiante (str).
    Proceso: convierte el dato a mayúscula y verifica que sea F, M o X.
    Salida: devuelve True si es válido o False si no lo es.
    """

    genero = genero.upper()

    return genero == "F" or genero == "M" or genero == "X"


def validar_legajo(legajo: str) -> bool:
    """
    Entrada: recibe el legajo como texto (str).
    Proceso: verifica que tenga exactamente cinco cifras numéricas
    y que no comience con cero.
    Salida: devuelve True si es válido o False si no lo es.
    """

    if len(legajo) != 5:
        return False

    for caracter in legajo:
        if caracter < "0" or caracter > "9":
            return False

    if legajo[0] == "0":
        return False

    return True


def validar_nota(nota: str) -> bool:
    """
    Entrada: recibe una calificación como texto (str).
    Proceso: verifica que sea un número entero entre 1 y 10.
    Salida: devuelve True si es válida o False si no lo es.
    """

    if len(nota) == 0:
        return False

    for caracter in nota:
        if caracter < "0" or caracter > "9":
            return False

    numero = int(nota)

    return numero >= 1 and numero <= 10


def validar_materia(materia: str) -> bool:
    """
    Entrada: recibe el número de materia como texto (str).
    Proceso: verifica que sea un número entero entre 1 y 5.
    Salida: devuelve True si es válido o False si no lo es.
    """

    if len(materia) == 0:
        return False

    for caracter in materia:
        if caracter < "0" or caracter > "9":
            return False

    numero = int(materia)

    return numero >= 1 and numero <= 5


# ==================================================
# FUNCIONES DE CARGA
# ==================================================

def cargar_nombre() -> str:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita el apellido y nombre del estudiante
    y valida que contenga solamente letras y espacios.
    Salida: devuelve el nombre validado (str).
    """

    nombre = input("Ingrese apellido y nombre: ")

    while not validar_nombre(nombre):
        print("Error: ingrese solamente letras.")
        nombre = input("Ingrese apellido y nombre: ")

    return nombre


def cargar_genero() -> str:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita el género y verifica que sea F, M o X,
    aceptando mayúsculas y minúsculas.
    Salida: devuelve el género validado en mayúscula (str).
    """

    genero = input("Ingrese género (F/M/X): ")

    while not validar_genero(genero):
        print("Error: ingrese F, M o X.")
        genero = input("Ingrese género (F/M/X): ")

    return genero.upper()


def cargar_legajo(legajos: list) -> int:
    """
    Entrada: recibe la lista de legajos.
    Proceso: solicita un legajo, verifica que tenga cinco cifras
    y que no se encuentre repetido en la lista.
    Salida: devuelve el legajo validado convertido a entero.
    """

    legajo = input("Ingrese legajo: ")

    while not validar_legajo(legajo) or int(legajo) in legajos:
        print("Error: legajo inválido o repetido.")
        legajo = input("Ingrese legajo: ")

    return int(legajo)


def cargar_nota() -> int:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita una calificación y verifica que sea
    un número entero entre 1 y 10.
    Salida: devuelve la nota validada convertida a entero.
    """

    nota = input("Ingrese calificación (1-10): ")

    while not validar_nota(nota):
        print("Error: ingrese una nota entre 1 y 10.")
        nota = input("Ingrese calificación (1-10): ")

    return int(nota)


def cargar_datos(calificaciones: list, nombres: list,
                 generos: list, legajos: list) -> None:
    """
    Entrada: recibe la matriz de calificaciones y las listas
    de nombres, géneros y legajos.
    Proceso: solicita y valida los datos de los 30 estudiantes
    y sus cinco calificaciones. Reinicia los legajos para
    permitir una nueva carga sin conservar datos anteriores.
    Salida: no devuelve valores. Modifica la matriz y las listas.
    """

    for i in range(len(legajos)):
        legajos[i] = 0

    for i in range(len(nombres)):

        print("\nESTUDIANTE", i + 1)

        nombres[i] = cargar_nombre()
        generos[i] = cargar_genero()
        legajos[i] = cargar_legajo(legajos)

        for j in range(len(calificaciones[i])):
            print("Materia", j + 1)
            calificaciones[i][j] = cargar_nota()


# ==================================================
# FUNCIONES PARA MOSTRAR LOS DATOS
# ==================================================

def mostrar_uno(calificaciones: list, nombres: list,
                generos: list, legajos: list,
                promedios: list, i: int,
                mostrar_promedio: bool) -> None:
    """
    Entrada: recibe la matriz, las listas paralelas, la lista
    de promedios, el índice del estudiante y un valor booleano.
    Proceso: muestra los datos correspondientes al estudiante
    ubicado en la posición indicada. El booleano determina
    si se muestra o no el promedio.
    Salida: no devuelve valores. Muestra los datos por pantalla.
    """

    print("\nLegajo:", legajos[i])
    print("Nombre:", nombres[i])
    print("Género:", generos[i])

    for j in range(len(calificaciones[i])):
        print("Materia", j + 1, ":", calificaciones[i][j])

    if mostrar_promedio:
        print("Promedio:", promedios[i])


def mostrar_todos(calificaciones: list, nombres: list,
                  generos: list, legajos: list,
                  promedios: list,
                  mostrar_promedio: bool) -> None:
    """
    Entrada: recibe la matriz, las listas paralelas,
    la lista de promedios y un valor booleano.
    Proceso: recorre todos los estudiantes y llama a mostrar_uno()
    para mostrar los datos de cada uno.
    Salida: no devuelve valores. Muestra todos los estudiantes.
    """

    for i in range(len(nombres)):

        print("\n-------------------------")

        mostrar_uno(calificaciones, nombres, generos,
                    legajos, promedios, i, mostrar_promedio)


# ==================================================
# FUNCION DE CALCULO DE PROMEDIOS
# ==================================================

def calcular_promedios(calificaciones: list) -> list:
    """
    Entrada: recibe la matriz de calificaciones.
    Proceso: suma las cinco notas de cada estudiante y divide
    el resultado por la cantidad de materias.
    Salida: devuelve una lista con el promedio de cada estudiante.
    """

    promedios = [0.0] * len(calificaciones)

    for i in range(len(calificaciones)):

        suma = 0

        for j in range(len(calificaciones[i])):
            suma += calificaciones[i][j]

        promedios[i] = suma / len(calificaciones[i])

    return promedios


# ==================================================
# FUNCION DE ORDENAMIENTO
# ==================================================

def ordenar_datos(calificaciones: list, nombres: list,
                  generos: list, legajos: list,
                  promedios: list, orden: str) -> None:
    """
    Entrada: recibe la matriz, las listas paralelas,
    la lista de promedios y el criterio de ordenamiento (ASC/DESC).
    Proceso: utiliza el método burbuja para ordenar los estudiantes
    según sus promedios. Intercambia también las posiciones
    correspondientes de todas las estructuras.
    Salida: no devuelve valores. Modifica y ordena las estructuras.
    """

    for i in range(len(promedios) - 1):

        for j in range(len(promedios) - 1 - i):

            intercambiar = False

            if orden == "ASC" and promedios[j] > promedios[j + 1]:
                intercambiar = True

            elif orden == "DESC" and promedios[j] < promedios[j + 1]:
                intercambiar = True

            if intercambiar:

                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]

                calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]

                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

                generos[j], generos[j + 1] = generos[j + 1], generos[j]

                legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]


# ==================================================
# FUNCIONES DE PROMEDIO POR MATERIA
# ==================================================

def promedio_materia(calificaciones: list, j: int) -> float:
    """
    Entrada: recibe la matriz de calificaciones y el índice
    de la materia (columna).
    Proceso: suma las calificaciones de todos los estudiantes
    en esa materia y divide por la cantidad de estudiantes.
    Salida: devuelve el promedio general de la materia (float).
    """

    suma = 0

    for i in range(len(calificaciones)):
        suma += calificaciones[i][j]

    return suma / len(calificaciones)


def mostrar_materia(calificaciones: list, j: int) -> None:
    """
    Entrada: recibe la matriz de calificaciones y el índice
    de la materia.
    Proceso: calcula el promedio general de la materia
    y muestra su nombre y resultado.
    Salida: no devuelve valores. Muestra una materia por pantalla.
    """

    promedio = promedio_materia(calificaciones, j)

    print("MATERIA", j + 1, "- Promedio:", round(promedio, 2))


def mostrar_materias(calificaciones: list) -> None:
    """
    Entrada: recibe la matriz de calificaciones.
    Proceso: calcula los promedios generales de las materias,
    identifica el mayor y recorre nuevamente las columnas
    para mostrar todas las materias que tengan ese promedio.
    Salida: no devuelve valores. Muestra las materias con
    mayor promedio general.
    """

    mayor = promedio_materia(calificaciones, 0)

    for j in range(1, len(calificaciones[0])):

        promedio = promedio_materia(calificaciones, j)

        if promedio > mayor:
            mayor = promedio

    for j in range(len(calificaciones[0])):

        promedio = promedio_materia(calificaciones, j)

        if promedio == mayor:
            mostrar_materia(calificaciones, j)


# ==================================================
# FUNCIONES DE BUSQUEDA
# ==================================================

def buscar_legajo(legajos: list, buscado: int) -> int:
    """
    Entrada: recibe la lista de legajos y el número de legajo
    que se desea buscar.
    Proceso: recorre la lista y compara cada elemento
    con el legajo buscado.
    Salida: devuelve la posición del legajo si lo encuentra
    o -1 si no existe.
    """

    for i in range(len(legajos)):

        if legajos[i] == buscado:
            return i

    return -1


def buscar_y_mostrar(legajos: list, calificaciones: list,
                     nombres: list, generos: list,
                     promedios: list) -> None:
    """
    Entrada: recibe las listas de legajos, nombres, géneros,
    promedios y la matriz de calificaciones.
    Proceso: solicita un legajo, lo valida y llama a buscar_legajo()
    para encontrar su posición. Si existe, llama a mostrar_uno().
    Salida: no devuelve valores. Muestra los datos del estudiante
    encontrado o informa que no existe.
    """

    dato = input("Ingrese el legajo a buscar: ")

    while not validar_legajo(dato):
        print("Error: legajo inválido.")
        dato = input("Ingrese el legajo a buscar: ")

    buscado = int(dato)

    posicion = buscar_legajo(legajos, buscado)

    if posicion != -1:

        mostrar_uno(calificaciones, nombres, generos,
                    legajos, promedios, posicion, True)

    else:
        print("No se encontró el estudiante.")


# ==================================================
# FUNCION DE CONTAR CALIFICACIONES
# ==================================================

def contar_calificaciones(calificaciones: list,
                          materia: int) -> list:
    """
    Entrada: recibe la matriz de calificaciones y el número
    de materia (del 1 al 5).
    Proceso: recorre la columna correspondiente y cuenta
    cuántas veces aparece cada calificación del 1 al 10.
    Salida: devuelve una lista de diez elementos donde cada
    posición representa la cantidad de apariciones de una nota.
    """

    contador = [0] * 10

    for i in range(len(calificaciones)):

        nota = calificaciones[i][materia - 1]

        contador[nota - 1] += 1

    return contador


# ==================================================
# FUNCION DEL MENU
# ==================================================

def mostrar_menu() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: muestra por pantalla las opciones disponibles
    para operar el programa.
    Salida: no devuelve valores. Imprime el menú.
    """

    print("\n========= MENU =========")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedios")
    print("4 - Ordenar por promedio DESC")
    print("5 - Materias con mayor promedio")
    print("6 - Buscar estudiante por legajo")
    print("7 - Contar calificaciones por materia")
    print("8 - Salir")
    print("========================")
