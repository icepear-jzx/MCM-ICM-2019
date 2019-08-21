import pygame
import sys
import time
import random
import math


class Man:
    def __init__(self, py, px):
        self.py = py
        self.px = px
        self.y = int(self.py)
        self.x = int(self.px)
        self.tension = 0
        self.speed = [0, 0]

    def update(self, map_wall):
        if map_wall.wall[int(self.py + self.speed[0])][int(self.px + self.speed[1])] != 1:
            self.py += self.speed[0]
            self.y = int(self.py)
            self.px += self.speed[1]
            self.x = int(self.px)
        elif map_wall.wall[int(self.py + self.speed[0])][self.x] != 1:
            self.py += self.speed[0]
            self.y = int(self.py)
        elif map_wall.wall[self.y][int(self.px + self.speed[1])] != 1:
            self.px += self.speed[1]
            self.x = int(self.px)


class Map:
    def __init__(self):
        self.len_y = 90
        self.len_x = 240

        self.wall = [] * self.len_y
        for i in range(self.len_y):
            self.wall.append([0] * self.len_x)
        for i in range(self.len_y):
            for j in range(self.len_x):
                if i < 20 or i > 70 or j < 20 or j > 220:
                    self.wall[i][j] = 1
        for i in range(27, 63):
            for j in range(45, 47):
                self.wall[i][j] = 1
        for i in range(20, 42):
            for j in range(69, 71):
                self.wall[i][j] = 1
        for i in range(48, 71):
            for j in range(69, 71):
                self.wall[i][j] = 1
        for i in range(20, 42):
            for j in range(94, 96):
                self.wall[i][j] = 1
        for i in range(48, 71):
            for j in range(94, 96):
                self.wall[i][j] = 1
        for i in range(27, 63):
            for j in range(121, 123):
                self.wall[i][j] = 1
        for i in range(20, 42):
            for j in range(146, 148):
                self.wall[i][j] = 1
        for i in range(48, 71):
            for j in range(146, 148):
                self.wall[i][j] = 1
        for i in range(31, 59):
            for j in range(170, 172):
                self.wall[i][j] = 1

        self.door = []
        self.count_door = [0, 0]
        for i in range(43, 48):
            for j in range(221, 224):
                self.door.append([i, j])
                self.wall[i][j] = 0
        for i in range(17, 20):
            for j in range(141, 146):
                self.door.append([i, j])
                self.wall[i][j] = 0


def create_people(map_wall, people, map_people):
    while len(people) < 200:
        x = random.randint(120, map_wall.len_x - 20)
        y = random.randint(20, map_wall.len_y - 20)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    while len(people) < 1000:
        x = random.randint(20, 120)
        y = random.randint(20, map_wall.len_y - 20)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)


def create_potential(map_wall, map_potential):
    temp1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    temp2 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    for now in map_wall.door:
        queue = []
        queue.append(now)
        if now[1] < 200:
            map_potential[now[0]][now[1]] = 0
        else:
            map_potential[now[0]][now[1]] = 0
        while queue:
            now = queue.pop(0)
            for y, x in temp1:
                next = [now[0] + y, now[1] + x]
                if not map_wall.wall[next[0]][next[1]] and map_potential[next[0]][next[1]] > map_potential[now[0]][
                    now[1]] + 1:
                    map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1
                    queue.append(next)
            for y, x in temp2:
                next = [now[0] + y, now[1] + x]
                if not map_wall.wall[next[0]][next[1]] and map_potential[next[0]][next[1]] > map_potential[now[0]][
                    now[1]] + 1.4:
                    map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1.4
                    queue.append(next)


def update_potential(map_wall, map_potential):
    temp1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    temp2 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    for j in range(96, 121):
        map_wall.wall[50][j] = -1
        map_wall.wall[51][j] = -1
    for now in map_wall.door:
        queue = []
        queue.append(now)
        if now[1] < 200:
            map_potential[now[0]][now[1]] = 0
        else:
            map_potential[now[0]][now[1]] = 0
        while queue:
            now = queue.pop(0)
            for y, x in temp1:
                next = [now[0] + y, now[1] + x]
                if not map_wall.wall[next[0]][next[1]] and map_potential[next[0]][next[1]] > map_potential[now[0]][
                    now[1]] + 1:
                    map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1
                    queue.append(next)
            for y, x in temp2:
                next = [now[0] + y, now[1] + x]
                if not map_wall.wall[next[0]][next[1]] and map_potential[next[0]][next[1]] > map_potential[now[0]][
                    now[1]] + 1.4:
                    map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1.4
                    queue.append(next)


