import pygame as py

class FPS:
    def __init__(self, display : py.display, fontSize : int, clock : py.time.Clock):
        self.clock = clock
        self.display = display
        self.font = py.font.SysFont("Liberation Mono", fontSize)
    
    def Draw(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(f"FPS: {fps}", True, py.Color("WHITE"))
        self.display.blit(fps_text, (0, 0))

#Class that draw a player X and Y coordinates:
class Player_Position:
    def __init__(self, display : py.display, x : int, y : int, textPosX : int, textPosY : int, fontSize : int):
        self.x = x
        self.y = y
        self.textPosX = textPosX
        self.textPosY = textPosY
        self.display = display
        self.font = py.font.SysFont("JetBrains Mono", fontSize)

    def Draw(self):
        pos_text_x = self.font.render(f"Player_Position [x]: {self.x}", True, py.Color("WHITE"))
        pos_text_y = self.font.render(f"Player_Position [y]: {self.y}", True, py.Color("WHITE"))
        self.display.blit(pos_text_x, (self.textPosX, self.textPosY + 30))
        self.display.blit(pos_text_y, (self.textPosX, self.textPosY + 60))

#Class that draw a asteroid X and Y coordinates:
class Asteroid_Position:
    def __init__(self, display : py.display, x : int, y : int, textPosX : int, textPosY : int, fontSize : int):
        self.x = x
        self.y = y
        self.textPosX = textPosX
        self.textPosY = textPosY
        self.display = display
        self.font = py.font.SysFont("JetBrains Mono", fontSize)

    def Draw(self):
        pos_text_x = self.font.render(f"Asteroid_Position [x]: {self.x}", True, py.Color("WHITE"))
        pos_text_y = self.font.render(f"Asteroid_Position [y]: {self.y}", True, py.Color("WHITE"))
        self.display.blit(pos_text_x, (self.textPosX, self.textPosY + 30))
        self.display.blit(pos_text_y, (self.textPosX, self.textPosY + 60))

class Player_Health:
    def __init__(self, display : py.display, health : int,  textPosX : int, textPosY : int, fontSize : int):
        self.display = display
        self.textPosX = textPosX
        self.textPosY = textPosY
        self.health = health
        self.font = py.font.SysFont("JetBrains Mono", fontSize)
    
    def Draw(self):
        health_text = self.font.render(f"Player_Health: {self.health}", True, py.Color("WHITE"))
        self.display.blit(health_text, (self.textPosX, self.textPosY))

class Score:
    def __init__(self, display : py.display, score : int,  textPosX : int, textPosY : int, fontSize : int):
        self.display = display
        self.textPosX = textPosX
        self.textPosY = textPosY
        self.score = score
        self.font = py.font.SysFont("JetBrains Mono", fontSize)
    
    def Draw(self):
        score_text = self.font.render(f"Score: {self.score}", True, py.Color("WHITE"))
        self.display.blit(score_text, (self.textPosX, self.textPosY))