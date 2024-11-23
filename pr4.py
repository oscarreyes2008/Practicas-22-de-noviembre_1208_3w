def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales


caracter1 = 'a'
caracter2 = 'b'
print(f"¿'{caracter1}' es una vocal? {es_vocal(caracter1)}")
print(f"¿'{caracter2}' es una vocal? {es_vocal(caracter2)}")
