import pygame
import sys
import random
# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 60, 12
BRICK_WIDTH, BRICK_HEIGHT = 58, 20
BRICK_GAP = 2
BALL_SPEED = 2
PADDLE_SPEED = 2
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
BLUE = pygame.Color('blue')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
BRICK_COLORS = [BLUE, RED, GREEN, YELLOW] # List of brick colors
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake game by snoopstick')
# Game objects
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
paddle = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
bricks = [pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT) for x in range(0, SCREEN_WIDTH, BRICK_WIDTH + BRICK_GAP) for y in range(0, SCREEN_HEIGHT // 2, BRICK_HEIGHT + BRICK_GAP)]
dx, dy = BALL_SPEED, BALL_SPEED
# Score counter
score = 0 # Initialize score to zero
font = pygame.font.SysFont('Arial', 32) # Create a font object
# Ball speed variable
ball_speed_factor = 1.0 # Initialize ball speed factor to 1.0
# Game state variable
running = True # Initialize running flag to True
# Main loop
while running:
    # Game loop
    game_over = False # Initialize game over flag to False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Set running flag to False
                game_over = True # Set game over flag to True
        # Ball movement
        ball.move_ip(dx * ball_speed_factor, dy * ball_speed_factor) # Multiply ball speed by factor
        if ball.left < 0 or ball.right > SCREEN_WIDTH:
            dx *= -1
        if ball.top < 0:
            dy *= -1
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-PADDLE_SPEED, 0)
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.move_ip(PADDLE_SPEED, 0)
        # Ball and paddle collision
        if ball.colliderect(paddle):
            dy *= -1
        # Ball and brick collision
        for brick in bricks:
            if ball.colliderect(brick):
                dy *= -1
                bricks.remove(brick)
                score += 1 # Increment score by one
                # Increase ball speed factor by 10% every time score is a multiple of 10
                if score % 10 == 0:
                    ball_speed_factor *= 1.1
        # Check if ball falls down
        if ball.bottom > SCREEN_HEIGHT:
            game_over = True # Set game over flag to True
        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.rect(screen, WHITE, ball)    
        # Assign each brick a color based on a diagonal pattern formula
        for i, brick in enumerate(bricks):
            color_index = (i // (SCREEN_WIDTH // (BRICK_WIDTH + BRICK_GAP)) + i % (SCREEN_WIDTH // (BRICK_WIDTH + BRICK_GAP))) % len(BRICK_COLORS) # Get the color index from the formula
            color = BRICK_COLORS[color_index] # Get the color from the list
            pygame.draw.rect(screen, color, brick)
        # Render score text
        text = font.render(f'Score: {score}', True, WHITE) # Create a text surface with the score
        screen.blit(text, (10, 10)) # Blit the text surface on the screen at a position
        pygame.display.flip()
        pygame.time.wait(10)
    # Game over message
    text = font.render('Game Over', True, WHITE) # Create a text surface with the message
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2 , SCREEN_HEIGHT // 2 - text.get_height() // 2)) # Blit the text surface on the center of the screen
    pygame.display.flip()
    pygame.time.wait(1000) # Wait for 1 second
    # Retry message
    text = font.render('Press SPACE to retry', True, WHITE) # Create a text surface with the message
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2 , SCREEN_HEIGHT // 2 + text.get_height())) # Blit the text surface below the game over message
    pygame.display.flip()
    # Wait for user input
    retry = False # Initialize retry flag to False
    while not retry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Set running flag to False
                retry = True # Set retry flag to True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    retry = True # Set retry flag to True
                    # Reset game objects
                    ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
                    paddle = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
                    bricks = [pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT) for x in range(0, SCREEN_WIDTH, BRICK_WIDTH + BRICK_GAP) for y in range(0, SCREEN_HEIGHT // 2, BRICK_HEIGHT + BRICK_GAP)]
                    dx, dy = BALL_SPEED, BALL_SPEED
                    # Reset score counter
                    score = 0
                    # Reset ball speed factor
                    ball_speed_factor = 1.0
pygame.quit()
quit()



