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
        self.fireman = 0
        self.speed = [0, 0]

    def update(self, map_wall):
        if self.fireman:
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
        else:
            if not map_wall.wall[int(self.py + self.speed[0])][int(self.px + self.speed[1])]:
                self.py += self.speed[0]
                self.y = int(self.py)
                self.px += self.speed[1]
                self.x = int(self.px)
            elif not map_wall.wall[int(self.py + self.speed[0])][self.x]:
                self.py += self.speed[0]
                self.y = int(self.py)
            elif not map_wall.wall[self.y][int(self.px + self.speed[1])]:
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
                self.wall[i][j] = 1

        for i in range(20, 70):
            for j in range(20, 110):
                self.wall[i][j] = 0
        for i in range(20, 70):
            for j in range(130, 220):
                self.wall[i][j] = 0
        for i in range(43, 48):
            for j in range(110, 130):
                self.wall[i][j] = 0

        for i in range(47, 48):
            for j in range(110, 130):
                self.wall[i][j] = -1
        for i in range(47, 55):
            for j in range(109, 110):
                self.wall[i][j] = -1

        self.door = []
        self.count_door = [0, 0]
        for i in range(43, 48):
            for j in range(220, 223):
                self.door.append([i, j])
                self.wall[i][j] = 0
        for i in range(43, 48):
            for j in range(17, 20):
                self.door.append([i, j])
                self.wall[i][j] = 0


def create_people(map_wall, people, map_people):
    while len(people) < 500:
        x = random.randint(20, 110)
        y = random.randint(20, map_wall.len_y - 20)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    man = Man(47, 170)
    man.fireman = 1
    map_people[47][170].append(man)
    people.append(man)


def create_potential(map_wall, map_potential_man, map_potential_fireman):
    temp1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    temp2 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    for now in map_wall.door:
        queue = []
        queue.append(now)
        if now[1] < 100:
            map_potential_fireman[now[0]][now[1]] = 0
            while queue:
                now = queue.pop(0)
                for y, x in temp1:
                    next = [now[0] + y, now[1] + x]
                    if not map_wall.wall[next[0]][next[1]] and map_potential_fireman[next[0]][next[1]] > \
                            map_potential_fireman[now[0]][
                                now[1]] + 1:
                        map_potential_fireman[next[0]][next[1]] = map_potential_fireman[now[0]][now[1]] + 1
                        queue.append(next)
                for y, x in temp2:
                    next = [now[0] + y, now[1] + x]
                    if not map_wall.wall[next[0]][next[1]] and map_potential_fireman[next[0]][next[1]] > \
                            map_potential_fireman[now[0]][
                                now[1]] + 1.4:
                        map_potential_fireman[next[0]][next[1]] = map_potential_fireman[now[0]][now[1]] + 1.4
                        queue.append(next)
        else:
            map_potential_man[now[0]][now[1]] = 0
            while queue:
                now = queue.pop(0)
                for y, x in temp1:
                    next = [now[0] + y, now[1] + x]
                    if map_wall.wall[next[0]][next[1]] != 1 and map_potential_man[next[0]][next[1]] > \
                            map_potential_man[now[0]][
                                now[1]] + 1:
                        map_potential_man[next[0]][next[1]] = map_potential_man[now[0]][now[1]] + 1
                        queue.append(next)
                for y, x in temp2:
                    next = [now[0] + y, now[1] + x]
                    if map_wall.wall[next[0]][next[1]] != 1 and map_potential_man[next[0]][next[1]] > \
                            map_potential_man[now[0]][
                                now[1]] + 1.4:
                        map_potential_man[next[0]][next[1]] = map_potential_man[now[0]][now[1]] + 1.4
                        queue.append(next)


