import pygame
import random
import time;
import math

estimatedFps = 2000
c = [255,0,0]
vt = 400 # Värvi muutumise kiirus
vv = 40  # Mängijate muutumise kiirus

class Game:
    def __init__(self):
        pygame.init()                                               # Thank you for the base "engine" code @blimly & @Gorane7 <3
        self.t0 = time.time()
        self.window_size = (640, 480)
        self.window = pygame.display.set_mode((self.window_size), pygame.RESIZABLE)                  # MIND BLOWN
        pygame.display.set_caption("Kullimang V.0.0")
        self.clock = pygame.time.Clock()

        self.wx, self.wy = pygame.display.get_surface().get_size()  # Get window resolution

        self.x, self.y = 120, self.wy/2            # Scalable starting position
        self.running = True
        self.fpsCount = True
        self.moveX = 0                             # Initialize some values
        self.moveY = 0
        self.color = [100, 100, 100]

        self.x2, self.y2 = self.wx - 120,self.wy/2 # "I am proud of this" -silver

        self.moveX2 = 0
        self.moveY2 = 0
        
        self.end_counter = 0
        self.state = "ingame"
        self.end_surface = pygame.Surface(self.window_size)
        self.end_surface.fill((255, 0, 0))
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        #############################
        self.cycle = 0
        self.fpsTimes = []
        for i in range(estimatedFps):
            self.fpsTimes.append(estimatedFps)

        self.fpsText = ""

        #############################

        

    def event(self):

        #################
        t1 = time.time()
        dt = (t1-self.t0) # Kiiremini värve vahetada
        
        self.t0 = t1

        self.fpsText = ""
        if self.fpsCount:
            self.fpsTimes.pop()
            self.fpsTimes.insert(0, math.floor(1/dt))
            self.fpsText = str(math.floor(sum(self.fpsTimes)/len(self.fpsTimes)))
        #################
        event_list = pygame.event.get()
        self.x += self.moveX*vv*dt
        self.y += self.moveY*vv*dt
        self.x2 += self.moveX2*vv*dt                  # This is absolutely genius!
        self.y2 += self.moveY2*vv*dt
        #self.color[0] = random.randint(0, 255)     # Will replace by smooth RGB fade later 
        #self.color[1] = random.randint(0, 255)     # Replace finished!
        #self.color[2] = random.randint(0, 255)
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.fpsCount ^=True
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.moveX = 20
                    self.moveY = 0
                elif event.key == pygame.K_LEFT:
                    self.moveX =- 20
                    self.moveY = 0
                elif event.key == pygame.K_DOWN:
                    self.moveX = 0
                    self.moveY = 20
                elif event.key == pygame.K_UP:
                   self.moveX = 0
                   self.moveY =- 20
        for event in event_list:            # If in doubt, just double use the function and hope for the best LOL
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_d:   # P2 controls
                    self.moveX2 = 20
                    self.moveY2 = 0
                elif event.key == pygame.K_a:
                    self.moveX2 =- 20
                    self.moveY2 = 0
                elif event.key == pygame.K_s:
                    self.moveX2 = 0
                    self.moveY2 = 20
                elif event.key == pygame.K_w:
                   self.moveX2 = 0
                   self.moveY2 =- 20

        if self.y < 0 :                 # P1 logic
            self.moveY = 10             # Used to be here to teleport player
        if self.x > self.wx - 40:       # to the other side of the window upon
            self.moveX = -10            # reaching the end, but was replaced
        if self.x < 0:                  # by an epic BOUNCE function.
            self.moveX = 10
        if self.y > self.wy - 40:
            self.moveY = -10

        if self.y2 < 0:                 # P2 logic
            self.moveY2 = 10
        if self.x2 > self.wx - 40:
            self.moveX2 = -10
        if self.x2 < 0:
            self.moveX2 = 10
        if self.y2 > self.wy - 40:
            self.moveY2 = -10

################################## Ei puutu


        if(self.cycle==0): ## Suurenda teist väärtust
            c[1] += vt*dt
            if(c[1] >= 255):
                c[1] = 255
                self.cycle=1
        elif(self.cycle==1): ## Hakka esimest väärtust vähendama
            c[0] -= vt*dt
            if(c[0] <=0):
                c[0] = 0
                self.cycle=2
        elif(self.cycle==2): ## Hakka viimast väärtust suurendama
            c[2] += vt*dt
            if(c[2] >=255):
                c[2] = 255
                self.cycle=3
        elif(self.cycle==3): ## Hakka teist väärtust vähendama
            c[1] -= vt*dt
            if(c[1] <=0):
                c[1] = 0
                self.cycle=4
        elif(self.cycle==4): ## Hakka esimest väärtust vähendama
            c[0] += vt*dt
            if(c[0] >=255):
                c[0] = 255
                self.cycle=5
        elif(self.cycle==5): ## Hakka esimest väärtust vähendama
            c[2] -= vt*dt
            if(c[2] <= 0):
                c[2] = 0
                self.cycle=0

        









###################################

        if abs((self.y - self.y2)) < 40 and abs((self.x - self.x2)) < 40:   # INSANE COLLISION TESTER
            self.state = "gameover"


    def update(self):
        pass
        if self.state == "gameover":        # Budget endscreen logic
            self.end_counter += 10
            if self.end_counter >= 200:
                self.running = False

    def render(self):
        self.window.fill((51, 0, 0))
        pygame.draw.rect(self.window, (c[0], c[1], c[2]), (self.x, self.y, 40, 40))                  # Draw P1
        pygame.draw.rect(self.window, (255-c[0], 255-c[1], 255-c[2]), (self.x2, self.y2, 40, 40))    # And P2, with opposite colors
        self.window.blit(self.font.render(self.fpsText, True, (255,0,0), (0,0,255)), (10,10))

        

        if self.state == "gameover":
            self.end_surface.set_alpha(self.end_counter)    # Render endscreen I think
            self.window.blit(self.end_surface, (0, 0))

        pygame.display.update()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            #self.clock.tick(300)     # BAD BAD BAD BAD BAD BAD BAD BAD


if __name__ == '__main__':      # I honestly have no clue what this does
    game = Game()
    game.run()
    pygame.quit()