# ==================================================
# FUNCIONES DE VALIDACION
# ==================================================

def validar_nombre(nombre: str) -> bool:
    """
    Entrada: recibe el apellido y nombre del estudiante (str).
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


def cargar_legajo(estudiantes: list) -> int:
    """
    Entrada: recibe la lista de diccionarios de estudiantes.
    Proceso: solicita un legajo, verifica que tenga cinco cifras
    y que no se encuentre repetido.
    Salida: devuelve el legajo validado convertido a entero.
    """

    legajo = input("Ingrese legajo: ")

    while not validar_legajo(legajo) or buscar_legajo(estudiantes, int(legajo)) != -1:
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


def cargar_notas() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita y valida las cinco calificaciones
    correspondientes a las materias del estudiante.
    Salida: devuelve una lista con las cinco notas.
    """

    notas = [0] * 5

    for i in range(len(notas)):
        print("Materia", i + 1)
        notas[i] = cargar_nota()

    return notas


def cargar_datos() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita los datos de los 1000 estudiantes.
    Para cada uno crea un diccionario con legajo, nombre,
    género, notas y promedio inicial.
    Salida: devuelve la lista completa de diccionarios.
    """

    estudiantes = []

    for i in range(1000):

        print("\nESTUDIANTE", i + 1)

        estudiante = {}

        estudiante["Legajo"] = cargar_legajo(estudiantes)
        estudiante["Nombre"] = cargar_nombre()
        estudiante["Genero"] = cargar_genero()
        estudiante["Notas"] = cargar_notas()
        estudiante["Promedio"] = 0.0

        estudiantes += [estudiante]

    return estudiantes


# ==================================================
# FUNCIONES PARA MOSTRAR LOS DATOS
# ==================================================

def mostrar_encabezado() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: muestra los títulos de las columnas del informe.
    Salida: no devuelve valores. Imprime el encabezado.
    """

    print("\nLEGAJO | NOMBRE | GENERO | N1 | N2 | N3 | N4 | N5 | PROM")


def mostrar_uno(estudiante: dict) -> None:
    """
    Entrada: recibe el diccionario de un estudiante.
    Proceso: accede a sus claves y muestra el legajo, nombre,
    género, cinco calificaciones y promedio.
    Salida: no devuelve valores. Muestra un estudiante.
    """

    notas = estudiante["Notas"]

    print(estudiante["Legajo"], "|",
          estudiante["Nombre"], "|",
          estudiante["Genero"], "|",
          notas[0], "|",
          notas[1], "|",
          notas[2], "|",
          notas[3], "|",
          notas[4], "|",
          estudiante["Promedio"])


def mostrar_todos(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios de estudiantes.
    Proceso: recorre todos los diccionarios y llama a
    mostrar_uno() para mostrar los datos de cada estudiante.
    Salida: no devuelve valores. Muestra todos los estudiantes.
    """

    mostrar_encabezado()

    for i in range(len(estudiantes)):
        mostrar_uno(estudiantes[i])


# ==================================================
# FUNCION DE CALCULO DE PROMEDIOS
# ==================================================

def calcular_promedios(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios de estudiantes.
    Proceso: suma las cinco notas de cada estudiante,
    calcula el promedio y lo guarda en la clave Promedio.
    Salida: no devuelve valores. Modifica los diccionarios.
    """

    for i in range(len(estudiantes)):

        suma = 0

        for j in range(len(estudiantes[i]["Notas"])):
            suma += estudiantes[i]["Notas"][j]

        estudiantes[i]["Promedio"] = suma / len(estudiantes[i]["Notas"])


# ==================================================
# FUNCION DE ORDENAMIENTO
# ==================================================

def ordenar_datos(estudiantes: list, orden: str) -> None:
    """
    Entrada: recibe la lista de diccionarios y el criterio
    de ordenamiento (ASC o DESC).
    Proceso: utiliza el método burbuja para ordenar los
    diccionarios según el promedio de cada estudiante.
    Salida: no devuelve valores. Modifica el orden de la lista.
    """

    for i in range(len(estudiantes) - 1):

        for j in range(len(estudiantes) - 1 - i):

            intercambiar = False

            if orden == "ASC" and estudiantes[j]["Promedio"] > estudiantes[j + 1]["Promedio"]:
                intercambiar = True

            elif orden == "DESC" and estudiantes[j]["Promedio"] < estudiantes[j + 1]["Promedio"]:
                intercambiar = True

            if intercambiar:

                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]


# ==================================================
# FUNCIONES DE PROMEDIO POR MATERIA
# ==================================================

def promedio_materia(estudiantes: list, indice: int) -> float:
    """
    Entrada: recibe la lista de diccionarios y el índice
    de la materia.
    Proceso: suma las calificaciones de todos los estudiantes
    correspondientes a esa materia y divide por la cantidad
    de estudiantes.
    Salida: devuelve el promedio general de la materia (float).
    """

    suma = 0

    for i in range(len(estudiantes)):
        suma += estudiantes[i]["Notas"][indice]

    return suma / len(estudiantes)


def mostrar_materia(estudiantes: list, indice: int) -> None:
    """
    Entrada: recibe la lista de diccionarios y el índice
    de una materia.
    Proceso: calcula el promedio general de la materia
    y muestra su nombre y resultado.
    Salida: no devuelve valores. Muestra una materia.
    """

    promedio = promedio_materia(estudiantes, indice)

    print("MAT_", indice + 1, "- Promedio:", round(promedio, 2))


