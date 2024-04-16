import pygame as py
import player
from asteroid import Asteroid_ball
import text
import sys
import sound
from random import randint
from random import choice

py.init()
class Game():
    def __init__(self, FPS : int):
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 960
        self.display = py.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        py.display.set_caption("ver - alpha")

        self.time = py.time.Clock()
        self.time_to_spawn = 0
        self.FPS = FPS
        
        self.score = 0
        self.paused = False

        self.player = player.Player(xPos=self.SCREEN_WIDTH / 2, yPos=self.SCREEN_HEIGHT / 2, width=200, height=200, display=self.display)
        #self.asteroid_ball = Asteroid_ball(xPos=randint(-300, self.SCREEN_WIDTH + 300), yPos=randint(-300, self.SCREEN_HEIGHT - 300), width=150, height=150, speed=randint(1, 4), display=self.display)

        self.background_sound = sound.Sound("sounds/music/background.mp3", volume=0.01)
        self.Hit_sound = sound.Sound("sounds/hit/hit.mp3", volume=0.1)
        self.Bullet_sound = [sound.Sound("sounds/bullet/bullet_1.mp3", volume=0.1),sound.Sound("sounds/bullet/bullet_2.mp3", volume=0.1), sound.Sound("sounds/bullet/bullet_3.mp3", volume=0.1)]
        self.Asteroids = []

    def Check_collision(self, asteroid):  
        for bullet in self.player.bullets:
            if asteroid.rotated_rect.collidepoint(bullet.x, bullet.y):
                self.Hit_sound.Play()
                self.player.bullets.remove(bullet)
                self.Asteroids.remove(asteroid)
                self.score += 1
                
                if asteroid in self.Asteroids:
                    self.Asteroids.remove(asteroid)
            
        if asteroid.rotated_rect.collidepoint(self.player.x, self.player.y):
                if asteroid in self.Asteroids:
                    self.Hit_sound.Play()
                    self.player.Take_damage(5)
                    self.Asteroids.remove(asteroid)
                   
    def run(self):
        run = True
        self.background_sound.Play()
        while run:
            self.display.fill(py.Color("Black"))
            self.time.tick(self.FPS)
            
            #I declare the text drawing function here, otherwise the position numbers are not updated.
            #=======================================================================================================================================================================#
            self.FPS_text = text.FPS(display=self.display, fontSize=30, clock=self.time)
            self.player_pos_text = text.Player_Position(display=self.display, x=int(self.player.x), y=int(self.player.y), textPosX=0, textPosY=30, fontSize=18)
            self.player_health_text = text.Player_Health(display=self.display, health=self.player.health, textPosX=0, textPosY=self.SCREEN_HEIGHT - 50, fontSize=18)
            self.score_text = text.Score(display=self.display, score=self.score, textPosX=0, textPosY=500, fontSize=28)
            #=======================================================================================================================================================================#
            
            self.AsteroidsPositionsX = [randint(-100, -50), randint(self.SCREEN_WIDTH + 100, self.SCREEN_WIDTH + 200)]
            self.AsteroidsPositionsY = [randint(-100, 500), randint(-100, 500)]
            #new_PosX = randint(-150, self.SCREEN_WIDTH + 150)
            #new_PosY = randint(-150, self.SCREEN_HEIGHT - 150)
            asteroid = Asteroid_ball(xPos=choice(self.AsteroidsPositionsX), yPos=choice(self.AsteroidsPositionsY), width=150, height=150, speed=randint(1, 4), display=self.display)
            
            #Main event handler:
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False
                    sys.exit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        self.player.Shoot()
                        self.Bullet_sound[randint(0, 2)].Play()
                    if event.key == py.K_w:
                        self.player.Take_damage(10)
                    if event.key == py.K_SPACE:
                        self.player.Heal(50)
                    if event.key == py.K_d:
                        self.Asteroids.clear()
                        self.Hit_sound.Play()
                    
                    #FIXME: 
                    #if event.key == py.K_p:
                    #    self.time.tick(0)
                        #if self.time.tick(0):
                        #    self.time.tick(self.FPS)
            
            self.time_to_spawn += 1
            if(self.time_to_spawn == 100):                
                self.Asteroids.append(asteroid)
                self.time_to_spawn = 0
            
            for asteroid in self.Asteroids:
                asteroid.Movement(self.player.x, self.player.y)
                asteroid.Draw()
                self.Check_collision(asteroid)
                                   
            for bullet in self.player.bullets:
                bullet.Update()
                bullet.Draw()   
            
            self.player.Movement()
            self.player.Draw()        

            #FPS Drawing:
            self.FPS_text.Draw()
            self.player_pos_text.Draw()
            self.player_health_text.Draw()
            self.score_text.Draw()

            py.display.update()
            py.display.flip()

if __name__ == '__main__':
    #Best fps for this game = 60, if more game becomes not stable.
    game = Game(FPS=60)
    game.run()