import pygame
import random
import time

pygame.init()


# Make the window full screen
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Snake")

# Get screen size dynamically
screen_width, screen_height = pygame.display.get_surface().get_size()


# Snake setup
snake_x, snake_y = screen_width // 2, screen_height // 2
width, height = 20, 20
vel = 5

# Score setup
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(score), True, (255, 255, 255))

# Apple setup
red_size = 20
red_x = random.randint(0, screen_width - red_size)
red_y = random.randint(0, screen_height - red_size)

direction = "none"
run = True




while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Press ESC to quit fullscreen easily
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_x > 0:
        direction = "left"
    if keys[pygame.K_RIGHT] and snake_x < screen_width - width:
        direction = "right"
    if keys[pygame.K_UP] and snake_y > 0:
        direction = "up"
    if keys[pygame.K_DOWN] and snake_y < screen_height - height:
        direction = "down"

    # Movement
    if direction == "left":
        snake_x -= vel
    if direction == "right":
        snake_x += vel
    if direction == "up":
        snake_y -= vel
    if direction == "down":
        snake_y += vel

    # Collision rects
    snake_rect = pygame.Rect(snake_x, snake_y, width, height)
    apple_rect = pygame.Rect(red_x, red_y, red_size, red_size)

    # Collision with apple
    if snake_rect.colliderect(apple_rect):
        vel += 1
        score += 1
        text = font.render(str(score), True, (255, 255, 255))
        red_x = random.randint(0, screen_width - red_size)
        red_y = random.randint(0, screen_height - red_size)

    # Border collision
    if (snake_x < 0 or snake_x + width > screen_width or
        snake_y < 0 or snake_y + height > screen_height):
        run = False

    # Draw everything
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), snake_rect)
    pygame.draw.rect(win, (255, 0, 0), apple_rect)
    win.blit(text, (10, 10))
    pygame.display.update()

quit
