import os
import pygame
from create_field import field
from Pause import Pause
import DialogueNpc


class Game:
    def __init__(self, character, name):
        pygame.init()

        self.winw, self.winh = 1000, 600
        self.winx, self.winy = 2852, 1805

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("TheQuiz")

        self.level = field
        self.directory = os.getcwd()

        self.character = character

        self.walkRight, self.walkLeft, self.walkUp, self.walkDown = [], [], [], []
        self.load_animations()

        self.clock = pygame.time.Clock()

        self.startx, self.starty = 468, 210
        self.right = None
        self.up = None

        self.name = name

        self.font = pygame.font.SysFont('Trebuchet MS', 12)
        self.font.set_bold(True)

        self.font1 = pygame.font.SysFont('Trebuchet MS', 20)

        self.k = 0

        self.pushed = None

        self.anim, self.speed = 0, 10

        self.set_interface()
        self.load_npc()

        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.pushed = 'exit'
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        p = Pause(self.screen, self)
                        if p.pushed == p.quit:
                            self.pushed = 'exit_main'
                            running = False
                    if event.key == 101:
                        if abs(self.npc1_x - self.startx) < 50 and abs(self.npc1_y - self.starty) < 50:
                            phrases = DialogueNpc.create_dialogue1()
                            dialogue = DialogueNpc.Dialogue1(self.screen, self, phrases)
                            if dialogue.pushed == 'exit':
                                self.pushed = 'exit'
                                running = False

            x, y = self.winx - self.winw // 2, self.winy - self.winh // 2
            # print(y // 36, x // 36)
            # print(self.winx, self.winy)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.winx += self.speed
                self.left, self.up = True, None
            elif keys[pygame.K_RIGHT]:
                self.winx -= self.speed
                self.left, self.up = False, None
            elif keys[pygame.K_UP]:
                self.winy += self.speed
                self.up, self.left = True, None
            elif keys[pygame.K_DOWN]:
                self.winy -= self.speed
                self.up, self.left = False, None
            else:
                self.left, self.up = None, None
                self.anim = 0

            if self.winx > 4736:
                self.winx = 4736
            if self.winx < 1001:
                self.winx = 1001
            if self.winy > 2803:
                self.winy = 2803
            if self.winy < 600:
                self.winy = 600

            self.render()
            pygame.display.flip()

    def load_animations(self):
        for i in range(1, 4):
            self.walkRight.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/RIGHT_" + str(i) + '.png'),
                    (48, 64)))
            self.walkLeft.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/LEFT_" + str(i) + '.png'),
                    (48, 64)))
            self.walkUp.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/UP_" + str(i) + '.png'),
                    (48, 64)))
            self.walkDown.append(
                pygame.transform.scale(
                    pygame.image.load(self.directory + "/sprites/" + self.character + "/DOWN_" + str(i) + '.png'),
                    (48, 64)))
        self.STAY = pygame.transform.scale(
            pygame.image.load(self.directory + "/sprites/" + self.character + "/STAY" + '.png'), (48, 64))

    def load_npc(self):
        self.oldMan = pygame.transform.scale(
            pygame.image.load(self.directory + '/sprites/OldMan.png'), (48, 64))

    def set_interface(self):
        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(self.directory + '/levels/MainLocation.png')
        self.background_rect = self.background_surf.get_rect(bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        self.nick = self.font.render(self.name, 1, pygame.Color('blue'))
        self.nameNpc1 = self.font.render("Brain Fuck", 1, pygame.Color('blue'))
        self.controls1 = self.font1.render("esc - Пауза", 1, (0, 0, 0))
        self.controls2 = self.font1.render("e - Взаимодействовать", 1, (0, 0, 0))

    def render(self):
        self.screen.fill((0, 0, 0))

        self.background_rect = self.background_surf.get_rect(bottomright=(self.winx, self.winy))
        self.screen.blit(self.background_surf, self.background_rect)

        self.screen.blit(self.nick, (self.startx - self.nick.get_width() // 2 + 24,
                                     self.starty - self.nick.get_height() // 2))
        self.npc1_x, self.npc1_y = 1150 + (self.winx - 2852), -550 + self.winy - 1805
        self.screen.blit(self.nameNpc1, (self.npc1_x - 10, self.npc1_y - 20))
        self.screen.blit(self.oldMan, (self.npc1_x, self.npc1_y))

        self.screen.blit(self.controls1, (780, 525))
        self.screen.blit(self.controls2, (780, 550))

        print((1150 + (self.winx - 2852), -450 + self.winy - 1805))

        if self.anim + 1 >= 30:
            self.anim = 0

        if self.left is None and self.up is None:
            self.screen.blit(self.STAY, (self.startx, self.starty))
            self.anim = 0
        else:
            if int(self.k) == 1:
                self.anim += 1
                self.k = 0
            if not self.left and not (self.left is None):
                self.screen.blit(self.walkRight[self.anim % 3], (self.startx, self.starty))
            elif self.left:
                self.screen.blit(self.walkLeft[self.anim % 3], (self.startx, self.starty))
            elif self.up:
                self.screen.blit(self.walkUp[self.anim % 3], (self.startx, self.starty))
            elif not self.up:
                self.screen.blit(self.walkDown[self.anim % 3], (self.startx, self.starty))
            self.k += 0.15


if __name__ == "__main__":
    def test():
        HEROES = ['1(Townfolk-Child-M-001)', '2(Townfolk-Child-M)', '3(Townfolk-Adult-M-006)',
                  '4(coriander publish.)', '5(Mushroom-01)', '6(Cultist)']

        hero = HEROES[1]
        Game(hero, "SuperHero")


    test()
