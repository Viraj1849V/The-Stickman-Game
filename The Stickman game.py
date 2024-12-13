import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickman Game")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,5)

# Stickman properties
stickman_pos = [WIDTH // 2, HEIGHT - 100]
stickman_speed = 5

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# Function to create a new obstacle
def create_obstacle():
    x_pos = random.randint(0, WIDTH - obstacle_width)
    y_pos = -obstacle_height
    return [x_pos, y_pos]

# Add initial obstacles
for _ in range(5):
    obstacles.append(create_obstacle())

# Score
score = 0
font = pygame.font.Font(None, 50)

# Game loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        stickman_pos[0] -= stickman_speed
    if keys[pygame.K_RIGHT]:
        stickman_pos[0] += stickman_speed

    # Update obstacle positions
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            obstacles.append(create_obstacle())
            score += 1
            if score % 5 == 0:  # Increase speed every 5 points
                obstacle_speed += 1

    # Check for collisions
    for obstacle in obstacles:
        if (stickman_pos[0] < obstacle[0] + obstacle_width and
            stickman_pos[0] + 20 > obstacle[0] and
            stickman_pos[1] < obstacle[1] + obstacle_height and
            stickman_pos[1] + 50 > obstacle[1]):
            running = False  # End the game if collision occurs

    # Drawing
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (stickman_pos[0], stickman_pos[1] - 50), 20)  # Head
    pygame.draw.line(screen, BLACK, (stickman_pos[0], stickman_pos[1] - 30), (stickman_pos[0], stickman_pos[1] + 30), 5)  # Body
    pygame.draw.line(screen, BLACK, (stickman_pos[0], stickman_pos[1] - 10), (stickman_pos[0] - 20, stickman_pos[1] + 20), 5)  # Left arm
    pygame.draw.line(screen, BLACK, (stickman_pos[0], stickman_pos[1] - 10), (stickman_pos[0] + 20, stickman_pos[1] + 20), 5)  # Right arm
    pygame.draw.line(screen, BLACK, (stickman_pos[0], stickman_pos[1] + 30), (stickman_pos[0] - 20, stickman_pos[1] + 70), 5)  # Left leg
    pygame.draw.line(screen, BLACK, (stickman_pos[0], stickman_pos[1] + 30), (stickman_pos[0] + 20, stickman_pos[1] + 70), 5)  # Right leg

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10,10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
