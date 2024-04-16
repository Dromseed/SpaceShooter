import pygame
import sys

class Spaceship:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def rotate(self, angle_change):
        self.angle += angle_change

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect)

pygame.init()

# Установка размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating Spaceship")

# Создание объекта космического корабля
spaceship = Spaceship(screen_width // 2, screen_height // 2, "image/player.png")

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка пользовательского ввода
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.rotate(1)
    if keys[pygame.K_RIGHT]:
        spaceship.rotate(-1)

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отображение корабля
    spaceship.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
