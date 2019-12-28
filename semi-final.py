import pygame as pg
from sys import exit
import random
import time

pg.init()

#遊戲設定
class Settings():

    def __init__(self):
        # 視窗大小
        self.width = 960
        self.height = 720

        # 字體及大小
        self.sfont = pg.font.SysFont("Comic Sans MS", 44)
        self.mfont = pg.font.SysFont("Comic Sans MS", 54)
        self.lfont = pg.font.SysFont("Comic Sans MS", 122)

        # 顏色
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.PINK = (255, 192, 203)
        self.DARKBLUE = (0, 0, 111)

        # 時間
        self.limited_time = 40

        # 載入多個檔案
        self.bg1_1 = pg.image.load("bg1_1.jpg")
        self.bg1_2 = pg.image.load("bg1_2.jpg")
        self.bg2_1 = pg.image.load("bg2_1.jpg")
        self.bg2_2 = pg.image.load("bg2_2.jpg")
        self.bg3_1 = pg.image.load("bg3_1.jpg")
        self.bg3_2 = pg.image.load("bg3_2.jpg")
        self.bg4_1 = pg.image.load("bg4_1.jpg")
        self.bg4_2 = pg.image.load("bg4_2.jpg")
        self.bg5_1 = pg.image.load("bg5_1.jpg")
        self.bg5_2 = pg.image.load("bg5_2.jpg")
        self.main_bg = pg.image.load("main_bg.jpg")
        self.result_bg = pg.image.load("result_bg.jpg")
        self.blue_f_image = pg.image.load('blue_flower.png')
        self.pink_f_image = pg.image.load('pink_flower.png')
        self.orange_f_image = pg.image.load('orange_flower.png')
        self.tree_image = pg.image.load('tree.png')
        self.grass_image = pg.image.load('grass.png')
        self.yellow_b_image = pg.image.load('yellow_balloon.png')
        self.orange_b_image = pg.image.load('orange_balloon.png')
        self.green_b_image = pg.image.load('green_balloon.png')
        self.purple_b_image = pg.image.load('purple_balloon.png')
        self.blue_b_image = pg.image.load('blue_balloon.png')
        self.red_b_image = pg.image.load('red_balloon.png')
        self.sun_image = pg.image.load('sun.png')
        self.moon_image = pg.image.load('moon.png')
        self.star1_image = pg.image.load('star1.png')
        self.star2_image = pg.image.load('star2.png')
        self.bomb_image = pg.image.load('bomb.png')
        self.bg_music_file = r'bg_song.mp3'

        #調整物件大小
        self.blue_f = pg.transform.scale(self.blue_f_image, (60, 80))
        self.pink_f = pg.transform.scale(self.pink_f_image, (60, 80))
        self.orange_f = pg.transform.scale(self.orange_f_image, (60, 80))
        self.tree = pg.transform.scale(self.tree_image, (300, 350))
        self.grass = pg.transform.scale(self.grass_image, (60, 40))
        self.yellow_b = pg.transform.scale(self.yellow_b_image, (45, 55))
        self.orange_b = pg.transform.scale(self.orange_b_image, (45, 55))
        self.green_b = pg.transform.scale(self.green_b_image, (45, 55))
        self.purple_b = pg.transform.scale(self.purple_b_image, (45, 55))
        self.blue_b = pg.transform.scale(self.blue_b_image, (45, 55))
        self.red_b = pg.transform.scale(self.red_b_image, (45, 55))
        self.sun = pg.transform.scale(self.sun_image, (110, 110))
        self.moon = pg.transform.scale(self.moon_image, (85, 95))
        self.star1 = pg.transform.scale(self.star1_image, (30, 30))
        self.star2 = pg.transform.scale(self.star2_image, (25, 25))
        self.bomb = pg.transform.scale(self.bomb_image, (150, 150))

    def onlyletters_per_game(self):
        onlyletters = []
        for each in range(20):
            onlyletter = random.choice('qwertyuiopasdfghjklmnbvcxz')
            onlyletters.append(onlyletter)
        return onlyletters

    def balloons_per_game(self):
        balloonord = [my_setting.yellow_b, my_setting.orange_b, my_setting.green_b, my_setting.purple_b, my_setting.blue_b, my_setting.red_b]
        balloons = []
        for each in range(21):
            balloon = balloonord[random.randint(0, 5)]
            balloons.append(balloon)
        return balloons

    def game_bg(self, Time, Move, Score, Correct, Wrong, letters, balloon):
        if 40 >= Time > 38 or 2 >= Time > 0:
            screen.blit(my_setting.bg1_1, (0, 0))
            screen.blit(my_setting.sun, (800, 100))
        elif 38 >= Time > 36 or 4 >= Time > 2:
            screen.blit(my_setting.bg1_2, (0, 0))
            screen.blit(my_setting.sun, (800, 100))
        elif 36 >= Time > 34 or 6 >= Time > 4:
            screen.blit(my_setting.bg2_1, (0, 0))
            screen.blit(my_setting.sun, (800, 100))
        elif 34 >= Time > 32 or 8 >= Time > 6:
            screen.blit(my_setting.bg2_2, (0, 0))
            screen.blit(my_setting.sun, (800, 100))
        elif 32 >= Time > 30 or 10 >= Time > 8:
            screen.blit(my_setting.bg3_1, (0, 0))
        elif 30 >= Time > 28 or 12 >= Time > 10:
            screen.blit(my_setting.bg3_2, (0, 0))
        elif 28 >= Time > 26 or 14 >= Time > 12:
            screen.blit(my_setting.bg4_1, (0, 0))
            screen.blit(my_setting.moon, (60, 70))
        elif 26 >= Time > 24 or 16 >= Time > 14:
            screen.blit(my_setting.bg4_2, (0, 0))
            screen.blit(my_setting.moon, (60, 70))
            screen.blit(my_setting.star2, (570, 230))
        elif 24 >= Time > 22 or 18 >= Time > 16:
            screen.blit(my_setting.bg5_1, (0, 0))
            screen.blit(my_setting.moon, (60, 70))
            screen.blit(my_setting.star1, (120, 190))
            screen.blit(my_setting.star2, (570, 230))
        elif 22 >= Time > 20 or 20 >= Time > 18:
            screen.blit(my_setting.bg5_2, (0, 0))
            screen.blit(my_setting.moon, (60, 70))
            screen.blit(my_setting.star1, (120, 190))
            screen.blit(my_setting.star2, (570, 230))

        if Score >= 100:
            screen.blit(my_setting.blue_f, [640, 570])
        if Score >= 200:
            screen.blit(my_setting.pink_f, [350, 600])
        if Score >= 350:
            screen.blit(my_setting.orange_f, [500, 590])
        if Score >= 500:
            screen.blit(my_setting.grass, [420, 630])
        if Score >= 650:
            screen.blit(my_setting.tree, [580, 230])
        if Score >= 800:
            screen.blit(my_setting.blue_f, [100, 580])
        if Score >= 1000:
            screen.blit(my_setting.pink_f, [800, 500])
        if Score >= 1200:
            screen.blit(my_setting.orange_f, [260, 540])
        if Score >= 1500:
            screen.blit(my_setting.grass, [520, 530])
        if Score >= 1800:
            screen.blit(my_setting.grass, [280, 660])

        for i in range(10 - Move):
            text = my_setting.mfont.render(letters[i + Move], True, my_setting.BLACK)
            finalballoon = balloon[i + Move]
            screen.blit(finalballoon, (194 + 55 * (i + Move), 75))
            screen.blit(text, (205 + 55 * (i + Move), 80))

        if Move > 10:
            for i in range(10 - (Move - 10)):
                text = my_setting.mfont.render(letters[i + 10 + (Move - 10)], True, my_setting.BLACK)
                finalballoon = balloon[i + 10 + (Move - 10)]
                screen.blit(finalballoon, (194 + 55 * (i + (Move - 10)), 155))
                screen.blit(text, (205 + 55 * (i + (Move - 10)), 160))
        else:
            for i in range(10):
                text = my_setting.mfont.render(letters[i + 10], True, my_setting.BLACK)
                finalballoon = balloon[i + 10]
                screen.blit(finalballoon, (194 + 55 * i, 155))
                screen.blit(text, (205 + 55 * i, 160))

        if 40 >= Time > 38 or 2 >= Time > 0:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.DARKBLUE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.DARKBLUE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.DARKBLUE)
        elif 38 >= Time > 36 or 4 >= Time > 2:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.DARKBLUE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.DARKBLUE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.DARKBLUE)
        elif 36 >= Time > 34 or 6 >= Time > 4:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.DARKBLUE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.DARKBLUE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.DARKBLUE)
        elif 34 >= Time > 32 or 8 >= Time > 6:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.DARKBLUE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.DARKBLUE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.DARKBLUE)
        elif 32 >= Time > 30 or 10 >= Time > 8:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.WHITE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.WHITE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.WHITE)
        elif 30 >= Time > 28 or 12 >= Time > 10:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.WHITE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.WHITE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.WHITE)
        elif 28 >= Time > 26 or 14 >= Time > 12:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.WHITE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.WHITE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.WHITE)
        elif 26 >= Time > 24 or 16 >= Time > 14:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.WHITE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.WHITE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.WHITE)
        elif 24 >= Time > 22 or 18 >= Time > 16:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.WHITE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.WHITE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.WHITE)
        elif 22 >= Time > 20 or 20 >= Time > 18:
            score_display = my_setting.sfont.render("Score : %s" % Score, True, my_setting.WHITE)
            Correct_display = my_setting.sfont.render("Correct : %s" % Correct, True, my_setting.WHITE)
            Wrong_display = my_setting.sfont.render("Wrong : %s" % Wrong, True, my_setting.WHITE)

        screen.blit(score_display, (360, 255))
        screen.blit(Correct_display, (360, 295))
        screen.blit(Wrong_display, (360, 335))
        pg.display.update()


