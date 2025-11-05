import pygame
import random
import math
import os

# Initialize Pygame and mixer for sound
pygame.init()
pygame.mixer.init()

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

# Load assets
try:
    OLD_KANYE_IMG = pygame.image.load(os.path.join("assets", "old_kanye.png"))
    NEW_KANYE_IMG = pygame.image.load(os.path.join("assets", "new_kanye.png"))
    GEAR_IMG = pygame.image.load(os.path.join("assets", "gear.png"))
    GEAR_IMG = pygame.transform.scale(GEAR_IMG, (30, 30))  # Scale gear image
    COLLECT_SOUND = pygame.mixer.Sound(os.path.join("assets", "collect.wav"))
except Exception as e:
    print(
        f"Warning: Some assets couldn't be loaded. Using fallback graphics. Error: {e}"
    )
    OLD_KANYE_IMG = None
    NEW_KANYE_IMG = None
    GEAR_IMG = None
    COLLECT_SOUND = None

# Game constants
WINNING_SCORE = 30
PLAYER_SPEED = 3

# Clock for framerate
clock = pygame.time.Clock()


# Player class
class Player:
    def __init__(self, x, y, color, image=None):
        self.x = x
        self.y = y
        self.radius = 30
        self.color = color
        self.image = image
        if self.image:
            self.image = pygame.transform.scale(self.image, (60, 60))
        self.dx = random.choice([-PLAYER_SPEED, PLAYER_SPEED])
        self.dy = random.choice([-PLAYER_SPEED, PLAYER_SPEED])
        self.score = 0
        self.won = False

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - self.radius < 50 or self.x + self.radius > WIDTH - 50:
            self.dx *= -1
            # Keep player inside bounds
            self.x = max(50 + self.radius, min(self.x, WIDTH - 50 - self.radius))
        if self.y - self.radius < 50 or self.y + self.radius > HEIGHT - 50:
            self.dy *= -1
            # Keep player inside bounds
            self.y = max(50 + self.radius, min(self.y, HEIGHT - 50 - self.radius))

    def handle_collision(self, other):
        # Calculate distance between centers
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.hypot(dx, dy)

        if distance < self.radius + other.radius:
            # Calculate collision angle
            angle = math.atan2(dy, dx)

            # Swap velocities in the direction of collision
            self_dx = self.dx
            self_dy = self.dy

            self.dx = other.dx
            self.dy = other.dy

            other.dx = self_dx
            other.dy = self_dy

            # Move balls apart to prevent sticking
            overlap = (self.radius + other.radius - distance) / 2
            self.x += math.cos(angle) * overlap
            self.y += math.sin(angle) * overlap
            other.x -= math.cos(angle) * overlap
            other.y -= math.sin(angle) * overlap

    def draw(self, screen):
        if self.image:
            rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, rect)
        else:
            pygame.draw.circle(
                screen, self.color, (int(self.x), int(self.y)), self.radius, 4
            )


class Gear:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)
        self.radius = 15
        self.angle = 0
        self.image = GEAR_IMG

    def draw(self, screen):
        self.angle += 5
        if self.image:
            # Create a rotated copy of the gear image
            rotated_gear = pygame.transform.rotate(self.image, self.angle)
            # Get the rect for the rotated image
            rect = rotated_gear.get_rect(center=(self.x, self.y))
            # Draw the rotated image
            screen.blit(rotated_gear, rect)
        else:
            # Fallback to geometric shape if image not available
            points = []
            for i in range(8):
                angle_rad = math.radians(self.angle + i * 45)
                r = self.radius + (3 if i % 2 == 0 else -3)
                points.append(
                    (self.x + math.cos(angle_rad) * r, self.y + math.sin(angle_rad) * r)
                )
            pygame.draw.polygon(screen, GRAY, points, 2)

    def respawn(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)


def show_winner(winner_text):
    font = pygame.font.SysFont("Arial", 48)
    text = font.render(winner_text + " WINS!", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    font_small = pygame.font.SysFont("Arial", 24)
    restart_text = font_small.render("Press SPACE to restart", True, GRAY)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(restart_text, restart_rect)


def reset_game():
    global old_kanye, new_kanye, gear
    old_kanye = Player(200, 300, BLUE, OLD_KANYE_IMG)
    new_kanye = Player(400, 300, RED, NEW_KANYE_IMG)
    gear = Gear()


# Setup initial game state
reset_game()

# Main game loop
running = True
game_over = False

while running:
    screen.fill(BLACK)

    # Draw game area
    pygame.draw.rect(screen, BLUE, (50, 50, WIDTH - 100, HEIGHT - 100), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                game_over = False
                reset_game()

    if not game_over:
        # Move players
        old_kanye.move()
        new_kanye.move()

        # Check for collision between players
        old_kanye.handle_collision(new_kanye)

        # Draw everything
        gear.draw(screen)
        old_kanye.draw(screen)
        new_kanye.draw(screen)

        # Collision detection with gear
        for player in [old_kanye, new_kanye]:
            distance = math.hypot(player.x - gear.x, player.y - gear.y)
            if distance < player.radius + gear.radius:
                player.score += 1
                if COLLECT_SOUND:
                    COLLECT_SOUND.play()
                gear.respawn()

                # Check for winner
                if player.score >= WINNING_SCORE:
                    game_over = True
                    player.won = True

        # Draw progress bars (inside game area)
        bar_width = WIDTH - 200  # Adjusted to fit inside game area
        pygame.draw.rect(
            screen, BLUE, (75, 70, old_kanye.score * (bar_width / WINNING_SCORE), 10)
        )
        pygame.draw.rect(
            screen, RED, (75, 90, new_kanye.score * (bar_width / WINNING_SCORE), 10)
        )

        # Labels (inside game area)
        font = pygame.font.SysFont("Arial", 18)
        screen.blit(font.render(f"Old Kanye: {old_kanye.score}", True, BLUE), (75, 55))
        screen.blit(font.render(f"New Kanye: {new_kanye.score}", True, RED), (75, 75))

    else:
        # Show winner screen
        winner = "Old Kanye" if old_kanye.won else "New Kanye"
        show_winner(winner)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
