# IMPORTANTE: NO borrar los comentarios

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def agregar_puntaje (self, puntos): 
        self.puntaje += puntos


    def obtener_puntaje(self):
        return self.puntaje
    


if __name__ == "__main__":
    print("Comencemos a practicar con objetos")
    # Alumno:
    # A la clase Jugador agrege un método 
    # llamado "agregar_puntaje"
    # el cual reciba por parámetro un número
    # Ese nuḿero se deberá sumar al puntaje
    # almacenado en la variable self.puntaje
    # dentro del objeto
    # A medida que se invoque el método para
    # ir aumentando el valor de puntaje,
    # este deberá ir incrementando (acumulador)

    # Ver los ejemplos a continuación de lo que
    # se espera al utilizar el método:

    # jugador1 = Jugador("Laura")
    while True:
        jugador_1 = input('Ingrese el nombre del jugador que desea agregar: ')
        if jugador_1 is None:
            print('Ingresa un nombre por favor !')
        else:
            nuevo_jugador = Jugador(jugador_1)
            break

    puntaje = nuevo_jugador.obtener_puntaje()
    print(f"*****Al momento de la consulta el puntaje inicial de {jugador_1} es: ", puntaje)
    print()

    print(f'Vamos a ingresar valores nuevos para {jugador_1}')
    while True:
        try:
            puntos = int(input(f'Ingrese los puntos que desea que se sumen al jugador {jugador_1}: '))
            break
        except ValueError:
            print('!!!!! Ingresa un valor valido !!!!!! ')
        
    
    nuevo_jugador.agregar_puntaje(puntos)

    puntaje_nuevo = nuevo_jugador.obtener_puntaje()
    print()
    print(f'El puntaje de {jugador_1} ha sido modificado, el nuevo valor es: ',puntaje_nuevo)
    # Este valor de puntaje debe ser 0
    # Ya que es el valor inicial y no hemos
    # sumado nada hasta ahora
    # puntaje = jugador_1.obtener_puntaje()
    # print("Al momento de la consulta el puntaje inicial es: ", puntaje)

    # Agregar 10 puntos:
    # jugador1.agregar_puntaje(10)

    # Este valor de puntaje debe ser 10
    # Ya que hemos agregado 10 puntos
    # puntaje = jugador1.obtener_puntaje()
    # print("Nuevo puntaje del jugador:", puntaje)
    
    # Agregar 5 puntos:
    # jugador1.agregar_puntaje(5)

    # Este valor de puntaje debe ser 15
    # Ya que hemos agregado 5 puntos
    # puntaje = jugador1.obtener_puntaje()
    # print("Nuevo puntaje del jugador:", puntaje)


    print("terminamos")
