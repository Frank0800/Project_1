# Project_1

# 正式project
import pygame as pg
import sys
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
game_active = False
# 計時器
timing = False

pg.init()

# 設定視窗
width, height = 960, 720
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Typing speed game")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))

#字體與大小設定
font = pg.font.SysFont("Comic Sans MS", 48)

# 儲存一次遊戲中的全部字母（100個）
total_letters = letters_per_game()

for i in range(10):
    text = font.render(total_letters[i], True, (0,0,255), (255,255,255))
    bg.blit(text, (205 + 55*i ,80))

for i in range(10):
    text = font.render(total_letters[i + 10], True, (0,0,255), (255,255,255))
    bg.blit(text, (205 + 55*i, 160))

screen.blit(bg, (0, 0))
pg.display.update()

#clock = pg.time.Clock()  # 建立時間元件

# 關閉程式的程式碼
while True:
    #clock.tick(30)  # 每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_RETURN] and not game_active:
        scores = 0
        remaining_time = limited_time
        game_active = True
        timing = True

    if timing:
        start_time = time.perf_counter()
        timing = False

    # 遊戲還未開始時執行的操作
    #if not game_active:

    # 遊戲進行時執行的操作
    #if game_active:



    pg.display.flip()



    # screen.blit(bg, (0, 0))  # 重繪視窗
    # pg.display.update()  # 更新視窗

pg.quit()