def update_all(map_wall, people, map_people, map_potential_man, map_potential_fireman, map_count,count_step):
    temp = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    p = 3
    for man in people:
        if man.fireman and man.x <= 20:
            print(count_step)
        if man.fireman:
            map_potential = map_potential_fireman
        else:
            map_potential = map_potential_man
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
                    if not man.fireman:
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

        if man.fireman:
            min_y = 0
            min_x = -1
            avg_speed[0] += min_y * (3 * count + 1)
            avg_speed[1] += min_x * (3 * count + 1)
            avg_speed[0] /= count * 4 + 1
            avg_speed[1] /= count * 4 + 1
        else:
            avg_speed[0] += min_y * (count + 1)
            avg_speed[1] += min_x * (count + 1)
            avg_speed[0] /= count * 2 + 1
            avg_speed[1] /= count * 2 + 1
        if man.fireman and 32 <= count_step <= 36:
            avg_speed[1] = 0
            avg_speed[0] = 1
        elif man.fireman and 36 <= count_step <= 39:
            avg_speed[1] = -1
            avg_speed[0] = 0
        elif man.fireman and 40 <= count_step <= 45:
            avg_speed[1] = -1
            avg_speed[0] = -1
        if avg_speed[0] > 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001))
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_down - 1 / 5.4))) * c
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
            elif avg_speed[1] < 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
            else:
                man.speed[1] = 0
        elif avg_speed[0] < 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001)) + math.pi
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_up - 1 / 5.4))) * c
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
            elif avg_speed[1] < 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
        else:
            man.speed[0] = 0
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4)))
            elif avg_speed[1] < 0:
                man.speed[1] = -1.32 * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4)))
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


def show_all(screen, map_wall, map_people, map_potential_man, map_potential_fireman):
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_potential_man[i][j] > 255:
                pygame.draw.rect(screen, (0, 0, 0), ((5 * j, 5 * i), (5, 5)))
            else:
                pygame.draw.rect(screen, (
                    (255 - map_potential_man[i][j]), (255 - map_potential_man[i][j]),
                    (255 - map_potential_man[i][j])),
                                 ((5 * j, 5 * i), (5, 5)))
    for y, x in map_wall.door:
        if x < 100:
            pygame.draw.rect(screen, (180, 0, 0), ((5 * x, 5 * y), (5, 5)))
        else:
            pygame.draw.rect(screen, (0, 180, 0), ((5 * x, 5 * y), (5, 5)))
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_wall.wall[i][j] == -1:
                pygame.draw.rect(screen, (255, 150, 0), ((5 * j, 5 * i), (5, 5)))
            if map_people[i][j]:
                pygame.draw.circle(screen, (0, 100, 180), (5 * j + 3, 5 * i + 3), 2)
                for man in map_people[i][j]:
                    if man.fireman:
                        pygame.draw.circle(screen, (255, 0, 0), (5 * j + 3, 5 * i + 3), 2)
                        break
            if map_wall.wall[i][j] == 1:
                pygame.draw.rect(screen, (50, 50, 50), ((5 * j, 5 * i), (5, 5)))



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
    map_potential_man = [] * map_wall.len_y
    map_potential_fireman = [] * map_wall.len_y
    map_count = [] * map_wall.len_y
    for i in range(map_wall.len_y):
        map_people.append([])
        for j in range(map_wall.len_x):
            map_people[i].append([])
        map_potential_man.append([1000] * map_wall.len_x)
        map_potential_fireman.append([1000] * map_wall.len_x)
        map_count.append([0] * map_wall.len_x)
    create_people(map_wall, people, map_people)
    create_potential(map_wall, map_potential_man, map_potential_fireman)

    count_step = 0

    while people:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)

        count_step += 1

        if count_step == 37:
            for i in range(47, 48):
                for j in range(110, 130):
                    map_wall.wall[i][j] = 0
            for i in range(47, 55):
                for j in range(109, 110):
                    map_wall.wall[i][j] = 0

        update_all(map_wall, people, map_people, map_potential_man, map_potential_fireman, map_count,count_step)
        show_all(screen, map_wall, map_people, map_potential_man, map_potential_fireman)
            
        pygame.display.flip()

        time.sleep(0.01)
    
    print('Total steps:', count_step)
    time.sleep(2)


gui()
