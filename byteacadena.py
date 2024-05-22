def byte_ascii(value):
    
    # Convertir el binario a un valor decimal
    valor_decimal = int(value, 2)
    
    # Obtener el carácter ASCII correspondiente
    caracter = chr(valor_decimal)
    
    # Formatear la salida
    result = f"{caracter}-{valor_decimal}"
    
    return result