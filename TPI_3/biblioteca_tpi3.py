import csv
import json


# --------------------------------------------------
# VALIDACIONES
# --------------------------------------------------

def validar_legajo(legajo: str) -> bool:
    """
    Entrada: recibe el legajo como texto.
    Proceso: verifica que tenga cinco cifras numéricas.
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


def validar_nombre(nombre: str) -> bool:
    """
    Entrada: recibe el nombre y apellido.
    Proceso: verifica que contenga solamente letras y espacios.
    Salida: devuelve True si es válido o False si no lo es.
    """
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
    letras += "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

    if nombre == "":
        return False

    for caracter in nombre:
        if caracter not in letras and caracter != " ":
            return False

    return True


def validar_genero(genero: str) -> bool:
    """
    Entrada: recibe el género.
    Proceso: comprueba que sea F, M o X.
    Salida: devuelve True si es válido o False si no lo es.
    """
    if genero == "F" or genero == "M" or genero == "X":
        return True

    return False


def validar_nota(nota: str) -> bool:
    """
    Entrada: recibe una nota como texto.
    Proceso: verifica que sea un número entero entre 1 y 10.
    Salida: devuelve True si es válida o False si no lo es.
    """
    if nota == "":
        return False

    for caracter in nota:
        if caracter < "0" or caracter > "9":
            return False

    if int(nota) >= 1 and int(nota) <= 10:
        return True

    return False


def validar_materia(materia: str) -> bool:
    """
    Entrada: recibe el número de materia.
    Proceso: verifica que esté entre 1 y 5.
    Salida: devuelve True si es válido o False si no lo es.
    """
    if materia == "1" or materia == "2" or materia == "3" or materia == "4" or materia == "5":
        return True

    return False


# --------------------------------------------------
# BÚSQUEDA DE LEGAJO
# --------------------------------------------------

def buscar_legajo(estudiantes: list, buscado: int) -> int:
    """
    Entrada: recibe la lista de estudiantes y un legajo.
    Proceso: recorre la lista buscando el legajo indicado.
    Salida: devuelve la posición del estudiante o -1 si no existe.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == buscado:
            return i

    return -1


# --------------------------------------------------
# CARGA DE DATOS POR CONSOLA
# --------------------------------------------------

def cargar_legajo(estudiantes: list) -> int:
    """
    Entrada: recibe la lista de estudiantes cargados.
    Proceso: solicita un legajo, lo valida y comprueba que no esté repetido.
    Salida: devuelve el legajo como entero.
    """
    valido = False

    while not valido:
        dato = input("Ingrese legajo de cinco cifras: ")

        if validar_legajo(dato):
            legajo = int(dato)

            if buscar_legajo(estudiantes, legajo) == -1:
                valido = True
            else:
                print("Error: el legajo ya existe.")
        else:
            print("Error: el legajo debe tener cinco cifras.")

    return legajo


def cargar_nombre() -> str:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita el nombre y valida que contenga letras y espacios.
    Salida: devuelve el nombre ingresado.
    """
    valido = False

    while not valido:
        nombre = input("Ingrese apellido y nombre: ")

        if validar_nombre(nombre):
            valido = True
        else:
            print("Error: ingrese solamente letras y espacios.")

    return nombre


def cargar_genero() -> str:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita el género y valida F, M o X.
    Salida: devuelve el género en mayúscula.
    """
    valido = False

    while not valido:
        genero = input("Ingrese género (F/M/X): ")
        genero = genero.upper()

        if validar_genero(genero):
            valido = True
        else:
            print("Error: ingrese F, M o X.")

    return genero


def cargar_nota() -> int:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita una nota y valida que sea un entero entre 1 y 10.
    Salida: devuelve la nota como entero.
    """
    valido = False

    while not valido:
        dato = input("Ingrese nota (1 a 10): ")

        if validar_nota(dato):
            valido = True
        else:
            print("Error: la nota debe ser un entero entre 1 y 10.")

    return int(dato)


def cargar_notas() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita las cinco notas del estudiante.
    Salida: devuelve una lista con las cinco notas.
    """
    notas = []

    for i in range(5):
        print("Materia", i + 1)
        nota = cargar_nota()
        notas += [nota]

    return notas


