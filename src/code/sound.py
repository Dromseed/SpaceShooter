import pygame as py

class Sound:
    def __init__(self, sound_File : str, volume : float):
        self.sound_File = sound_File
        self.volume = volume
    
    def Play(self):
        self.sound = py.mixer.Sound(self.sound_File)
        self.sound.set_volume(self.volume)
        self.sound.play()