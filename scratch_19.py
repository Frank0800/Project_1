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


# def numletters_per_game():
#     numletters = []
#     for each in range(20):
#         numletter = random.choice('1234567890qwertyuiopasdfghjklmnbvcxz')
#         numletters.append(numletter)
#     return numletters


def balloons_per_game():
    balloonord = [balloon_1, balloon_2, balloon_3, balloon_4, balloon_5, balloon_6]
    balloons = []
    for each in range(20):
        balloon = balloonord[random.randint(0,5)]
        balloons.append(balloon)
    return balloons



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
bg1 = pg.image.load("/Users/xinyi/Desktop/bg1_1.jpg")
bg15 = pg.image.load("/Users/xinyi/Desktop/bg1_2.jpg")
bg2 = pg.image.load("/Users/xinyi/Desktop/bg2_1.jpg")
bg25 = pg.image.load("/Users/xinyi/Desktop/bg2_2.jpg")
bg3 = pg.image.load("/Users/xinyi/Desktop/bg3_1.jpg")
bg35 = pg.image.load("/Users/xinyi/Desktop/bg3_2.jpg")
bg4 = pg.image.load("/Users/xinyi/Desktop/bg4_1.jpg")
bg45 = pg.image.load("/Users/xinyi/Desktop/bg4_2.jpg")
bg5 = pg.image.load("/Users/xinyi/Desktop/bg5_1.jpg")
bg55 = pg.image.load("/Users/xinyi/Desktop/bg5_2.jpg")
bg_2 = pg.image.load("/Users/xinyi/Desktop/main_bg.jpg")
bg_3 = pg.image.load("/Users/xinyi/Desktop/result_bg.jpg")


blue = pg.image.load('/Users/xinyi/Desktop/blue_flower.png')
blues = pg.transform.scale(blue,(60,80))
pink = pg.image.load('/Users/xinyi/Desktop/pink_flower.png')
pinks = pg.transform.scale(pink,(60,80))
orange = pg.image.load('/Users/xinyi/Desktop/orange_flower.png')
oranges = pg.transform.scale(orange,(60,80))
tree = pg.image.load('/Users/xinyi/Desktop/tree.png')
trees = pg.transform.scale(tree,(300,350))
grass = pg.image.load('/Users/xinyi/Desktop/grass.png')
grasses = pg.transform.scale(grass,(60,40))
balloon_yellow_ord = pg.image.load('/Users/xinyi/Desktop/yellow_balloon.png')
balloon_1 = pg.transform.scale(balloon_yellow_ord, (45, 55))
balloon_orange_ord = pg.image.load('/Users/xinyi/Desktop/orange_balloon.png')
balloon_2 = pg.transform.scale(balloon_orange_ord, (45, 55))
balloon_green_ord = pg.image.load('/Users/xinyi/Desktop/green_balloon.png')
balloon_3 = pg.transform.scale(balloon_green_ord, (45, 55))
balloon_purple_ord = pg.image.load('/Users/xinyi/Desktop/purple_balloon.png')
balloon_4 = pg.transform.scale(balloon_purple_ord, (45, 55))
balloon_blue_ord = pg.image.load('/Users/xinyi/Desktop/blue_balloon.png')
balloon_5 = pg.transform.scale(balloon_blue_ord, (45, 55))
balloon_red_ord = pg.image.load('/Users/xinyi/Desktop/red_balloon.png')
balloon_6 = pg.transform.scale(balloon_red_ord, (45, 55))

sun_ord = pg.image.load('/Users/xinyi/Desktop/sun.png')
sun = pg.transform.scale(sun_ord, (110, 110))
moon_ord = pg.image.load('/Users/xinyi/Desktop/moon.png')
moon = pg.transform.scale(moon_ord, (85, 95))
star1_ord = pg.image.load('/Users/xinyi/Desktop/star1.png')
star1 = pg.transform.scale(star1_ord, (30, 30))
star2_ord = pg.image.load('/Users/xinyi/Desktop/star2.png')
star2 = pg.transform.scale(star2_ord, (25, 25))