def cargar_un_estudiante(estudiantes: list) -> dict:
    """
    Entrada: recibe la lista de estudiantes cargados.
    Proceso: solicita y valida todos los datos de un estudiante.
    Salida: devuelve un diccionario con los datos del estudiante.
    """
    estudiante = {}

    estudiante["legajo"] = cargar_legajo(estudiantes)
    estudiante["nombre"] = cargar_nombre()
    estudiante["genero"] = cargar_genero()
    estudiante["notas"] = cargar_notas()
    estudiante["promedio"] = None

    return estudiante


def cargar_datos_manual() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: carga por consola los datos de 1000 estudiantes.
    Salida: devuelve la lista de diccionarios.
    """
    estudiantes = []

    for i in range(1000):
        print("\nESTUDIANTE", i + 1)
        estudiante = cargar_un_estudiante(estudiantes)
        estudiantes += [estudiante]

    return estudiantes


# --------------------------------------------------
# CARGA DESDE ARCHIVO CSV
# --------------------------------------------------

def cargar_datos_csv(ruta: str) -> list:
    """
    Entrada: recibe la ruta o nombre del archivo CSV.
    Proceso: lee cada fila, valida sus datos y agrega los estudiantes válidos.
    Salida: devuelve una lista de diccionarios.
    """
    estudiantes = []

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:

            numero_fila = 0

            for linea in archivo:
                
                numero_fila += 1

                fila = linea.strip().split(",")
                
                print(fila)
                
                print("Cantidad de campos:", len(fila))
                
                if len(fila) == 9:
                    legajo = fila[0].strip()
                    nombre = fila[1].strip()
                    genero = fila[2].strip().upper()

                    if validar_legajo(legajo) and validar_nombre(nombre) and validar_genero(genero):

                        if buscar_legajo(estudiantes, int(legajo)) == -1:
                            notas_validas = True
                            notas = []

                            for i in range(3, 8):
                                dato_nota = fila[i].strip()

                                if validar_nota(dato_nota):
                                    notas += [int(dato_nota)]
                                else:
                                    notas_validas = False

                            if notas_validas:
                                estudiante = {
                                    "legajo": int(legajo),
                                    "nombre": nombre,
                                    "genero": genero,
                                    "notas": notas,
                                    "promedio": None
                                }

                                estudiantes += [estudiante]
                            else:
                                print("Fila", numero_fila, ": contiene notas inválidas.")
                        else:
                            print("Fila", numero_fila, ": legajo repetido.")
                    else:
                        print("Fila", numero_fila, ": contiene datos inválidos.")
                else:
                    print("Fila", numero_fila, ": cantidad incorrecta de campos.")

        print("\nSe cargaron", len(estudiantes), "estudiantes desde el CSV.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")
    except OSError:
        print("Error al intentar leer el archivo.")

    return estudiantes


# --------------------------------------------------
# MOSTRAR DATOS
# --------------------------------------------------

def mostrar_encabezado() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: muestra los títulos de las columnas.
    Salida: imprime el encabezado del informe.
    """
    print("\nLEGAJO | NOMBRE | GENERO | N1 | N2 | N3 | N4 | N5 | PROM")
    print("-" * 85)


def mostrar_uno(estudiante: dict) -> None:
    """
    Entrada: recibe un diccionario de estudiante.
    Proceso: muestra todos los datos del estudiante en una fila.
    Salida: imprime los datos.
    """
    notas = estudiante["notas"]

    if estudiante["promedio"] is None:
        promedio = "-"
    else:
        promedio = round(estudiante["promedio"], 2)

    print(
        estudiante["legajo"], "|",
        estudiante["nombre"], "|",
        estudiante["genero"], "|",
        notas[0], "|",
        notas[1], "|",
        notas[2], "|",
        notas[3], "|",
        notas[4], "|",
        promedio
    )


