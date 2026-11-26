
import csv
import json


# =========================
# VALIDACIONES
# =========================

def es_entero(dato: str) -> bool:
    """
    Entrada: recibe un dato de tipo texto.
    Proceso: verifica que todos sus caracteres sean números.
    Salida: devuelve True o False.
    """
    if dato == "":
        return False

    for caracter in dato:
        if caracter < "0" or caracter > "9":
            return False

    return True


def validar_legajo(legajo: str) -> bool:
    """
    Entrada: recibe el legajo como texto.
    Proceso: verifica que tenga exactamente cinco dígitos.
    Salida: devuelve True si es válido o False si no lo es.
    """
    if len(legajo) == 5:
        return es_entero(legajo)

    return False


def validar_nombre(nombre: str) -> bool:
    """
    Entrada: recibe el nombre y apellido.
    Proceso: verifica que contenga solamente letras y espacios.
    Salida: devuelve True si es válido o False si no lo es.
    """
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóúü "
    letras += "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

    if nombre == "":
        return False

    for caracter in nombre:
        if caracter not in letras:
            return False

    return True


def validar_genero(genero: str) -> bool:
    """
    Entrada: recibe el género.
    Proceso: verifica que sea F, M o X.
    Salida: devuelve True si es válido o False si no lo es.
    """
    if genero == "F" or genero == "M" or genero == "X":
        return True

    return False


def validar_nota(nota: str) -> bool:
    """
    Entrada: recibe una nota como texto.
    Proceso: verifica que sea un entero entre 1 y 10.
    Salida: devuelve True si es válida o False si no lo es.
    """
    if es_entero(nota):
        numero = int(nota)

        if numero >= 1 and numero <= 10:
            return True

    return False


def buscar_legajo(estudiantes: list, legajo: str) -> int:
    """
    Entrada: recibe la lista de estudiantes y un legajo.
    Proceso: recorre la lista buscando el legajo.
    Salida: devuelve la posición o -1 si no existe.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo:
            return i

    return -1


# =========================
# CARGA DE DATOS
# =========================

def cargar_legajo(estudiantes: list) -> str:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita y valida un legajo de cinco dígitos
    que no esté repetido.
    Salida: devuelve el legajo válido.
    """
    valido = False

    while not valido:
        legajo = input("Ingrese el legajo: ")

        if validar_legajo(legajo):
            if buscar_legajo(estudiantes, legajo) == -1:
                valido = True
            else:
                print("Error: el legajo ya existe.")
        else:
            print("Error: debe ingresar exactamente cinco dígitos.")

    return legajo


def cargar_nombre() -> str:
    """
    Entrada: solicita el nombre y apellido.
    Proceso: valida que contenga solamente letras y espacios.
    Salida: devuelve el nombre válido.
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
    Entrada: solicita el género.
    Proceso: valida que sea F, M o X.
    Salida: devuelve el género válido.
    """
    valido = False

    while not valido:
        genero = input("Ingrese género (F/M/X): ").upper()

        if validar_genero(genero):
            valido = True
        else:
            print("Error: ingrese F, M o X.")

    return genero


def cargar_nota() -> int:
    """
    Entrada: solicita una calificación.
    Proceso: valida que sea un entero entre 1 y 10.
    Salida: devuelve la nota válida.
    """
    valido = False

    while not valido:
        nota = input("Ingrese la nota (1 a 10): ")

        if validar_nota(nota):
            valido = True
        else:
            print("Error: la nota debe estar entre 1 y 10.")

    return int(nota)


def cargar_notas() -> list:
    """
    Entrada: solicita las cinco calificaciones.
    Proceso: carga y valida cada nota.
    Salida: devuelve una lista con cinco notas.
    """
    notas = []

    for i in range(5):
        print("Materia", i + 1)
        nota = cargar_nota()
        notas += [nota]

    return notas


