def es_palindromo(cadena):
    
    cadena = cadena.replace(" ", "").lower()
    
    return cadena == cadena[::-1]

# Ejemplo de uso
print(es_palindromo("zapato"))  
print(es_palindromo("Mbappe"))   
print(es_palindromo("la payola no se baña"))  