def mostrar_todos(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: recorre la lista y llama a mostrar_uno para cada estudiante.
    Salida: imprime todos los estudiantes.
    """
    mostrar_encabezado()

    for estudiante in estudiantes:
        mostrar_uno(estudiante)


# --------------------------------------------------
# CÁLCULO DE PROMEDIOS
# --------------------------------------------------

def calcular_promedio(estudiante: dict) -> float:
    """
    Entrada: recibe un diccionario de estudiante.
    Proceso: suma las cinco notas y calcula su promedio.
    Salida: devuelve el promedio calculado.
    """
    suma = 0

    for nota in estudiante["notas"]:
        suma += nota

    return suma / 5


def calcular_promedios(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: calcula el promedio de cada uno y lo guarda en su diccionario.
    Salida: modifica la clave promedio de cada estudiante.
    """
    for estudiante in estudiantes:
        estudiante["promedio"] = calcular_promedio(estudiante)

    print("Se calcularon los promedios correctamente.")


# --------------------------------------------------
# ORDENAMIENTO
# --------------------------------------------------

def ordenar_estudiantes(estudiantes: list, orden: str) -> None:
    """
    Entrada: recibe la lista de estudiantes y el orden ASC o DESC.
    Proceso: ordena los diccionarios según su promedio mediante burbuja.
    Salida: modifica la lista original.
    """
    for i in range(len(estudiantes) - 1):
        for j in range(len(estudiantes) - 1 - i):

            if orden == "ASC":
                condicion = estudiantes[j]["promedio"] > estudiantes[j + 1]["promedio"]
            else:
                condicion = estudiantes[j]["promedio"] < estudiantes[j + 1]["promedio"]

            if condicion:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]


# --------------------------------------------------
# PROMEDIO GENERAL POR MATERIA
# --------------------------------------------------

def promedio_materia(estudiantes: list, indice: int) -> float:
    """
    Entrada: recibe la lista de estudiantes y el índice de una materia.
    Proceso: suma las notas de esa materia y calcula el promedio general.
    Salida: devuelve el promedio de la materia.
    """
    suma = 0

    for estudiante in estudiantes:
        suma += estudiante["notas"][indice]

    return suma / len(estudiantes)


def mostrar_materia(estudiantes: list, indice: int) -> None:
    """
    Entrada: recibe la lista de estudiantes y el índice de una materia.
    Proceso: calcula y muestra el promedio de esa materia.
    Salida: imprime el nombre y el promedio de la materia.
    """
    promedio = promedio_materia(estudiantes, indice)
    print("MAT_" + str(indice + 1), ":", round(promedio, 2))


