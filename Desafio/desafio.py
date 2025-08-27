import re

texto = "En el núcleo del sistema, el valor crítico se establece en 42, un entero positivo que contrasta con los valores negativos como -5 o -273 usados en cálculos de criogenia; además, las mediciones de precisión como la temperatura corporal (36.6 °C) o el punto de ebullición del agua (100.0 °C) requieren flotantes, mientras que la validación de permisos devuelve un booleano (True para acceso concedido, False para denegado), todo ello acompañado de mensajes como 'Hola' o 'Error: recurso bloqueado' y organizado en listas de configuración como [1, 2, 3] o [-10, 0, 25.5]."

def encontrar_enteros(texto):
    patron_enteros = r"[-]?\d+"
    return re.findall(patron_enteros, texto)

def encontrar_flotantes(texto):
    patron_flotantes = r"\d+\.\d+"
    return re.findall(patron_flotantes, texto)

def encontrar_booleans(texto):
    patron_booleans = r"(true|false)"
    return re.findall(patron_booleans, texto, re.IGNORECASE)

def encontrar_strings(texto):
    patron_strings = r"\'(.*?)\'"
    return re.findall(patron_strings, texto)

def encontrar_listas(texto):
    patron_listas = r"\[\d+(?:,\s\d+)*\]"
    return re.findall(patron_listas, texto)

def analizar_texto(texto):
    resultados = {
        'enteros': encontrar_enteros(texto),
        'flotantes': encontrar_flotantes(texto),
        'booleanos': encontrar_booleans(texto),
        'strings': encontrar_strings(texto),
        'listas': encontrar_listas(texto)        
    }

    return resultados

def mostrar_resultados(resultados):
    print("----------------")
    print(f"Número entero: {resultados['enteros']}")
    print(f"Cantidad de elementos encontrados: {len(resultados['enteros'])}")
    print("----------------")
    print(f"Número flotante: {resultados['flotantes']}")
    print(f"Cantidad de elementos encontrados: {len(resultados['flotantes'])}")
    print("----------------")
    print(f"Booleano: {resultados['booleanos']}")
    print(f"Cantidad de elementos encontrados: {len(resultados['booleanos'])}")
    print("----------------")
    print(f"String: {resultados['strings']}")
    print(f"Cantidad de elementos encontrados: {len(resultados['strings'])}")
    print("----------------")
    print(f"Lista de números: {resultados['listas']}")
    print(f"Cantidad de elementos encontrados: {len(resultados['listas'])}")


resultados = analizar_texto(texto)
mostrar_resultados(resultados)