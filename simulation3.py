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
        if not map_wall.wall[int(self.py + self.speed[0])][self.x]:
            self.py += self.speed[0]
            self.y = int(self.py)
        if not map_wall.wall[self.y][int(self.px + self.speed[1])]:
            self.px += self.speed[1]
            self.x = int(self.px)


class Map:
    def __init__(self):
        self.len_y = 640
        self.len_x = 1270

        self.wall = [] * self.len_y
        for i in range(self.len_y):
            self.wall.append([0] * self.len_x)
        for i in range(self.len_y):
            for j in range(self.len_x):
                self.wall[i][j] = 1
        for i in range(20, 70):
            for j in range(170, 370):
                self.wall[i][j] = 0
        for i in range(20, 70):
            for j in range(420, 570):
                self.wall[i][j] = 0
        for i in range(20, 220):
            for j in range(580, 630):
                self.wall[i][j] = 0
        for i in range(80, 220):
            for j in range(370, 420):
                self.wall[i][j] = 0
        for i in range(170, 220):
            for j in range(420, 570):
                self.wall[i][j] = 0
        for i in range(20, 70):
            for j in range(640, 840):
                self.wall[i][j] = 0
        for i in range(80, 160):
            for j in range(780, 820):
                self.wall[i][j] = 0
        for i in range(170, 220):
            for j in range(640, 820):
                self.wall[i][j] = 0
        for i in range(20, 160):
            for j in range(850, 900):
                self.wall[i][j] = 0
        for i in range(170, 220):
            for j in range(950, 1250):
                self.wall[i][j] = 0
        for i in range(220, 470):
            for j in range(950, 1000):
                self.wall[i][j] = 0
        for i in range(230, 410):
            for j in range(1200, 1250):
                self.wall[i][j] = 0
        for i in range(420, 470):
            for j in range(1200, 1250):
                self.wall[i][j] = 0
        for i in range(420, 470):
            for j in range(950, 1190):
                self.wall[i][j] = 0
        for i in range(420, 620):
            for j in range(770, 900):
                self.wall[i][j] = 0
        for i in range(420, 460):
            for j in range(370, 760):
                self.wall[i][j] = 0
        for i in range(480, 620):
            for j in range(530, 580):
                self.wall[i][j] = 0
        for i in range(580, 620):
            for j in range(180, 760):
                self.wall[i][j] = 0
        for i in range(560, 620):
            for j in range(20, 170):
                self.wall[i][j] = 0
        for i in range(420, 580):
            for j in range(390, 410):
                self.wall[i][j] = 0

        for i in range(43, 48):
            for j in range(370, 900):
                self.wall[i][j] = 0
        for i in range(193, 198):
            for j in range(370, 1000):
                self.wall[i][j] = 0
        for i in range(45, 200):
            for j in range(395, 400):
                self.wall[i][j] = 0
        for i in range(45, 200):
            for j in range(795, 800):
                self.wall[i][j] = 0
        for i in range(45, 195):
            for j in range(870, 875):
                self.wall[i][j] = 0
        for i in range(195, 430):
            for j in range(1220, 1225):
                self.wall[i][j] = 0
        for i in range(445, 450):
            for j in range(520, 1225):
                self.wall[i][j] = 0
        for i in range(595, 600):
            for j in range(120, 900):
                self.wall[i][j] = 0
        for i in range(430, 600):
            for j in range(555, 560):
                self.wall[i][j] = 0

        # for i in range(43, 48):
        #     for j in range(847, 850):
        #         self.wall[i][j] = -1
        # for i in range(193, 198):
        #     for j in range(820, 823):
        #         self.wall[i][j] = -1
        # for i in range(577, 580):
        #     for j in range(390, 410):
        #         self.wall[i][j] = -1

        self.door = []
        self.door_dic = {}
        self.count_door = [0, 0]
        for i in range(70, 73):
            for j in range(550, 555):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 1
        for i in range(167, 170):
            for j in range(500, 505):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 2
        for i in range(220, 223):
            for j in range(800, 805):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 3
        for i in range(220, 223):
            for j in range(1100, 1105):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 4
        for i in range(170, 175):
            for j in range(1250, 1253):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 5
        for i in range(300, 305):
            for j in range(1000, 1003):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 6
        for i in range(340, 345):
            for j in range(1000, 1003):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 7
        for i in range(417, 420):
            for j in range(400, 405):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 8
        for i in range(417, 420):
            for j in range(805, 810):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 9
        for i in range(465, 470):
            for j in range(1250, 1253):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 10
        for i in range(620, 623):
            for j in range(80, 85):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 11


def create_people(map_wall, people, map_people):
    while len(people) < 6000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(20, map_wall.len_y - 20)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)


def create_potential(map_wall, map_potential):
    temp1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    temp2 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    for now in map_wall.door:
        if map_wall.door_dic[tuple(now)] == 1:
            queue = []
            queue.append(now)
            # map_potential[now[0]][now[1]] = 50
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
        elif map_wall.door_dic[tuple(now)] == 8:
            queue = []
            queue.append(now)
            # map_potential[now[0]][now[1]] = 150
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
        elif map_wall.door_dic[tuple(now)] == 9:
            queue = []
            queue.append(now)
            # map_potential[now[0]][now[1]] = 150
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
        else:
            queue = []
            queue.append(now)
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


