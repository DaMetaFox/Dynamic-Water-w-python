#@Git Hub: DaMetafox 


import pygame as pg

class WaterBody():
    def __init__(self, window, topleft_x, topleft_y, width, height,
                 K = 0.0045,
                 D = 0.0050,
                 SPREAD = 0.038,
                 SPRING_SEPARATION = 4, 
                 COLOR = [40, 53, 255], 
                 ALPHA = 60
                 ):
        
        self.wd = window

        self.topleft_x = topleft_x
        self.topleft_y = topleft_y
        
        self.height = height
        self.width = width
        
        self.SPREAD = SPREAD
        self.COLOR = COLOR
        self.ALPHA = ALPHA
        self.SPRING_SEPARATION = SPRING_SEPARATION
        
        self.surface = pg.Surface([width, height*3])
        self.surface.set_colorkey([0, 0, 0])
        self.surface.set_alpha(self.ALPHA)
        
        self.target_height = height*2
        
        #{x:WaterBody.Spring(), ...}
        self.springs = {i:self.Spring(self, self.target_height, K, D) for i in range(0, width+1, self.SPRING_SEPARATION)}
        
        self.mask_topleft_x = self.topleft_x
        self.mask_topleft_y = self.topleft_y - self.target_height
        
        self.__update_surface()
    
    #also updates the mask
    def __update_surface(self):
        self.surface.fill([0, 0, 0])
        
        #list[x, y]
        points_list = [[i, self.springs[i].height] for i in self.springs]
        line = points_list.copy()
        
        points_list.append([self.width, self.height*3]) #right bottom
        points_list.append([0, self.height*3]) # left bottom
        
        pg.draw.polygon(self.surface, self.COLOR, points_list)
        
        pg.draw.lines(self.surface, [255, 255, 255], False, line, width=3)
        self.mask = pg.mask.from_surface(self.surface)
        self.shallow_mask = pg.mask.from_threshold(self.surface, (255, 255, 255), (1, 1, 1, 255))
        
    def __blit(self):
        self.wd.blit(self.surface, [self.topleft_x, self.topleft_y-2*self.height])

    def update(self):
        self.chaining()
        for i in self.springs.values():
            i.update()
        self.__update_surface()
        self.__blit()
    
    def chaining(self):
        
        left_deltas = [0 for i in self.springs]
        right_deltas = [0 for i in self.springs]

        for i in range(1, len(self.springs)-1):
            spring = self.springs[i*self.SPRING_SEPARATION]
            left_spring = self.springs[(i-1)*self.SPRING_SEPARATION]
            right_spring = self.springs[(i+1)*self.SPRING_SEPARATION]
            
            
            left_deltas[i] = self.SPREAD * (spring.height - left_spring.height)
            left_spring.velocity += left_deltas[i]
            
            right_deltas[i] = self.SPREAD * (spring.height - right_spring.height)
            right_spring.velocity += right_deltas[i]
            
    def splash(self, center_x, width, force):
        center_x = round(center_x, 0)
        
        left_pixel_x = center_x-width/2 #this value is in pixels
        i = 0
        while True:
            if (left_pixel_x + i) % self.SPRING_SEPARATION == 0:
                left_pixel_x = left_pixel_x + i
                break
            if (left_pixel_x - i) % self.SPRING_SEPARATION == 0:
                left_pixel_x = left_pixel_x - i
                break
            i += 1
        
        for i in range(width//self.SPRING_SEPARATION):
            self.springs[left_pixel_x+(i*self.SPRING_SEPARATION)].velocity += force
    
    def is_on_water(self, mask, topleft_x, topleft_y):
        offset_x = topleft_x - self.mask_topleft_x
        offset_y = topleft_y - self.mask_topleft_y
        
        return self.mask.overlap(mask, (offset_x, offset_y))
    
    def is_on_shallow(self, mask, topleft_x, topleft_y):
        offset_x = topleft_x - self.mask_topleft_x
        offset_y = topleft_y - self.mask_topleft_y
        
        return self.shallow_mask.overlap(mask, (offset_x, offset_y))
    
    class Spring:
        def __init__(self, waterbody, height, K, D):
            self.waterbody = waterbody

            #f = -k*x
            #loss = -d*v
            #CONSTANTS
            self.K = K
            self.D = D

            self.height = height
            self.spring_extension = self.height-self.waterbody.target_height
            
            self.force = 0
            self.velocity = 0

        def update(self):
            spring_extension = self.height - self.waterbody.target_height
            
            loss = -self.D * self.velocity
            self.force = -self.K * spring_extension + loss
            
            self.velocity += self.force
            self.height += self.velocity
