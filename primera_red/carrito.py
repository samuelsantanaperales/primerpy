import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrito esquivando obstáculos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clase para el carro del jugador
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Clase para los obstáculos
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Crear el carro del jugador
player = Car()
all_sprites.add(player)

# Crear obstáculos
for i in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()

    # Verificar colisiones
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        running = False

    # Renderizar
    SCREEN.fill(WHITE)
    all_sprites.draw(SCREEN)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)

pygame.quit()
sys.exit()
