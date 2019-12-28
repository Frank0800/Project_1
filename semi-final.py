import pygame as pg
from sys import exit
import random
import time


def onlyletters_per_game():
    onlyletters = []
    for each in range(20):
        onlyletter = random.choice('qwertyuiopasdfghjklmnbvcxz')
        onlyletters.append(onlyletter)
    return onlyletters

def balloons_per_game():
    balloonord = [balloon_1, balloon_2, balloon_3, balloon_4, balloon_5, balloon_6]
    balloons = []
    for each in range(21):
        balloon = balloonord[random.randint(0, 5)]
        balloons.append(balloon)
    return balloons

def game_bg(Time, Move, Score, Correct, Wrong, letters, balloon):
    if 40 >= Time > 38 or 2 >= Time > 0:
        screen.blit(bg1_1, (0, 0))
        screen.blit(sun, (800, 100))
    elif 38 >= Time > 36 or 4 >= Time > 2:
        screen.blit(bg1_2, (0, 0))
        screen.blit(sun, (800, 100))
    elif 36 >= Time > 34 or 6 >= Time > 4:
        screen.blit(bg2_1, (0, 0))
        screen.blit(sun, (800, 100))
    elif 34 >= Time > 32 or 8 >= Time > 6:
        screen.blit(bg2_2, (0, 0))
        screen.blit(sun, (800, 100))
    elif 32 >= Time > 30 or 10 >= Time > 8:
        screen.blit(bg3_1, (0, 0))
    elif 30 >= Time > 28 or 12 >= Time > 10:
        screen.blit(bg3_2, (0, 0))
    elif 28 >= Time > 26 or 14 >= Time > 12:
        screen.blit(bg4_1, (0, 0))
        screen.blit(moon, (60, 70))
    elif 26 >= Time > 24 or 16 >= Time > 14:
        screen.blit(bg4_2, (0, 0))
        screen.blit(moon, (60, 70))
        screen.blit(star2, (570, 230))
    elif 24 >= Time > 22 or 18 >= Time > 16:
        screen.blit(bg5_1, (0, 0))
        screen.blit(moon, (60, 70))
        screen.blit(star1, (120, 190))
        screen.blit(star2, (570, 230))
    elif 22 >= Time > 20 or 20 >= Time > 18:
        screen.blit(bg5_2, (0, 0))
        screen.blit(moon, (60, 70))
        screen.blit(star1, (120, 190))
        screen.blit(star2, (570, 230))

    if Score >= 100:
        screen.blit(blues, [640, 570])
    if Score >= 200:
        screen.blit(pinks, [350, 600])
    if Score >= 350:
        screen.blit(oranges, [500, 590])
    if Score >= 500:
        screen.blit(grasses, [420, 630])
    if Score >= 650:
        screen.blit(trees, [580, 230])
    if Score >= 800:
        screen.blit(blues, [100, 580])
    if Score >= 1000:
        screen.blit(pinks, [800, 500])
    if Score >= 1200:
        screen.blit(oranges, [260, 540])
    if Score >= 1500:
        screen.blit(grasses, [520, 530])
    if Score >= 1800:
        screen.blit(grasses, [280, 660])

    for i in range(10 - Move):
        text = font.render(letters[i + Move], True, (0, 0, 0))
        finalballoon = balloon[i + Move]
        screen.blit(finalballoon, (194 + 55 * (i + Move), 75))
        screen.blit(text, (205 + 55 * (i + Move), 80))

    if Move > 10:
        for i in range(10 - (Move - 10)):
            text = font.render(letters[i + 10 + (Move - 10)], True, (0, 0, 0))
            finalballoon = balloon[i + 10 + (Move - 10)]
            screen.blit(finalballoon, (194 + 55 * (i + (Move - 10)), 155))
            screen.blit(text, (205 + 55 * (i + (Move - 10)), 160))
    else:
        for i in range(10):
            text = font.render(letters[i + 10], True, (0, 0, 0))
            finalballoon = balloon[i + 10]
            screen.blit(finalballoon, (194 + 55 * i, 155))
            screen.blit(text, (205 + 55 * i, 160))

    if 40 >= Time > 38 or 2 >= Time > 0:
        score_display = sfont.render("Score : %s" % Score, True, (0, 0, 111))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (0, 0, 111))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (0, 0, 111))
    elif 38 >= Time > 36 or 4 >= Time > 2:
        score_display = sfont.render("Score : %s" % Score, True, (0, 0, 111))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (0, 0, 111))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (0, 0, 111))
    elif 36 >= Time > 34 or 6 >= Time > 4:
        score_display = sfont.render("Score : %s" % Score, True, (0, 0, 111))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (0, 0, 111))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (0, 0, 111))
    elif 34 >= Time > 32 or 8 >= Time > 6:
        score_display = sfont.render("Score : %s" % Score, True, (0, 0, 111))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (0, 0, 111))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (0, 0, 111))
    elif 32 >= Time > 30 or 10 >= Time > 8:
        score_display = sfont.render("Score : %s" % Score, True, (255, 255, 255))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (255, 255, 255))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (255, 255, 255))
    elif 30 >= Time > 28 or 12 >= Time > 10:
        score_display = sfont.render("Score : %s" % Score, True, (255, 255, 255))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (255, 255, 255))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (255, 255, 255))
    elif 28 >= Time > 26 or 14 >= Time > 12:
        score_display = sfont.render("Score : %s" % Score, True, (255, 255, 255))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (255, 255, 255))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (255, 255, 255))
    elif 26 >= Time > 24 or 16 >= Time > 14:
        score_display = sfont.render("Score : %s" % Score, True, (255, 255, 255))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (255, 255, 255))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (255, 255, 255))
    elif 24 >= Time > 22 or 18 >= Time > 16:
        score_display = sfont.render("Score : %s" % Score, True, (255, 255, 255))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (255, 255, 255))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (255, 255, 255))
    elif 22 >= Time > 20 or 20 >= Time > 18:
        score_display = sfont.render("Score : %s" % Score, True, (255, 255, 255))
        Correct_display = sfont.render("Correct : %s" % Correct, True, (255, 255, 255))
        Wrong_display = sfont.render("Wrong : %s" % Wrong, True, (255, 255, 255))

    screen.blit(score_display, (360, 255))
    screen.blit(Correct_display, (360, 295))
    screen.blit(Wrong_display, (360, 335))
    pg.display.update()


