import pygame as py
import math

class Bullet():
    def __init__(self, display : py.display, x: int, y : int, angle : int):
        self.display = display
        self.x = x
        self.y = y     
        self.angle = angle
        self.speed = 10

    def Update(self):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = -self.speed * math.sin(math.radians(self.angle))
        self.x += dx 
        self.y += dy

    def Draw(self):
        py.draw.circle(self.display, py.Color("WHITE"), (self.x, self.y), radius=5)


class Player():
    def __init__(self, xPos: int, yPos: int, width: int, height: int, display: py.display):
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        self.x = xPos
        self.y = yPos
        self.width = width
        self.height = height
        self.display = display
        
        self.image = py.transform.scale(py.image.load("image/player/player.png"), (self.width, self.height))
        self.rect_image = self.image.get_rect()

        self.angle = 0
        self.rotation_speed = 5
        self.max_speed = 8
        self.speed = 5
        self.deceleration = 0.1
        self.health = 100

        self.bullets = []

    def Draw(self):
        # Rotate the player image
        rotate_player = py.transform.rotate(self.image, self.angle)
        self.rotated_rect = rotate_player.get_rect(center=(self.x, self.y))
        self.display.blit(rotate_player, self.rotated_rect)

        # Draw bullets
        for bullet in self.bullets:
            bullet.Draw()

    def Movement(self):
        key = py.key.get_pressed()
        #if key[py.K_UP]:
            #Increasing speed when moving forward
        #    self.speed = min(self.speed + 0.1, self.max_speed)
        #elif self.speed > 0:
            # Decreasing speed, if not key pressed  "up" and speed over 0
        #    self.speed = max(self.speed - self.deceleration, 0)
        
        #Calculate the change in coordinates based on angle and speed
        #dx = self.speed * math.cos(math.radians(self.angle))
        #dy = -self.speed * math.sin(math.radians(self.angle))
        #self.x += dx
        #self.y += dy

        if key[py.K_LEFT]:
            self.angle += self.rotation_speed
        if key[py.K_RIGHT]:
            self.angle -= self.rotation_speed

        #Check when the player leaves the out of bounds
        if self.x < -50:
            self.x = self.SCREEN_WIDTH + 50
        elif self.x > self.SCREEN_WIDTH + 50:
            self.x = -50
        if self.y < -50:
            self.y = self.SCREEN_HEIGHT + 50
        elif self.y > self.SCREEN_HEIGHT + 50:
            self.y = -50

    
    def Shoot(self):
        # Creating a bullet and adding it to array
        bullet = Bullet(self.display, self.x, self.y, self.angle)
        self.bullets.append(bullet)

        # Limit on the number of bullets
        if len(self.bullets) > 10:
            del self.bullets[0]
    
    def Death(self, asteroid_x, asteroid_y):
        if asteroid_x == self.x and asteroid_y == self.y:
            self.health -= 1

    def Take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def Heal(self, amount):
        self.health += amount
        if self.health > 100:  
            self.health = 100