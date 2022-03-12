import pygame
import random

## Krt ei toimi

class Game:
    def __init__(self):
        pygame.init()                                               #Thank you for the base "engine" code @blimly & @Gorane7 <3
        
        self.window_size = (640, 480)
        self.window = pygame.display.set_mode((self.window_size), 
                                 pygame.RESIZABLE)                  #MIND BLOWN
        self.clock = pygame.time.Clock()

        self.wx, self.wy = pygame.display.get_surface().get_size()  #Get window resolution

        self.x, self.y = 120, self.wy/2            #Scalable starting position
        self.running = True

        self.moveX = 0                             #Initialize some values
        self.moveY = 0
        self.color = [100, 100, 100]

        self.x2, self.y2 = self.wx - 120,self.wy/2 #"I am proud of this" -silver

        self.moveX2 = 0
        self.moveY2 = 0

        self.end_counter = 0
        self.state = "ingame"
        self.end_surface = pygame.Surface(self.window_size)
        self.end_surface.fill((255, 0, 0))

        

    def event(self):
        event_list = pygame.event.get()
        self.x += self.moveX
        self.y += self.moveY
        self.x2 += self.moveX2                  #This is absolutely genius!
        self.y2 += self.moveY2
        self.color[0] = random.randint(0, 255)     #Will replace by smooth RGB fade later 
        self.color[1] = random.randint(0, 255)
        self.color[2] = random.randint(0, 255)
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
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
        for event in event_list:            #TIf in doubt, just double use the function and hope for the best LOL
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_d:   #P2 controls
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

        if self.y < 0 :                 #P1 logic
            self.y = self.wy - 10
        if self.x > self.wx - 10:
            self.x = 0
        if self.x < 0:
            self.x = self.wx - 10
        if self.y > self.wy - 10:
            self.y = 0

        if self.y2 < 0:                 #P2 logic
            self.y2 = self.wy - 10
        if self.x2 > self.wx - 10:
            self.x2 = 0
        if self.x2 < 0:
            self.x2 = self.wx - 10
        if self.y2 > self.wy - 10:
            self.y2 = 0

        print(self.x, self.y, "VS", self.x2, self.y2)   #Some debug code
        if abs((self.y - self.y2)) < 70 and abs((self.x - self.x2)) < 70:
            self.state = "gameover"


    def update(self):
        pass
        if self.state == "gameover":        #Budget endscreen logic
            self.end_counter += 10
            if self.end_counter >= 200:
                self.running = False

    def render(self):
        self.window.fill((51, 0, 0))
        pygame.draw.rect(self.window, (self.color[0], self.color[1], self.color[2]), (self.x, self.y, 40, 40))                  #Draw P1
        pygame.draw.rect(self.window, (255-self.color[0], 255-self.color[1], 255-self.color[2]), (self.x2, self.y2, 40, 40))    #And P2

        if self.state == "gameover":
            self.end_surface.set_alpha(self.end_counter)    #Render endscreen I think
            self.window.blit(self.end_surface, (0, 0))

        pygame.display.update()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(60)     #BAD BAD BAD BAD BAD BAD BAD BAD


if __name__ == '__main__':      #I honestly have no clue what this does
    game = Game()
    game.run()
    pygame.quit()