#主程式
my_setting = Settings()

# 遊戲時間限制
limited_time = my_setting.limited_time
# 遊戲觸發器
game_main = True
game_active = False
game_result = False
# 計時器
timing = False
countdown = False

# 設定視窗(可省
screen = pg.display.set_mode((my_setting.width, my_setting.height))
pg.display.set_caption("Typing speed game")
screen.fill(my_setting.WHITE)

# 儲存一次遊戲中的全部字母（20個）
total_onlyletters = my_setting.onlyletters_per_game()
total_balloons = my_setting.balloons_per_game()
pg.display.update()

#播放背景音樂
file = my_setting.bg_music_file
pg.mixer.init()
track = pg.mixer.music.load(file)
pg.mixer.music.play(loops=50)

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

        screen.fill(my_setting.BLACK)

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN] and not game_active:
            scores = 0
            correct = 0
            wrong = 0
            combo = 0
            max_combo = 0
            move = 0
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

            screen.blit(my_setting.main_bg, (0, 0))
            text = my_setting.sfont.render("Press enter to start", True, my_setting.BLACK)
            screen.blit(text, (341, 500))
            text = my_setting.lfont.render("Typing Game", True, my_setting.BLACK, my_setting.WHITE)
            screen.blit(text, (215, 240))

        # 遊戲進行時執行的操作
        if game_active:

            if 0 <= move <= 20:

                total_letters = total_onlyletters

                if event.type == pg.KEYDOWN and event.key != pg.K_RETURN:
                    move += 1
                    if event.key == ord(total_letters[move - 1]):
                        correct += 1
                        combo += 1
                        if combo > max_combo:
                            max_combo = combo
                        if 0 <= combo < 20:
                            scores += 20
                        elif 20 <= combo < 40:
                            scores += 30
                        elif 40 <= combo < 60:
                            scores += 50
                        elif 60 <= combo < 80:
                            scores += 80
                        elif 80 <= combo < 100:
                            scores += 150
                        elif 100 <= combo < 200:
                            scores += 300
                        elif combo >= 200:
                            scores += 1000

                    else:
                        wrong += 1
                        combo = 0
                if move == 20:
                    total_onlyletters = my_setting.onlyletters_per_game()
                    total_balloons = my_setting.balloons_per_game()

    # 顯示背景、物件
    if game_active:
        my_setting.game_bg(remaining_time, move, scores, correct, wrong, total_letters, total_balloons)
        if move == 20:
            move = 0

    if countdown:
        current_time = time.perf_counter()
        remaining_time = int(limited_time - (current_time - start_time)) + 1
        text = my_setting.mfont.render("%s" % remaining_time, True, my_setting.WHITE)

        # 將原時間用畫布蓋住
        cover = pg.Surface((45, 35))
        cover = cover.convert()
        cover.fill((40, 34, 28))

        screen.blit(my_setting.bomb, (800, 570))
        screen.blit(cover, (850, 640))
        screen.blit(text, (845, 635))

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

        screen.fill(my_setting.BLACK)
        screen.blit(my_setting.result_bg, (0, 0))
        text = my_setting.sfont.render("Score: %s" % scores, True, my_setting.PINK)
        screen.blit(text, (180, 100))
        text = my_setting.sfont.render("Best Combo: %s" % max_combo, True, my_setting.PINK)
        screen.blit(text, (180, 160))
        text = my_setting.sfont.render("Correct: %s" % correct, True, my_setting.PINK)
        screen.blit(text, (180, 220))
        text = my_setting.sfont.render("Wrong: %s" % wrong, True, my_setting.PINK)
        screen.blit(text, (180, 280))
        text = my_setting.sfont.render("Accuracy: %s" % accuracy + "%", True, my_setting.PINK)
        screen.blit(text, (180, 340))
        text = my_setting.sfont.render("Total speed: %s words/min" % total_speed, True, my_setting.PINK)
        screen.blit(text, (180, 400))
        text = my_setting.sfont.render("Precise speed: %s words/min" % precise_speed, True, my_setting.PINK)
        screen.blit(text, (180, 460))
        text = my_setting.sfont.render("Press enter to retry", True, my_setting.PINK)
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
