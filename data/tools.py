import os
import pygame as pg

from . import setup

class Control(object):
    def __init__(self):
        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.run = True

    def process(self, keys_pressed):
        # else:
        #     if court.initial_data[court.ball.position] != translate_piece_to_data("net"):
        #         court.update_position("empty", court.ball.position)
        #     court.update_position("ball", new_position)
        if keys_pressed[pg.K_LEFT]:
            print('left')
            # new_position = court.ball.position + court.directions["left"]
            # is_valid(court.data[new_position]) and court.move_ball(new_position)
        elif keys_pressed[pg.K_UP]:
            print('up')
            # new_position = court.ball.position + court.directions["up"]
            # is_valid(court.data[new_position]) and court.move_ball(new_position)
        elif keys_pressed[pg.K_RIGHT]:
            print('right')
            # new_position = court.ball.position + court.directions["right"]
            # is_valid(court.data[new_position]) and court.move_ball(new_position)
        elif keys_pressed[pg.K_DOWN]:
            print('down')
            # new_position = court.ball.position + court.directions["down"]
            # is_valid(court.data[new_position]) and court.move_ball(new_position)

    def end_loop(self):
        self.run = False

    def event_loop(self):
    # loops through events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.end_loop()
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.process(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            # elif event.type == pg.MOUSEBUTTONDOWN:

    def draw(self, interpolate):
        # self.state_machine.draw(self.screen, interpolate)
        pg.display.update()
        # self.show_fps()

    def main(self):

        lag = 0.0
        while self.run:

            self.event_loop()
            lag += self.clock.tick(setup.FPS)
            self.event_loop()
            while lag >= setup.TIME_PER_UPDATE:
                # self.update()
                lag -= setup.TIME_PER_UPDATE
            self.draw(lag/setup.TIME_PER_UPDATE)

            # # sets window fill colour

        # ends game
        pg.quit()
