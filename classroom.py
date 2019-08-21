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
        self.len_y = 40
        self.len_x = 37

        self.wall = [] * self.len_y
        for i in range(self.len_y):
            self.wall.append([0] * self.len_x)
        for i in range(self.len_y):
            for j in range(self.len_x):
                if i < 10 or i > 29 or j < 10 or j > 26:
                    self.wall[i][j] = 1
        for i in range(11, 19):
            self.wall[i][12] = 1
            self.wall[i][14] = 1
            self.wall[i][16] = 1
            self.wall[i][18] = 1
            self.wall[i][20] = 1
            self.wall[i][22] = 1
        for i in range(22, 29):
            self.wall[i][14] = 1
            self.wall[i][16] = 1
            self.wall[i][18] = 1
            self.wall[i][20] = 1
            self.wall[i][22] = 1
        for i in range(18, 23):
            self.wall[i][25] = 1

        self.door = []
        for i in range(30, 32):
            for j in range(11, 13):
                self.door.append([i, j])
                self.wall[i][j] = 0
        for i in range(30, 32):
            for j in range(24, 26):
                self.door.append([i, j])
                self.wall[i][j] = 0


def create_people(map_wall, people, map_people):
    while len(people) < 80:
        x = random.randint(10, map_wall.len_x - 10)
        y = random.randint(10, map_wall.len_y - 10)
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
        map_potential[now[0]][now[1]] = 0
        while queue:
            now = queue.pop(0)
            for y, x in temp1:
                next = [now[0] + y, now[1] + x]
                if map_wall.wall[next[0]][next[1]] != 1 and map_potential[next[0]][next[1]] > map_potential[now[0]][
                    now[1]] + 1:
                    map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1
                    queue.append(next)
            for y, x in temp2:
                next = [now[0] + y, now[1] + x]
                if map_wall.wall[next[0]][next[1]] != 1 and map_potential[next[0]][next[1]] > map_potential[now[0]][
                    now[1]] + 1.4:
                    map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1.4
                    queue.append(next)


def update_all(map_wall, people, map_people, map_potential):
    temp = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
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

        while True:
            i = random.randint(0, len(temp) - 1)
            temp_y, temp_x = temp[i]
            if map_potential[y + temp_y][x + temp_x] < map_potential[y][x]:
                min_y = temp_y
                min_x = temp_x
                break

        avg_speed[0] += min_y * (count + 1)
        avg_speed[1] += min_x * (count + 1)
        avg_speed[0] /= count * 2 + 1
        avg_speed[1] /= count * 2 + 1
        if avg_speed[0] > 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001))
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_down - 1 / 5.4))) * c
            # man.speed[0] = max([-0.05, min([man.speed[0], 1.32])])
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_right - 1 / 5.4))) * s
                # man.speed[1] = max([-0.05, min([man.speed[1], 1.32])])
            elif avg_speed[1] < 0:
                man.speed[1] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_left - 1 / 5.4))) * s
                # man.speed[1] = max([-1.32, min([man.speed[1], 0.05])])
            else:
                man.speed[1] = 0
        elif avg_speed[0] < 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001)) + math.pi
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_up - 1 / 5.4))) * c
            # man.speed[0] = max([-1.32, min([man.speed[0], 0.05])])
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_right - 1 / 5.4))) * s
                # man.speed[1] = max([-0.05, min([man.speed[1], 1.32])])
            elif avg_speed[1] < 0:
                man.speed[1] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_left - 1 / 5.4))) * s
                # man.speed[1] = max([-1.32, min([man.speed[1], 0.05])])
        else:
            man.speed[0] = 0
            if avg_speed[1] > 0:
                man.speed[1] = 1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_right - 1 / 5.4)))
                # man.speed[1] = max([-0.05, min([man.speed[1], 1.32])])
            elif avg_speed[1] < 0:
                man.speed[1] = -1.32 * (1 - math.exp(-3 * (10 * 0.25 / count_left - 1 / 5.4)))
                # man.speed[1] = max([-1.32, min([man.speed[1], 0.05])])
            else:
                man.speed[1] = 0

        man.speed[0] = max([-1.32, min([man.speed[0], 1.32])])
        man.speed[1] = max([-1.32, min([man.speed[1], 1.32])])


    for man in people:
        x = man.x
        y = man.y
        if [y, x] in map_wall.door:
            map_people[y][x].pop(map_people[y][x].index(man))
            people.pop(people.index(man))
            continue
        map_people[y][x].pop(map_people[y][x].index(man))
        man.update(map_wall)
        map_people[man.y][man.x].append(man)


def show_all(screen, map_wall, map_people, map_potential):
    for i in range(map_wall.len_y):
        for j in range(map_wall.len_x):
            if map_people[i][j]:
                pygame.draw.circle(screen, (0, 100, 180), (30*j+15, 30*i+15), 13)
            if map_wall.wall[i][j]:
                pygame.draw.rect(screen, (50, 50, 50), ((30 * j, 30 * i), (30, 30)), 0)
    for y, x in map_wall.door:
        pygame.draw.rect(screen, (0, 180, 0), ((30 * x, 30 * y), (30, 30)), 0)


def gui():
    pygame.init()
    screen = pygame.display.set_mode((1200, 1100))
    bg_color = (230, 230, 230)
    pygame.display.set_caption('Simulation')

    map_wall = Map()
    people = []
    map_people = [] * map_wall.len_y
    map_potential = [] * map_wall.len_y
    for i in range(map_wall.len_y):
        map_people.append([])
        for j in range(map_wall.len_x):
            map_people[i].append([])
        map_potential.append([1000] * map_wall.len_x)
    create_people(map_wall, people, map_people)
    create_potential(map_wall, map_potential)

    count_step = 0

    while people:
        count_step += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)

        update_all(map_wall, people, map_people, map_potential)
        show_all(screen, map_wall, map_people, map_potential)
        pygame.display.flip()
        time.sleep(0.5)

    print(count_step)


def no_gui():
    map_wall = Map()
    people = []
    map_people = [] * map_wall.len_y
    map_potential = [] * map_wall.len_y
    for i in range(map_wall.len_y):
        map_people.append([])
        for j in range(map_wall.len_x):
            map_people[i].append([])
        map_potential.append([1000] * map_wall.len_x)
    create_people(map_wall, people, map_people)
    create_potential(map_wall, map_potential)

    count_step = 0

    while people:
        count_step += 1
        update_all(map_wall, people, map_people, map_potential)
    
    print(count_step)


gui()
