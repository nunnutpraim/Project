import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Player settings
player_width = 100
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 70
player_speed = 100

# Bullet settings
bullet_speed = 7
bullets = []

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create bullet at player position
                bullets.append(pygame.Rect(
                    player_x + player_width//2 - 2,
                    player_y,
                    5,
                    10
                ))
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    
    # Bullet movement
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()