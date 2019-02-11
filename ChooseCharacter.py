import pygame
import eztext
import os


class ChooseCharacter:
    def __init__(self, choosed=0):
        pygame.init()

        pygame.mouse.set_visible(False)
<<<<<<< HEAD
        surf = pygame.image.load('sprites/ForGUI/cursor1.png')

        self.screen = pygame.display.set_mode((1000, 600))
        self.text = ''
        self.font = pygame.font.Font('sprites/freesansbold.ttf', 30)
        self.choosed = choosed

        self.pushed = None

        textbox = eztext.Input(maxlength=10, color=(0, 0, 0), prompt='',
                               font=pygame.font.Font('sprites/freesansbold.ttf', 30))
        textbox.set_pos(670, 155)

=======

        self.screen = pygame.display.set_mode((1000, 600))

        self.font = pygame.font.Font('sprites/freesansbold.ttf', 30)

        self.choosed = choosed
        self.pushed = None

>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659
        self.set_interface()

        running = True
        while running:
<<<<<<< HEAD
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.chooseButtons)):
                        if self.chooseButtons[i].collidepoint(event.pos):
                            pygame.draw.rect(self.screen, pygame.Color('black'),
                                             self.chooseButtons[self.choosed], 2)
                            pygame.draw.rect(self.screen, pygame.Color('red'),
                                             self.chooseButtons[i], 2)
                            self.choosed = i

=======
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.pushed = 'exit'
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.chooseButtons)):
                        if self.chooseButtons[i].collidepoint(event.pos):
                            self.choosed = i
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659
                        elif self.back.collidepoint(event.pos):
                            self.pushed = self.back
                            running = False
                        elif self.start.collidepoint(event.pos):
                            self.pushed = self.start
                            running = False

<<<<<<< HEAD
            # ПОЛЕ ВВОДА НИКА
            pygame.draw.rect(self.screen, (250, 175, 255),
                             pygame.Rect(665, 150, self.inp_width, self.inp_height))
            pygame.draw.rect(self.screen, (0, 0, 0),
                             pygame.Rect(665, 150, self.inp_width, self.inp_height), 2)
            textbox.update(events)
            textbox.draw(self.screen)

            self.render()

            pos = pygame.mouse.get_pos()
            rect = surf.get_rect(topleft=pos)
            self.screen.blit(surf, rect)

            pygame.display.flip()

    def render(self):

        self.screen.blit(self.background_surf, self.background_rect)
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        self.back = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))
        self.chooseButtons = []
=======
            self.render()

            pygame.display.flip()

    def render(self):
        # ФОН
        self.screen.blit(self.background_surf, self.background_rect)

        # ПОЛЕ ВВОДА НИКА
        pygame.draw.rect(self.screen, (250, 175, 255),
                         pygame.Rect(665, 150, 200, 43))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(665, 150, 200, 43), 2)
        self.textbox.update(self.events)
        self.textbox.draw(self.screen)

        # НАЗАД
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))

        # ПЕРСОНАЖИ
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659
        i = 0
        for y in range(150, 301, 150):
            for x in range(50, 351, 150):
                i += 1
<<<<<<< HEAD
                pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(x, y, 100, 100))
                self.chooseButtons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                           pygame.Rect(x, y, 100, 100), 2))

                character = pygame.image.load('sprites/characters/' + str(i) + '.png')
                character = pygame.transform.scale(character, (97, 97))
                self.screen.blit(character, (x + 2, y + 2))
        pygame.draw.rect(self.screen, pygame.Color('red'), self.chooseButtons[self.choosed], 2)
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(750, 515, 200, 35))
        self.start = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 515, 200, 35), 2)

        self.screen.blit(self.text_start, (self.text_x_2, self.text_y_2))
        self.screen.blit(self.text_view, (self.text_x_3, self.text_y_3))
        self.screen.blit(self.text_name, (self.text_x_4, self.text_y_4))
        self.inp_width, self.inp_height = self.text_name.get_width(), self.text_name.get_height()
