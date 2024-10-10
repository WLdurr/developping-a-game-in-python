import pygame

pygame.init()

# Define aesthetics of window
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Alchemist')
screen.fill(background_colour)

# Define the player
player_color = (255, 0, 0)  # Red color for the player
player_radius = 20  # Radius of the player
player_x = 600  # Starting x position (middle of the screen)
player_y = 450  # Starting y position (middle of the screen)
player_speed = 8  # Speed of the player movement

clock = pygame.time.Clock()

# Update the display
pygame.display.flip()

# Variable to keep our game loop running
running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of all keys
    keys = pygame.key.get_pressed()

    # Move the player based on key input (WASD)
    if keys[pygame.K_w]:  # Move up
        player_y -= player_speed
    if keys[pygame.K_s]:  # Move down
        player_y += player_speed
    if keys[pygame.K_a]:  # Move left
        player_x -= player_speed
    if keys[pygame.K_d]:  # Move right
        player_x += player_speed

    # Fill the background color
    screen.fill(background_colour)

    # Draw the player as a circle
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()