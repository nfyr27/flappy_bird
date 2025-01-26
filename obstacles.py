"""
Модуль для препятствий
"""

import random

from constants import *


class Obstacles(pg.sprite.Sprite):
    """
    Класс препятствий
    """
    def __init__(self, a, b, speed):
        super(Obstacles, self).__init__()

        width_obstacle = 32
        height_obstacle = 80

        num_images = 8
        spritesheet = pg.image.load("Flappy Bird Assets 1.6 (RaR)/Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png")
        list_images = []
        for i in range(num_images // 2):
            for j in range(2):
                x = i * width_obstacle
                y = j * height_obstacle
                rect = pg.Rect(x, y, width_obstacle, height_obstacle)
                image = spritesheet.subsurface(rect)
                image = pg.transform.scale_by(image, TILE_SCALE)
                list_images.append(image)

        self.image = random.choice(list_images)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(a, b)
        self.speed = speed

    def update(self):
        """
        Метод для обновлений. Устанавливается скорость движения препятстий
        :return: 
        """
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()