def cargar_un_estudiante(estudiantes: list) -> dict:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita y valida todos los datos de un estudiante.
    Salida: devuelve un diccionario con sus datos.
    """
    legajo = cargar_legajo(estudiantes)
    nombre = cargar_nombre()
    genero = cargar_genero()
    notas = cargar_notas()

    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "genero": genero,
        "notas": notas,
        "promedio": None
    }

    return estudiante


def cargar_datos_manual(estudiantes: list) -> list:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: permite agregar estudiantes manualmente hasta llegar a 1000
    o hasta que el usuario decida finalizar.
    Salida: devuelve la lista actualizada.
    """
    continuar = "S"

    while len(estudiantes) < 1000 and continuar == "S":

        print("\nESTUDIANTE", len(estudiantes) + 1)

        estudiante = cargar_un_estudiante(estudiantes)

        estudiantes += [estudiante]

        if len(estudiantes) < 1000:
            continuar = input("¿Desea cargar otro estudiante? (S/N): ").upper()

            while continuar != "S" and continuar != "N":
                print("Error: ingrese S o N.")
                continuar = input("¿Desea cargar otro estudiante? (S/N): ").upper()

    print("\nCantidad total de estudiantes:", len(estudiantes))

    return estudiantes



def cargar_datos_csv(estudiantes: list) -> list:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: lee las filas del CSV, valida los datos y agrega
    estudiantes hasta alcanzar el límite de 1000.
    Salida: devuelve la lista actualizada.
    """
    ruta = input("Ingrese el nombre o ruta del archivo CSV: ")

    cantidad_inicial = len(estudiantes)

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:

            lector = csv.reader(archivo)

            numero_fila = 0
            fila = next(lector, None)

            while fila is not None and len(estudiantes) < 1000:

                numero_fila += 1

                if len(fila) == 9:

                    legajo = fila[0].strip()
                    nombre = fila[1].strip()
                    genero = fila[2].strip().upper()

                    if validar_legajo(legajo) and validar_nombre(nombre) and validar_genero(genero):

                        if buscar_legajo(estudiantes, legajo) == -1:

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
                                    "legajo": legajo,
                                    "nombre": nombre,
                                    "genero": genero,
                                    "notas": notas,
                                    "promedio": None
                                }

                                estudiantes += [estudiante]

                            else:
                                print("Fila", numero_fila, ": notas inválidas.")

                        else:
                            print("Fila", numero_fila, ": legajo repetido.")

                    else:
                        print("Fila", numero_fila, ": datos inválidos.")

                else:
                    print("Fila", numero_fila, ": cantidad incorrecta de campos.")

                fila = next(lector, None)

        cantidad_agregada = len(estudiantes) - cantidad_inicial

        print("\nSe agregaron", cantidad_agregada, "estudiantes desde el CSV.")
        print("Cantidad total de estudiantes:", len(estudiantes))

        if len(estudiantes) == 1000:
            print("Se alcanzó el límite de 1000 estudiantes.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")

    except OSError:
        print("Error al intentar leer el archivo.")

    return estudiantes


# =========================
# NORMALIZACION
# =========================

def normalizar_estudiante(estudiante: dict) -> dict:
    """
    Entrada: recibe un diccionario de estudiante.
    Proceso: convierte los datos de texto a mayúsculas.
    Salida: devuelve el diccionario normalizado.
    """
    estudiante["nombre"] = estudiante["nombre"].upper()
    estudiante["genero"] = estudiante["genero"].upper()

    return estudiante


def normalizar_datos(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: utiliza map para normalizar los datos de texto.
    Salida: modifica la lista original.
    """
    estudiantes[:] = list(map(normalizar_estudiante, estudiantes))

    print("Los datos se normalizaron correctamente.")


# =========================
# MOSTRAR ESTUDIANTES
# =========================

def mostrar_encabezado() -> None:
    """
    Entrada: no recibe datos.
    Proceso: muestra el encabezado del informe.
    Salida: imprime los títulos de las columnas.
    """
    print()
    print("LEGAJO | NOMBRE | GENERO | N1 | N2 | N3 | N4 | N5 | PROM")
    print("-" * 90)


def mostrar_uno(estudiante: dict) -> None:
    """
    Entrada: recibe un diccionario de estudiante.
    Proceso: obtiene y organiza sus datos.
    Salida: muestra los datos de un estudiante.
    """
    promedio = estudiante["promedio"]

    if promedio is None:
        promedio = "-"

    else:
        promedio = round(promedio, 2)

    print(
        estudiante["legajo"], "|",
        estudiante["nombre"], "|",
        estudiante["genero"], "|",
        estudiante["notas"][0], "|",
        estudiante["notas"][1], "|",
        estudiante["notas"][2], "|",
        estudiante["notas"][3], "|",
        estudiante["notas"][4], "|",
        promedio
    )


