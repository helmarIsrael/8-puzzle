from .sprite import Button
from .settings import *
import pygame

def create_button(screen, img, rect, type, cursor='arrow'):
    btn = Button()
    w,h = rect.width, rect.height
    if type == 'logo':
        rect.x = 10
        rect.y = (NAV_HEIGHT - h) / 2

    if type == 'shuffle':
        rect.x = ((WIDTH - w) / 2) - 100
        rect.y = HEIGHT - (NAV_HEIGHT + 100) - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -400)

    if type == 'solve':
        rect.x = ((WIDTH - w) / 2) + 110
        rect.y = HEIGHT - (NAV_HEIGHT + 100) - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -400)

    if type == 'help-btn':
        rect.x = WIDTH - w - 20
        rect.y = HEIGHT - h - 20

    if type == 'help-text':
        rect.x = int((WIDTH - w) / 2)
        rect.y = int(HEIGHT - (NAV_HEIGHT*2))

    if type == 'bfs':
        rect.x = int((WIDTH - w - 130) / 2)
        rect.y = HEIGHT - NAV_HEIGHT - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -150)

    if type == 'astar':
        rect.x = int((WIDTH - w + 200) / 2)
        rect.y = HEIGHT - NAV_HEIGHT - (TILESIZE*GAME_SIZE) - (TOP_MARGIN * -150)

    btn.draw_img(screen, img, rect)
 
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    return btn