def update_potential(map_wall, map_potential, count_step):
    temp1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    temp2 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    if count_step == 95:
        for i in range(48, 51):
            for j in range(395, 400):
                map_wall.wall[i][j] = -1
        for now in map_wall.door:
            if map_wall.door_dic[tuple(now)] == 1:
                queue = []
                queue.append(now)
                map_potential[now[0]][now[1]] = 45
                while queue:
                    now = queue.pop(0)
                    for y, x in temp1:
                        next = [now[0] + y, now[1] + x]
                        if not map_wall.wall[next[0]][next[1]] and map_potential[next[0]][next[1]] > \
                                map_potential[now[0]][
                                    now[1]] + 1:
                            map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1
                            queue.append(next)
                    for y, x in temp2:
                        next = [now[0] + y, now[1] + x]
                        if not map_wall.wall[next[0]][next[1]] and map_potential[next[0]][next[1]] > \
                                map_potential[now[0]][
                                    now[1]] + 1.4:
                            map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1.4
                            queue.append(next)


def update_all(map_wall, people, map_people, map_potential, map_count):
    temp = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    p = 3
    vm = 1.32 * 2
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

        min_y = 0
        min_x = 0
        if map_potential[y][x] < 10:
            for k in range(20):
                i = random.randint(0, len(temp) - 1)
                temp_y, temp_x = temp[i]
                if map_potential[y + temp_y][x + temp_x] < map_potential[y][x]:
                    min_y = temp_y
                    min_x = temp_x
                    break
        else:
            for k in range(20):
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
            man.speed[0] = vm * (1 - math.exp(-p * (10 * 0.25 / count_down - 1 / 5.4))) * c
            if avg_speed[1] > 0:
                man.speed[1] = vm * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
            elif avg_speed[1] < 0:
                man.speed[1] = vm * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
            else:
                man.speed[1] = 0
        elif avg_speed[0] < 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001)) + math.pi
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = vm * (1 - math.exp(-p * (10 * 0.25 / count_up - 1 / 5.4))) * c
            if avg_speed[1] > 0:
                man.speed[1] = vm * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
            elif avg_speed[1] < 0:
                man.speed[1] = vm * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
        else:
            man.speed[0] = 0
            if avg_speed[1] > 0:
                man.speed[1] = vm * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4)))
            elif avg_speed[1] < 0:
                man.speed[1] = -vm * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4)))
            else:
                man.speed[1] = 0
        man.speed[0] = max([-vm, min([man.speed[0], vm])])
        man.speed[1] = max([-vm, min([man.speed[1], vm])])

    count_door = 999
    for man in people:
        x = man.x
        y = man.y
        map_count[y][x] += 1
        if [y, x] in map_wall.door and count_door:
            count_door -= 1
            map_people[y][x].pop(map_people[y][x].index(man))
            people.pop(people.index(man))
            continue
        map_people[y][x].pop(map_people[y][x].index(man))
        man.update(map_wall)
        map_people[man.y][man.x].append(man)


def show_all(screen, map_wall, map_people, map_potential):
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_potential[i][j] > 500:
                pygame.draw.circle(screen, (0, 0, 0), (j, i), 0)
            else:
                pygame.draw.circle(screen, (
                    (255 - 0.5 * map_potential[i][j]), (255 - 0.5 * map_potential[i][j]),
                    (255 - 0.5 * map_potential[i][j])), (j, i), 0)
            if map_people[i][j]:
                pygame.draw.circle(screen, (0, 100, 180), (j, i), 2)
            if map_wall.wall[i][j] == 1:
                pygame.draw.circle(screen, (50, 50, 50), (j, i), 0)
            elif map_wall.wall[i][j] == -1:
                pygame.draw.circle(screen, (150, 0, 0), (j, i), 0)
    for y, x in map_wall.door:
        pygame.draw.circle(screen, (0, 180, 0), (x, y), 0)


def show_count(screen, map_wall, map_count):
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_count[i][j] > 80:
                pygame.draw.circle(screen, (255, 0, 0), (j, i), 0)
            elif map_count[i][j] > 60:
                pygame.draw.circle(screen, (255, 20, 20), (j, i), 0)
            elif map_count[i][j] > 30:
                pygame.draw.circle(screen, (255, 40, 40), (j, i), 0)
                # pygame.draw.circle(screen, (255, (255 - 4.2*map_count[i][j]), (255 - 4.2*map_count[i][j])), (j, i), 0)
            elif map_count[i][j] > 10:
                pygame.draw.circle(screen, (255, 100, 100), (j, i), 0)
            elif map_count[i][j] > 0:
                pygame.draw.circle(screen, (255, 200, 200), (j, i), 0)
            if map_wall.wall[i][j] == 1:
                pygame.draw.circle(screen, (0, 0, 0), (j, i), 0)
            elif map_wall.wall[i][j] == -1:
                pygame.draw.circle(screen, (150, 0, 0), (j, i), 0)


def gui():
    pygame.init()
    screen = pygame.display.set_mode((1270, 640))
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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        if people:
            count_step += 1
            # update_potential(map_wall, map_potential, count_step)
            update_all(map_wall, people, map_people, map_potential, map_count)
            show_all(screen, map_wall, map_people, map_potential)
            if count_step % 60 == 1:
                pygame.image.save(screen, 'pic' + str(int(count_step / 60)) + '.jpg')
            print(count_step, len(people), map_count[68][550])
        else:
            show_count(screen, map_wall, map_count)
            pygame.image.save(screen, 'pic' + '.jpg')
            print(count_step)
            break
        pygame.display.flip()
        time.sleep(0.01)


gui()
