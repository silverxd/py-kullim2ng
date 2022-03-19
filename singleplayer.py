import pygame
import random
import time
import math

estimatedFps = 60
c = [255, 0, 0]
vt = 400  # Värvi muutumise kiirus
vv = 40  # Mängijate  kiirus
bol = 400


class Game:
    def __init__(self):



        pygame.init()  # Thank you for the base "engine" code @blimly & @Gorane7 <3

        self.soundTrack = pygame.mixer.Sound("epic.mp3")
        self.bounce = pygame.mixer.Sound("playerBounce.wav")

        self.cycle = 0
        self.t0 = time.time()
        self.window_size = (640, 480)
        self.window = pygame.display.set_mode((self.window_size), pygame.RESIZABLE)  # MIND BLOWN
        pygame.display.set_caption("Kullimang SINGLEPLAYER V.0.0")
        self.clock = pygame.time.Clock()
        self.runningInt = 1
        self.wx, self.wy = pygame.display.get_surface().get_size()  # Get window resolution

        self.x, self.y = self.wx - 120, self.wy / 2  # "I am proud of this" -silver
        self.running = True
        self.fpsCount = True
        self.moveX = 0  # Initialize some values
        self.moveY = 0
        self.color = [100, 100, 100]
        self.score = 0

        self.playersize = 40
        self.end_counter = 0
        self.state = "ingame"
        self.end_surface = pygame.Surface(self.window_size)
        self.end_surface.fill((255, 0, 0))
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.ballSpeed = bol
        #############################
        self.cycle = 0
        self.fpsTimes = []
        for i in range(estimatedFps):
            self.fpsTimes.append(estimatedFps)

        self.ballPos = [50, 50]
        self.ballDir = [random.randint(-100, 100), random.randint(-100, 100)]
        self.fpsText = ""

        #############################

    def event(self):

        #################
        t1 = time.time()
        dt = (t1 - self.t0)  # Kiiremini värve vahetada
        self.score += self.runningInt * dt

        self.t0 = t1

        self.fpsText = ""
        if self.fpsCount:
            self.fpsTimes.pop()
            self.fpsTimes.insert(0, math.floor(1 / dt))
            self.fpsText = str(math.floor(sum(self.fpsTimes) / len(self.fpsTimes)))
        #################
        event_list = pygame.event.get()
        self.x += self.moveX * vv * dt * self.playersize / 40  # This is absolutely genius!
        self.y += self.moveY * vv * dt * self.playersize / 40

        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.fpsCount ^= True
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    self.moveX = 20
                    self.moveY = 0
                elif event.key == pygame.K_LEFT:
                    self.moveX = - 20
                    self.moveY = 0
                elif event.key == pygame.K_DOWN:
                    self.moveX = 0
                    self.moveY = 20
                elif event.key == pygame.K_UP:
                    self.moveX = 0
                    self.moveY = - 20
                elif event.key == pygame.K_RETURN and self.state == "gameover":  # Äkki töötab?
                    self.ballSpeed = bol
                    self.runningInt = 1
                    self.score = 0
                    self.state = "ingame"
                    print("game not over")
                    self.end_counter = 0
                    self.cycle = 0
                    self.ballPos = [self.playersize + 10, self.playersize + 10]
                    self.ballDir = [random.randint(-100, 100), random.randint(-100, 100)]
                    self.moveX = 0
                    self.moveY = 0
                    self.x, self.y = self.wx - 120, self.wy / 2
                    self.end_surface.set_alpha(0)

        for event in event_list:

            if event.type == pygame.VIDEORESIZE:
                self.wx, self.wy = pygame.display.get_surface().get_size()
                self.end_surface = pygame.Surface((self.wx, self.wy))  # Endscreen fix
                self.end_surface.fill((255, 0, 0))  # If window is resized and there
                if self.moveX == 0 and self.moveY == 0:  # is no movement yet, move the
                    self.x, self.y = self.wx - 120, self.wy / 2  # players to the edge of the new window


        if self.y < 20:  # Põrke loogika
            pygame.mixer.Sound.play(self.bounce)
            self.moveY = 10
        if self.x > self.wx - 20 - self.playersize:
            pygame.mixer.Sound.play(self.bounce)
            self.moveX = -10
        if self.x < 20:
            pygame.mixer.Sound.play(self.bounce)
            self.moveX = 10
        if self.y > self.wy - 20 - self.playersize:
            pygame.mixer.Sound.play(self.bounce)
            self.moveY = -10


        print("Dir : ", self.ballDir)


        if (self.x == self.wx - 120 and self.y == self.wy / 2):  # Ei teadnud kuidas teistpidi pöörata.
            3*3
        else:
            self.ballSpeed += dt*100
            totalSpeed = math.sqrt(self.ballDir[0]**2 + self.ballDir[1]**2)
            speed = self.ballSpeed / (totalSpeed+1)
            self.ballPos[0] += self.ballDir[0] * dt * speed
            self.ballPos[1] += self.ballDir[1] * dt * speed

        if self.ballPos[0] < 30:
            pygame.mixer.Sound.play(self.bounce)
            self.ballDir[0] = random.randint(-100, 100) + random.choice([-2, 2])

            self.ballPos[0] = 30
            self.ballDir[0] *= -1
        if self.ballPos[0] > self.wx - 30:
            pygame.mixer.Sound.play(self.bounce)
            self.ballDir[0] = random.randint(-100, 100) + random.choice([-2, 2])
            self.ballPos[0] = self.wx - 30
            self.ballDir[0] *= -1

        if self.ballPos[1] < 30:
            pygame.mixer.Sound.play(self.bounce)
            self.ballDir[1] = random.randint(-100, 100) + random.choice([-2, 2])
            self.ballPos[1] = 30
            self.ballDir[1] *= -1

        if self.ballPos[1] > self.wy - 30:
            pygame.mixer.Sound.play(self.bounce)
            self.ballDir[1] = random.randint(-100, 100) +  random.choice([-2, 2])
            self.ballPos[1] = self.wy - 30
            self.ballDir[1] *= -1


        ########
        s = self.cycle

        c[[1, 0, 2][s % 3]] += dt * vt * (1 - 2 * (s % 2))
        if (c[[1, 0, 2][s % 3]] >= 255 or c[[1, 0, 2][s % 3]] < 0):
            c[[1, 0, 2][s % 3]] = 255 * (1 - s % 2)
            s = (s + 1) % 6
        self.cycle = s

        if abs((self.ballPos[1] - self.y)) < self.playersize + 5 and abs(
                (self.ballPos[0] - self.x)) < self.playersize + 5:  # INSANE COLLISION TESTER
            self.state = "gameover"


    ##  Mart lubas - (allkiri)
    def update(self):
        pass
        if self.state == "gameover":  # Budget endscreen logic
            self.end_counter += 10

    def render(self):
        self.window.fill((51, 0, 0))
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, self.playersize, self.playersize))  # Draw P1


        pygame.draw.circle(self.window, (c[0], c[1], c[2]), (self.ballPos[0], self.ballPos[1]), self.playersize / 2, 10)


        pygame.draw.rect(self.window, (c[0], c[1], c[2]),
                         [0, 0, self.wx, self.wy], 20)
        self.window.blit(self.font.render(self.fpsText, True, (255, 0, 0), (0, 0, 255)), (10, 10))

        if self.state == "gameover":
            self.moveX = 0
            self.moveY = 0
            self.ballSpeed = 0
            self.runningInt = 0
            self.end_surface.set_alpha(self.end_counter)  # Render endscreen I think
            self.window.blit(self.end_surface, (0, 0))
            if self.end_counter >= 200:
                self.scoreText = self.font.render("Score : " + str(math.floor(self.score)), True, (255, 255, 255))
                self.gameovertext = self.font.render('SEPPO NO MOOR!', True, (255, 255, 255))
                self.gameovertext2 = self.font.render('Press ENTER to play again!', True, (255, 255, 255))
                self.window.blit(self.scoreText, ((self.wx - self.scoreText.get_width()) / 2,
                                                  240 - self.scoreText.get_height() / 2 - 30))  # sketchy AF code but it works
                self.window.blit(self.gameovertext, ((self.wx - self.gameovertext.get_width()) / 2,
                                                     240 - self.gameovertext.get_height() / 2))  # sketchy AF code but it works
                self.window.blit(self.gameovertext2, ((self.wx - self.gameovertext2.get_width()) / 2,
                                                      240 - self.gameovertext2.get_height() / 2 + 30))  # ok this only works for default window size, will fix later

        pygame.display.update()

    def run(self):
        pygame.mixer.Sound.play(self.soundTrack)
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(480)  # 500 is NOT the magic number


if __name__ == '__main__':  # I learned that this runs the game itself!
    game = Game()
    game.run()
    pygame.quit()
