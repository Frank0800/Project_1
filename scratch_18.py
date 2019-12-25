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


def numletters_per_game():
    numletters = []
    for each in range(20):
        numletter = random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')
        numletters.append(numletter)
    return numletters


def balloons_per_game():
    balloonord = [balloon_1, balloon_2, balloon_3, balloon_4, balloon_5, balloon_6]
    balloons = []
    for each in range(20):
        balloon = balloonord[random.randint(0,5)]
        balloons.append(balloon)
    return balloons



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
bg1 = pg.image.load("/Users/xinyi/Desktop/background1.jpg")
bg2 = pg.image.load("/Users/xinyi/Desktop/background2.jpg")
bg3 = pg.image.load("/Users/xinyi/Desktop/background3.jpg")
bg4 = pg.image.load("/Users/xinyi/Desktop/background4.jpg")
bg5 = pg.image.load("/Users/xinyi/Desktop/background5.jpg")
bg_2 = pg.image.load("/Users/xinyi/Desktop/istockphoto-626401042-1024x1024.jpg")
bg_3 = pg.image.load("/Users/xinyi/Desktop/maxresdefault.jpg")


blue = pg.image.load('/Users/xinyi/Desktop/blue.png')  # 載入藍花
blues = pg.transform.scale(blue,(60,80))  # 把藍花縮小
pink = pg.image.load('/Users/xinyi/Desktop/pink.png')  # 載入粉花
pinks = pg.transform.scale(pink,(60,80))  # 把粉花縮小
orange = pg.image.load('/Users/xinyi/Desktop/orange.png')  # 載入橘花
oranges = pg.transform.scale(orange,(60,80))  # 把橘花縮小
tree = pg.image.load('/Users/xinyi/Desktop/tree.png')  # 載入樹
trees = pg.transform.scale(tree,(300,350))  # 把樹縮小
grass = pg.image.load('/Users/xinyi/Desktop/grass.png')  # 載入草
grasses = pg.transform.scale(grass,(60,40))  # 把草縮小
balloon_yellow_ord = pg.image.load('/Users/xinyi/Desktop/yellowballoon.png')
balloon_1 = pg.transform.scale(balloon_yellow_ord, (45, 55))
balloon_orange_ord = pg.image.load('/Users/xinyi/Desktop/orangeballoon.png')
balloon_2 = pg.transform.scale(balloon_orange_ord, (45, 55))
balloon_green_ord = pg.image.load('/Users/xinyi/Desktop/greenballoon.png')
balloon_3 = pg.transform.scale(balloon_green_ord, (45, 55))
balloon_purple_ord = pg.image.load('/Users/xinyi/Desktop/purpleballoon.png')
balloon_4 = pg.transform.scale(balloon_purple_ord, (45, 55))
balloon_blue_ord = pg.image.load('/Users/xinyi/Desktop/blueballoon.png')
balloon_5 = pg.transform.scale(balloon_blue_ord, (45, 55))
balloon_red_ord = pg.image.load('/Users/xinyi/Desktop/redballoon.png')
balloon_6 = pg.transform.scale(balloon_red_ord, (45, 55))

sun_ord = pg.image.load('/Users/xinyi/Desktop/sun.png')
sun = pg.transform.scale(sun_ord, (100, 100))
moon_ord = pg.image.load('/Users/xinyi/Desktop/moon.png')
moon = pg.transform.scale(moon_ord, (75, 85))
star1_ord = pg.image.load('/Users/xinyi/Desktop/star1.png')
star1 = pg.transform.scale(star1_ord, (25, 35))
star2_ord = pg.image.load('/Users/xinyi/Desktop/star2.png')
star2 = pg.transform.scale(star2_ord, (35, 45))


file = r'/Users/xinyi/Desktop/closer.mp3'
pg.mixer.init()
track = pg.mixer.music.load(file)

pg.mixer.music.play()

temp = 1

# 字體與大小設定
sfont = pg.font.SysFont("Comic Sans MS", 36)
font = pg.font.SysFont("Comic Sans MS", 48)
lfont = pg.font.SysFont("Comic Sans MS", 96)

