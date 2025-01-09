import pygame as pg
from constants import *
from bird import Bird

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Flappy Bird")


        self.bird = Bird()

        self.setup()

    def setup(self):
        self.mode = "game"
        self.clock = pg.time.Clock()
        self.is_running = False

        self.run()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()
        quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.bird.jump()
    def update(self):
        ...
    def draw(self):
        pg.display.flip()

if __name__ == "__main__":
    game = Game()