import pygame
import os
import sys

running = True
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()
    
    
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

    
def start_screen():
    # Главное меню
    fon = pygame.transform.scale(load_image('mainmenu.png'), (800, 600))
    screen.blit(fon, (0, 0))
    menu_sprites = pygame.sprite.Group()
    # Кнопка для перехода в следующее меню
    play = pygame.sprite.Sprite()
    play.image = load_image("play.png", -1)
    play.rect = play.image.get_rect()
    play.rect.x = 160
    play.rect.y = 225
    menu_sprites.add(play)
    # Кнопка для выхода из игры
    exit = pygame.sprite.Sprite()
    exit.image = load_image("exit.png", -1)
    exit.rect = exit.image.get_rect()
    exit.rect.x = 160
    exit.rect.y = 390
    menu_sprites.add(exit) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play.rect.collidepoint(event.pos[0], event.pos[1]):
                    return True
                if exit.rect.collidepoint(event.pos[0], event.pos[1]):
                    terminate()
        menu_sprites.draw(screen)
        pygame.display.flip()
        

def slot_screen():
    # Меню выбора файла сохранения
    fon = pygame.transform.scale(load_image('menu.png'), (800, 600))
    screen.blit(fon, (0, 0))
    menu_sprites = pygame.sprite.Group()
    # Кнопки для выбора файла
    one = pygame.sprite.Sprite()
    size = (218, 218)
    one.image = pygame.transform.scale(load_image("level1.png", -1), size)
    one.rect = one.image.get_rect()
    one.rect.x = 27
    one.rect.y = 160
    menu_sprites.add(one)
    two = pygame.sprite.Sprite()
    two.image = pygame.transform.scale(load_image("level2.png", -1), size)
    two.rect = two.image.get_rect()
    two.rect.x = 292
    two.rect.y = 160
    menu_sprites.add(two) 
    three = pygame.sprite.Sprite()
    three.image = pygame.transform.scale(load_image("level3.png", -1), size)
    three.rect = three.image.get_rect()
    three.rect.x = 553
    three.rect.y = 160
    menu_sprites.add(three)         
    text = 'Выберите файл сохранения'
    font = pygame.font.Font(None, 40)
    string_rendered = font.render(text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 205
    intro_rect.y = 70
    screen.blit(string_rendered, intro_rect)   
    # Кнопка для выхода в предыдущее меню
    exit = pygame.sprite.Sprite()
    exit.image = load_image("exit.png", -1)
    exit.rect = exit.image.get_rect()
    exit.rect.x = 160
    exit.rect.y = 440
    menu_sprites.add(exit)     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Меню выбора уровня передается номер файла и прогресс,
                # прочитанный из этого файла
                if one.rect.collidepoint(event.pos[0], event.pos[1]):
                    filename = 'data/file1.txt'
                    f = open(filename, encoding="utf8")
                    progress = ''.join(f.readlines())                    
                    return ['1', progress]
                if two.rect.collidepoint(event.pos[0], event.pos[1]):
                    filename = 'data/file2.txt'
                    f = open(filename, encoding="utf8")
                    progress = ''.join(f.readlines())                    
                    return ['2', progress]
                if three.rect.collidepoint(event.pos[0], event.pos[1]):
                    filename = 'data/file3.txt'
                    f = open(filename, encoding="utf8")
                    progress = ''.join(f.readlines())                    
                    return ['3', progress]
                if exit.rect.collidepoint(event.pos[0], event.pos[1]):
                    return -1                
        menu_sprites.draw(screen)
        pygame.display.flip()
        
def level_select(filelist):
    # Меню выбора уровня
    # Номер файла
    nfile = filelist[0]
    if len(filelist[1]) == 2:
        # Если пользователь попал в меню из уровня, в файл и в переменную
        # записывается его прогресс, если уровень был пройден
        filename = 'data/file' + nfile + '.txt'
        f = open(filename, encoding="utf8")     
        progress = ''.join(f.readlines())   
        f.close()
        if filelist[1][1] == '1':
            f = open(filename, encoding="utf8", mode="w")            
            progress = list(progress)
            progress[int(filelist[1][0])] = '1'
            progress = ''.join(progress)   
            f.write(progress)
            f.close()
    else:
        # Если пользователь попал в меню из предыдущего меню, прогресс
        # передается уже в виде переменной
        progress = filelist[1]
    fon = pygame.transform.scale(load_image('menu.png'), (800, 600))
    screen.blit(fon, (0, 0))
    menu_sprites = pygame.sprite.Group()
    # Кнопки выбора уровня
    one = pygame.sprite.Sprite()
    one.image = load_image("level1.png", -1)
    one.rect = one.image.get_rect()
    one.rect.x = 37
    one.rect.y = 200
    menu_sprites.add(one)
    two = pygame.sprite.Sprite()
    two.image = load_image("level2.png", -1)
    two.rect = two.image.get_rect()
    two.rect.x = 184
    two.rect.y = 200
    menu_sprites.add(two) 
    three = pygame.sprite.Sprite()
    three.image = load_image("level3.png", -1)
    three.rect = three.image.get_rect()
    three.rect.x = 330
    three.rect.y = 200
    menu_sprites.add(three)         
    four = pygame.sprite.Sprite()
    four.image = load_image("level4.png", -1)
    four.rect = four.image.get_rect()
    four.rect.x = 476
    four.rect.y = 200
    menu_sprites.add(four) 
    five = pygame.sprite.Sprite()
    five.image = load_image("level5.png", -1)
    five.rect = five.image.get_rect()
    five.rect.x = 624
    five.rect.y = 200
    menu_sprites.add(five)      
    text = 'Выберите уровень'
    font = pygame.font.Font(None, 40)
    string_rendered = font.render(text, 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = 275
    intro_rect.y = 70
    screen.blit(string_rendered, intro_rect)   
    exit = pygame.sprite.Sprite()
    exit.image = load_image("exit.png", -1)
    exit.rect = exit.image.get_rect()
    exit.rect.x = 160
    exit.rect.y = 440
    menu_sprites.add(exit)     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Если пользователь выбрал уровень и прошел предыдущие,
                # возвращаются номер уровня, прогресс и номер файла сохранения
                if one.rect.collidepoint(event.pos[0], event.pos[1]):
                    return [1, progress, nfile]
                if (two.rect.collidepoint(event.pos[0], event.pos[1]) and
                    progress[0] == '1'):
                    return [2, progress, nfile]
                if (three.rect.collidepoint(event.pos[0], event.pos[1]) and
                    progress[1] == '1'):
                    return [3, progress, nfile]
                if (four.rect.collidepoint(event.pos[0], event.pos[1]) and
                    progress[2] == '1'):
                    return [4, progress, nfile]
                if (five.rect.collidepoint(event.pos[0], event.pos[1]) and
                    progress[3] == '1'):
                    return [5, progress, nfile]
                if exit.rect.collidepoint(event.pos[0], event.pos[1]):
                    return 0                
        menu_sprites.draw(screen)
        pygame.display.flip()
    
    
def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину    
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')    
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))

