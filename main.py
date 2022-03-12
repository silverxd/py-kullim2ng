import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1900, 1050), 
                                 pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.wx, self.wy = pygame.display.get_surface().get_size()

        self.x, self.y = 120, self.wy/2
        self.running = True

        self.moveX = 0
        self.moveY = 0
        self.color = [100, 100, 100]

        self.x2, self.y2 = self.wx - 120,self.wy/2

        self.moveX2 = 0
        self.moveY2 = 0


        

    def event(self):
        event_list = pygame.event.get()
        self.x += self.moveX
        self.y += self.moveY
        self.x2 += self.moveX2
        self.y2 += self.moveY2
        self.color[0] = random.randint(0, 255)
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
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_d:
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

        if self.y < 0 :
            self.y = self.wy - 10
        if self.x > self.wx - 10:
            self.x = 0
        if self.x < 0:
            self.x = self.wx - 10
        if self.y > self.wy - 10:
            self.y = 0

        if self.y2 < 0:
            self.y2 = self.wy - 10
        if self.x2 > self.wx - 10:
            self.x2 = 0
        if self.x2 < 0:
            self.x2 = self.wx - 10
        if self.y2 > self.wy - 10:
            self.y2 = 0

        print(self.x, self.y, "VS", self.x2, self.y2)
        if abs((self.y - self.y2)) < 70 and abs((self.x - self.x2)) < 70:
            self.running = False


    def update(self):
        pass

    def render(self):
        self.window.fill((51, 0, 0))
        pygame.draw.rect(self.window, (self.color[0], self.color[1], self.color[2]), (self.x, self.y, 40, 40))
        pygame.draw.rect(self.window, (255-self.color[0], 255-self.color[1], 255-self.color[2]), (self.x2, self.y2, 40, 40))

        pygame.display.update()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
