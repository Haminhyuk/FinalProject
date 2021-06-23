# 파이 게임 함수
import pygame
import sys
import random
from pygame.locals import *

# 음악 관련 함수
import pysynth as ps
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest
from src.MarkovMusic import MusicMatrix
from pprint import pprint

# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLINK = [(224, 255, 255), (192, 240, 255), (128, 224, 255), (64, 192, 255), (128, 224, 255), (192, 240, 255)]

# 이미지 로딩
imgTitle = pygame.image.load("image/music.jpg")
imgTitle2 = pygame.image.load("image/eegtitle.png")
imgTitle2 = pygame.transform.scale(imgTitle2, [700,700])
music_block1 = pygame.image.load("Melody/2do.png")
music_block1 = pygame.transform.scale(music_block1, [80,80])
music_block2 = pygame.image.load("Melody/2re.png")
music_block2 = pygame.transform.scale(music_block2, [80,80])
music_block3 = pygame.image.load("Melody/2mi.png")
music_block3 = pygame.transform.scale(music_block3, [80,80])
music_block4 = pygame.image.load("Melody/2pa.png")
music_block4 = pygame.transform.scale(music_block4, [80,80])
music_block5 = pygame.image.load("Melody/2sol.png")
music_block5 = pygame.transform.scale(music_block5, [80,80])
music_block6 = pygame.image.load("Melody/2la.png")
music_block6 = pygame.transform.scale(music_block6, [80,80])
music_block7 = pygame.image.load("Melody/2si.png")
music_block7 = pygame.transform.scale(music_block7, [80,80])
music_block8 = pygame.image.load("Melody/2hDo.png")
music_block8 = pygame.transform.scale(music_block8, [80,80])

music_block9 = pygame.image.load("Melody/4do.png")
music_block9 = pygame.transform.scale(music_block9, [80,80])
music_block10 = pygame.image.load("Melody/4re.png")
music_block10 = pygame.transform.scale(music_block10, [80,80])
music_block11 = pygame.image.load("Melody/4mi.png")
music_block11 = pygame.transform.scale(music_block11, [80,80])
music_block12 = pygame.image.load("Melody/4pa.png")
music_block12 = pygame.transform.scale(music_block12, [80,80])
music_block13 = pygame.image.load("Melody/4sol.png")
music_block13 = pygame.transform.scale(music_block13, [80,80])
music_block14 = pygame.image.load("Melody/4la.png")
music_block14 = pygame.transform.scale(music_block14, [80,80])
music_block15 = pygame.image.load("Melody/4si.png")
music_block15 = pygame.transform.scale(music_block15, [80,80])
music_block16 = pygame.image.load("Melody/4hdo.png")
music_block16 = pygame.transform.scale(music_block16, [80,80])

music_block17 = pygame.image.load("Melody/8do.png")
music_block17 = pygame.transform.scale(music_block17, [80,80])
music_block18 = pygame.image.load("Melody/8re.png")
music_block18 = pygame.transform.scale(music_block18, [80,80])
music_block19 = pygame.image.load("Melody/8mi.png")
music_block19 = pygame.transform.scale(music_block19, [80,80])
music_block20 = pygame.image.load("Melody/8pa.png")
music_block20 = pygame.transform.scale(music_block20, [80,80])
music_block21 = pygame.image.load("Melody/8sol.png")
music_block21 = pygame.transform.scale(music_block21, [80,80])
music_block22 = pygame.image.load("Melody/8la.png")
music_block22 = pygame.transform.scale(music_block22, [80,80])
music_block23 = pygame.image.load("Melody/8si.png")
music_block23 = pygame.transform.scale(music_block23, [80,80])
music_block24 = pygame.image.load("Melody/8hdo.png")
music_block24 = pygame.transform.scale(music_block24, [80,80])



songbox = pygame.image.load("image/soundicon.png")
songbox = pygame.transform.scale(songbox, [80,80])

randomsongbox = pygame.image.load("image/soundicon.png")
randomsongbox = pygame.transform.scale(randomsongbox, [80,80])

next_stage = pygame.image.load("image/stairs.png")
floor2 = pygame.image.load("image/floor3.png")
floor2 = pygame.transform.scale(floor2, [80,80])

Input1 = pygame.image.load("image/Input1.png")
Input1 = pygame.transform.scale(Input1, [80,80])
Input2 = pygame.image.load("image/Input2.png")
Input2 = pygame.transform.scale(Input2, [80,80])
Input3 = pygame.image.load("image/Input3.png")
Input3 = pygame.transform.scale(Input3, [80,80])

