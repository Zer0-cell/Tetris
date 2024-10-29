import pygame as pg
import math

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24, 89, 117)

SPRITE_DIR_PATH = 'assets/sprites'
FONT_PATH = 'assets/font/KarmaticArcade-6Yrp1.ttf'

ANIM_TIME_INTERVAL = 200  
FAST_ANIM_TIME_INTERVAL = 20

TILE_SIZE = 40
FIELD_SIZE = FIELD_W, FIELD_H = 8, 15
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

class Text:
    def __init__(self, app):
        self.app = app
        self.font = pg.freetype.Font(FONT_PATH)

    def get_color(self):
        time = pg.time.get_ticks() * 0.001
        n_sin = lambda t: (math.sin(t) * 0.5 + 0.5) * 255
        return n_sin(time * 0.5), n_sin(time * 0.2), n_sin(time * 0.9)

    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.595, WIN_H * 0.02),
                            text='TETRIS', fgcolor=self.get_color(),
                            size=TILE_SIZE * 1.32, bgcolor='black')  
        self.font.render_to(self.app.screen, (WIN_W * 0.65, WIN_H * 0.22),
                            text='next', fgcolor='orange',
                            size=TILE_SIZE * 1.12, bgcolor='black')  
        self.font.render_to(self.app.screen, (WIN_W * 0.64, WIN_H * 0.67),
                            text='score', fgcolor='orange',
                            size=TILE_SIZE * 1.12, bgcolor='black') 
        self.font.render_to(self.app.screen, (WIN_W * 0.64, WIN_H * 0.8),
                            text=f'{self.app.tetris.score}', fgcolor='white',
                            size=TILE_SIZE * 1.44)  