def mostrar_materias(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios de estudiantes.
    Proceso: calcula los promedios generales de las cinco
    materias, identifica el mayor y recorre nuevamente
    las materias para mostrar todas las que tengan ese promedio.
    Salida: no devuelve valores. Muestra las materias
    con mayor promedio general.
    """

    mayor = promedio_materia(estudiantes, 0)

    for j in range(1, 5):

        promedio = promedio_materia(estudiantes, j)

        if promedio > mayor:
            mayor = promedio

    for j in range(5):

        promedio = promedio_materia(estudiantes, j)

        if promedio == mayor:
            mostrar_materia(estudiantes, j)


# ==================================================
# FUNCIONES DE BUSQUEDA
# ==================================================

def buscar_legajo(estudiantes: list, buscado: int) -> int:
    """
    Entrada: recibe la lista de diccionarios y el número
    de legajo que se desea buscar.
    Proceso: recorre los diccionarios y compara el legajo
    de cada estudiante con el número buscado.
    Salida: devuelve la posición del estudiante si lo encuentra
    o -1 si no existe.
    """

    for i in range(len(estudiantes)):

        if estudiantes[i]["Legajo"] == buscado:
            return i

    return -1


def buscar_y_mostrar(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios de estudiantes.
    Proceso: solicita un legajo, lo valida y llama a
    buscar_legajo() para encontrar su posición.
    Si existe, muestra los datos del estudiante.
    Salida: no devuelve valores. Muestra el estudiante
    encontrado o informa que no existe.
    """

    dato = input("Ingrese el legajo a buscar: ")

    while not validar_legajo(dato):
        print("Error: legajo inválido.")
        dato = input("Ingrese el legajo a buscar: ")

    buscado = int(dato)

    posicion = buscar_legajo(estudiantes, buscado)

    if posicion != -1:

        mostrar_encabezado()
        mostrar_uno(estudiantes[posicion])

    else:
        print("No se encontró el estudiante.")


# ==================================================
# FUNCION DE CONTAR CALIFICACIONES
# ==================================================

def contar_calificaciones(estudiantes: list, materia: int) -> list:
    """
    Entrada: recibe la lista de diccionarios y el número
    de materia (del 1 al 5).
    Proceso: recorre las notas de todos los estudiantes
    en la materia seleccionada y cuenta las repeticiones
    de cada calificación del 1 al 10.
    Salida: devuelve una lista de diez elementos donde cada
    posición representa la cantidad de apariciones de una nota.
    """

    contador = [0] * 10

    for i in range(len(estudiantes)):

        nota = estudiantes[i]["Notas"][materia - 1]

        contador[nota - 1] += 1

    return contador


# ==================================================
# FUNCIONES DE LAS OPCIONES DEL MENU
# ==================================================

def opcion_1() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: llama a cargar_datos() para ingresar los datos
    de los 1000 estudiantes.
    Salida: devuelve la lista de diccionarios cargada.
    """

    estudiantes = cargar_datos()

    print("\nDatos cargados correctamente.")

    return estudiantes


def opcion_2(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios.
    Proceso: llama a mostrar_todos() para recorrer y mostrar
    todos los estudiantes.
    Salida: no devuelve valores. Muestra todos los datos.
    """

    mostrar_todos(estudiantes)


def opcion_3(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios.
    Proceso: llama a calcular_promedios() para calcular
    y guardar el promedio de cada estudiante.
    Salida: no devuelve valores. Modifica la clave Promedio.
    """

    calcular_promedios(estudiantes)

    print("\nPromedios calculados correctamente.")


def opcion_4(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios.
    Proceso: ordena los estudiantes por promedio descendente
    y llama a mostrar_todos() para mostrar el resultado.
    Salida: no devuelve valores. Ordena y muestra los estudiantes.
    """

    ordenar_datos(estudiantes, "DESC")

    mostrar_todos(estudiantes)


def opcion_5(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios.
    Proceso: llama a mostrar_materias() para identificar
    y mostrar las materias con mayor promedio general.
    Salida: no devuelve valores. Muestra las materias.
    """

    mostrar_materias(estudiantes)


def opcion_6(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios.
    Proceso: llama a buscar_y_mostrar() para localizar
    un estudiante por su legajo.
    Salida: no devuelve valores. Muestra los datos encontrados.
    """

    buscar_y_mostrar(estudiantes)


def opcion_7(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de diccionarios.
    Proceso: solicita una materia, valida el dato y llama
    a contar_calificaciones() para contar las repeticiones
    de cada nota.
    Salida: no devuelve valores. Muestra las frecuencias.
    """

    materia = input("Ingrese el número de materia (1-5): ")

    while not validar_materia(materia):
        print("Error: ingrese un número entre 1 y 5.")
        materia = input("Ingrese el número de materia (1-5): ")

    contador = contar_calificaciones(estudiantes, int(materia))

    print("\nREPETICIONES DE CALIFICACIONES")

    for i in range(len(contador)):
        print("Nota", i + 1, ":", contador[i])


def opcion_8() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: informa que el programa está finalizando.
    Salida: no devuelve valores. Muestra un mensaje por pantalla.
    """

    print("Saliendo del programa...")


# ==================================================
# FUNCION DEL MENU
# ==================================================

def mostrar_menu() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: muestra las opciones disponibles del programa.
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