Make1 = pygame.image.load("image/Make1.png")
Make1 = pygame.transform.scale(Make1, [80,80])
Make2 = pygame.image.load("image/Make2.png")
Make2 = pygame.transform.scale(Make2, [80,80])
Make3 = pygame.image.load("image/Make3.png")
Make3 = pygame.transform.scale(Make3, [80,80])

imgWall = pygame.image.load("image/wall.png")
imgWall2 = pygame.image.load("image/wall2.png")
imgDark = pygame.image.load("image/dark.png")

imgFloor = [
    pygame.image.load("image/floor.png")
]
imgPlayer = [
    pygame.image.load("image/mychr0.png"),
    pygame.image.load("image/mychr1.png"),
    pygame.image.load("image/mychr2.png"),
    pygame.image.load("image/mychr3.png"),
    pygame.image.load("image/mychr4.png"),
    pygame.image.load("image/mychr5.png"),
    pygame.image.load("image/mychr6.png"),
    pygame.image.load("image/mychr7.png"),
    pygame.image.load("image/mychr8.png")
]

pygame.mixer.init()
se = [pygame.mixer.Sound("sound/do2.wav"),
      pygame.mixer.Sound("sound/re2.wav"),
      pygame.mixer.Sound("sound/mi2.wav"),
      pygame.mixer.Sound("sound/fa2.wav"),
      pygame.mixer.Sound("sound/sol2.wav"),
      pygame.mixer.Sound("sound/la2.wav"),
      pygame.mixer.Sound("sound/si2.wav"),
      pygame.mixer.Sound("sound/hdo2.wav")
      ]

se4 = [pygame.mixer.Sound("sound/hdo4.wav")]




songlist = [['c4', 2], ['d4', 2], ['e4', 2], ['f4', 2], ['g4', 2], ['a4', 2], ['b4', 2], ['c5', 2], 
            ['c4', 4], ['d4', 4], ['e4', 4], ['f4', 4], ['g4', 4], ['a4', 4], ['b4', 4], ['c5', 4],
            ['c4', 8], ['d4', 8], ['e4', 8], ['f4', 8], ['g4', 8], ['a4', 8], ['b4', 8], ['c5', 8]]
# 변수 선언
idx = 0
tmr = 0
floor = 0
fl_max = 1
stage = 1
pl_x = 0
pl_y = 0
pl_d = 0
pl_a = 0




MAZE_W = 11
MAZE_H = 9
maze = []
song = []
random_song = []

for y in range(MAZE_H):
    maze.append([0] * MAZE_W)

