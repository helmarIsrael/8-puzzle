from .sprite import Button
from .settings import *
import pygame

def create_button(screen, img, rect, type, cursor='arrow'):
    btn = Button()
    w,h = rect.width, rect.height

    if type == 'shuffle':
        rect.x = ((WIDTH - w) / 2) - 100
        rect.y = HEIGHT - (NAV_HEIGHT + 100) - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -650)

    if type == 'solve':
        rect.x = ((WIDTH - w) / 2) + 110
        rect.y = HEIGHT - (NAV_HEIGHT + 100) - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -650)

    if type == 'bfs':
        rect.x = int((WIDTH - w - 130) / 2)
        rect.y = HEIGHT - NAV_HEIGHT - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -400)

    if type == 'astar':
        rect.x = int((WIDTH - w + 200) / 2)
        rect.y = HEIGHT - NAV_HEIGHT - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -400)

    btn.draw_img(screen, img, rect)
 
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    return btn