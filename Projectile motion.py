# Currently, this version of the simulation assumes initial velocity in the y-direction is 0.
# Some errors need to be fixed: Note that +x is right, +y is down!

import math
import pygame

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projectile Motion Simulation With Air Resistance")


class Ball:
    def __init__(self, x, y, radius, mass, drag, velocity, degrees): #Angle is in degrees
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.drag = drag
        self.velocity_x = velocity * math.cos (degrees * math.pi / 180)
        self.velocity_y = - velocity * math.sin (degrees * math.pi / 180)
        self.acceleration_x = (- drag * self.velocity_x) / mass # Need to fix this part
        self.acceleration_y = 9.8 + (drag * self.velocity_y / mass)  # You can adjust this value for gravity

    def update(self):
        # Update the object's position
        self.velocity_y += self.acceleration_y

        if self.velocity_y == 0:
            self.acceleration_y = 9.8 - (self.drag * self.velocity_y / self.mass)
        
        if self.velocity_y == (self.mass * 9.8 / self.drag):
            print("Terminal velocity has been reached")
        
        self.velocity_x += self.acceleration_x

        if self.velocity_x == 0:
            self.velocity_x = 0
        
        self.y += self.velocity_y
        self.x += self.velocity_x  # Added horizontal motion

        # Check if the ball hits the ground
        # if self.y >= ground_y - self.radius:
        #     self.y = ground_y - self.radius  # Keep the ball above or on the ground
        #     self.velocity_y = 0

    def draw(self, screen):
        # Draw the object (ball in this case)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

ground_y = 550  # Height of the ground
ball_radius = 10  # Radius of the ball
ball_x = 500  # Initial x-position of the ball
ball_y = ground_y - ball_radius # Initial y-position of the ball
ball_mass = 30 # Mass of the ball
ball_drag = 10 # Drag coefficient of the ball
ball_velocity = 50 #Initial velocity of the ball
ball_angle = 40

# Create a ball object starting at the ground
ball = Ball(ball_x, ball_y, ball_radius, ball_mass, ball_drag, ball_velocity, ball_angle)

# Create a ground surface
ground_color = (0, 255, 0)  # Green color for the ground
ground = pygame.Surface((800, 50))
ground.fill(ground_color)

trajectory_points = []  # List to store trajectory points

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the object
    ball.update()

    # Add the current position to the trajectory points
    trajectory_points.append((ball.x, ball.y))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ground
    pygame.draw.rect(screen, (0, 255, 0), (0, ground_y, 800, 50))  # Green ground rectangle

    # Draw the trajectory
    if len(trajectory_points) > 1:
        pygame.draw.lines(screen, (255, 0, 0), False, trajectory_points, 2)

    # Draw the object
    ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(300)

pygame.quit()