stage = 1
def make_maze():
    global maze
    if stage == 1:
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 27, 0, 0, 0, 0, 1],
                [1, 3, 4, 5, 6, 0, 7, 8, 9, 10, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 11, 12, 13, 14, 0, 15, 16, 17, 18, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 19, 20, 21, 22, 0, 23, 24, 25, 26, 1],
                [1, 0, 0, 0, 0, 27, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
    if stage == 2:
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 37, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 28, 0, 0, 0, 29, 0, 0, 1],
                [1, 0, 0, 30, 0, 0, 0, 30, 0, 0, 1],
                [1, 0, 31, 32, 33, 0, 34, 35, 36, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        '''
        #주변 벽
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W -1] = 1
        
        
    #2분 음표 도레미파
    count = 3
    for x in range(1, 5):
        maze[2][x] = count
        count = count + 1
        
    #2분 음표 솔라시도
    count = 7
    for x in range(6, 10):
        maze[2][x] = count
        count = count + 1
        
    #다음 스테이지로 가는 계단
    maze[1][5] = 11
    maze[7][5] = 11
    '''


def draw_maze(bg, fnt):
    bg.fill(CYAN)
    for y in range(-4, 6):
        for x in range(-5, 6):
            X = (x + 5) * 80
            Y = (y + 4) * 80
            dx = pl_x + x
            dy = pl_y + y
            if 0 <= dx and dx < MAZE_W and 0  <= dy and dy < MAZE_H:
                if maze[dy][dx] == 0:
                    bg.blit(imgFloor[maze[dy][dx]], [X,Y])
                if maze[dy][dx] == 3:
                    bg.blit(music_block1, [X, Y])
                if maze[dy][dx] == 4:
                    bg.blit(music_block2, [X, Y])
                if maze[dy][dx] == 5:
                    bg.blit(music_block3, [X, Y])
                if maze[dy][dx] == 6:
                    bg.blit(music_block4, [X, Y])
                if maze[dy][dx] == 7:
                    bg.blit(music_block5, [X, Y])
                if maze[dy][dx] == 8:
                    bg.blit(music_block6, [X, Y])
                if maze[dy][dx] == 9:
                    bg.blit(music_block7, [X, Y])
                if maze[dy][dx] == 10:
                    bg.blit(music_block8, [X, Y])
                if maze[dy][dx] == 11:
                    bg.blit(music_block9, [X, Y])                    
                if maze[dy][dx] == 12:
                    bg.blit(music_block10, [X, Y])
                if maze[dy][dx] == 13:
                    bg.blit(music_block11, [X, Y])
                if maze[dy][dx] == 14:
                    bg.blit(music_block12, [X, Y])
                if maze[dy][dx] == 15:
                    bg.blit(music_block13, [X, Y])
                if maze[dy][dx] == 16:                   
                    bg.blit(music_block14, [X, Y])
                if maze[dy][dx] == 17:                   
                    bg.blit(music_block15, [X, Y])
                if maze[dy][dx] == 18:                   
                    bg.blit(music_block16, [X, Y])
                if maze[dy][dx] == 19:                   
                    bg.blit(music_block17, [X, Y])
                if maze[dy][dx] == 20:                   
                    bg.blit(music_block18, [X, Y])
                if maze[dy][dx] == 21:                   
                    bg.blit(music_block19, [X, Y])
                if maze[dy][dx] == 22:                   
                    bg.blit(music_block20, [X, Y])
                if maze[dy][dx] == 23:                   
                    bg.blit(music_block21, [X, Y])
                if maze[dy][dx] == 24:                   
                    bg.blit(music_block22, [X, Y])
                if maze[dy][dx] == 25:                   
                    bg.blit(music_block23, [X, Y])
                if maze[dy][dx] == 26:                   
                    bg.blit(music_block24, [X, Y])
                if maze[dy][dx] == 27:                   
                    bg.blit(next_stage, [X, Y])
                if maze[dy][dx] == 28:                   
                    bg.blit(songbox, [X, Y])
                if maze[dy][dx] == 29:                   
                    bg.blit(randomsongbox, [X, Y])
                if maze[dy][dx] == 30:
                    bg.blit(floor2, [X, Y])
                if maze[dy][dx] == 31:
                    bg.blit(Input1, [X, Y])
                if maze[dy][dx] == 32:
                    bg.blit(Input2, [X, Y])
                if maze[dy][dx] == 33:
                    bg.blit(Input3, [X, Y])
                if maze[dy][dx] == 34:
                    bg.blit(Make1, [X, Y])
                if maze[dy][dx] == 35:
                    bg.blit(Make2, [X, Y])
                if maze[dy][dx] == 36:
                    bg.blit(Make3, [X, Y])
                if maze[dy][dx] == 37:
                    bg.blit(next_stage, [X, Y])    
                if maze[dy][dx] == 1:
                    bg.blit(imgWall, [X,Y - 40])
                    if dy >= 1 and maze[dy - 1][dx] == 1:
                        bg.blit(imgWall2, [X, Y - 80])
            if x == 0 and y == 0:
                bg.blit(imgPlayer[pl_a], [X,Y - 40])


def move_player(key):  # 주인공 이동
    global idx, tmr, pl_x, pl_y, pl_d, pl_a
    
    
    
    
    
    # 2분 음표 도를 먹었을 시
    if maze[pl_y][pl_x] == 3:
        song.append(['c4', 2])
        se[0].play()
        idx = 3
        tmr = 0
        return put_event()
            
    # 2분 음표 레를 먹었을 시
    if maze[pl_y][pl_x] == 4:
        song.append(['d4', 2])
        se[1].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 2분 음표 미를 먹었을 시
    if maze[pl_y][pl_x] == 5:
        song.append(['e4', 2])
        se[2].play()
        idx = 3
        tmr = 0
        return put_event()

    # 2분 음표 파를 먹었을 시
    if maze[pl_y][pl_x] == 6:
        song.append(['f4', 2])
        se[3].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 2분 음표 솔을 먹었을 시
    if maze[pl_y][pl_x] == 7:
        song.append(['g4', 2])
        se[4].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 2분 음표 라를 먹었을 시
    if maze[pl_y][pl_x] == 8:
        song.append(['a4', 2])
        se[5].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 2분 음표 시를 먹었을 시
    if maze[pl_y][pl_x] == 9:
        song.append(['b4', 2])
        se[6].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 2분 음표 높은 도를 먹었을 시
    if maze[pl_y][pl_x] == 10:
        song.append(['c5', 2])
        se[7].play()
        idx = 3
        tmr = 0
        return put_event()

    # 4분 음표 도를 먹었을 시
    if maze[pl_y][pl_x] == 11:
        song.append(['c4', 4])
        se[0].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 4분 음표 레를 먹었을 시
    if maze[pl_y][pl_x] == 12:
        song.append(['d4', 4])
        se[1].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 4분 음표 미를 먹었을 시
    if maze[pl_y][pl_x] == 13:
        song.append(['e4', 4])
        se[2].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 4분 음표 파를 먹었을 시
    if maze[pl_y][pl_x] == 14:
        song.append(['f4', 4])
        se[3].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 4분 음표 솔을 먹었을 시
    if maze[pl_y][pl_x] == 15:
        song.append(['g4', 4])
        se[4].play()
        idx = 3
        tmr = 0
        return put_event() 
    
    # 4분 음표 라를 먹었을 시
    if maze[pl_y][pl_x] == 16:
        song.append(['a4', 4])
        se[5].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 4분 음표 시를 먹었을 시
    if maze[pl_y][pl_x] == 17:
        song.append(['b5', 4])
        se[6].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 4분 음표 높은 도를 먹었을 시
    if maze[pl_y][pl_x] == 18:
        song.append(['c5', 4])
        se[7].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 도를 먹었을 시
    if maze[pl_y][pl_x] == 19:
        song.append(['c4', 8])
        se[0].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 레를 먹었을 시
    if maze[pl_y][pl_x] == 20:
        song.append(['d4', 8])
        se[1].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 미를 먹었을 시
    if maze[pl_y][pl_x] == 21:
        song.append(['e4', 8])
        se[2].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 파를 먹었을 시
    if maze[pl_y][pl_x] == 22:
        song.append(['f4', 8])
        se[3].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 솔을 먹었을 시
    if maze[pl_y][pl_x] == 23:
        song.append(['g4', 8])
        se[4].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 라를 먹었을 시
    if maze[pl_y][pl_x] == 24:
        song.append(['a4', 8])
        se[5].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 시를 먹었을 시
    if maze[pl_y][pl_x] == 25:
        song.append(['b4', 8])
        se[6].play()
        idx = 3
        tmr = 0
        return put_event()
    
    # 8분 음표 높은 도를 먹었을 시
    if maze[pl_y][pl_x] == 26:
        song.append(['c5', 8])
        se[7].play()
        idx = 3
        tmr = 0
        return put_event()
            
    # 계단에 닿음
    if maze[pl_y][pl_x] == 27:
        idx = 2
        tmr = 0
        return
    
    # 연주한 곡을 들을 수 있는 오브젝트
    if maze[pl_y][pl_x] == 28:
        pygame.mixer.music.load("examples/makesong2.wav")
        pygame.mixer.music.play(1)
        tmr = 0
        return put_event()
    
    # 알고리즘에 의해 만들어진 곡을 들을 수 있는 오브젝트
    if maze[pl_y][pl_x] == 29:
        pygame.mixer.music.load("result/random_makesong2.wav")
        pygame.mixer.music.play(1)
        tmr = 0
        return put_event()
    
    if maze[pl_y][pl_x] == 37:
        stage = 1
        idx = 2
        tmr = 0
        return 

    
    # 방향 키로 상하좌우 이동
    x = pl_x
    y = pl_y
    if key[K_UP] == 1:
        pl_d = 0
        if maze[pl_y - 1][pl_x] != 1:
            pl_y = pl_y - 1
    if key[K_DOWN] == 1:
        pl_d = 1
        if maze[pl_y + 1][pl_x] != 1:
            pl_y = pl_y + 1
    if key[K_LEFT] == 1:
        pl_d = 2
        if maze[pl_y][pl_x - 1] != 1:
            pl_x = pl_x - 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if maze[pl_y][pl_x + 1] != 1:
            pl_x = pl_x + 1
    pl_a = pl_d * 2
    if pl_x != x or pl_y != y:  # 이동 시 식량 및 체력 계산
        pl_a = pl_a + tmr % 2  # 이동 시 걷기 애니메이션

def put_event():  
    global pl_x, pl_y, pl_d, pl_a

    # 플레이어 초기 위치
    while True:
        pl_x = 5
        pl_y = 4
        if (maze[pl_y][pl_x] == 0):
            break
    pl_d = 1
    pl_a = 2                

def draw_text(bg, txt, x, y, fnt, col):  # 그림자 포함한 문자 표시
    sur = fnt.render(txt, True, BLACK)
    bg.blit(sur, [x + 1, y + 2])
    sur = fnt.render(txt, True, col)
    bg.blit(sur, [x, y])
    
def draw_para(bg, fnt):  # 주인공 능력 표시
    X = 30
    Y = 600
    col = WHITE
    
    list2 = []
    for x in song:
        if x[0] == 'c4':
            list2.append('Do')
        elif x[0] == 'd4':
            list2.append('Re')
        elif x[0] == 'e4':
            list2.append('Mi')
        elif x[0] == 'f4':
            list2.append('Fa')
        elif x[0] == 'g4':
            list2.append('Sol')
        elif x[0] == 'a4':
            list2.append('La')
        elif x[0] == 'b4':
            list2.append('Si')
        elif x[0] == 'c5':
            list2.append('hDo')
             
    draw_text(bg, "Melody:" + str(list2) , X , Y + 6, fnt, col)


def make_midi(midi_path, notes, bpm=120):
    note_names = 'c c# d d# e f f# g g# a a# b'.split()

    result = NoteSeq()
    for n in notes:
        duration = 1. / n[1]

        if n[0].lower() == 'r':
            result.append(Rest(dur=duration))
        else:
            pitch = n[0][:-1]
            octave = int(n[0][-1]) + 1
            pitch_number = note_names.index(pitch.lower())
            
            result.append(Note(pitch_number, octave=octave, dur=duration))
            
    midi = Midi(number_tracks=1, tempo=bpm)
    midi.seq_notes(result, track=0)
    midi.write(midi_path)
    

def main():
    global idx, tmr, stage, pl_a
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Music Game")
    screen = pygame.display.set_mode((880,720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    fontS = pygame.font.Font(None, 30)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
                
        tmr = tmr + 1
        key = pygame.key.get_pressed()
            
        if idx == 0:  # 타이틀 화면
            screen.fill(BLACK)
            screen.blit(imgTitle, [-20, 0])
            screen.blit(imgTitle2,[80, 100])
            draw_text(screen, "Press Any Key", 330, 560, font, BLINK[tmr % 6])
            if key[K_UP] or key[K_DOWN] or key[K_LEFT] or key[K_RIGHT]  == 1:
                make_maze()
                put_event()
                idx = 1
                
        # 
        elif idx == 1:
            move_player(key)
            draw_maze(screen, fontS)
            draw_para(screen, fontS)
            
            if stage == 1:
                draw_text(screen, "Input Melody", 60, 40, fontS, WHITE)
            if stage == 2:
                draw_text(screen, "Listen to Input music and make music!", 60, 40, fontS, WHITE)
                
            
            
        #화면 전환 효과(맨 위와 아래) 및 노래 만들기(중간 부분)
        elif idx == 2:
            draw_maze(screen, fontS)
            if 1 <= tmr and tmr <= 5:
                h = 80 * tmr
                pygame.draw.rect(screen, BLACK, [0,0,880,h])
                pygame.draw.rect(screen, BLACK, [0,720 - h, 880, h])
            if tmr == 5:
                stage = 1
                if stage == 1:
                    stage = stage + 1
                    make_maze()
                    ps.make_wav(song, fn='examples/makesong2.wav')
                    matrix = MusicMatrix(song)
                    start_note = song[0]
                    random_song = []
                    for i in range(0, 30):
                        start_note = matrix.next_note(start_note)
                        random_song.append(start_note)    
                    ps.make_wav(random_song, fn='result/random_makesong2.wav')
                    put_event()
    
            if 6 <= tmr and tmr <= 9:
                h = 80 * (10 - tmr)
                pygame.draw.rect(screen, BLACK, [0,0,880,h])
                pygame.draw.rect(screen, BLACK, [0,720 - h,880,h])
            if tmr == 10:
                idx = 1
                
        elif idx == 3:  # 오브젝트 터치시 발생하는 이벤트
            draw_maze(screen, fontS)
            draw_text(screen, "Input Complete!", 330, 240, font, WHITE)
            if tmr == 10:
                idx = 1


                                
          
                
               
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
