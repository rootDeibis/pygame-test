import pygame
import os
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Juego")

# Carga los cuadros del GIF animado
frames = []
frame_files = sorted(os.listdir("player_frames"))
for file in frame_files:
    if file.endswith(".gif"):
        frame = pygame.image.load(os.path.join("player_frames", file)).convert_alpha()
        # Redimensiona la imagen a la mitad de su tamaño original
        frame = pygame.transform.scale(frame, (frame.get_width() // 4, frame.get_height() // 4))
        frames.append(frame)

# Índice del cuadro actual
current_frame = 0

# Contador de retraso entre cuadros
frame_delay = 1000

# Posición inicial del jugador
player_pos = [0, 0]

# Bucle del juego
running = True

# Velocidad de movimiento
movement_speed = 0.25
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            

    # Manejo de entrada del usuario
    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        player_pos[0] -= movement_speed
        moving = True
    if keys[pygame.K_RIGHT]:
        player_pos[0] += movement_speed
        moving = True
    if keys[pygame.K_UP]:
        player_pos[1] -= movement_speed
        moving = True
    if keys[pygame.K_DOWN]:
        player_pos[1] += movement_speed
        moving = True
        
        

    # Limpia la pantalla con un color de fondo
    screen.fill((0, 0, 0))

    # Dibuja el cuadro actual del jugador en la posición actual
    screen.blit(frames[current_frame], player_pos)

    # Actualiza el índice del cuadro actual si el jugador se está moviendo y ha pasado suficiente tiempo desde el último cambio de cuadro
    if moving and frame_delay == 0:
        current_frame = (current_frame + 1) % len(frames)
        frame_delay = 10 # Agrega un retraso de 10 fotogramas entre cada cambio de cuadro

    # Decrementa el contador de retraso entre cuadros si es mayor que cero
    if frame_delay > 0:
        frame_delay -= 1

    # Actualiza la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
