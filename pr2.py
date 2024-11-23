def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


numero1 = 45
numero2 = 70
numero3 = 48
resultado = max_de_tres(numero1, numero2, numero3)
print(f"El número mayor entre {numero1}, {numero2} y {numero3} es {resultado}")
