"""
Основной файл проекта. Здесь находится класс "Game"
"""

from constants import *
from bird import Bird
from obstacles import Obstacles


class Game:
    """
    Основной класс игры. Он описывает основные компоненты игры
    """

    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Flappy Bird")

        self.setup()

    def setup(self):
        """
        Используется для создания новой игры. Устанавливаются все атрибуты класса
        :return:
        """
        self.mode = "game"
        self.clock = pg.time.Clock()
        self.is_running = False

        self.bird = Bird()
        self.upper_obstacles = pg.sprite.Group()
        self.lower_obstacles = pg.sprite.Group()
        self.background = pg.image.load("Flappy Bird Assets 1.6 (RaR)/Flappy Bird Assets/Background/Background5.png")
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.bird)
        self.score = 0
        self.timer = 2000
        self.time = pg.time.get_ticks()
        self.score_timer = 2000
        self.score_time = pg.time.get_ticks()
        self.speed = 5

        self.run()

    def run(self):
        """
        Метод для запуска игры. Начало игрового цикла
        :return:
        """
        self.is_running = True
        while self.is_running:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()
        quit()

    def event(self):
        """
        Метод проверки события. Проверка нажатий кнопок клавиатуры и мыши
        :return:
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.bird.jump()
            if event.type == pg.KEYDOWN and self.mode == "game over":
                self.mode = "game"
                self.setup()

    def update(self):
        """
        Метод для обновления. Обновляется режим игры, а также атрибуты и группы спрайтов
        :return:
        """
        if self.mode == "game over":
            return
        self.bird.update()
        self.upper_obstacles.update()
        self.lower_obstacles.update()

        if self.bird.rect.y >= SCREEN_HEIGHT:
            self.mode = "game over"

        if self.time + self.timer < pg.time.get_ticks():
            upper_obstacle = Obstacles(-64, -32, self.speed)
            lower_obstacle = Obstacles(SCREEN_HEIGHT - 180, SCREEN_HEIGHT - 100, self.speed)
            self.all_sprites.add(upper_obstacle, lower_obstacle)
            self.upper_obstacles.add(upper_obstacle)
            self.lower_obstacles.add(lower_obstacle)
            self.time = pg.time.get_ticks()
        if pg.sprite.spritecollide(self.bird, self.upper_obstacles, False) or pg.sprite.spritecollide(self.bird,
                                                                                                      self.lower_obstacles,
                                                                                                      False):
            self.mode = "game over"

        if self.score_time + self.score_timer < pg.time.get_ticks():
            self.score += 1
            self.score_time = pg.time.get_ticks()
            if self.score % 5 == 0:
                self.speed += 1
                self.timer -= 200
                if self.timer <= 500:
                    self.timer = 500

    def draw(self):
        """
        Метод для отрисовки. Отображаются все группы спрайтов и выводится текст на экран
        :return:
        """
        pg.display.flip()
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)

        if self.mode == "game":
            score_text = font.render(str(self.score), True, (255, 255, 255))
            score_text_rect = score_text.get_rect(topleft=(50, 10))
            self.screen.blit(score_text, score_text_rect)

        if self.mode == "game over":
            text = font.render("Вы проиграли", True, (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            score_text = font.render(f"Вы набрали {self.score} очков", True, (255, 0, 0))
            score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            self.screen.blit(text, text_rect)
            self.screen.blit(score_text, score_text_rect)
        pg.display.flip()


if __name__ == "__main__":
    game = Game()