# 遊戲時間限制
limited_time = 40
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
bg1_1 = pg.image.load("/Users/terence/Documents/pyCourse/bg1_1.jpg")
bg1_2 = pg.image.load("/Users/terence/Documents/pyCourse/bg1_2.jpg")
bg2_1 = pg.image.load("/Users/terence/Documents/pyCourse/bg2_1.jpg")
bg2_2 = pg.image.load("/Users/terence/Documents/pyCourse/bg2_2.jpg")
bg3_1 = pg.image.load("/Users/terence/Documents/pyCourse/bg3_1.jpg")
bg3_2 = pg.image.load("/Users/terence/Documents/pyCourse/bg3_2.jpg")
bg4_1 = pg.image.load("/Users/terence/Documents/pyCourse/bg4_1.jpg")
bg4_2 = pg.image.load("/Users/terence/Documents/pyCourse/bg4_2.jpg")
bg5_1 = pg.image.load("/Users/terence/Documents/pyCourse/bg5_1.jpg")
bg5_2 = pg.image.load("/Users/terence/Documents/pyCourse/bg5_2.jpg")
main_bg = pg.image.load("/Users/terence/Documents/pyCourse/main_bg.jpg")
result_bg = pg.image.load("/Users/terence/Documents/pyCourse/result_bg.jpg")

