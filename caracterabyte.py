
def char_byte(value):

    # Obtener el valor ASCII del carácter
    valor_ascii = ord(value)

    # Convertir el valor ASCII a binario y eliminar el prefijo '0b'
    binario = bin(valor_ascii)[2:]

    # Para asegurarnos de que tenga 8 bits, rellenamos con ceros a la izquierda
    binario = binario.zfill(8)

    # Retornar el resultado
    return binario
