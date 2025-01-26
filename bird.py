"""
Модуль персонажа
"""


from constants import *

class Bird(pg.sprite.Sprite):
    """
    Класс персонажа
    """
    def __init__(self):
        super(Bird, self).__init__()

        self.load_animation()
        self.current_animation = self.idle_animation
        self.current_image = 0

        self.image = self.current_animation[self.current_image]

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Начальное положение персонажа

        self.phys_box = pg.Rect(0, 0, self.rect.w * 0.5, self.rect.h)

        # Начальная скорость и гравитация
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5
        self.is_jumping = False
        self.timer = pg.time.get_ticks()
        self.interval = 200


    def update(self):
        """
        Метод для обновления. Здесь проверяются нажатия кнопок мыши
        :return:
        """
        mouse = pg.mouse.get_pressed()
        if mouse[0] and not self.is_jumping:
            self.jump()

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

    def jump(self):
        """
        Метод для прыжков. Устанавливается скорость прыжка
        :return:
        """
        self.velocity_y = -TILE_SCALE * 3   # скорость прыжка вверх
        self.is_jumping = True

    def load_animation(self):
        """
        Метод для загрузки файлов.
        :return:
        """
        tile_size = 16

        self.idle_animation = []
        num_images = 4
        spritesheet = pg.image.load("Flappy Bird Assets 1.6 (RaR)/Flappy Bird Assets/Player/StyleBird1/Bird1-1.png")
        for i in range(num_images):
            x = i * tile_size
            y = 0
            rect = pg.Rect(x, y, tile_size, tile_size)
            image = spritesheet.subsurface(rect)
            image = pg.transform.scale_by(image, TILE_SCALE)
            self.idle_animation.append(image)