s = (70, 70)
ps = (65, 65)
ps3 = (195, 195)
ps2 = (190, 190)
tile_images = {'wall1': pygame.transform.scale(load_image('01floor.png'), s), 
               'empty1': pygame.transform.scale(load_image('01wall.png'), s),
               'doord': pygame.transform.scale(load_image('01dd.png'), s),
               'dooru1': pygame.transform.scale(load_image('01ud1.png'), s),
               'dooru2': pygame.transform.scale(load_image('01ud2.png'), s),
               'window1': pygame.transform.scale(load_image('01window.png'), s),
               'ldhall': pygame.transform.scale(load_image('01dhl.png'), s),
               'luhall': pygame.transform.scale(load_image('01uhl.png'), s),
               'rdhall': pygame.transform.scale(load_image('01dhr.png'), s),
               'ruhall': pygame.transform.scale(load_image('01uhr.png'), s),
               'ddd': pygame.transform.scale(load_image('01dwd.png'), s),
               'ddu': pygame.transform.scale(load_image('01uwd.png'), s),
               'udd': pygame.transform.scale(load_image('01dwd.png'), s),
               'udu': pygame.transform.scale(load_image('01uwd.png'), s),
               'fdd': pygame.transform.scale(load_image('01dwd.png'), s),
               'fdu': pygame.transform.scale(load_image('01uwd.png'), s),               
               'ground': pygame.transform.scale(load_image('01ground.png'), s),
               'sky1': pygame.transform.scale(load_image('01sky.png'), s),
               'skywall1': pygame.transform.scale(load_image('01sky.png'), s),
               'ivan': pygame.transform.scale(load_image('01ivan.png'), s),
               'ladder': pygame.transform.scale(load_image('01ladder.png'), s),
               'bag': pygame.transform.scale(load_image('01bag.png'), s),
               'wall12': pygame.transform.scale(load_image('01wall.png'), s),
               'finish1': pygame.transform.scale(load_image('01floor.png'), s),
               'wall2': pygame.transform.scale(load_image('02ground.png'), s),
               'stairs': pygame.transform.scale(load_image('02stairs.png'), s),
               'grass2': pygame.transform.scale(load_image('02grass.png'), s),
               'paint1': pygame.transform.scale(load_image('02p1.png'), s),
               'paint2': pygame.transform.scale(load_image('02p2.png'), s),
               'paint3': pygame.transform.scale(load_image('02p3.png'), s),
               'sky2': pygame.transform.scale(load_image('02sky.png'), s),
               'window2': pygame.transform.scale(load_image('02window.png'), s),
               'empty2': pygame.transform.scale(load_image('02wall.png'), s),
               'finish2': pygame.transform.scale(load_image('02stairs.png'), s),
               'poma': pygame.transform.scale(load_image('02poma.png'), s),
               'sky3': pygame.transform.scale(load_image('03sky.png'), s),
               'skywall3': pygame.transform.scale(load_image('03sky.png'), s),
               'dirt': pygame.transform.scale(load_image('03dirt.png'), s),
               'snow': pygame.transform.scale(load_image('03snow.png'), s),
               'trees': pygame.transform.scale(load_image('03trees.png'), s),
               'finish3': pygame.transform.scale(load_image('03snow.png'), s),
               'miller': pygame.transform.scale(load_image('03miller.png'), s),
               'sky4': pygame.transform.scale(load_image('04bg.png'), s),
               'skywall4': pygame.transform.scale(load_image('04bg.png'), s),
               'wall4': pygame.transform.scale(load_image('04ground.png'), s),
               'finish4': pygame.transform.scale(load_image('04ground.png'), s),
               'aivan': pygame.transform.scale(load_image('04aivan.png'), s),
               'sky5': pygame.transform.scale(load_image('05sky.png'), s),
               'skywall5': pygame.transform.scale(load_image('05sky.png'), s),
               'wall5': pygame.transform.scale(load_image('05grass.png'), s)}
player_image = pygame.transform.scale(load_image('andrewstandr.png', -1), ps)

tile_width = tile_height = 70

    # Класс игрока
    
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, pos_x, pos_y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        # В какую сторону смотрит персонаж
        self.direction = 'r'
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

    def cut_sheet(self, sheet, columns, rows):
        self.frames = []
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
                
    # Класс врагов и босса
                
class AnimatedTile(pygame.sprite.Sprite):
    def __init__(self, sheet, pos_x, pos_y, tiletype):
        super().__init__(tiles_group, all_sprites)
        self.frames = []
        self.cut_sheet(sheet, 2, 1)
        self.cur_frame = 0
        self.x = pos_x
        self.y = pos_y
        # Вид врага - обычный или босс
        self.type = tiletype
        # Количество здоровья босса
        self.life = 10
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

    def cut_sheet(self, sheet, columns, rows):
        self.frames = []
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        
    def destroyed(self):
        # Уничтожение врагов
        self.type = 'sky4'
        self.image = pygame.transform.scale(load_image('04bg.png'), s)
        
        
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        # Вид ячейки
        self.type = tile_type
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(tile_width * pos_x, tile_height * pos_y)
        
        
class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0
        
    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
    
    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 500 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 400 // 2)
        
        
# основной персонаж
player = None
        
# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
        
    # Команды генерации уровней
        
