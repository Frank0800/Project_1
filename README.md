#2019 PBC Autumn project version1
import pygame as pg
from sys import exit
import random
import time

def letters_per_game():
    letters = []
    for each in range(100):
        letter = random.choice('qwertyuiopasdfghjklmnbvcxz')
        letters.append(letter)
    return letters

# 遊戲時間限制
limited_time = 30
# 遊戲觸發
game_main = True
game_active = False
# 計時器
timing = False
countdown = False
game_result = False

pg.init()

# 設定視窗
width, height = 960, 720
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Typing speed game")
screen.fill((255, 255, 255))

#將原時間用畫布蓋住
cover = pg.Surface((185, 70))
cover = cover.convert()
cover.fill((0, 0, 0))

# 字體與大小設定
sfont = pg.font.SysFont("Comic Sans MS", 36)
font = pg.font.SysFont("Comic Sans MS", 48)
lfont = pg.font.SysFont("Comic Sans MS", 96)

# 儲存一次遊戲中的全部字母（100個）
total_letters = letters_per_game()
pg.display.update()

# 關閉程式的程式碼
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

        screen.fill((0, 0, 0))

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN] and not game_active:
            scores = 0
            correct = 0
            wrong = 0
            combo = 0
            max_combo = 0
            move1 = 0
            move2 = 19
            move3 = 39
            move4 = 59
            move5 = 79
            remaining_time = limited_time
            game_main = False
            game_active = True
            timing = True

        if timing:
            start_time = time.perf_counter()
            countdown = True
            timing = False

        # 遊戲還未開始時執行的操作
        if game_main:
            text = sfont.render("press enter to start", True, (255, 192, 203))
            screen.blit(text, (300, 500))
            text = lfont.render("Typing Game", True, (255, 192, 203))
            screen.blit(text, (200, 160))

        # 遊戲進行時執行的操作
        if game_active:

            if 0 <= move1 < 20:
                if event.type == pg.KEYDOWN and event.key != pg.K_RETURN:
                    move1 += 1
                    if event.key == ord(total_letters[move1 - 1]):
                        correct += 1
                        combo += 1
                        if combo > max_combo:
                            max_combo = combo
                        if 0 <= combo < 10:
                            scores += 10
                        if 10 <= combo < 20:
                            scores += 15
                        if 20 <= combo < 40:
                            scores += 25
                    else:
                        wrong += 1
                        combo = 0
                for i in range(10 - move1):
                    text = font.render(total_letters[i + move1], True, (255, 192, 203))
                    screen.blit(text, (205 + 55 * (i + move1), 80))
                if move1 > 10:
                    for i in range(10 - (move1 - 10)):
                        text = font.render(total_letters[i + 10 + (move1 - 10)], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * (i + (move1 - 10)), 160))
                else:
                    for i in range(10):
                        text = font.render(total_letters[i + 10], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * i, 160))
                score_display = sfont.render("score:%s" % scores, True, (200, 100, 100))
                screen.blit(score_display, (120, 360))
                correct_display = sfont.render("correct:%s" % correct, True, (200, 100, 100))
                screen.blit(correct_display, (120, 450))
                wrong_display = sfont.render("wrong:%s" % wrong, True, (200, 100, 100))
                screen.blit(wrong_display, (360, 450))

            if move1 == 20 and move2 != 40:
                if event.type == pg.KEYDOWN:
                    move2 += 1
                    if event.key == ord(total_letters[move2 - 1]):
                        correct += 1
                        combo += 1
                        if combo > max_combo:
                            max_combo = combo
                        if 0 <= combo < 10:
                            scores += 10
                        if 10 <= combo < 20:
                            scores += 15
                        if 20 <= combo < 40:
                            scores += 25
                        if 40 <= combo < 60:
                            scores += 40
                    else:
                        wrong += 1
                        combo = 0
                for i in range(10 - (move2 - 20)):
                    text = font.render(total_letters[i + move2], True, (255, 192, 203))
                    screen.blit(text, (205 + 55 * (i + (move2 - 20)), 80))
                if move2 > 30:
                    for i in range(10 - (move2 - 30)):
                        text = font.render(total_letters[i + 30 + (move2 - 30)], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * (i + (move2 - 30)), 160))
                else:
                    for i in range(10):
                        text = font.render(total_letters[i + 30], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * i, 160))
                score_display = sfont.render("score:%s" % scores, True, (200, 100, 100))
                screen.blit(score_display, (120, 360))
                correct_display = sfont.render("score:%s" % correct, True, (200, 100, 100))
                screen.blit(correct_display, (120, 450))
                wrong_display = sfont.render("wrong:%s" % wrong, True, (200, 100, 100))
                screen.blit(wrong_display, (360, 450))

            if move2 == 40 and move3 != 60:
                if event.type == pg.KEYDOWN:
                    move3 += 1
                    if event.key == ord(total_letters[move3 - 1]):
                        correct += 1
                        combo += 1
                        if combo > max_combo:
                            max_combo = combo
                        if 0 <= combo < 10:
                            scores += 10
                        if 10 <= combo < 20:
                            scores += 15
                        if 20 <= combo < 40:
                            scores += 25
                        if 40 <= combo < 60:
                            scores += 40
                        if 60 <= combo < 80:
                            scores += 70
                    else:
                        wrong += 1
                        combo = 0
                for i in range(10 - (move3 - 40)):
                    text = font.render(total_letters[i + move3], True, (255, 192, 203))
                    screen.blit(text, (205 + 55 * (i + (move3 - 40)), 80))
                if move3 > 50:
                    for i in range(10 - (move3 - 50)):
                        text = font.render(total_letters[i + 50 + (move3 - 50)], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * (i + (move3 - 50)), 160))
                else:
                    for i in range(10):
                        text = font.render(total_letters[i + 50], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * i, 160))
                score_display = sfont.render("score:%s" % scores, True, (200, 100, 100))
                screen.blit(score_display, (120, 360))
                correct_display = sfont.render("score:%s" % correct, True, (200, 100, 100))
                screen.blit(correct_display, (120, 450))
                wrong_display = sfont.render("wrong:%s" % wrong, True, (200, 100, 100))
                screen.blit(wrong_display, (360, 450))

            if move3 == 60 and move4 != 80:
                if event.type == pg.KEYDOWN:
                    move4 += 1
                    if event.key == ord(total_letters[move4 - 1]):
                        correct += 1
                        combo += 1
                        if combo > max_combo:
                            max_combo = combo
                        if 0 <= combo < 10:
                            scores += 10
                        if 10 <= combo < 20:
                            scores += 15
                        if 20 <= combo < 40:
                            scores += 25
                        if 40 <= combo < 60:
                            scores += 40
                        if 60 <= combo < 80:
                            scores += 70
                        if 80 <= combo <= 100:
                            scores += 100
                    else:
                        wrong += 1
                        combo = 0
                for i in range(10 - (move4 - 60)):
                    text = font.render(total_letters[i + move4], True, (255, 192, 203))
                    screen.blit(text, (205 + 55 * (i + (move4 - 60)), 80))
                if move4 > 70:
                    for i in range(10 - (move4 - 70)):
                        text = font.render(total_letters[i + 70 + (move4 - 70)], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * (i + (move4 - 70)), 160))
                else:
                    for i in range(10):
                        text = font.render(total_letters[i + 70], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * i, 160))
                score_display = sfont.render("score:%s" % scores, True, (200, 100, 100))
                screen.blit(score_display, (120, 360))
                correct_display = sfont.render("score:%s" % correct, True, (200, 100, 100))
                screen.blit(correct_display, (120, 450))
                wrong_display = sfont.render("wrong:%s" % wrong, True, (200, 100, 100))
                screen.blit(wrong_display, (360, 450))

            if move4 == 80 and move5 != 100:
                if event.type == pg.KEYDOWN:
                    move5 += 1
                    if event.key == ord(total_letters[move5 - 1]):
                        correct += 1
                        combo += 1
                        if combo > max_combo:
                            max_combo = combo
                        if 0 <= combo < 10:
                            scores += 10
                        if 10 <= combo < 20:
                            scores += 15
                        if 20 <= combo < 40:
                            scores += 25
                        if 40 <= combo < 60:
                            scores += 40
                        if 60 <= combo < 80:
                            scores += 70
                        if 80 <= combo <= 100:
                            scores += 100
                    else:
                        wrong += 1
                        combo = 0
                for i in range(10 - (move5 - 80)):
                    text = font.render(total_letters[i + move5], True, (255, 192, 203))
                    screen.blit(text, (205 + 55 * (i + (move5 - 80)), 80))
                if move5 > 90:
                    for i in range(10 - (move5 - 90)):
                        text = font.render(total_letters[i + 90 + (move5 - 90)], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * (i + (move5 - 90)), 160))
                else:
                    for i in range(10):
                        text = font.render(total_letters[i + 90], True, (255, 192, 203))
                        screen.blit(text, (205 + 55 * i, 160))
                if move5 == 100:
                    game_result = True
                    game_active = False
                    timing = False
                    countdown = False
                score_display = sfont.render("score:%s" % scores, True, (200, 100, 100))
                screen.blit(score_display, (120, 360))
                correct_display = sfont.render("score:%s" % correct, True, (200, 100, 100))
                screen.blit(correct_display, (120, 450))
                wrong_display = sfont.render("wrong:%s" % wrong, True, (200, 100, 100))
                screen.blit(wrong_display, (360, 450))


    if countdown:
        current_time = time.perf_counter()
        remaining_time = int(limited_time - (current_time - start_time)) + 1
        text = font.render("time: %s" % remaining_time, True, (255, 192, 203))
        screen.blit(cover, (640, 450))
        screen.blit(text, (640, 450))
        if remaining_time <= 0:
            game_active = False
            game_result = True
            countdown = False

    if game_result:
        if correct != 0:
            accuracy = (100 * correct / (correct + wrong)) // 1
            total_speed = 2 * (correct + wrong)
            precise_speed = 2 * correct
        else:
            accuracy = 0
            total_speed = 0
            precise_speed = 0

        screen.fill((0, 0, 0))
        text = sfont.render("Score: %s" % scores, True, (255, 192, 203))
        screen.blit(text, (180, 100))
        text = sfont.render("Best Combo: %s" % max_combo, True, (255, 192, 203))
        screen.blit(text, (180, 160))
        text = sfont.render("Correct: %s" % correct, True, (255, 192, 203))
        screen.blit(text, (180, 220))
        text = sfont.render("Wrong: %s" % wrong, True, (255, 192, 203))
        screen.blit(text, (180, 280))
        text = sfont.render("Accuracy: %s" % accuracy + "%", True, (255, 192, 203))
        screen.blit(text, (180, 340))
        text = sfont.render("total speed: %s words/min" % total_speed, True, (255, 192, 203))
        screen.blit(text, (180, 400))
        text = sfont.render("precise speed: %s words/min" % precise_speed, True, (255, 192, 203))
        screen.blit(text, (180, 460))
        text = sfont.render("Press enter to retry", True, (255, 192, 203))
        screen.blit(text, (300, 580))
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                scores = 0
                correct = 0
                wrong = 0
                combo = 0
                max_combo = 0
                remaining_time = limited_time
                game_main = False
                game_active = True
                timing = True
                game_result = False

    pg.display.update()

pg.quit()