def mostrar_materias_mayor_promedio(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: calcula los promedios de las cinco materias y busca el mayor.
    Salida: muestra todas las materias que tienen el mayor promedio.
    """
    if len(estudiantes) == 0:
        print("No hay estudiantes cargados.")
        return

    mayor = promedio_materia(estudiantes, 0)

    for i in range(1, 5):
        promedio = promedio_materia(estudiantes, i)

        if promedio > mayor:
            mayor = promedio

    print("\nMATERIA/S CON MAYOR PROMEDIO GENERAL")

    for i in range(5):
        promedio = promedio_materia(estudiantes, i)

        if promedio == mayor:
            mostrar_materia(estudiantes, i)


# --------------------------------------------------
# BÚSQUEDA Y MUESTRA POR LEGAJO
# --------------------------------------------------

def buscar_y_mostrar(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita un legajo, lo valida, lo busca y muestra sus datos.
    Salida: imprime el estudiante encontrado o un mensaje si no existe.
    """
    valido = False

    while not valido:
        dato = input("Ingrese el legajo a buscar: ")

        if validar_legajo(dato):
            valido = True
        else:
            print("Error: el legajo debe tener cinco cifras.")

    posicion = buscar_legajo(estudiantes, int(dato))

    if posicion != -1:
        mostrar_encabezado()
        mostrar_uno(estudiantes[posicion])
    else:
        print("No se encontró un estudiante con ese legajo.")


# --------------------------------------------------
# FRECUENCIA DE CALIFICACIONES
# --------------------------------------------------

def contar_calificaciones(estudiantes: list, materia: int) -> list:
    """
    Entrada: recibe la lista de estudiantes y el índice de la materia.
    Proceso: cuenta cuántas veces aparece cada nota del 1 al 10.
    Salida: devuelve una lista de diez contadores.
    """
    contadores = [0] * 10

    for estudiante in estudiantes:
        nota = estudiante["notas"][materia]
        contadores[nota - 1] += 1

    return contadores


def mostrar_frecuencias(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita una materia, cuenta sus notas y muestra las frecuencias.
    Salida: imprime la cantidad de veces que aparece cada nota.
    """
    valido = False

    while not valido:
        materia = input("Ingrese la materia (1 a 5): ")

        if validar_materia(materia):
            valido = True
        else:
            print("Error: ingrese una materia entre 1 y 5.")

    contadores = contar_calificaciones(estudiantes, int(materia) - 1)

    print("\nFRECUENCIA DE NOTAS - MAT_" + materia)

    for i in range(10):
        print("Nota", i + 1, ":", contadores[i])


# --------------------------------------------------
# GUARDAR ARCHIVO JSON
# --------------------------------------------------

def guardar_json(estudiantes: list, ruta: str) -> None:
    """
    Entrada: recibe la lista de estudiantes y el nombre del archivo JSON.
    Proceso: guarda la lista de diccionarios en formato JSON.
    Salida: crea el archivo indicado o muestra un mensaje de error.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)

        print("Los datos se guardaron correctamente en el archivo JSON.")

    except OSError:
        print("Error al intentar guardar el archivo.")


# --------------------------------------------------
# FUNCIONES DE CADA OPCIÓN DEL MENÚ
# --------------------------------------------------

def opcion_1() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: solicita el nombre del CSV y carga sus datos.
    Salida: devuelve la lista de estudiantes obtenida del archivo.
    """
    ruta = input("Ingrese el nombre o ruta del archivo CSV: ")
    return cargar_datos_csv(ruta)


def opcion_2() -> list:
    """
    Entrada: no recibe parámetros.
    Proceso: realiza la carga manual de los estudiantes.
    Salida: devuelve la lista de estudiantes.
    """
    return cargar_datos_manual()


def opcion_3(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: recorre la lista y muestra todos los estudiantes.
    Salida: imprime los datos por consola.
    """
    mostrar_todos(estudiantes)


def opcion_4(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: calcula y guarda el promedio de cada estudiante.
    Salida: modifica los diccionarios de la lista.
    """
    calcular_promedios(estudiantes)


def opcion_5(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita el orden ASC o DESC, ordena y muestra los datos.
    Salida: modifica y muestra la lista ordenada.
    """
    orden = input("Ingrese ASC para ascendente o DESC para descendente: ")
    orden = orden.upper()

    while orden != "ASC" and orden != "DESC":
        print("Orden inválido.")
        orden = input("Ingrese ASC o DESC: ")
        orden = orden.upper()

    ordenar_estudiantes(estudiantes, orden)
    mostrar_todos(estudiantes)


def opcion_6(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: busca las materias con mayor promedio general.
    Salida: muestra las materias encontradas.
    """
    mostrar_materias_mayor_promedio(estudiantes)


def opcion_7(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: busca un estudiante mediante su legajo.
    Salida: muestra todos sus datos si existe.
    """
    buscar_y_mostrar(estudiantes)


def opcion_8(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: cuenta las repeticiones de cada nota en una materia.
    Salida: muestra las diez frecuencias.
    """
    mostrar_frecuencias(estudiantes)


def opcion_9(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita el nombre del archivo y guarda los datos en JSON.
    Salida: crea el archivo JSON.
    """
    ruta = input("Ingrese el nombre del archivo JSON: ")
    guardar_json(estudiantes, ruta)


def opcion_10() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: informa que el programa finalizó.
    Salida: imprime un mensaje de despedida.
    """
    print("Fin del programa.")


# --------------------------------------------------
# MENÚ
# --------------------------------------------------

def mostrar_menu() -> None:
    """
    Entrada: no recibe parámetros.
    Proceso: muestra las opciones disponibles.
    Salida: imprime el menú por consola.
    """
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cargar datos desde archivo CSV")
    print("2 - Cargar datos manualmente")
    print("3 - Mostrar todos los datos")
    print("4 - Calcular promedios")
    print("5 - Ordenar y mostrar por promedio")
    print("6 - Mostrar materia/s con mayor promedio")
    print("7 - Buscar estudiante por legajo")
    print("8 - Contar calificaciones de una materia")
    print("9 - Guardar datos en archivo JSON")
    print("10 - Salir")
