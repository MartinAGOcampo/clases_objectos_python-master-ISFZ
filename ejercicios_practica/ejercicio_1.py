# IMPORTANTE: NO borrar los comentarios

class Jugador():
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def obtener_puntaje(self):
        return self.puntaje


if __name__ == "__main__":
    print("Comencemos a practicar con objetos")
    # Alumno:
    # En este archivo ya tiene una clase creada
    # para representar a un Jugador. Esta clase posee:
    # --> el nombre del jugador
    # --> el puntaje inicial del jugador
    # --> un método para obtener el puntaje del jugador

    # 1) Deberá crear un jugador (un variable) a partir de esta clase
    # Al momento de crear el objeto debe indicar un nombre
    # para el jugador

    print('En la resolucion del ejercicio implemente un sistema de carga de jugadores por teclado ' \
    'donde se va cargar tambien el puntaje. Luego mediante una iteracion se va mostrar en pantalla ' \
    'los puntajes de los jugadores ingresados')

    jugadores_varios = []

    while True:
                nombre_jugador = input('Ingrese el nombre del jugador que desea agregar (si desea parar escriba "stop"): ')
                if nombre_jugador.lower() == 'stop':
                    break
                if not nombre_jugador:
                    print('Ingresa un valor por favor! ')
                    continue

                try:
                    puntaje_jugador = int(input(f'Ingrese el puntaje del jugador {nombre_jugador}: '))
            
                except ValueError:
                    print('Ingrese un valor valido')
                    continue    
                
                nuevo_jugador = Jugador(nombre_jugador, puntaje_jugador)
                jugadores_varios.append(nuevo_jugador)
                print('Jugador creado exitosamente! ')
                print()
            

    # 2) Utilice el método "obtener_puntaje"
    # para leer el puntaje actual del jugador
    # Almacene el puntaje obtenido del método
    # en una variable llamada "puntaje"
    print()
    print('Recupeando datos de los jugadores: ')
    for jugador in jugadores_varios:
        puntaje = jugador.obtener_puntaje()
        print(f"El puntaje del jugador {jugador.nombre} es/son {puntaje} puntos")
    # Imprimir en pantalla la variable "puntaje"
    print()
    print("terminamos")
    print('Gracias')
