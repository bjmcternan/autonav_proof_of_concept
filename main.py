import math
import pygame as pg
from pygame.math import Vector2
from bot_sprite import Player

def main():
    lInc = 0
    rInc = 0
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    player = Player((420, 420),0)
    playersprite = pg.sprite.RenderPlain((player))

    clock = pg.time.Clock()
    done = False
    while not done:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONUP:
                x, y = pg.mouse.get_pos()
                player.add_coordinate(x, y, 0)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_KP7:
                    lInc += .2
                if event.key == pg.K_KP9:
                    rInc += .2
                if event.key == pg.K_KP1:
                    lInc -= .2
                if event.key == pg.K_KP3:
                    rInc -= .2
                if event.key == pg.K_KP5:
                    rInc = 0
                    lInc = 0
        if(lInc > 1):
            lInc = 1
        elif(lInc < -1):
            lInc = -1

        if(rInc > 1):
            rInc = 1
        elif(rInc < -1):
            rInc = -1
        
        playersprite.update()

        screen.fill((255, 255, 255))
        playersprite.draw(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()
    pg.quit()