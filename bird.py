import pygame as pg
from constants import *

class Bird:
    def __init__(self):
        super(Bird, self).__init__()

        self.load_animations()
        self.current_animation = self.idle_animation
        self.current_image = 0

        self.image = self.current_animation[self.current_image]

        self.rect = self.image.get_rect()
        self.rect.center = ()  # Начальное положение персонажа

        self.phys_box = pg.Rect(0, 0, self.rect.w * 0.5, self.rect.h)

        # Начальная скорость и гравитация
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 2
        self.is_jumping = False
        self.timer = pg.time.get_ticks()
        self.interval = 200
        self.hp = 10
        self.damage_timer = pg.time.get_ticks()
        self.damage_interval = 1000


    def update(self):


    def jump(self):
        self.velocity_y = -TILE_SCALE * 8
        self.is_jumping = True

    def load_animation(self):
        tile_size = 16

        self.idle_animation = []
        num_images = 4
        spriteshet = pg.image.load("Flappy Bird Assets 1.6 (RaR)/Flappy Bird Assets/Player/StyleBird1/Bird1-1.png")
        for i in range(num_images):
            x = i * tile_size
            y = 0
            rect = pg.Rect(x, y, tile_size, tile_size)
            image = spriteshet.subsurface(rect)
            image = pg.transform.scale_by(image, TILE_SCALE)
            self.idle_animation.append(image)