def generate_level1(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('sky1', x, y)
            elif level[y][x] == '#':
                Tile('wall1', x, y)
            elif level[y][x] == 't':
                Tile('wall12', x, y)                
            elif level[y][x] == 'i':
                Tile('ivan', x, y)            
            elif level[y][x] == 'x':
                Tile('finish1', x, y)              
            elif level[y][x] == 'c':
                Tile('skywall1', x, y)              
            elif level[y][x] == 'l':
                Tile('ladder', x, y)              
            elif level[y][x] == 'd':
                Tile('empty1', x, y)              
            elif level[y][x] == 'a':
                Tile('doord', x, y)              
            elif level[y][x] == 'q':
                Tile('dooru1', x, y)              
            elif level[y][x] == 'w':
                Tile('dooru2', x, y)              
            elif level[y][x] == 'h':
                Tile('ddd', x, y)              
            elif level[y][x] == 'y':
                Tile('ddu', x, y)             
            elif level[y][x] == 'v':
                Tile('udd', x, y)              
            elif level[y][x] == 'f':
                Tile('udu', x, y)                         
            elif level[y][x] == 'k':
                Tile('fdd', x, y)              
            elif level[y][x] == 'o':
                Tile('fdu', x, y)    
            elif level[y][x] == 'm':
                Tile('window1', x, y)             
            elif level[y][x] == '1':
                Tile('ldhall', x, y)             
            elif level[y][x] == '2':
                Tile('rdhall', x, y)                
            elif level[y][x] == '3':
                Tile('luhall', x, y)                
            elif level[y][x] == '4':
                Tile('ruhall', x, y)                
            elif level[y][x] == 'b':
                Tile('bag', x, y)                
            elif level[y][x] == 'g':
                Tile('ground', x, y)                
            elif level[y][x] == '@':
                Tile('empty1', x, y)
                img = load_image("andrewstandr.png", -1)
                img = pygame.transform.scale(img, ps)
                new_player = AnimatedSprite(img, 1, 1, x, y) 
    # вернем игрока, а также размер поля в клетках            
    return new_player, x, y


def generate_level2(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('sky2', x, y)
            elif level[y][x] == '#':
                Tile('wall2', x, y)               
            elif level[y][x] == 'f':
                Tile('poma', x, y)            
            elif level[y][x] == 'x':
                Tile('finish2', x, y)              
            elif level[y][x] == 'g':
                Tile('grass2', x, y)             
            elif level[y][x] == 'd':
                Tile('empty2', x, y)              
            elif level[y][x] == 'b':
                Tile('stairs', x, y)              
            elif level[y][x] == '1':
                Tile('paint1', x, y)              
            elif level[y][x] == '2':
                Tile('paint2', x, y)              
            elif level[y][x] == '3':
                Tile('paint3', x, y)              
            elif level[y][x] == 'p':
                Tile('window2', x, y)                
            elif level[y][x] == '@':
                Tile('empty2', x, y)
                img = load_image("andrewstandr.png", -1)
                img = pygame.transform.scale(img, ps)
                new_player = AnimatedSprite(img, 1, 1, x, y)
            elif level[y][x] == 'o':
                # Враги
                Tile('empty2', x, y)  
                img = load_image("02troll.png", -1)
                img = pygame.transform.scale(img, (140, 70))
                AnimatedTile(img, x, y, 'enemy')            
            elif level[y][x] == 'u':
                Tile('empty2', x, y)  
                img = load_image("02gnome.png", -1)
                img = pygame.transform.scale(img, (140, 70))
                AnimatedTile(img, x, y, 'enemy')       
    return new_player, x, y
                
                
def generate_level3(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('sky3', x, y)
            elif level[y][x] == 'c':
                Tile('skywall3', x, y)               
            elif level[y][x] == 'g':
                Tile('dirt', x, y)            
            elif level[y][x] == 'x':
                Tile('finish3', x, y)              
            elif level[y][x] == 'u':
                Tile('snow', x, y)             
            elif level[y][x] == 't':
                Tile('trees', x, y)              
            elif level[y][x] == 'm':
                Tile('miller', x, y)            
            elif level[y][x] == '@':
                Tile('trees', x, y)
                img = load_image("andrewstandr.png", -1)
                img = pygame.transform.scale(img, ps)
                new_player = AnimatedSprite(img, 1, 1, x, y)
            elif level[y][x] == 'w':
                Tile('sky3', x, y)  
                img = load_image("03wolf.png", -1)
                img = pygame.transform.scale(img, (140, 70))
                AnimatedTile(img, x, y, 'enemy')     
    return new_player, x, y


def generate_level4(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('sky4', x, y)
            elif level[y][x] == 'c':
                Tile('skywall4', x, y)               
            elif level[y][x] == 'g':
                Tile('wall4', x, y)            
            elif level[y][x] == 'x':
                Tile('finish4', x, y)            
            elif level[y][x] == 'y':
                Tile('aivan', x, y)            
            elif level[y][x] == '@':
                Tile('sky4', x, y)
                img = load_image("andrewstandr.png", -1)
                img = pygame.transform.scale(img, ps)
                new_player = AnimatedSprite(img, 1, 1, x, y)
            elif level[y][x] == 'a':
                Tile('sky4', x, y)  
                img = load_image("04a.png", -1)
                img = pygame.transform.scale(img, (140, 70))
                AnimatedTile(img, x, y, 'enemy')     
            elif level[y][x] == 'b':
                Tile('sky4', x, y)  
                img = load_image("04b.png", -1)
                img = pygame.transform.scale(img, (140, 70))
                AnimatedTile(img, x, y, 'enemy')     
    return new_player, x, y


def generate_level5(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('sky5', x, y)
            elif level[y][x] == 'c':
                Tile('skywall5', x, y)               
            elif level[y][x] == 'g':
                Tile('wall5', x, y)        
            elif level[y][x] == '@':
                Tile('sky5', x, y)
                img = load_image("andrewstandr.png", -1)
                img = pygame.transform.scale(img, ps)
                new_player = AnimatedSprite(img, 1, 1, x, y)
            elif level[y][x] == 'i':
                # Босс
                Tile('sky5', x, y)  
                img = load_image("05ivanboss.png", -1)
                img = pygame.transform.scale(img, (140, 70))
                AnimatedTile(img, x, y, 'boss')     
    return new_player, x, y

    # Команда, меняющая спрайт игрока в зависимости от обстоятельств


def chsp(n1, n2, d, c, r, s, x, y, p):
    img = pygame.transform.scale(load_image(n1 + n2 + d + '.png', -1), s)
    p.cut_sheet(img, c, r)
    p.cur_frame = 0
    p.image = p.frames[p.cur_frame]
    p.rect.x += x
    p.rect.y += y
    p.mask = pygame.mask.from_surface(p.image)


# Уровни

def level_one(nfile):
    fon = load_image('01screen.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    infoscreen = True
    # Экран с информацией перед уровнем
    while infoscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
    player, level_x, level_y = generate_level1(load_level('level1.txt'))    
    player_group.add(player)
    camera = Camera()
    # Перемнные движения
    up = False
    down = False
    jump = False
    left = False
    right = False
    # Найдена ли карточка для прохода через дверь
    dooropen = False
    # Показывать ли текст о карточке
    showtext = False
    # Падает ли игрок после того, как прыгнул
    afterjump = False
    # На сколько пикселей вверх поднялся игрок во время прыжка
    n = 0
    # Периодичность, с которой обновляются спрайты
    pixels = 0
    # Сколько времени отображается текст
    textt = 0
    levelplay = True
    while levelplay:
        t = clock.tick()
        moved = True
        moveu = True
        mover = True
        movel = True      
        # Проверка, можно ли воспользоваться лестницей
        stairsup = False
        stairsdown = False
        for tile in tiles_group:
            type = tile.type        
            if (pygame.sprite.collide_mask(player, tile) and (type == 'ddd' or
                type == 'ddu')):
                stairsup = True
            elif (pygame.sprite.collide_mask(player, tile) and (type == 'udd' or
                type == 'udu')):
                stairsdown = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                # Проверка, должен ли двигаться игрок
                if event.key == pygame.K_SPACE:
                    jump = True           
                    d = player.direction
                    chsp('andrew', 'jump', d, 1, 1, ps, 218, 168, player)
                if event.key == pygame.K_LEFT:
                    left = True       
                    if not jump and not afterjump:
                        player.direction = 'l'
                        chsp('andrew', 'walk', 'l', 3, 3, ps3, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = True         
                    if not jump and not afterjump:
                        player.direction = 'r'
                        chsp('andrew', 'walk', 'r', 3, 3, ps2, 218, 170, player)
                # Если нажата клавиша вверх и персонаж находится на лестнице,
                # он по ней поднимается
                elif event.key == pygame.K_UP and stairsdown:
                    player.rect.y = player.rect.y + 350
                elif event.key == pygame.K_UP and stairsup:
                    player.rect.y = player.rect.y - 350          
                # выход из уровня
                if event.key == pygame.K_ESCAPE:
                    # Возвращается номер файла, номер уровня и 0, т.к. он не
                    # пройден
                    return [nfile, '00']
            if event.type == pygame.KEYUP:
                # Если персонаж перестал двигаться, меняется его спрайт
                if event.key == pygame.K_LEFT:
                    left = False
                    player.direction = 'l'
                    chsp('andrew', 'stand', 'l', 1, 1, ps, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = False
                    player.direction = 'r'
                    chsp('andrew', 'stand', 'r', 1, 1, ps, 218, 167, player)
        for tile in tiles_group:
            type = tile.type
            # Проверка, не уперся ли персонаж в стену
            if (pygame.sprite.collide_mask(player, tile) and (type == 'wall1' or
                type == 'skywall1' or type == 'ground' or type == 'wall12')):
                if (player.rect.bottom - tile.rect.top >= 5 and
                    player.rect.bottom - tile.rect.top <= 11):
                    moved = False
                elif (tile.rect.bottom - player.rect.top >= 4 and
                      tile.rect.bottom - player.rect.top <= 10):
                    moveu = False
                elif (player.rect.right - tile.rect.left >= 21 and 
                      player.rect.right - tile.rect.left <= 32):
                    mover = False
                elif (tile.rect.right - player.rect.left >= 21 and
                      tile.rect.right - player.rect.left <= 32):
                    movel = False
            if (pygame.sprite.collide_mask(player, tile) and (type == 'fdd' or 
                type == 'fdu') and not dooropen):
                if (player.rect.right - tile.rect.left >= 21 and 
                    player.rect.right - tile.rect.left <= 32):
                    mover = False                
            # Проверка, нашел ли персонаж карточку
            if (pygame.sprite.collide_mask(player, tile) and type == 'bag' and 
                not dooropen):
                dooropen = True
                showtext = True
            # Если персонаж наступил на этот блок, уровень завершен
            if pygame.sprite.collide_mask(player, tile) and type == 'finish1':
                levelplay = False
        # Прыжок
        if jump:
            if n == 0 and moved:
                jump = False
            else:
                n += 5
                if n <= 140:
                    up = True
                else:
                    n = 0
                    jump = False
                    up = False
                    afterjump = True
        # Падение
        if moved:
            player.rect.y += 5
        # Движение вверх, влево, вправо
        if up and moveu:
            player.rect.y -= 10
        if left and movel:
            # После прыжка спрайт меняется
            if afterjump and not moved:
                afterjump = False       
                player.direction = 'l'
                chsp('andrew', 'walk', 'l', 3, 3, ps3, 218, 168, player)
            player.rect.x -= 7
        if right and mover:
            if afterjump and not moved:
                afterjump = False                     
                player.direction = 'r'
                chsp('andrew', 'walk', 'r', 3, 3, ps2, 218, 170, player)
            player.rect.x += 7
        # После прыжка спрайт меняется
        if afterjump and not moved:      
            afterjump = False
            d = player.direction
            chsp('andrew', 'stand', d, 1, 1, ps, 218, 168, player)
        pixels = pixels + 1
        # Обновление спрайта
        if pixels % 3 == 0:
            player.update()
        if pixels == 99:
            pixels = 0
        # изменяем ракурс камеры
        camera.update(player); 
        # обновляем положение всех спрайтов
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        # Текст показывается, если найдена карточка, и потом исчезает
        if showtext:
            textt = textt + 1
            if textt <= 40:
                text = 'Карточка найдена'
                font = pygame.font.Font(None, 40)
                string_rendered = font.render(text, 1, pygame.Color('white'))
                intro_rect = string_rendered.get_rect()
                intro_rect.x = 275
                intro_rect.y = 70
                screen.blit(string_rendered, intro_rect)
            else:
                showtext = False
        pygame.display.flip()
    # Экран, показывающийся после прохождения уровня
    fon = load_image('finishlevel.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    finishscreen = True
    while finishscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
                    # Возвращается номер файла, номер уровня и 1, т.к. он 
                    # пройден
                    return [nfile, '01']
                

def level_two(nfile):
    fon = load_image('02screen.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    infoscreen = True
    while infoscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
    player, level_x, level_y = generate_level2(load_level('level2.txt'))    
    player_group.add(player)
    camera = Camera()
    up = False
    down = False
    jump = False
    left = False
    right = False
    afterjump = False
    n = 0
    pixels = 0
    levelplay = True
    # Сколько времени прошло с момента столкновения игрока и врага
    hurt = 0
    # Сколько здоровья у игрока
    life = 3
    # Погиб ли игрок
    gameover = False
    # Правильное отображение врагов
    for tile in tiles_group:
        type = tile.type
        if type == 'enemy':
            tile.rect.x -= 15
            tile.rect.y -= 5   
    while levelplay:
        hearts = pygame.sprite.Group()
        t = clock.tick()
        moved = True
        moveu = True
        mover = True
        movel = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True           
                    d = player.direction
                    chsp('andrew', 'jump', d, 1, 1, ps, 218, 168, player)
                if event.key == pygame.K_LEFT:
                    left = True       
                    if not jump and not afterjump:
                        player.direction = 'l'
                        chsp('andrew', 'walk', 'l', 3, 3, ps3, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = True         
                    if not jump and not afterjump:
                        player.direction = 'r'
                        chsp('andrew', 'walk', 'r', 3, 3, ps2, 218, 170, player)  
                if event.key == pygame.K_ESCAPE:
                    return [nfile, '10']
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                    player.direction = 'l'
                    chsp('andrew', 'stand', 'l', 1, 1, ps, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = False
                    player.direction = 'r'
                    chsp('andrew', 'stand', 'r', 1, 1, ps, 218, 167, player)
        for tile in tiles_group:
            type = tile.type
            if type == 'enemy':
                # обновление спрайтов врагов
                if pixels % 3 == 0:
                    tile.update()                
                # Здоровье игрока уменьшается при столкновении с врагами
                if pygame.sprite.collide_mask(player, tile):
                    if hurt == 0:
                        life = life - 1
                    hurt = hurt + 1
                    # Какое-то время здоровье не уменьшается
                    if hurt == 20:
                        hurt = 0
            if (pygame.sprite.collide_mask(player, tile) and (type == 'wall2' or
                type == 'stairs')):
                if (player.rect.bottom - tile.rect.top >= 5 and
                    player.rect.bottom - tile.rect.top <= 11):
                    moved = False
                elif (tile.rect.bottom - player.rect.top >= 4 and
                      tile.rect.bottom - player.rect.top <= 10):
                    moveu = False
                elif (player.rect.right - tile.rect.left >= 21 and 
                      player.rect.right - tile.rect.left <= 32):
                    mover = False
                elif (tile.rect.right - player.rect.left >= 21 and
                      tile.rect.right - player.rect.left <= 32):
                    movel = False
            if pygame.sprite.collide_mask(player, tile) and type == 'finish2':
                levelplay = False
        if jump:
            if n == 0 and moved:
                jump = False
            else:
                n += 5
                if n <= 140:
                    up = True
                else:
                    n = 0
                    jump = False
                    up = False
                    afterjump = True
        if moved:
            player.rect.y += 5
        if up and moveu:
            player.rect.y -= 10
        if left and movel:
            if afterjump and not moved:
                afterjump = False       
                player.direction = 'l'
                chsp('andrew', 'walk', 'l', 3, 3, ps3, 218, 168, player)
            player.rect.x -= 7
        if right and mover:
            if afterjump and not moved:
                afterjump = False                     
                player.direction = 'r'
                chsp('andrew', 'walk', 'r', 3, 3, ps2, 218, 170, player)
            player.rect.x += 7
        if afterjump and not moved:      
            afterjump = False
            d = player.direction
            chsp('andrew', 'stand', d, 1, 1, ps, 218, 168, player)
        pixels = pixels + 1
        if pixels % 3 == 0:
            player.update()
        if pixels == 99:
            pixels = 0
        # Если кончились все жизни, игра окончена
        if life <= 0:
            gameover = True
            levelplay = False
        camera.update(player); 
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        # отрисовка сердечек
        if life >= 1:
            life1 = pygame.sprite.Sprite()
            life1.image = load_image("heart.png", -1)
            life1.rect = life1.image.get_rect()
            life1.rect.x = 50
            life1.rect.y = 50
            hearts.add(life1)
        if life >= 2:
            life2 = pygame.sprite.Sprite()
            life2.image = load_image("heart.png", -1)
            life2.rect = life2.image.get_rect()
            life2.rect.x = 100
            life2.rect.y = 50
            hearts.add(life2)
        if life == 3:
            life3 = pygame.sprite.Sprite()
            life3.image = load_image("heart.png", -1)
            life3.rect = life3.image.get_rect()
            life3.rect.x = 150
            life3.rect.y = 50
            hearts.add(life3)
        hearts.draw(screen)
        pygame.display.flip()
    # Если игра окончена, показывается соответствующая картинка
    if gameover:
        fon = load_image('gameover.png')
        screen.blit(fon, (0, 0))        
        pygame.display.flip()
        goscreen = True
        while goscreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        goscreen = False            
                        return [nfile, '10']
    fon = load_image('finishlevel.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    finishscreen = True
    while finishscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
                    return [nfile, '11']
                
                
def level_three(nfile):
    fon = load_image('03screen.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    infoscreen = True
    while infoscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
    player, level_x, level_y = generate_level3(load_level('level3.txt'))    
    player_group.add(player)
    camera = Camera()
    up = False
    down = False
    jump = False
    left = False
    right = False
    afterjump = False
    n = 0
    pixels = 0
    levelplay = True
    hurt = 0
    life = 3
    gameover = False
    for tile in tiles_group:
        type = tile.type
        if type == 'enemy':
            tile.rect.x -= 15
            tile.rect.y -= 5   
    while levelplay:
        hearts = pygame.sprite.Group()
        t = clock.tick()
        moved = True
        moveu = True
        mover = True
        movel = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True           
                    d = player.direction
                    chsp('andrew', 'jump', d, 1, 1, ps, 218, 168, player)
                if event.key == pygame.K_LEFT:
                    left = True       
                    if not jump and not afterjump:
                        player.direction = 'l'
                        chsp('andrew', 'walk', 'l', 3, 3, ps3, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = True         
                    if not jump and not afterjump:
                        player.direction = 'r'
                        chsp('andrew', 'walk', 'r', 3, 3, ps2, 218, 170, player)  
                if event.key == pygame.K_ESCAPE:
                    return [nfile, '20']
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                    player.direction = 'l'
                    chsp('andrew', 'stand', 'l', 1, 1, ps, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = False
                    player.direction = 'r'
                    chsp('andrew', 'stand', 'r', 1, 1, ps, 218, 167, player)
        for tile in tiles_group:
            type = tile.type
            if type == 'enemy':
                if pixels % 3 == 0:
                    tile.update()                
                if pygame.sprite.collide_mask(player, tile):
                    if hurt == 0:
                        life = life - 1
                    hurt = hurt + 1
                    if hurt == 20:
                        hurt = 0
            if (pygame.sprite.collide_mask(player, tile) and (type == 'dirt' or
                type == 'snow' or type == 'skywall3')):
                if (player.rect.bottom - tile.rect.top >= 5 and
                    player.rect.bottom - tile.rect.top <= 11):
                    moved = False
                elif (tile.rect.bottom - player.rect.top >= 4 and
                      tile.rect.bottom - player.rect.top <= 10):
                    moveu = False
                elif (player.rect.right - tile.rect.left >= 21 and 
                      player.rect.right - tile.rect.left <= 32):
                    mover = False
                elif (tile.rect.right - player.rect.left >= 21 and
                      tile.rect.right - player.rect.left <= 32):
                    movel = False
            if pygame.sprite.collide_mask(player, tile) and type == 'finish3':
                levelplay = False
        if jump:
            if n == 0 and moved:
                jump = False
            else:
                n += 5
                if n <= 140:
                    up = True
                else:
                    n = 0
                    jump = False
                    up = False
                    afterjump = True
        if moved:
            player.rect.y += 5
        if up and moveu:
            player.rect.y -= 10
        if left and movel:
            if afterjump and not moved:
                afterjump = False       
                player.direction = 'l'
                chsp('andrew', 'walk', 'l', 3, 3, ps3, 218, 168, player)
            player.rect.x -= 7
        if right and mover:
            if afterjump and not moved:
                afterjump = False                     
                player.direction = 'r'
                chsp('andrew', 'walk', 'r', 3, 3, ps2, 218, 170, player)
            player.rect.x += 7
        if afterjump and not moved:      
            afterjump = False
            d = player.direction
            chsp('andrew', 'stand', d, 1, 1, ps, 218, 168, player)
        pixels = pixels + 1
        if pixels % 3 == 0:
            player.update()
        if pixels == 99:
            pixels = 0
        if life <= 0:
            gameover = True
            levelplay = False
        camera.update(player); 
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        if life >= 1:
            life1 = pygame.sprite.Sprite()
            life1.image = load_image("heart.png", -1)
            life1.rect = life1.image.get_rect()
            life1.rect.x = 50
            life1.rect.y = 50
            hearts.add(life1)
        if life >= 2:
            life2 = pygame.sprite.Sprite()
            life2.image = load_image("heart.png", -1)
            life2.rect = life2.image.get_rect()
            life2.rect.x = 100
            life2.rect.y = 50
            hearts.add(life2)
        if life == 3:
            life3 = pygame.sprite.Sprite()
            life3.image = load_image("heart.png", -1)
            life3.rect = life3.image.get_rect()
            life3.rect.x = 150
            life3.rect.y = 50
            hearts.add(life3)
        hearts.draw(screen)
        pygame.display.flip()
    if gameover:
        fon = load_image('gameover.png')
        screen.blit(fon, (0, 0))        
        pygame.display.flip()
        goscreen = True
        while goscreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        goscreen = False            
                        return [nfile, '20']
    fon = load_image('finishlevel.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    finishscreen = True
    while finishscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
                    return [nfile, '21']

def level_four(nfile):
    fon = load_image('04screen.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    infoscreen = True
    while infoscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
    player, level_x, level_y = generate_level4(load_level('level4.txt'))    
    player_group.add(player)
    camera = Camera()
    # Какой персонаж выбран в данный момент
    aorm = 'andrew'
    # Как высоко прыгает персонаж
    aormn = 140
    up = False
    down = False
    jump = False
    left = False
    right = False
    afterjump = False
    n = 0
    # Сколько пикселей пролетела пуля
    b = 0
    # x пули
    bx = 0
    # y пули
    by = 0
    # В какую сторону летит пуля
    bd = None
    pixels = 0
    levelplay = True
    # Летит ли пуля в данный момент
    bfly = False
    hurt = 0
    life = 3
    gameover = False
    for tile in tiles_group:
        type = tile.type
        if type == 'enemy':
            tile.rect.x -= 15
            tile.rect.y -= 5   
    while levelplay:
        hearts = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        t = clock.tick()
        moved = True
        moveu = True
        mover = True
        movel = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                # Смена персонажа
                if event.key == pygame.K_c:
                    if aorm == 'andrew':
                        aorm = 'miller'
                        aormn = 70
                    else:
                        aorm = 'andrew'
                        aormn = 140
                if event.key == pygame.K_s:
                    # Выстрел, создание пули
                    if b == 0 and aorm == 'miller' and bfly == False:
                        bullet = pygame.sprite.Sprite()
                        # Направление полета пули
                        bd = player.direction
                        bullet.image = load_image('wind' + bd + '.png', -1)
                        bullet.rect = bullet.image.get_rect()
                        bx = player.rect.x
                        if bd == 'r':
                            bx = bx + 35
                        by = player.rect.y
                        bullet.rect.x = bx
                        bullet.rect.y = by
                        bullets.add(bullet)
                        bfly = True
                if event.key == pygame.K_SPACE:
                    jump = True           
                    d = player.direction
                    chsp(aorm, 'jump', d, 1, 1, ps, 218, 168, player)
                if event.key == pygame.K_LEFT:
                    left = True       
                    if not jump and not afterjump:
                        player.direction = 'l'
                        chsp(aorm, 'walk', 'l', 3, 3, ps3, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = True         
                    if not jump and not afterjump:
                        player.direction = 'r'
                        chsp(aorm, 'walk', 'r', 3, 3, ps2, 218, 170, player)  
                if event.key == pygame.K_ESCAPE:
                    return [nfile, '30']
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                    player.direction = 'l'
                    chsp(aorm, 'stand', 'l', 1, 1, ps, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = False
                    player.direction = 'r'
                    chsp(aorm, 'stand', 'r', 1, 1, ps, 218, 167, player)
        for tile in tiles_group:
            type = tile.type
            if type == 'enemy':
                if pixels % 3 == 0:
                    tile.update()                
                if pygame.sprite.collide_mask(player, tile):
                    if hurt == 0:
                        life = life - 1
                    hurt = hurt + 1
                    if hurt == 20:
                        hurt = 0
                if bfly:
                    if pygame.sprite.collide_mask(bullet, tile):
                        # Если пуля задевает врага, враг исчезает, пуля тоже
                        tile.destroyed()
                        bfly = False
                        b = 0  
                    
            if (pygame.sprite.collide_mask(player, tile) and (type == 'wall4' or
                type == 'skywall4')):
                if (player.rect.bottom - tile.rect.top >= 5 and
                    player.rect.bottom - tile.rect.top <= 11):
                    moved = False
                elif (tile.rect.bottom - player.rect.top >= 4 and
                      tile.rect.bottom - player.rect.top <= 10):
                    moveu = False
                elif (player.rect.right - tile.rect.left >= 21 and 
                      player.rect.right - tile.rect.left <= 32):
                    mover = False
                elif (tile.rect.right - player.rect.left >= 21 and
                      tile.rect.right - player.rect.left <= 32):
                    movel = False
            if pygame.sprite.collide_mask(player, tile) and type == 'finish4':
                levelplay = False
        if jump:
            if n == 0 and moved:
                jump = False
            else:
                n += 5
                if n <= aormn:
                    up = True
                else:
                    n = 0
                    jump = False
                    up = False
                    afterjump = True
        if bfly:
            # Пуля может пролететь максимум 280 пикселей
            if b <= 280:
                # Полет пули
                bullet = pygame.sprite.Sprite()
                bullet.image = load_image('wind' + bd + '.png', -1)
                bullet.rect = bullet.image.get_rect()
                bullet.rect.y = by
                if bd == 'r':
                    bullet.rect.x = bx + b
                else:
                    bullet.rect.x = bx - b
                b = b + 5
                bullets.add(bullet)
            else:
                b = 0            
                bfly = False
        if moved:
            player.rect.y += 5
        if up and moveu:
            player.rect.y -= 10
        if left and movel:
            if afterjump and not moved:
                afterjump = False       
                player.direction = 'l'
                chsp(aorm, 'walk', 'l', 3, 3, ps3, 218, 168, player)
            player.rect.x -= 7
        if right and mover:
            if afterjump and not moved:
                afterjump = False                     
                player.direction = 'r'
                chsp(aorm, 'walk', 'r', 3, 3, ps2, 218, 170, player)
            player.rect.x += 7
        if afterjump and not moved:      
            afterjump = False
            d = player.direction
            chsp(aorm, 'stand', d, 1, 1, ps, 218, 168, player)
        pixels = pixels + 1
        if pixels % 3 == 0:
            player.update()
        if pixels == 99:
            pixels = 0
        if life <= 0:
            gameover = True
            levelplay = False
        camera.update(player); 
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        for sprite in bullets:
            camera.apply(sprite)        
        bullets.draw(screen)
        if life >= 1:
            life1 = pygame.sprite.Sprite()
            life1.image = load_image("heart.png", -1)
            life1.rect = life1.image.get_rect()
            life1.rect.x = 50
            life1.rect.y = 50
            hearts.add(life1)
        if life >= 2:
            life2 = pygame.sprite.Sprite()
            life2.image = load_image("heart.png", -1)
            life2.rect = life2.image.get_rect()
            life2.rect.x = 100
            life2.rect.y = 50
            hearts.add(life2)
        if life == 3:
            life3 = pygame.sprite.Sprite()
            life3.image = load_image("heart.png", -1)
            life3.rect = life3.image.get_rect()
            life3.rect.x = 150
            life3.rect.y = 50
            hearts.add(life3)
        hearts.draw(screen)
        pygame.display.flip()
    if gameover:
        fon = load_image('gameover.png')
        screen.blit(fon, (0, 0))        
        pygame.display.flip()
        goscreen = True
        while goscreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        goscreen = False            
                        return [nfile, '30']
    fon = load_image('finishlevel.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    finishscreen = True
    while finishscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
                    return [nfile, '31']
        

def level_five(nfile):
    fon = load_image('05screen.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    infoscreen = True
    while infoscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
    spells = pygame.sprite.Group()
    player, level_x, level_y = generate_level5(load_level('level5.txt'))    
    player_group.add(player)
    camera = Camera()
    aorm = 'andrew'
    aormn = 140
    up = False
    down = False
    jump = False
    left = False
    right = False
    afterjump = False
    n = -1
    b = 0
    bx = 0
    by = 0
    bd = None
    # Количество пикселей, которые пролетело заклинание
    s = -1
    # x заклинания
    sx = 0
    # y заклинания
    sy = 0
    pixels = 0
    levelplay = True
    bfly = False
    hurt = 0
    life = 3
    gameover = False
    for tile in tiles_group:
        type = tile.type
        if type == 'enemy':
            tile.rect.x -= 15
            tile.rect.y -= 5   
    while levelplay:
        hearts = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        t = clock.tick()
        moved = True
        moveu = True
        mover = True
        movel = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if aorm == 'andrew':
                        aorm = 'miller'
                        aormn = 70
                    else:
                        aorm = 'andrew'
                        aormn = 140
                if event.key == pygame.K_s:
                    if b == 0 and aorm == 'miller' and bfly == False:
                        bullet = pygame.sprite.Sprite()
                        bd = player.direction
                        bullet.image = load_image('wind' + bd + '.png', -1)
                        bullet.rect = bullet.image.get_rect()
                        bx = player.rect.x
                        if bd == 'r':
                            bx = bx + 35
                        by = player.rect.y
                        bullet.rect.x = bx
                        bullet.rect.y = by
                        bullets.add(bullet)
                        bfly = True
                if event.key == pygame.K_SPACE:
                    jump = True           
                    d = player.direction
                    chsp(aorm, 'jump', d, 1, 1, ps, 218, 168, player)
                if event.key == pygame.K_LEFT:
                    left = True       
                    if not jump and not afterjump:
                        player.direction = 'l'
                        chsp(aorm, 'walk', 'l', 3, 3, ps3, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = True         
                    if not jump and not afterjump:
                        player.direction = 'r'
                        chsp(aorm, 'walk', 'r', 3, 3, ps2, 218, 170, player)  
                if event.key == pygame.K_ESCAPE:
                    return [nfile, '40']
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                    player.direction = 'l'
                    chsp(aorm, 'stand', 'l', 1, 1, ps, 218, 168, player)
                elif event.key == pygame.K_RIGHT:
                    right = False
                    player.direction = 'r'
                    chsp(aorm, 'stand', 'r', 1, 1, ps, 218, 167, player)
        for tile in tiles_group:
            type = tile.type
            if type == 'boss':
                if pixels % 3 == 0:
                    tile.update()                
                # В самом начале создается заклинание
                if s == -1:
                    spell = pygame.sprite.Sprite()
                    spell.image = load_image('05spell.png', -1)
                    spell.rect = spell.image.get_rect()
                    sx = tile.rect.x
                    sy = tile.rect.y
                    s = s + 1
                    spell.rect.x = sx - s
                    spell.rect.y = sy + 50
                    spells.add(spell)
                # Заклинание пролетает 420 пикселей, потом оно возвращается в
                # изначальное положение и летит с начала
                elif s <= 420:
                    s = s + 5
                    spell.rect.x = sx - s - 2300
                else:
                    s = 0
                    spell.rect.x = sx - s
                if pygame.sprite.collide_mask(player, tile):
                    # При столкновении с боссом игрок теряет здоровье
                    if hurt == 0:
                        life = life - 1
                    hurt = hurt + 1
                    if hurt == 20:
                        hurt = 0
                if bfly:
                    if pygame.sprite.collide_mask(bullet, tile):
                        # При столкновении пули и босса последний теряет жизнь
                        tile.life -= 1
                        # Когда у босса не остается жизней, уровень пройден
                        if tile.life == 0:
                            levelplay = False
                        bfly = False
                        b = 0           
            if (pygame.sprite.collide_mask(player, tile) and (type == 'wall5' or
                type == 'skywall5')):
                if (player.rect.bottom - tile.rect.top >= 5 and
                    player.rect.bottom - tile.rect.top <= 11):
                    moved = False
                elif (tile.rect.bottom - player.rect.top >= 4 and
                      tile.rect.bottom - player.rect.top <= 10):
                    moveu = False
                elif (player.rect.right - tile.rect.left >= 21 and 
                      player.rect.right - tile.rect.left <= 32):
                    mover = False
                elif (tile.rect.right - player.rect.left >= 21 and
                      tile.rect.right - player.rect.left <= 32):
                    movel = False
            if pygame.sprite.collide_mask(player, tile) and type == 'finish4':
                levelplay = False
        for sprite in spells:
            # Если игрок заденет заклинание, у него уменьшается здоровье
            if pygame.sprite.collide_mask(player, sprite):
                if hurt == 0:
                    life = life - 1
                hurt = hurt + 1
                if hurt == 20:
                    hurt = 0   
        if jump:
            if n == 0 and moved:
                jump = False
            else:
                n += 5
                if n <= aormn:
                    up = True
                else:
                    n = 0
                    jump = False
                    up = False
                    afterjump = True
        if bfly:
            if b <= 280:
                bullet = pygame.sprite.Sprite()
                bullet.image = load_image('wind' + bd + '.png', -1)
                bullet.rect = bullet.image.get_rect()
                bullet.rect.y = by
                if bd == 'r':
                    bullet.rect.x = bx + b
                else:
                    bullet.rect.x = bx - b
                b = b + 5
                bullets.add(bullet)
            else:
                b = 0            
                bfly = False
        if moved:
            player.rect.y += 5
        if up and moveu:
            player.rect.y -= 10
        if left and movel:
            if afterjump and not moved:
                afterjump = False       
                player.direction = 'l'
                chsp(aorm, 'walk', 'l', 3, 3, ps3, 218, 168, player)
            player.rect.x -= 7
        if right and mover:
            if afterjump and not moved:
                afterjump = False                     
                player.direction = 'r'
                chsp(aorm, 'walk', 'r', 3, 3, ps2, 218, 170, player)
            player.rect.x += 7
        if afterjump and not moved:      
            afterjump = False
            d = player.direction
            chsp(aorm, 'stand', d, 1, 1, ps, 218, 168, player)
        pixels = pixels + 1
        if pixels % 3 == 0:
            player.update()
        if pixels == 99:
            pixels = 0
        if life <= 0:
            gameover = True
            levelplay = False
        camera.update(player); 
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        for sprite in bullets:
            camera.apply(sprite)        
        for sprite in spells:
            camera.apply(sprite)   
        bullets.draw(screen)
        spells.draw(screen)
        if life >= 1:
            life1 = pygame.sprite.Sprite()
            life1.image = load_image("heart.png", -1)
            life1.rect = life1.image.get_rect()
            life1.rect.x = 50
            life1.rect.y = 50
            hearts.add(life1)
        if life >= 2:
            life2 = pygame.sprite.Sprite()
            life2.image = load_image("heart.png", -1)
            life2.rect = life2.image.get_rect()
            life2.rect.x = 100
            life2.rect.y = 50
            hearts.add(life2)
        if life == 3:
            life3 = pygame.sprite.Sprite()
            life3.image = load_image("heart.png", -1)
            life3.rect = life3.image.get_rect()
            life3.rect.x = 150
            life3.rect.y = 50
            hearts.add(life3)
        hearts.draw(screen)
        pygame.display.flip()
    if gameover:
        fon = load_image('gameover.png')
        screen.blit(fon, (0, 0))        
        pygame.display.flip()
        goscreen = True
        while goscreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        goscreen = False            
                        return [nfile, '40']
    fon = load_image('ending.png')
    screen.blit(fon, (0, 0))
    pygame.display.flip()
    finishscreen = True
    while finishscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    infoscreen = False              
                    return [nfile, '41']        
        
        
while running:
    if start_screen():
        n = 0
        while n == 0:
            filelist = slot_screen()
            # Если нажата кнопка выйти, переход в преыдущее меню
            if filelist == -1:
                break
            while filelist != -1:
                n = level_select(filelist)
                # Если нажата кнопка выйти, переход в преыдущее меню
                if n == 0:
                    break
                # Переход в уровень, если он открыт
                elif n[0] == 1:
                    filelist = level_one(n[2])
                elif n[0] == 2 and n[1][0] == '1':
                    filelist = level_two(n[2])
                elif n[0] == 3 and n[1][1] == '1':
                    filelist = level_three(n[2])                
                elif n[0] == 4 and n[1][2] == '1':
                    filelist = level_four(n[2])                                
                elif n[0] == 5 and n[1][3] == '1':
                    filelist = level_five(n[2])                