# 儲存一次遊戲中的全部字母（20個）
total_onlyletters = onlyletters_per_game()
# pg.display.update()
total_numletters = numletters_per_game()
# pg.display.update()
total_balloons = balloons_per_game()
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
            screen.blit(bg_2, (0, 0))
            text = sfont.render("Press enter to start", True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (370, 500))
            text = lfont.render("Typing Game", True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (270, 200))



        # 遊戲進行時執行的操作
        if game_active:
            if temp == 1:
                screen.blit(bg1, (0, 0))
                screen.blit(sun, (800, 130))
            elif temp == 2 or temp == 8:
                screen.blit(bg2, (0, 0))
                screen.blit(sun, (800, 130))
            elif temp == 3 or temp == 7:
                screen.blit(bg3, (0, 0))
                screen.blit(star1, (120, 70))
            elif temp == 4 or temp == 6:
                screen.blit(bg4, (0, 0))
                screen.blit(moon, (60, 130))
                screen.blit(star1, (120, 70))
            elif temp == 5:
                screen.blit(bg5, (0, 0))
                screen.blit(moon, (60, 130))
                screen.blit(star1, (120, 70))
                screen.blit(star2, (520, 230))

            # 將原時間用畫布蓋住
            cover = pg.Surface((150, 40))
            cover = cover.convert()
            if temp == 1:
                cover.fill((24, 151, 229))
            elif temp == 2 or temp == 8:
                cover.fill((0, 96, 209))
            elif temp == 3 or temp == 7:
                cover.fill((0, 44, 184))
            elif temp == 4 or temp == 6:
                cover.fill((1, 5, 168))
            elif temp == 5:
                cover.fill((0, 0, 122))



            if 0 <= move1 <= 20:

                if correct < 20:
                    total_letters = total_onlyletters
                elif correct >= 20:
                    total_letters = total_numletters


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

                if correct >= 5:
                    screen.blit(blues, [640, 570])
                if correct >= 10:
                    screen.blit(pinks, [350, 600])
                if correct >= 15:
                    screen.blit(oranges, [500, 590])
                if correct >= 20:
                    screen.blit(grasses, [420, 630])
                if correct >= 25:
                    screen.blit(trees, [580, 230])
                if correct >= 30:
                    screen.blit(blues, [100, 580])
                if correct >= 35:
                    screen.blit(pinks, [800, 500])
                if correct >= 40:
                    screen.blit(oranges, [260, 540])
                if correct >= 45:
                    screen.blit(grasses, [520, 530])
                if correct >= 50:
                    screen.blit(grasses, [280, 660])



                for i in range(10 - move1):
                    text = font.render(total_letters[i + move1], True, (0, 0, 0))
                    finalballoon = total_balloons[i + move1]
                    screen.blit(finalballoon, (194 + 55 * (i + move1), 75))
                    screen.blit(text, (205 + 55 * (i + move1), 80))


                if move1 > 10:
                    for i in range(10 - (move1 - 10)):
                        text = font.render(total_letters[i + 10 + (move1 - 10)], True, (0, 0, 0))
                        finalballoon = total_balloons[i + 10 + (move1 - 10)]
                        screen.blit(finalballoon, (194 + 55 * (i + (move1 - 10)), 155))
                        screen.blit(text, (205 + 55 * (i + (move1 - 10)), 160))
                else:
                    for i in range(10):
                        text = font.render(total_letters[i + 10], True, (0, 0, 0))
                        finalballoon = total_balloons[i + 10]
                        screen.blit(finalballoon, (194 + 55 * i, 155))
                        screen.blit(text, (205 + 55 * i, 160))

                if temp == 1:
                    score_display = sfont.render("Score : %s" % scores, True, (10, 60, 150))
                    correct_display = sfont.render("Correct : %s" % correct, True, (10, 60, 150))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (10, 60, 150))
                elif temp == 2 or temp == 8:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))
                elif temp == 3 or temp == 7:
                    score_display = sfont.render("Score : %s" % scores, True, (0, 0, 0))
                    correct_display = sfont.render("Correct : %s" % correct, True, (0, 0, 0))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (0, 0, 0))
                elif temp == 4 or temp == 6:
                    score_display = sfont.render("Score : %s" % scores, True, (0, 0, 0))
                    correct_display = sfont.render("Correct : %s" % correct, True, (0, 0, 0))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (0, 0, 0))
                elif temp == 5:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))


                screen.blit(score_display, (360, 270))
                screen.blit(correct_display, (360, 320))
                screen.blit(wrong_display, (360, 370))



                if move1 == 20 and correct < 20:
                    move1 = 0

                    if temp <= 7:
                        temp += 1
                    elif temp == 8:
                        temp = 1


                    total_onlyletters = onlyletters_per_game()
                    total_balloons = balloons_per_game()
                    pg.display.update()

                elif move1 == 20 and correct >= 20:
                    move1 = 0

                    if temp <= 7:
                        temp += 1
                    elif temp == 8:
                        temp = 1


                    total_numletters = numletters_per_game()
                    total_balloons = balloons_per_game()
                    pg.display.update()



    if countdown:
        current_time = time.perf_counter()
        remaining_time = int(limited_time - (current_time - start_time)) + 1
        text = font.render("Time: %s" % remaining_time, True, (255, 255, 255))
        screen.blit(cover, (780, 65))
        screen.blit(text, (780, 65))
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
        screen.blit(bg_3, (0, 0))
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