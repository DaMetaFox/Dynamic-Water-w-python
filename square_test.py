import pygame as pg
from waterBody import WaterBody
from math import sqrt

class Square():
    def __init__(self, window, pos):
        self.wd = window
        self.raw_width = 60

        self.VEL = 7
        self.VEL_ON_WATER = 4.3
        self.direction = pg.math.Vector2(0, 0)

        #surface
        self.surface_width = sqrt((self.raw_width**2)*2)
        self.surface = pg.Surface((self.surface_width, self.surface_width))
        self.surface.set_colorkey((0, 0, 0))
        self.mask = pg.mask.from_surface(self.surface)
        
        #raw_surface
        self.raw_surface = pg.Surface((self.raw_width, self.raw_width))
        self.raw_surface.fill((255, 0, 0))
        self.raw_surface.set_colorkey((0, 0, 0))
        
        #positions
        self.topleft_x = pos[1]
        self.topleft_y = pos[0]
        self.center_x = lambda : self.topleft_x + self.surface_width/2
        self.center_y = lambda : self.topleft_y + self.surface_width/2
        
        self.on_shallow = False
        
    def rotate(self):
        angle = self.direction.angle_to(pg.math.Vector2(0, 0))
        self.surface = pg.transform.rotate(self.raw_surface, angle)
        self.mask = pg.mask.from_surface(self.surface)
    
    def move_to_mouse(self, mouse_x, mouse_y):
        
        #maybe the mouse is offscreen
        if mouse_x == None or mouse_y == None:
            return
        
        self.direction.x = mouse_x - self.center_x()
        self.direction.y = mouse_y - self.center_y()
        if self.direction.magnitude() > self.VEL:
            self.direction.normalize_ip()
             
            self.topleft_x += self.direction.x * self.VEL
            self.topleft_y += self.direction.y * self.VEL
            
            self.rotate()
        else:
            self.direction.x, self.direction.y = 0, 0
    
    def blit(self):
        self.wd.blit(self.surface, (self.topleft_x, self.topleft_y))
        
    def update(self, mouse_x, mouse_y):
        self.move_to_mouse(mouse_x, mouse_y)
        self.blit()



if __name__ == '__main__':
    
    #constants
    BACKGROUND_COLOR = (71, 200, 231)
    FPS = 50
    
    window = pg.display.set_mode((1000, 700))
    square = Square(window, (200, 200))
    water = WaterBody(window, 0, 400, 1000, 300, D=0.009)
    clock = pg.time.Clock()
    running = True
    
    while running:
        window.fill(BACKGROUND_COLOR)
        clock.tick(FPS)
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        
        is_mouse_on_screen = pg.mouse.get_focused()
        if is_mouse_on_screen:
            mouse_pos = pg.mouse.get_pos()
            square.update(mouse_pos[0], mouse_pos[1])
        else:
            square.update(None, None)
        
        #check if the square is on the white line of the water
        if water.is_on_shallow(square.mask, square.topleft_x, square.topleft_y):
            if not square.on_shallow:
                splash_width = round(square.raw_width*1.2)
                splash_force = 0.5 * round(square.direction.y, 0)
                
                water.splash(square.center_x(), splash_width, splash_force)
                square.on_shallow = True
            else:
                square.on_shallow = False
            

        water.update()
        pg.display.update()
    
    pg.quit()
    quit()

        