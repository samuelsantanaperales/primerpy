import pygame
import math

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensiones de la pantalla
WIDTH = 800
HEIGHT = 600

# Parámetros del péndulo
L1 = 150  # Longitud del primer péndulo
L2 = 100  # Longitud del segundo péndulo
M1 = 10   # Masa del primer péndulo
M2 = 10   # Masa del segundo péndulo
G = 9.81  # Aceleración debido a la gravedad

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Péndulos Dobles")
clock = pygame.time.Clock()

def calculate_positions(theta1, theta2):
    x1 = L1 * math.sin(theta1)
    y1 = L1 * math.cos(theta1)
    x2 = x1 + L2 * math.sin(theta2)
    y2 = y1 + L2 * math.cos(theta2)
    return (x1, y1), (x2, y2)

def draw_pendulums(screen, theta1, theta2):
    screen.fill(WHITE)
    origin = (WIDTH // 2, HEIGHT // 2)
    color = BLACK
    pendulum1, pendulum2 = calculate_positions(theta1, theta2)
    pygame.draw.line(screen, color, origin, pendulum1, 2)
    pygame.draw.line(screen, color, pendulum1, pendulum2, 2)
    pygame.draw.circle(screen, color, origin, 5)  # Origen del péndulo 1
    pygame.draw.circle(screen, color, pendulum1, M1 // 2)  # Masa del péndulo 1
    pygame.draw.circle(screen, color, pendulum2, M2 // 2)  # Masa del péndulo 2

# Ángulos iniciales desviados de la vertical
theta1 = math.pi / 4
theta2 = math.pi / 6
omega1 = 0.0
omega2 = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calcular las aceleraciones angulares usando ecuaciones de movimiento
    alpha1 = (-G * (2 * M1 + M2) * math.sin(theta1) - M2 * G * math.sin(theta1 - 2 * theta2) - 2 * math.sin(theta1 - theta2) * M2 * (omega2 ** 2 * L2 + omega1 ** 2 * L1 * math.cos(theta1 - theta2))) / (L1 * (2 * M1 + M2 - M2 * math.cos(2 * theta1 - 2 * theta2)))
    alpha2 = (2 * math.sin(theta1 - theta2) * (omega1 ** 2 * L1 * (M1 + M2) + G * (M1 + M2) * math.cos(theta1) + omega2 ** 2 * L2 * M2 * math.cos(theta1 - theta2))) / (L2 * (2 * M1 + M2 - M2 * math.cos(2 * theta1 - 2 * theta2)))

    # Actualizar las velocidades angulares
    omega1 += alpha1
    omega2 += alpha2

    # Actualizar los ángulos
    theta1 += omega1
    theta2 += omega2

    # Dibujar los péndulos
    draw_pendulums(screen, theta1, theta2)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
