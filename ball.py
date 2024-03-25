import math
import pygame

class Ball:

    initialX = 0

    def __init__(self, x, y, radius, mass, drag, velocity, degrees, ground): #Angle is in degrees
        self.x = x
        initialX = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.drag = drag
        self.velocity_x = velocity * math.cos(degrees * math.pi / 180)
        self.velocity_y = -velocity * math.sin(degrees * math.pi / 180)
        self.ground = ground
        self.color = (255, 255, 255)  # Default color is white

    def update(self):
        # y-direction motion
        if self.velocity_y >= 0:
            print("Maximum height reached!")
            acceleration_y = 9.8 + (self.drag * self.velocity_y / self.mass)
            if abs(self.velocity_y) >= abs(self.mass * 9.8 / self.drag):
                print("Terminal Velocity Reached!")
                pass  
        else: 
            acceleration_y = 9.8 - (self.drag * self.velocity_y / self.mass)
        self.velocity_y += acceleration_y

        # x-direction motion
        acceleration_x = (-self.drag * self.velocity_x) / self.mass       
        if self.velocity_x <= 0:
            self.velocity_x = 0
        else:
            self.velocity_x += acceleration_x

        # Update position in the x and y directions
        self.y += self.velocity_y
        self.x += self.velocity_x

        self.isOnFloor()
    
    def isOnFloor(self):
        if self.y >= self.ground - self.radius and self.x > self.initialX:
            self.y = self.ground - self.radius  # Keep the ball above or on the ground
            self.velocity_y = 0
            self.velocity_x = 0
            print("Final x-coordinate: " + str(self.x) + " | " + "Final y-coordinate: " + str(self.y))
            return True
        else:
            print("X-direction velocity: " + str(self.velocity_x) + " | " + "Y-direction velocity: " + str(self.velocity_y))
            return False

    def draw(self, screen): # Draw the object (ball in this case)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    def draw_trajectory(self, screen, trajectory_points): # Draw the trajectory of the ball with its assigned color
        if len(trajectory_points) > 1:
            pygame.draw.lines(screen, self.color, False, trajectory_points, 2)