def mostrar_todos(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: recorre la lista y llama a mostrar_uno.
    Salida: muestra todos los estudiantes.
    """
    mostrar_encabezado()

    for estudiante in estudiantes:
        mostrar_uno(estudiante)


# =========================
# CALCULAR PROMEDIOS
# =========================

def calcular_promedios(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: utiliza lambda y map para calcular y guardar
    el promedio de cada estudiante.
    Salida: modifica la clave promedio de cada diccionario.
    """
    promedio = lambda notas: sum(notas) / len(notas)

    estudiantes[:] = list(
        map(
            lambda estudiante: dict(
                estudiante,
                promedio=promedio(estudiante["notas"])
            ),
            estudiantes
        )
    )

    print("Los promedios se calcularon correctamente.")


# =========================
# ORDENAR ESTUDIANTES
# =========================

def ordenar_estudiantes(estudiantes: list, orden: str) -> None:
    """
    Entrada: recibe la lista y el orden ASC o DESC.
    Proceso: ordena mediante el método burbuja según el promedio.
    Salida: modifica el orden de la lista original.
    """
    for i in range(len(estudiantes) - 1):

        for j in range(len(estudiantes) - 1 - i):

            if orden == "ASC":
                condicion = estudiantes[j]["promedio"] > estudiantes[j + 1]["promedio"]

            else:
                condicion = estudiantes[j]["promedio"] < estudiantes[j + 1]["promedio"]

            if condicion:
                auxiliar = estudiantes[j]
                estudiantes[j] = estudiantes[j + 1]
                estudiantes[j + 1] = auxiliar


# =========================
# FILTRAR PROMEDIOS MENORES A 4
# =========================

def filtrar_desaprobados(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: utiliza filter para seleccionar promedios menores a 4.
    Salida: muestra los estudiantes que cumplen la condición.
    """
    desaprobados = list(
        filter(
            lambda estudiante: estudiante["promedio"] < 4,
            estudiantes
        )
    )

    if len(desaprobados) > 0:
        print("\nESTUDIANTES CON PROMEDIO MENOR A 4")
        mostrar_todos(desaprobados)

    else:
        print("No hay estudiantes con promedio menor a 4.")


# =========================
# PROMEDIO POR MATERIA
# =========================

def calcular_promedio_materia(estudiantes: list, indice: int) -> float:
    """
    Entrada: recibe la lista y el índice de una materia.
    Proceso: suma las notas de esa materia y calcula el promedio.
    Salida: devuelve el promedio general de la materia.
    """
    suma = 0

    for estudiante in estudiantes:
        suma += estudiante["notas"][indice]

    return suma / len(estudiantes)


def mostrar_materia(indice: int, promedio: float) -> None:
    """
    Entrada: recibe el índice y el promedio de una materia.
    Proceso: identifica el nombre de la materia.
    Salida: muestra su promedio general.
    """
    print("MAT_", indice + 1, ":", round(promedio, 2))


def mostrar_materias_mayor_promedio(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: recorre las cinco materias y busca el mayor promedio.
    Salida: muestra todas las materias que tienen el mayor promedio.
    """
    if len(estudiantes) == 0:
        print("No hay estudiantes cargados.")
        return

    promedios = []

    for i in range(5):
        promedio = calcular_promedio_materia(estudiantes, i)
        promedios += [promedio]

    mayor = max(promedios)

    print("\nMATERIA/S CON MAYOR PROMEDIO GENERAL")

    for i in range(5):
        if promedios[i] == mayor:
            mostrar_materia(i, promedios[i])


# =========================
# BUSCAR ESTUDIANTE
# =========================

def buscar_estudiante(estudiantes: list, legajo: str) -> int:
    """
    Entrada: recibe la lista y el legajo buscado.
    Proceso: recorre los estudiantes buscando coincidencias.
    Salida: devuelve la posición o -1 si no existe.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo:
            return i

    return -1


def buscar_y_mostrar(estudiantes: list) -> None:
    """
    Entrada: recibe la lista de estudiantes.
    Proceso: solicita un legajo, lo busca y muestra sus datos.
    Salida: imprime el estudiante encontrado o un mensaje.
    """
    legajo = input("Ingrese el legajo a buscar: ")

    if validar_legajo(legajo):

        posicion = buscar_estudiante(estudiantes, legajo)

        if posicion != -1:
            mostrar_encabezado()
            mostrar_uno(estudiantes[posicion])

        else:
            print("No se encontró el estudiante.")

    else:
        print("Legajo inválido.")


# =========================
# CONTAR CALIFICACIONES
# =========================

def contar_calificaciones(estudiantes: list, materia: int) -> list:
    """
    Entrada: recibe la lista y el índice de una materia.
    Proceso: cuenta cuántas veces aparece cada nota.
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
    Proceso: solicita una materia y cuenta sus calificaciones.
    Salida: muestra la cantidad de veces que aparece cada nota.
    """
    materia = input("Ingrese la materia (1 a 5): ")

    if validar_nota(materia) and int(materia) <= 5:

        indice = int(materia) - 1

        contadores = contar_calificaciones(estudiantes, indice)

        print("\nFRECUENCIA DE NOTAS - MAT_", materia)

        for i in range(10):
            print("Nota", i + 1, ":", contadores[i])

    else:
        print("Error: debe ingresar una materia entre 1 y 5.")


# =========================
# GUARDAR JSON
# =========================

def guardar_json(estudiantes: list, ruta: str) -> None:
    """
    Entrada: recibe la lista de estudiantes y el nombre del archivo.
    Proceso: guarda los diccionarios en formato JSON.
    Salida: crea el archivo o muestra un mensaje de error.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)

        print("Los datos se guardaron correctamente en JSON.")

    except OSError:
        print("Error al intentar guardar el archivo.")


# =========================
# FUNCIONES DE LAS OPCIONES
# =========================

def opcion_1(estudiantes: list) -> list:
    """Carga estudiantes desde un archivo CSV."""
    return cargar_datos_csv(estudiantes)


def opcion_2(estudiantes: list) -> list:
    """Carga estudiantes manualmente."""
    return cargar_datos_manual(estudiantes)


def opcion_3(estudiantes: list) -> None:
    """Normaliza los datos de texto."""
    normalizar_datos(estudiantes)


def opcion_4(estudiantes: list) -> None:
    """Muestra todos los estudiantes."""
    mostrar_todos(estudiantes)


def opcion_5(estudiantes: list) -> None:
    """Calcula los promedios de todos los estudiantes."""
    calcular_promedios(estudiantes)


def opcion_6(estudiantes: list) -> None:
    """Ordena y muestra los estudiantes por promedio."""
    orden = input("Ingrese el orden (ASC/DESC): ").upper()

    while orden != "ASC" and orden != "DESC":
        print("Error: ingrese ASC o DESC.")
        orden = input("Ingrese el orden (ASC/DESC): ").upper()

    ordenar_estudiantes(estudiantes, orden)

    mostrar_todos(estudiantes)


def opcion_7(estudiantes: list) -> None:
    """Muestra los estudiantes con promedio menor a 4."""
    filtrar_desaprobados(estudiantes)


def opcion_8(estudiantes: list) -> None:
    """Muestra la materia o materias con mayor promedio."""
    mostrar_materias_mayor_promedio(estudiantes)


def opcion_9(estudiantes: list) -> None:
    """Busca y muestra un estudiante por su legajo."""
    buscar_y_mostrar(estudiantes)


def opcion_10(estudiantes: list) -> None:
    """Muestra la frecuencia de las notas de una materia."""
    mostrar_frecuencias(estudiantes)


def opcion_11(estudiantes: list) -> None:
    """Guarda los datos de los estudiantes en un archivo JSON."""
    ruta = input("Ingrese el nombre del archivo JSON: ")

    guardar_json(estudiantes, ruta)


def opcion_12() -> None:
    """Finaliza el programa."""
    print("Fin del programa.")


# =========================
# MENU
# =========================

def mostrar_menu() -> None:
    """Muestra las opciones disponibles."""
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cargar datos desde archivo CSV")
    print("2 - Cargar datos manualmente")
    print("3 - Normalizar datos")
    print("4 - Mostrar todos los datos")
    print("5 - Calcular promedios")
    print("6 - Ordenar y mostrar por promedio")
    print("7 - Mostrar promedios menores a 4")
    print("8 - Materia/s con mayor promedio")
    print("9 - Buscar estudiante por legajo")
    print("10 - Contar calificaciones de una materia")
    print("11 - Guardar datos en archivo JSON")
    print("12 - Salir")
