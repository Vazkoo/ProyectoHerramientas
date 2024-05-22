
# Se importan las funciones de los otros archivos
from caracterabyte import char_byte
from palabraacaracter  import chain_byte
from byteacadena import byte_ascii



def main():

    # El menu de opciones
    print("GENERADOR ASCII")
    print("1. sí desea pasar de un caracter a byte")
    print("2. sí desea pasar de una palabra a byte")
    print("3. sí desea pasar de byte a ASCII")

    # Variable que guardara la opcion escogida por el usuario
    answer = int(input())

    # Filtos por si escoge alguna de las 3 opciones y que se hará
    if answer == 1:
        # Variable donde se guarda el valor del caracter que el usuario escoga
        value = input("¿Que caracter queires usar?:  ")
        # Si el valor es mas que solo un caracter no se ejecuta la funcion, sino, si se ejecuta
        if  len(value) != 1:
            print("debe ser solo un caracter.")
        else:
            print(f"tu caracter en bytes es: {char_byte(value)}")
    
    elif answer == 2:
        # Variable donde se guarda el valor del caracter que el usuario escoga
        value_2 = input("¿Que cadena deseas usar?")
        # Si el valor tiene menos que dos caracteres no se ejecuta la funcion, sino, si se ejecuta
        if len(value_2) < 2:
            print("debe ser una cadena, osea dos o mas caracteres.")
        else:
            print(f"el valor binario de tu cadena es: {chain_byte(value_2)}")
    
    elif answer == 3:
        value_3 = str(input("¿Cual es el numero binario que quieres usar:"))
        print(f"El valor ASCII del binario es: {byte_ascii((value_3))}")
    # Si no se escoge un numero entre 1 y 3 se retorna que no se ha escogido ninguna de las opciones disponibles
    else:
        print("NO HAS ESCOGIDO UNA OPCION DISPONIBLE")




# Para asegurarse que siempre que se ejecute el archivo comienze por main()
if __name__ == "__main__":
    main()