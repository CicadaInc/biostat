from MainMenu import MainMenu
from NewMainMenu import NewMainMenu
from LevelMenu import LevelMenu
from ChooseCharacter import ChooseCharacter
import Multiplayer
import PlaySonata
import pygame

mainWin0 = NewMainMenu()

while True:
    if mainWin0.pushed == pygame.Rect(375, 400, 250, 50):
        mainWin = MainMenu()
        if mainWin.pushed == pygame.Rect(375, 150, 251, 51):  # Играть
            chooseChar = ChooseCharacter()
            if chooseChar.pushed:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                    mainWin = NewMainMenu()

                elif chooseChar.pushed == pygame.Rect(750, 515, 201, 36):  # Старт
                    lvlWin = LevelMenu()
                    if lvlWin.pushed == pygame.Rect(750, 515, 201, 36):
                        gameWin = PlaySonata.play()
                        if gameWin.pushed == 'exit':
                            break
                    elif lvlWin.pushed == pygame.Rect(50, 515, 201, 36):
                        chooseChar = ChooseCharacter()
                        continue
                    else:
                        break
            else:
                break

        elif mainWin.pushed == pygame.Rect(375, 250, 251, 51):  # Мультиплеер
            chooseChar = ChooseCharacter()
            if chooseChar.pushed:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):
                    mainWin = NewMainMenu()
                    continue
                if chooseChar.pushed == pygame.Rect(750, 515, 201, 36):
                    gameWin = Multiplayer.play()
                    if gameWin.pushed == 'exit':
                        break
                else:
                    break

            else:
                break

        elif mainWin.pushed == pygame.Rect(375, 350, 251, 51):  # Настройки
            pass
        elif mainWin.pushed == pygame.Rect(375, 450, 251, 51):  # Выход
            break
    elif mainWin0.pushed == 'exit':
        break
