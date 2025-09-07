import re
def buscar_datos(texto):
    resultados = []

    expresiones = {
        "entero": r"-?\d+",
        "flotante": r"\d+\.\d+",
        "booleano": r"(true|false)",
        "string": r"\'(.*?)\'",
        "lista": r"\[[^\]]*\]"
    }

#Iterar y buscar cada tipo de dato en el texto

    for tipo, expresion in expresiones.items():
        for coincidencia in re.finditer(expresion, texto):
            resultados.append((coincidencia.group(), tipo))
    
    return resultados

texto = 'El valor es 2233342, temp -43 la temperatura es -36.6, la respuesta es True también true o false y False, el mensaje es "Hola" y la lista es [1, 2, 3] y tambien [-1, 4, 6.9]'
print("Texto de entrada:", texto, "\n")

resultados = buscar_datos(texto)

print("Resultados:")
for valor, tipo in resultados:
    print(f"* {valor}: {tipo}")