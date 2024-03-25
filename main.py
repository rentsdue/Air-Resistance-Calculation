import pygame
from ball import Ball


# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projectile Motion Simulation With Air Resistance")

ground_y = 550  # Height of the ground
ball_radius = 10  # Radius of the ball
ball_x = 0  # Initial x-position of the ball
ball_y = ground_y - ball_radius # Initial y-position of the ball
ball_mass = 40 # Mass of the ball
ball_drag = 10 # Drag coefficient of the ball
ball_velocity = 200 #Initial velocity of the ball
ball_angles = [35, 40, 45] # Angles of velocity
ball_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Colors for each trajectory
ballList = []  # List to store ball objects

# Create ball objects
for angle, color in zip(ball_angles, ball_colors):
    ballList.append(Ball(ball_x, ball_y, ball_radius, ball_mass, ball_drag, ball_velocity, angle, ground_y))
    ballList[-1].color = color  # Assign color to the ball trajectory

# Create a ground surface
ground_color = (0, 255, 0)  # Green color for the ground
ground = pygame.Surface((800, 50))
ground.fill(ground_color)

running = True
clock = pygame.time.Clock()
for ball in ballList:
    trajectory_points = []  # List to store trajectory points
    while running and not ball.isOnFloor():
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
        ball.draw_trajectory(screen, trajectory_points)

        # Draw the object
        ball.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(5)

pygame.quit()
