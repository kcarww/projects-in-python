import pygame
import sys
import random

pygame.init()

# Configurações iniciais
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Posições das paletas e da bola
ball_pos = [screen_width // 2, screen_height // 2]
ball_vel = [-3, 3]  # Velocidade inicial aleatória
paddle_width, paddle_height = 10, 100
left_paddle_pos = [50, screen_height // 2 - paddle_height // 2]
right_paddle_pos = [screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2]

# Placar
score_player1 = 0
score_player2 = 0

# Fonte para o texto do placar
font = pygame.font.Font(None, 36)

# Relógio para controlar os FPS
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mecanismo de controle das paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= 4
    if keys[pygame.K_s] and left_paddle_pos[1] < screen_height - paddle_height:
        left_paddle_pos[1] += 4
    if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
        right_paddle_pos[1] -= 4
    if keys[pygame.K_DOWN] and right_paddle_pos[1] < screen_height - paddle_height:
        right_paddle_pos[1] += 4

    # Movimento da bola
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Verifica colisão com as paredes superior e inferior
    if ball_pos[1] <= 0 or ball_pos[1] >= screen_height:
        ball_vel[1] = -ball_vel[1]

    # Verifica se a bola sai pelas laterais
    if ball_pos[0] <= 0:
        score_player2 += 1  # Jogador 2 marca ponto
        ball_pos = [screen_width // 2, screen_height // 2]  # Resetar posição da bola
        ball_vel = [random.choice([-3, 3]), random.choice([-3, 3])]  # Novas velocidades aleatórias
    elif ball_pos[0] >= screen_width:
        score_player1 += 1  # Jogador 1 marca ponto
        ball_pos = [screen_width // 2, screen_height // 2]  # Resetar posição da bola
        ball_vel = [random.choice([-3, 3]), random.choice([-3, 3])]  # Novas velocidades aleatórias

    # Verifica colisão com as paletas
    if (ball_pos[0] <= left_paddle_pos[0] + paddle_width and
        left_paddle_pos[1] <= ball_pos[1] <= left_paddle_pos[1] + paddle_height) or \
       (ball_pos[0] >= right_paddle_pos[0] - paddle_width and
        right_paddle_pos[1] <= ball_pos[1] <= right_paddle_pos[1] + paddle_height):
        ball_vel[0] = -ball_vel[0]

    # Preenche a tela
    screen.fill(BLACK)

    # Desenha a bola
    pygame.draw.circle(screen, WHITE, ball_pos, 10)

    # Desenha as paletas
    pygame.draw.rect(screen, WHITE, (left_paddle_pos[0], left_paddle_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (right_paddle_pos[0], right_paddle_pos[1], paddle_width, paddle_height))

    # Desenha o placar
    score_text = font.render(f"{score_player1} : {score_player2}", True, WHITE)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 20))

    # Atualiza a tela
    pygame.display.flip()

    # Mantém o jogo rodando a 60 FPS
    clock.tick(60)