=======
                pygame.draw.rect(self.screen, pygame.Color('black'), pygame.Rect(x, y, 100, 100), 2)

                if self.choosed == i - 1:
                    pygame.draw.rect(self.screen, pygame.Color('red'), pygame.Rect(x, y, 100, 100), 2)

                character = self.characters[i - 1]
                self.screen.blit(character, (x + 2, y + 2))

        # СТАРТ
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(750, 515, 200, 35))
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 515, 200, 35), 2)

        # НАДПИСИ
        self.screen.blit(self.text_start, (self.text_x_2, self.text_y_2))
        self.screen.blit(self.text_view, (self.text_x_3, self.text_y_3))
        self.screen.blit(self.text_name, (self.text_x_4, self.text_y_4))

        # КУРСОР
        pos = pygame.mouse.get_pos()
        rect = self.cursor.get_rect(topleft=pos)
        self.screen.blit(self.cursor, rect)
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659

    def set_interface(self):
        directory = os.getcwd()

        # LOAD BACKGROUND
        self.background_surf = pygame.image.load(directory + '/backgrounds/quizFone.jpg')
        self.background_surf = pygame.transform.scale(self.background_surf, (1000, 600))
        self.background_rect = self.background_surf.get_rect(bottomright=(1000, 600))
        self.screen.blit(self.background_surf, self.background_rect)

<<<<<<< HEAD
        # BUTTON BACK
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(50, 515, 200, 35))
        self.back = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 515, 200, 35), 2)
        self.text_back = self.font.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()
        self.screen.blit(self.text_back, (self.text_x_1, self.text_y_1))

        # ОКНА ПЕРСОНАЖЕЙ
        self.chooseButtons = []
=======
        # КУРСОР
        self.cursor = pygame.image.load('sprites/ForGUI/cursor1.png')

        # ПОЛЕ ДЛЯ ВВОДА НИКА
        self.textbox = eztext.Input(maxlength=10, color=(0, 0, 0), prompt='', font=self.font)
        self.textbox.set_pos(670, 155)

        # BUTTON BACK
        self.back = pygame.Rect(50, 515, 200, 35)
        self.text_back = self.font.render("Назад", 1, (100, 25, 100))
        self.text_x_1, self.text_y_1 = 150 - self.text_back.get_width() // 2, 550 - self.text_back.get_height()

        # ОКНА ПЕРСОНАЖЕЙ
        self.chooseButtons, self.characters = [], []
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659
        i = 0
        for y in range(150, 301, 150):
            for x in range(50, 351, 150):
                i += 1
<<<<<<< HEAD
                pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(x, y, 100, 100))
                self.chooseButtons.append(pygame.draw.rect(self.screen, pygame.Color('black'),
                                                           pygame.Rect(x, y, 100, 100), 2))

                character = pygame.image.load('sprites/characters/' + str(i) + '.png')
                character = pygame.transform.scale(character, (97, 97))
                self.screen.blit(character, (x + 2, y + 2))
        pygame.draw.rect(self.screen, pygame.Color('red'), self.chooseButtons[self.choosed], 2)

        # КНОПКА СТАРТА
        pygame.draw.rect(self.screen, (250, 175, 255), pygame.Rect(750, 515, 200, 35))
        self.start = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 515, 200, 35), 2)
        self.text_start = self.font.render("Старт", 1, (100, 25, 100))
        self.text_x_2, self.text_y_2 = 850 - self.text_start.get_width() // 2, 550 - self.text_start.get_height()
        self.screen.blit(self.text_start, (self.text_x_2, self.text_y_2))
=======

                self.chooseButtons.append(pygame.Rect(x, y, 100, 100))

                character = pygame.image.load('sprites/characters/' + str(i) + '.png')
                self.characters.append(pygame.transform.scale(character, (97, 97)))

        # КНОПКА СТАРТА
        self.start = pygame.Rect(750, 515, 200, 35)
        self.text_start = self.font.render("Старт", 1, (100, 25, 100))
        self.text_x_2, self.text_y_2 = 850 - self.text_start.get_width() // 2, 550 - self.text_start.get_height()
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659

        # НАДПИСИ
        self.text_view = self.font.render("Выберите персонажа", 1, (100, 25, 100))
        self.text_x_3, self.text_y_3 = 65, 60
<<<<<<< HEAD
        self.screen.blit(self.text_view, (self.text_x_3, self.text_y_3))

        self.text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        self.text_x_4, self.text_y_4 = 665, 60
        self.screen.blit(self.text_name, (self.text_x_4, self.text_y_4))

        self.inp_width, self.inp_height = self.text_name.get_width(), self.text_name.get_height()
=======

        self.text_name = self.font.render("Введите имя", 1, (100, 25, 100))
        self.text_x_4, self.text_y_4 = 665, 60
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659


if __name__ == "__main__":
    def start():
<<<<<<< HEAD
        win = ChooseCharacter()
=======
        ChooseCharacter()
>>>>>>> 2e721446d5d6b615a33604de3db2da8c2b010659


    start()
