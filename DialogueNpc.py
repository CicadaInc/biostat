import pygame


class Dialogue1:
    def __init__(self, screen, game, phrases):
        self.screen = screen
        self.surface = pygame.Surface((200, 180), pygame.SRCALPHA)

        self.pushed = None

        self.phrases = phrases

        pygame.mouse.set_visible(False)

        self.game = game

        self.font = pygame.font.Font('fonts/comic.ttf', 15)
        self.font1 = pygame.font.Font('fonts/freesansbold.ttf', 18)

        self.close = pygame.Rect(50, 142, 100, 25)
        self.close_text = self.font1.render("Закрыть", 1, (0, 0, 0))

        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.close.collidepoint((x - 400, y - 200)):
                        running = False

            self.render()
            pygame.display.flip()

    def render(self):
        self.game.render()

        self.surface.fill((200, 220, 190))

        pygame.draw.rect(self.surface, (250, 175, 255), self.close)
        pygame.draw.rect(self.surface, (0, 0, 0), self.close, 2)

        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect(0, 0, 199, 179), 2)

        self.surface.blit(self.close_text, (65, 147))

        for phrase in self.phrases:
            self.surface.blit(phrase[0], phrase[1])

        self.screen.blit(self.surface, (400, 200))

        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)


def create_dialogue1():
    font = pygame.font.Font('fonts/comic.ttf', 15)

    return [(font.render("Здравствуй странник, я - Brain.", 1, (0, 0, 0)), (10, 10)),
            (font.render("А нарекли меня Fuck за заслуги.", 1, (0, 0, 0)), (10, 30)),
            (font.render("Также известен как язык", 1, (0, 0, 0)), (10, 50)),
            (font.render("Для выноса мозга", 1, (0, 0, 0)), (10, 70))]
