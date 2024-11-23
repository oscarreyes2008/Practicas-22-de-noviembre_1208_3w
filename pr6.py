def inversa(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida


texto = "saquen el vapo!"
resultado = inversa(texto)
print(f"La inversión de '{texto}' es '{resultado}'")
