
import pygame
import random
 
# Definimos algunos colores
MORADO = (238, 17, 208)
BLANCO = (255, 255, 255)
AMARILLO = (240, 216, 13 )
 
class Bloque(pygame.sprite.Sprite):
    """

    ¿Qué es una clase?:
    Las clases proveen una forma de empaquetar datos y funcionalidad juntos.
     Al crear una nueva clase, se crea un nuevo tipo de objeto, permitiendo crear nuevas instancias de ese tipo. 
     Cada instancia de clase puede tener atributos adjuntos para mantener su estado. 
     Las instancias de clase también pueden tener métodos (definidos por su clase) para modificar su estado.
    
    ****************************************
    ****************************************
    Esta clase representa el bloque      
    Deriva de la clase "Sprite" en Pygame
    Un sprite es una imagen bidimensional que forma parte de una escena gráfica aun mayor. 
    Habitualmente, un sprite es cierto tipo de objeto que interactúa.
    """
     
    def __init__(self, color, largo, alto):

        """ Constructor. Pasa el color al bloque, 
        y su posición x e y

    Un constructor es un metodo especial que Python llama para instanciar un objeto usando las definiciones encontradas en tu clase.
    Python usa este constructor para crear tareas como la inicialización (asignar valores a variables), que se necesiten para iniciar. 
    Los constructores tambien pueden verificar que tambien hay suficientes recursos para que el objecto desempeñe cualquier 
    otra tarea para iniciar.

        """

        # Llama al constructor de la clase padre (Sprite) 
        super().__init__() 
 
        # Crea una imagen del bloque y lo rellena de color.
        # Esto podría ser también una imagen cargada desde el disco duro.
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
 
        # Obtenemos el objeto rectángulo que posee las dimensiones de la imagen
        # Actualizamos la posición de ese objeto estableciendo los valores para 
        # rect.x y rect.y
        self.rect = self.image.get_rect()
 
# Inicializamos Pygame
pygame.init()
 
# Establecemos el alto y largo de la pantalla
pantalla_largo = 700
pantalla_alto = 400
pantalla=pygame.display.set_mode([pantalla_largo,pantalla_alto])
 
# Esta es una lista de 'sprites.' Cada bloque en el programa es
# añadido a la lista. La lista es gestionada por una clase llamada 'Group.'
bloque_lista = pygame.sprite.Group()
 
# Esta es una lista de cada uno de los sprites. Así como del resto de bloques y el bloque protagonista..
listade_todoslos_sprites = pygame.sprite.Group()
 
for i in range(50):
    # Esto representa un bloque
    bloque = Bloque(MORADO, 20, 15)
 
    # Establecemos una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(pantalla_largo)
    bloque.rect.y = random.randrange(pantalla_alto)
     
    # Añadimos el  bloque a la lista de objetos
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)
 
# Creamos un bloque protagonista AMARILLO
protagonista = Bloque(AMARILLO, 20, 15)
listade_todoslos_sprites.add(protagonista)
 
#Iteramos hasta que el usuario pulse el botón de salida
hecho = False
 
#  Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
marcador = 0
 
# -------- Bucle principal del Programa -----------
""""
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras 
se cumpla una condición (es decir, mientras la condición tenga el valor True).
"""
while not hecho:
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pulsó salir
            hecho = True # Marcamos que hemos terminado y salimos del bucle
 
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
 
    # Obtenemos la posición actual del ratón. Esto devuelve la posición
    # como una lista de dos números.
    pos = pygame.mouse.get_pos()
     
    # Extraemos la x e y de la lista, 
    # Tal como si extrajéramos letras de una cadena de texto.
    # Colocamos al objeto protagonista en la ubicación del ratón.
    protagonista.rect.x = pos[0]
    protagonista.rect.y = pos[1]
     
    # Observamos si el bloque protagonista ha colisionado con algo.
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, True)  
     
    # Comprobamos la lista de colisiones
    for bloque in lista_impactos_bloques:
        marcador += 1
        print( marcador )
         
    # Dibujamos todos los sprites
    listade_todoslos_sprites.draw(pantalla)
     
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
pygame.quit()