import pygame as pg
from waterBody import WaterBody

FPS = 60

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
pg.init()


class Rock():
    def __init__(self, pos:tuple):
        self.half_width = 15
        self.topleft_x = pos[0]
        self.topleft_y = pos[1]
        self.center_x = lambda : self.topleft_x + self.half_width
        self.center_y = lambda : self.topleft_y + self.half_width
        
        self.image = self.__load_image()
        self.mask = pg.mask.from_surface(self.image)
        self.is_wet = False
        

    def __load_image(self):
        image = pg.image.load("rock.png")
        image.set_colorkey((255, 255, 255))
        image = pg.transform.scale(image, (self.half_width*2, self.half_width*2))
        return image
    
    def update(self):
        if self.is_wet:
            self.topleft_y += 4
        else:
            self.topleft_y += 5



window = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pg.time.Clock()

rocks = []
water = WaterBody(window, 0, 500, WINDOW_WIDTH, 200, K=0.004, D=0.0035)


while True:
    window.fill((71, 200, 231))
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            rocks.append(Rock(pg.mouse.get_pos()))
    
    for rock in rocks:
        #water.is_in_shallow returns true if a mask is on the white line of the water
        if water.is_on_shallow(rock.mask, rock.topleft_x, rock.topleft_y):
            if rock.is_wet == False:
                splash_width = (rock.half_width+22)*2
                water.splash(rock.center_x(), splash_width, 2)
                
                rock.is_wet = True
        
        if rock.topleft_y > WINDOW_HEIGHT:
            rocks.remove(rock)
        
        rock.update()
        window.blit(rock.image, [rock.topleft_x, rock.topleft_y])
    water.update()
    
    pg.display.update()
