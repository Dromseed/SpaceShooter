import pygame as py
from random import randint
import math

class Asteroid_ball():
    def __init__(self, xPos: int, yPos: int, width: int, height: int, speed : int, display: py.display):
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        self.x = xPos
        self.y = yPos
        self.width = width
        self.height = height
        
        self.angle = 0
        self.rotation_speed = 10
        self.speed = speed
        
        self.display = display
        self.image = py.transform.scale(py.image.load("image/asteroids/asteroid_ball.png"), (self.width, self.height))

    
    def Draw(self):
        self.rotate = py.transform.rotate(self.image, self.angle)
        self.rotated_rect = self.rotate.get_rect(center=(self.x, self.y))
        self.display.blit(self.rotate, self.rotated_rect)
    
    def Movement(self, player_x, player_y):
        diff_x = player_x - self.x
        diff_y = player_y - self.y
        
        angle_to_player = math.atan2(diff_y, diff_x)
        
        self.angle = math.degrees(angle_to_player)
        
        dx = self.speed * math.cos(angle_to_player)
        dy = self.speed * math.sin(angle_to_player)

        self.x += dx
        self.y += dy

    def reset_position(self):
        self.x = randint(0, self.SCREEN_WIDTH)
        self.y = randint(0, self.SCREEN_HEIGHT)