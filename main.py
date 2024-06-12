import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Robot Simulation')

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Robot:
    def __init__(self, x=0, y=0, speed=1, angle=0):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def change_direction(self, angle):
        self.angle = angle

    def change_speed(self, speed):
        self.speed = speed

    def get_position(self):
        return (self.x, self.y)

    def get_direction_point(self, length=50):
        end_x = self.x + length * math.cos(math.radians(self.angle))
        end_y = self.y + length * math.sin(math.radians(self.angle))
        return (end_x, end_y)

class UserInput:
    def __init__(self, robot):
        self.robot = robot

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.robot.change_speed(self.robot.speed + 1)
        if keys[pygame.K_DOWN]:
            self.robot.change_speed(self.robot.speed - 1)
        if keys[pygame.K_LEFT]:
            self.robot.change_direction(self.robot.angle - 5)
        if keys[pygame.K_RIGHT]:
            self.robot.change_direction(self.robot.angle + 5)

def draw_text(surface, text, position, font_size=30, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

# Simulation parameters
robot = Robot(x=width//2, y=height//2, speed=1, angle=0)
user_input = UserInput(robot)
running = True
clock = pygame.time.Clock()

# Simulation loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    user_input.handle_input()

    # Move the robot
    robot.move()

    # Clear the screen
    window.fill(WHITE)

    # Draw the robot
    pygame.draw.circle(window, BLUE, (int(robot.x), int(robot.y)), 10)

    # Draw the laser indicating the direction
    direction_point = robot.get_direction_point()
    pygame.draw.line(window, RED, (int(robot.x), int(robot.y)), (int(direction_point[0]), int(direction_point[1])), 2)

    # Display the robot's coordinates
    coords = robot.get_position()
    draw_text(window, f'Coordinates: ({coords[0]:.2f}, {coords[1]:.2f})', (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
