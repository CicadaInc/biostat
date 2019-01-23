import pygame
import os


class NewMainMenu:
    def __init__(self):
        pygame.init()

        self.winWidth = 1000
        self.winHeight = 600
        self.screen = pygame.display.set_mode((self.winWidth, self.winHeight))

        self.y = 60

        self.pushed = None

        self.set_interface()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.buttons)):
                        if self.buttons[i].collidepoint(event.pos):
                            self.fall_coin()
                            self.pushed = self.buttons[i]
                            running = False

            pygame.display.flip()

    def fall_coin(self):
        clock = pygame.time.Clock()
        print(clock.tick())
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            if self.y < 410:
                self.y += 15
            else:
                break

            self.render()

            pygame.display.update()

    def render(self):
        self.screen.blit(self.background_surf, self.background_rect)

        self.screen.blit(self.text, (self.text_x, self.text_y))

        self.coinRect = self.coin.get_rect(bottomright=(520, self.y))
        self.screen.blit(self.coin, self.coinRect)

    def set_interface(self):
        directory = os.getcwd()

        self.background_surf = pygame.image.load(directory + '/backgrounds/main.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(self.background_surf, self.background_rect)

        # LOAD MUSIC
        pygame.mixer.music.load(directory + '/sounds/loading.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        font = pygame.font.Font('sprites/freesansbold.ttf', 30)

        # КНОПКИ
        self.buttons = [pygame.draw.rect(self.screen, (0, 0, 0),
                                         pygame.Rect(375, 400, 250, 50))]
        self.text = font.render('Insert coin', 1, (218, 114, 3))
        self.text_x, self.text_y = 500 - self.text.get_width() // 2, 400 + 25 - self.text.get_height() // 2
        self.screen.blit(self.text, (self.text_x, self.text_y))

        # МОНЕТКА
        self.coin = pygame.image.load('sprites/coin.png')
        self.coin = pygame.transform.scale(self.coin, (50, 60))
        self.coinRect = self.coin.get_rect(bottomright=(520, self.y))
        self.screen.blit(self.coin, self.coinRect)


if __name__ == "__main__":
    def start():
        win = NewMainMenu()


    start()
