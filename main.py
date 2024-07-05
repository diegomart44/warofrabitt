
"""
Objetivos

1- mejorar disparro con angulo
2- ajustar disparo hacia el oponente
3- agregar cazador, 
4- crear menu de inicio
5- modo multiplayer localhost y con servidor
6- Agregar hijos llorando por su madre
7- patentar
7- ganar en $


"""
import pygame
import sys
import math

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Batalla de Conejos')

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Carga de imágenes (necesitarás tus propias imágenes)
background = pygame.image.load('background.jpg')
rabbit_image = pygame.image.load('rabbit.png')
carrot_image = pygame.image.load('carrot.png')

# Redimensionar la imagen del conejo
rabbit_width, rabbit_height = 50, 50  # Ajusta el tamaño según sea necesario
rabbit_image = pygame.transform.scale(rabbit_image, (rabbit_width, rabbit_height))

# Redimensionar la imagen de la zanahoria
carrot_width, carrot_height = 20, 10  # Ajusta el tamaño según sea necesario
carrot_image = pygame.transform.scale(carrot_image, (carrot_width, carrot_height))

# Clase para las Zanahorias
class Carrot(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, power):
        super().__init__()
        self.image = carrot_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.power = power
        self.velocity = [self.power * math.cos(math.radians(self.angle)),
                         -self.power * math.sin(math.radians(self.angle))]
        self.gravity = 0.5  # Gravedad simulada para hacer el disparo más realista

    def update(self):
        self.velocity[1] += self.gravity  # Aplicar gravedad al proyectil
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom > HEIGHT:
            self.kill()

# Grupo de zanahorias
carrots = pygame.sprite.Group()

# Clase para los Conejos
class Rabbit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = rabbit_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 3
        self.selected = False

    def update(self):
        if self.selected:
            pygame.draw.rect(screen, RED, self.rect, 2)

# Grupo de conejos
rabbits = pygame.sprite.Group()
rabbit1 = Rabbit(100, HEIGHT - 100)
rabbit2 = Rabbit(WIDTH - 100, HEIGHT - 100)
rabbits.add(rabbit1, rabbit2)

# Función para dibujar texto en la pantalla
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Definir la fuente para renderizar texto
font = pygame.font.Font(None, 36)  # Puedes ajustar None a un archivo de fuente .ttf si deseas usar una fuente personalizada

# Variables para el sistema de turnos y disparo
turn = 0  # 0 para el conejo 1, 1 para el conejo 2
aiming = False
aim_start_pos = None
aim_end_pos = None
max_line_length = 100  # Longitud máxima de la línea de disparo

# Loop principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if (turn == 0 and rabbit1.rect.collidepoint(mouse_pos)) or (turn == 1 and rabbit2.rect.collidepoint(mouse_pos)):
                    aim_start_pos = rabbit1.rect.center if turn == 0 else rabbit2.rect.center
                    aiming = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and aiming:
                aim_end_pos = pygame.mouse.get_pos()
                dx = aim_end_pos[0] - aim_start_pos[0]
                dy = aim_end_pos[1] - aim_start_pos[1]
                angle = math.degrees(math.atan2(-dy, dx))
                power = min(math.hypot(dx, dy) / 10, 10)  # Limitar la potencia máxima
                if turn == 0:
                    carrot = Carrot(rabbit1.rect.centerx, rabbit1.rect.centery, angle, power)
                else:
                    carrot = Carrot(rabbit2.rect.centerx, rabbit2.rect.centery, angle, power)
                carrots.add(carrot)
                aim_start_pos = None
                aim_end_pos = None
                aiming = False
                turn = 1 - turn  # Cambiar de turno después de disparar

    # Actualizar movimiento de las zanahorias
    carrots.update()

    # Detección de colisiones
    for rabbit in rabbits:
        hits = pygame.sprite.spritecollide(rabbit, carrots, True)
        for hit in hits:
            rabbit.health -= 1
            if rabbit.health <= 0:
                rabbit.kill()

    # Dibujar fondo, conejos y zanahorias
    screen.blit(background, (0, 0))
    rabbits.draw(screen)
    carrots.draw(screen)

    # Dibujar la línea de puntería
    if aim_start_pos and aiming:
        pygame.draw.line(screen, RED, aim_start_pos, pygame.mouse.get_pos(), 2)

    # Mostrar la vida de cada conejo
    draw_text(f'Conejo 1 Vida: {rabbit1.health}', font, BLACK, screen, 20, 20)
    draw_text(f'Conejo 2 Vida: {rabbit2.health}', font, BLACK, screen, WIDTH - 200, 20)

    pygame.display.flip()

pygame.quit()
sys.exit()