def update_all(map_wall, people, map_people, map_potential, map_count):
    temp = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    p = 3
    for man in people:
        x = man.x
        y = man.y
        avg_speed = [0, 0]
        count_right = 0.0000001
        count_left = 0.0000001
        count_up = 0.0000001
        count_down = 0.0000001
        count = 0
        if [y, x] in map_wall.door:
            continue
        for i in range(y - 2, y + 3):
            for j in range(x - 2, x + 3):
                if map_wall.wall[i][j]:
                    if i < y:
                        count_up += 1
                    elif i > y:
                        count_down += 1
                    if j < x:
                        count_left += 1
                    elif j > x:
                        count_right += 1
                for item in map_people[i][j]:
                    avg_speed[0] += item.speed[0]
                    avg_speed[1] += item.speed[1]
                    count += 1
                    if i < y:
                        count_up += 1
                    elif i > y:
                        count_down += 1
                    if j < x:
                        count_left += 1
                    elif j > x:
                        count_right += 1

        if map_potential[y][x] < 10:
            while True:
                i = random.randint(0, len(temp) - 1)
                temp_y, temp_x = temp[i]
                if map_potential[y + temp_y][x + temp_x] < map_potential[y][x]:
                    min_y = temp_y
                    min_x = temp_x
                    break
        else:
            while True:
                i = random.randint(0, len(temp) - 1)
                temp_y, temp_x = temp[i]
                if map_potential[y + temp_y * 2][x + temp_x * 2] < map_potential[y][x]:
                    min_y = temp_y
                    min_x = temp_x
                    break
        # print(count)
        avg_speed[0] += min_y * (count + 1)
        avg_speed[1] += min_x * (count + 1)
        avg_speed[0] /= count * 2 + 1
        avg_speed[1] /= count * 2 + 1
        if avg_speed[0] > 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001))
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_down - 1 / 5.4))) * c
            # man.speed[0] = max([-0.05, min([man.speed[0], 1.32])])
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
                # man.speed[1] = max([-0.05, min([man.speed[1], 1.32])])
            elif avg_speed[1] < 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
                # man.speed[1] = max([-1.32, min([man.speed[1], 0.05])])
            else:
                man.speed[1] = 0
        elif avg_speed[0] < 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001)) + math.pi
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_up - 1 / 5.4))) * c
            # man.speed[0] = max([-1.32, min([man.speed[0], 0.05])])
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
                # man.speed[1] = max([-0.05, min([man.speed[1], 1.32])])
            elif avg_speed[1] < 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
                # man.speed[1] = max([-1.32, min([man.speed[1], 0.05])])
        else:
            man.speed[0] = 0
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4)))
                # man.speed[1] = max([-0.05, min([man.speed[1], 1.32])])
            elif avg_speed[1] < 0:
                man.speed[1] = -1.32 * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4)))
                # man.speed[1] = max([-1.32, min([man.speed[1], 0.05])])
            else:
                man.speed[1] = 0
        man.speed[0] = max([-1.32, min([man.speed[0], 1.32])])
        man.speed[1] = max([-1.32, min([man.speed[1], 1.32])])
        man.speed[0] *= 2
        man.speed[1] *= 2

    count_door = 999
    for man in people:
        x = man.x
        y = man.y
        map_count[y][x] += 1
        if [y, x] in map_wall.door and count_door:
            if x < 200:
                map_wall.count_door[0] += 1
            else:
                map_wall.count_door[1] += 1
            count_door -= 1
            map_people[y][x].pop(map_people[y][x].index(man))
            people.pop(people.index(man))
            continue
        map_people[y][x].pop(map_people[y][x].index(man))
        man.update(map_wall)
        map_people[man.y][man.x].append(man)


def show_all(screen, map_wall, map_people, map_potential):
    for y, x in map_wall.door:
        pygame.draw.circle(screen, (0, 180, 0), (x, y), 0)
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_potential[i][j] > 255:
                pygame.draw.rect(screen, (0, 0, 0), ((5 * j, 5 * i), (5, 5)))
            else:
                pygame.draw.rect(screen, (
                    (255 - map_potential[i][j]), (255 - map_potential[i][j]),
                    (255 - map_potential[i][j])),
                                 ((5 * j, 5 * i), (5, 5)))
            if map_people[i][j]:
                pygame.draw.circle(screen, (0, 100, 180), (5 * j + 3, 5 * i + 3), 2)
            if map_wall.wall[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), ((5 * j, 5 * i), (5, 5)))
            elif map_wall.wall[i][j] == -1:
                pygame.draw.rect(screen, (150, 0, 0), ((5 * j, 5 * i), (5, 5)))
            elif map_wall.wall[i][j] == -2:
                pygame.draw.rect(screen, (0, 150, 0), ((5 * j, 5 * i), (5, 5)))


def show_count(screen, map_wall, map_count):
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_count[i][j] > 255:
                pygame.draw.rect(screen, (255, 0, 0), ((5 * j, 5 * i), (5, 5)))
            else:
                pygame.draw.rect(screen, (255, (255 - map_count[i][j]), (255 - map_count[i][j])),
                                 ((5 * j, 5 * i), (5, 5)))
            if map_wall.wall[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), ((5 * j, 5 * i), (5, 5)))
            elif map_wall.wall[i][j] == -1:
                pygame.draw.rect(screen, (150, 0, 0), ((5 * j, 5 * i), (5, 5)))


def gui():

    pygame.init()
    screen = pygame.display.set_mode((1200, 450))
    bg_color = (230, 230, 230)
    pygame.display.set_caption('Simulation')

    map_wall = Map()
    people = []
    map_people = [] * map_wall.len_y
    map_potential = [] * map_wall.len_y
    map_count = [] * map_wall.len_y
    for i in range(map_wall.len_y):
        map_people.append([])
        for j in range(map_wall.len_x):
            map_people[i].append([])
        map_potential.append([1000] * map_wall.len_x)
        map_count.append([0] * map_wall.len_x)
    create_people(map_wall, people, map_people)
    create_potential(map_wall, map_potential)

    count_step = 0

    while people:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)

        count_step += 1
        update_all(map_wall, people, map_people, map_potential, map_count)
        show_all(screen, map_wall, map_people, map_potential)

        pygame.display.flip()

        if count_step == 10:
            pygame.image.save(screen, 'step10' + '.jpg')
        if count_step == 90:
            pygame.image.save(screen, 'step90' + '.jpg')

        time.sleep(0.01)
    
    show_count(screen, map_wall, map_count)
    pygame.display.flip()
    pygame.image.save(screen, 'step' + str(count_step) + '.jpg')
    print('Total steps:', count_step)
    time.sleep(5)


gui()