blue = pg.image.load('/Users/terence/Documents/pyCourse/blue_flower.png')  # 載入藍花
blues = pg.transform.scale(blue, (60, 80))  # 把藍花縮小
pink = pg.image.load('/Users/terence/Documents/pyCourse/pink_flower.png')  # 載入粉花
pinks = pg.transform.scale(pink, (60, 80))  # 把粉花縮小
orange = pg.image.load('/Users/terence/Documents/pyCourse/orange_flower.png')  # 載入橘花
oranges = pg.transform.scale(orange, (60, 80))  # 把橘花縮小
tree = pg.image.load('/Users/terence/Documents/pyCourse/tree.png')  # 載入樹
trees = pg.transform.scale(tree, (300, 350))  # 把樹縮小
grass = pg.image.load('/Users/terence/Documents/pyCourse/grass.png')  # 載入草
grasses = pg.transform.scale(grass, (60, 40))  # 把草縮小
balloon_yellow_ord = pg.image.load('/Users/terence/Documents/pyCourse/yellow_balloon.png')
balloon_1 = pg.transform.scale(balloon_yellow_ord, (45, 55))
balloon_orange_ord = pg.image.load('/Users/terence/Documents/pyCourse/orange_balloon.png')
balloon_2 = pg.transform.scale(balloon_orange_ord, (45, 55))
balloon_green_ord = pg.image.load('/Users/terence/Documents/pyCourse/green_balloon.png')
balloon_3 = pg.transform.scale(balloon_green_ord, (45, 55))
balloon_purple_ord = pg.image.load('/Users/terence/Documents/pyCourse/purple_balloon.png')
balloon_4 = pg.transform.scale(balloon_purple_ord, (45, 55))
balloon_blue_ord = pg.image.load('/Users/terence/Documents/pyCourse/blue_balloon.png')
balloon_5 = pg.transform.scale(balloon_blue_ord, (45, 55))
balloon_red_ord = pg.image.load('/Users/terence/Documents/pyCourse/red_balloon.png')
balloon_6 = pg.transform.scale(balloon_red_ord, (45, 55))

sun_ord = pg.image.load('/Users/terence/Documents/pyCourse/sun.png')
sun = pg.transform.scale(sun_ord, (110, 110))
moon_ord = pg.image.load('/Users/terence/Documents/pyCourse/moon.png')
moon = pg.transform.scale(moon_ord, (85, 95))
star1_ord = pg.image.load('/Users/terence/Documents/pyCourse/star1.png')
star1 = pg.transform.scale(star1_ord, (30, 30))
star2_ord = pg.image.load('/Users/terence/Documents/pyCourse/star2.png')
star2 = pg.transform.scale(star2_ord, (25, 25))

bomb_ord = pg.image.load('/Users/terence/Documents/pyCourse/bomb.png')
bomb = pg.transform.scale(bomb_ord, (150, 150))

# 字體與大小設定
sfont = pg.font.SysFont("Comic Sans MS", 44)
font = pg.font.SysFont("Comic Sans MS", 54)
lfont = pg.font.SysFont("Comic Sans MS", 122)

# 儲存一次遊戲中的全部字母（20個）
total_onlyletters = onlyletters_per_game()
total_balloons = balloons_per_game()
pg.display.update()

file = r'/Users/terence/Documents/pyCourse/bg_song.mp3'
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

        screen.fill((0, 0, 0))

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

            screen.blit(main_bg, (0, 0))
            text = sfont.render("Press enter to start", True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (341, 500))
            text = lfont.render("Typing Game", True, (0, 0, 0), (255, 255, 255))
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
                        if 0 <= combo < 10:
                            scores += 10
                        if 10 <= combo < 20:
                            scores += 15
                        if 20 <= combo < 40:
                            scores += 25
                    else:
                        wrong += 1
                        combo = 0
                if move == 20:
                    total_onlyletters = onlyletters_per_game()
                    total_balloons = balloons_per_game()

    # 顯示背景、物件
    if game_active:
        game_bg(remaining_time, move, scores, correct, wrong, total_letters, total_balloons)
        if move == 20:
            move = 0

    if countdown:
        current_time = time.perf_counter()
        remaining_time = int(limited_time - (current_time - start_time)) + 1
        text = font.render("%s" % remaining_time, True, (255, 255, 255))

        # 將原時間用畫布蓋住
        cover = pg.Surface((45, 35))
        cover = cover.convert()
        cover.fill((40, 34, 28))
        
        screen.blit(bomb, (800, 570))
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

        screen.fill((0, 0, 0))
        screen.blit(result_bg, (0, 0))
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
        text = sfont.render("Total speed: %s words/min" % total_speed, True, (255, 192, 203))
        screen.blit(text, (180, 400))
        text = sfont.render("Precise speed: %s words/min" % precise_speed, True, (255, 192, 203))
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
