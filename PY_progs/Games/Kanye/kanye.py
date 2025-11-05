import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Old Kanye vs New Kanye")

# Colors
BLACK = (15, 15, 15)
BLUE = (0, 120, 255)
RED = (220, 50, 50)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)

# Clock for framerate
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self, x, y, color, image_path=None):
        self.x = x
        self.y = y
        self.radius = 30
        self.color = color
        self.image = None
        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.dx = random.choice([-2, 2])
        self.dy = random.choice([-2, 2])
        self.score = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - self.radius < 50 or self.x + self.radius > WIDTH - 50:
            self.dx *= -1
        if self.y - self.radius < 50 or self.y + self.radius > HEIGHT - 50:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 4)
        if self.image:
            rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, rect)

# Gear class
class Gear:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)
        self.radius = 15
        self.angle = 0

    def draw(self, screen):
        self.angle += 5
        points = []
        for i in range(8):
            angle_rad = math.radians(self.angle + i * 45)
            r = self.radius + (3 if i % 2 == 0 else -3)
            points.append((self.x + math.cos(angle_rad) * r,
                           self.y + math.sin(angle_rad) * r))
        pygame.draw.polygon(screen, GRAY, points, 2)

    def respawn(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)

# Setup players
old_kanye = Player(200, 300, BLUE, None)
new_kanye = Player(400, 300, RED, None)
gear = Gear()

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (50, 50, WIDTH - 100, HEIGHT - 100), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move players
    old_kanye.move()
    new_kanye.move()

    # Draw everything
    gear.draw(screen)
    old_kanye.draw(screen)
    new_kanye.draw(screen)

    # Collision detection
    for player in [old_kanye, new_kanye]:
        distance = math.hypot(player.x - gear.x, player.y - gear.y)
        if distance < player.radius + gear.radius:
            player.score += 1
            gear.respawn()

    # Draw progress bars
    pygame.draw.rect(screen, BLUE, (100, 20, old_kanye.score * 10, 10))
    pygame.draw.rect(screen, RED, (100, 40, new_kanye.score * 10, 10))

    # Labels
    font = pygame.font.SysFont("Arial", 18)
    screen.blit(font.render("Old Kanye", True, BLUE), (20, 15))
    screen.blit(font.render("New Kanye", True, RED), (20, 35))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
