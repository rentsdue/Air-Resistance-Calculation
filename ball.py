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
        self.velocity_x = velocity * math.cos (degrees * math.pi / 180)
        self.velocity_y = - velocity * math.sin (degrees * math.pi / 180)
        self.ground = ground

    def update(self):
        # y-direction motion
        if self.velocity_y >= 0:
            print("Maximum height has been reached")
            acceleration_y = 9.8 + (self.drag * self.velocity_y / self.mass)
            if abs(self.velocity_y) >= abs(self.mass * 9.8 / self.drag):
                print("Terminal velocity has been reached")
        else: 
            acceleration_y = 9.8 - (self.drag * self.velocity_y / self.mass)
        self.velocity_y += acceleration_y

        # x-direction motion
        acceleration_x = (- self.drag * self.velocity_x) / self.mass       
        if self.velocity_x <= 0:
            self.velocity_x = 0
        else:
            self.velocity_x += acceleration_x

        #Update position in the x and y directions
        self.y += self.velocity_y
        self.x += self.velocity_x

        self.isOnFloor()
    
    def isOnFloor(self):
        if self.y >= self.ground - self.radius and self.x > self.initialX:
                self.y = self.ground - self.radius  # Keep the ball above or on the ground
                self.velocity_y = 0
                self.velocity_x = 0
                print("Final y-position: " + str(self.y) + " | " + "Final x-position: " + str(self.x))
                return True
        else:
            print("Velocity in the y direction: " + str(self.velocity_y) + " | " + "Velocity in the x direction: " + str(self.velocity_x))
            print("Position in the y direction: " + str(self.y) + " | " + "Position in the x direction: " + str(self.x))
            return False

    def draw(self, screen):
        # Draw the object (ball in this case)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
