from MainMenu import MainMenu
from NewMainMenu import NewMainMenu
from LevelMenu import LevelMenu
from ChooseCharacter import ChooseCharacter
import Multiplayer
import PlaySonata
import pygame

mainWin0 = NewMainMenu()

while True:
    if mainWin0.pushed == pygame.Rect(624, 392, 90, 40):
        mainWin = MainMenu()
        if mainWin.pushed == pygame.Rect(75, 200, 251, 51):  # Продолжить
            chooseChar = ChooseCharacter()
            if chooseChar.pushed:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):  # Назад
                    continue
                elif chooseChar.pushed == pygame.Rect(750, 515, 201, 36):  # Старт
                    lvlWin = LevelMenu()
                    if lvlWin.pushed == pygame.Rect(750, 515, 201, 36):
                        gameWin = PlaySonata.play()
                        if gameWin.pushed == 'exit':
                            break
                    elif lvlWin.pushed == pygame.Rect(50, 515, 201, 36):
                        chooseChar = ChooseCharacter()
                        continue
                    elif lvlWin.pushed == 'exit':
                        break
                    else:
                        break
            else:
                break

        elif mainWin.pushed == pygame.Rect(75, 300, 251, 51):  # Новая игра
            chooseChar = ChooseCharacter()
            if chooseChar.pushed:
                if chooseChar.pushed == pygame.Rect(50, 515, 201, 36):
                    continue
                if chooseChar.pushed == pygame.Rect(750, 515, 201, 36):
                    gameWin = Multiplayer.play()
                    if gameWin.pushed == 'exit':
                        break
                else:
                    break

            else:
                break

        elif mainWin.pushed == pygame.Rect(75, 400, 251, 51):  # Настройки
            pass
        elif mainWin.pushed == pygame.Rect(75, 500, 251, 51):  # Выход
            break
    elif mainWin0.pushed == 'exit':
        break