bomb_ord = pg.image.load('/Users/xinyi/Desktop/bomb.png')
bomb = pg.transform.scale(bomb_ord, (150, 150))



# if game_main or game_result:
#     file1 = r'/Users/xinyi/Desktop/Closer.mp3'
#     pg.mixer.init()
#     track = pg.mixer.music.load(file1)
#     pg.mixer.music.play()
#
# if game_active:
#     pg.mixer.music.stop()
#     file2 = r'/Users/xinyi/Desktop/Pokemon.mp3'
#     pg.mixer.init()
#     track = pg.mixer.music.load(file2)
#     pg.mixer.music.play()




# 字體與大小設定
sfont = pg.font.SysFont("Comic Sans MS", 44)
font = pg.font.SysFont("Comic Sans MS", 54)
lfont = pg.font.SysFont("Comic Sans MS", 122)

# 儲存一次遊戲中的全部字母（20個）
total_onlyletters = onlyletters_per_game()
# pg.display.update()
# total_numletters = numletters_per_game()
# pg.display.update()
total_balloons = balloons_per_game()
pg.display.update()

# temp = 0

file2 = r'/Users/xinyi/Desktop/Pokemon.mp3'
pg.mixer.init()
track = pg.mixer.music.load(file2)
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
            # file1 = r'/Users/xinyi/Desktop/Closer.mp3'
            # pg.mixer.init()
            # track = pg.mixer.music.load(file1)
            # pg.mixer.music.play()

            screen.blit(bg_2, (0, 0))
            text = sfont.render("Press enter to start", True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (341, 500))
            text = lfont.render("Typing Game", True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (215, 240))



        # 遊戲進行時執行的操作
        if game_active:

            # file2 = r'/Users/xinyi/Desktop/Pokemon.mp3'
            # pg.mixer.init()
            # track = pg.mixer.music.load(file2)
            # pg.mixer.music.play()


            if 40 >= remaining_time > 38 or 2 >= remaining_time > 0:
                screen.blit(bg1, (0, 0))
                screen.blit(sun, (800, 100))
            elif 38 >= remaining_time > 36 or 4 >= remaining_time > 2:
                screen.blit(bg15, (0, 0))
                screen.blit(sun, (800, 100))
            elif 36 >= remaining_time > 34 or 6 >= remaining_time > 4:
                screen.blit(bg2, (0, 0))
                screen.blit(sun, (800, 100))
            elif 34 >= remaining_time > 32 or 8 >= remaining_time > 6:
                screen.blit(bg25, (0, 0))
                screen.blit(sun, (800, 100))
            elif 32 >= remaining_time > 30 or 10 >= remaining_time > 8:
                screen.blit(bg3, (0, 0))
            elif 30 >= remaining_time > 28 or 12 >= remaining_time > 10:
                screen.blit(bg35, (0, 0))
            elif 28 >= remaining_time > 26 or 14 >= remaining_time > 12:
                screen.blit(bg4, (0, 0))
                screen.blit(moon, (60, 70))
            elif 26 >= remaining_time > 24 or 16 >= remaining_time > 14:
                screen.blit(bg45, (0, 0))
                screen.blit(moon, (60, 70))
                screen.blit(star2, (570, 230))
            elif 24 >= remaining_time > 22 or 18 >= remaining_time > 16:
                screen.blit(bg5, (0, 0))
                screen.blit(moon, (60, 70))
                screen.blit(star1, (120, 190))
                screen.blit(star2, (570, 230))
            elif 22 >= remaining_time > 20 or 20 >= remaining_time > 18:
                screen.blit(bg55, (0, 0))
                screen.blit(moon, (60, 70))
                screen.blit(star1, (120, 190))
                screen.blit(star2, (570, 230))




            # 將原時間用畫布蓋住
            cover = pg.Surface((45, 35))
            cover = cover.convert()
            cover.fill((40, 34, 28))



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

                if scores >= 100:
                    screen.blit(blues, [640, 570])
                if scores >= 200:
                    screen.blit(pinks, [350, 600])
                if scores >= 350:
                    screen.blit(oranges, [500, 590])
                if scores >= 500:
                    screen.blit(grasses, [420, 630])
                if scores >= 650:
                    screen.blit(trees, [580, 230])
                if scores >= 800:
                    screen.blit(blues, [100, 580])
                if scores >= 1000:
                    screen.blit(pinks, [800, 500])
                if scores >= 1200:
                    screen.blit(oranges, [260, 540])
                if scores >= 1500:
                    screen.blit(grasses, [520, 530])
                if scores >= 1800:
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

                if 40 >= remaining_time > 38 or 2 >= remaining_time > 0:
                    score_display = sfont.render("Score : %s" % scores, True, (0, 0, 111))
                    correct_display = sfont.render("Correct : %s" % correct, True, (0, 0, 111))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (0, 0, 111))
                elif 38 >= remaining_time > 36 or 4 >= remaining_time > 2:
                    score_display = sfont.render("Score : %s" % scores, True, (0, 0, 111))
                    correct_display = sfont.render("Correct : %s" % correct, True, (0, 0, 111))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (0, 0, 111))
                elif 36 >= remaining_time > 34 or 6 >= remaining_time > 4:
                    score_display = sfont.render("Score : %s" % scores, True, (0, 0, 111))
                    correct_display = sfont.render("Correct : %s" % correct, True, (0, 0, 111))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (0, 0, 111))
                elif 34 >= remaining_time > 32 or 8 >= remaining_time > 6:
                    score_display = sfont.render("Score : %s" % scores, True, (0, 0, 111))
                    correct_display = sfont.render("Correct : %s" % correct, True, (0, 0, 111))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (0, 0, 111))
                elif 32 >= remaining_time > 30 or 10 >= remaining_time > 8:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))
                elif 30 >= remaining_time > 28 or 12 >= remaining_time > 10:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))
                elif 28 >= remaining_time > 26 or 14 >= remaining_time > 12:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))
                elif 26 >= remaining_time > 24 or 16 >= remaining_time > 14:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))
                elif 24 >= remaining_time > 22 or 18 >= remaining_time > 16:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))
                elif 22 >= remaining_time > 20 or 20 >= remaining_time > 18:
                    score_display = sfont.render("Score : %s" % scores, True, (255, 255, 255))
                    correct_display = sfont.render("Correct : %s" % correct, True, (255, 255, 255))
                    wrong_display = sfont.render("Wrong : %s" % wrong, True, (255, 255, 255))


                screen.blit(score_display, (360, 255))
                screen.blit(correct_display, (360, 295))
                screen.blit(wrong_display, (360, 335))



                if move1 == 20:
                    # temp += 1
                    move1 = 0
                    total_onlyletters = onlyletters_per_game()
                    total_balloons = balloons_per_game()
                    pg.display.update()

                    # if temp >= 3:
                    #     total_numletters = numletters_per_game()
                    #     total_balloons = balloons_per_game()
                    #     pg.display.update()
                    # if temp < 3:
                    #     total_onlyletters = onlyletters_per_game()
                    #     total_balloons = balloons_per_game()
                    #     pg.display.update()


                    # if correct < 20:
                    #     total_onlyletters = onlyletters_per_game()
                    #     total_balloons = balloons_per_game()
                    #     pg.display.update()
                    # elif correct >= 20:
                    #     total_numletters = numletters_per_game()
                    #     total_balloons = balloons_per_game()
                    #     pg.display.update()




    if countdown:
        current_time = time.perf_counter()
        remaining_time = int(limited_time - (current_time - start_time)) + 1
        text = font.render("%s" % remaining_time, True, (255, 255, 255))
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

        # file3 = r'/Users/xinyi/Desktop/Closer.mp3'
        # pg.mixer.init()
        # track = pg.mixer.music.load(file3)
        # pg.mixer.music.play()

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