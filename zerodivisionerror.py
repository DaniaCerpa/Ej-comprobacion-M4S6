suma = 3000
contador = 0

try:
    division = suma/contador
    print (f"El resultado de la division entre {suma} y {contador} es: {division}")
    
except ZeroDivisionError:
    print("División por cero")
    
