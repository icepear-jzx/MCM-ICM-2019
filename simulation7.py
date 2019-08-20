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
        self.speed = [0, 0]

    def update(self, map_wall):
        if abs(map_wall.wall[int(self.py + self.speed[0])][int(self.px + self.speed[1])]) != 1:
            self.py += self.speed[0]
            self.y = int(self.py)
            self.px += self.speed[1]
            self.x = int(self.px)
        elif abs(map_wall.wall[int(self.py + self.speed[0])][self.x]) != 1:
            self.py += self.speed[0]
            self.y = int(self.py)
        elif abs(map_wall.wall[self.y][int(self.px + self.speed[1])]) != 1:
            self.px += self.speed[1]
            self.x = int(self.px)


class Map:
    def __init__(self):
        self.len_y = 620
        self.len_x = 1000

        self.wall = [] * self.len_y
        for i in range(self.len_y):
            self.wall.append([0] * self.len_x)
        for i in range(self.len_y):
            for j in range(self.len_x):
                self.wall[i][j] = 1
        for i in range(20, 120):
            for j in range(20, 980):
                self.wall[i][j] = 0
        for i in range(140, 240):
            for j in range(20, 980):
                self.wall[i][j] = 0
        for i in range(260, 360):
            for j in range(20, 980):
                self.wall[i][j] = 0
        for i in range(380, 480):
            for j in range(20, 980):
                self.wall[i][j] = 0
        for i in range(500, 600):
            for j in range(20, 980):
                self.wall[i][j] = 0

        for i in range(120, 140):
            for j in range(100, 103):
                self.wall[i][j] = 0
        for i in range(120, 140):
            for j in range(400, 403):
                self.wall[i][j] = 0
        for i in range(120, 140):
            for j in range(500, 503):
                self.wall[i][j] = 0
        for i in range(120, 140):
            for j in range(800, 803):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(100, 103):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(200, 203):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(300, 303):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(400, 403):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(500, 503):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(600, 603):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(700, 703):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(800, 803):
                self.wall[i][j] = 0
        for i in range(240, 260):
            for j in range(900, 903):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(150, 153):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(250, 253):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(350, 353):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(450, 453):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(550, 553):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(650, 653):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(750, 753):
                self.wall[i][j] = 0
        for i in range(360, 380):
            for j in range(850, 853):
                self.wall[i][j] = 0
        for i in range(480, 500):
            for j in range(100, 103):
                self.wall[i][j] = 0
        for i in range(480, 500):
            for j in range(400, 403):
                self.wall[i][j] = 0
        for i in range(480, 500):
            for j in range(500, 503):
                self.wall[i][j] = 0
        for i in range(480, 500):
            for j in range(800, 803):
                self.wall[i][j] = 0

        for j in range(20,980):
            self.wall[120][j] = -1
            self.wall[240][j] = -1
            self.wall[360][j] = -1
            self.wall[480][j] = -1

        self.door = []
        self.door_dic = {}
        self.count_door = [0, 0]
        for i in range(308, 313):
            for j in range(498, 503):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 26
        for i in range(308, 313):
            for j in range(248, 253):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 27
        for i in range(308, 313):
            for j in range(748, 753):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 28
        for i in range(548, 553):
            for j in range(498, 503):
                self.door.append([i, j])
                self.wall[i][j] = 0
                self.door_dic[(i, j)] = 29

        for i in range(120, 121):
            for j in range(100, 103):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 1
        for i in range(120, 121):
            for j in range(400, 403):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 2
        for i in range(120, 121):
            for j in range(500, 503):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 3
        for i in range(120, 121):
            for j in range(800, 803):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 4
        for i in range(240, 241):
            for j in range(100, 103):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 5
        for i in range(240, 241):
            for j in range(200, 203):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 6
        for i in range(240, 241):
            for j in range(300, 303):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 7
        for i in range(240, 241):
            for j in range(400, 403):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 8
        for i in range(240, 241):
            for j in range(500, 503):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 9
        for i in range(240, 241):
            for j in range(600, 603):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 10
        for i in range(240, 241):
            for j in range(700, 703):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 11
        for i in range(240, 241):
            for j in range(800, 803):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 12
        for i in range(240, 241):
            for j in range(900, 903):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 13
        for i in range(360, 361):
            for j in range(150, 153):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 14
        for i in range(360, 361):
            for j in range(250, 253):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 15
        for i in range(360, 361):
            for j in range(350, 353):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 16
        for i in range(360, 361):
            for j in range(450, 453):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 17
        for i in range(360, 361):
            for j in range(550, 553):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 18
        for i in range(360, 361):
            for j in range(650, 653):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 19
        for i in range(360, 361):
            for j in range(750, 753):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 20
        for i in range(360, 361):
            for j in range(850, 853):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 21
        for i in range(480, 481):
            for j in range(100, 103):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 22
        for i in range(480, 481):
            for j in range(400, 403):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 23
        for i in range(480, 481):
            for j in range(500, 503):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 24
        for i in range(480, 481):
            for j in range(800, 803):
                self.door.append([i, j])
                self.wall[i][j] = -2
                self.door_dic[(i, j)] = 25


def create_people(map_wall, people, map_people):
    while len(people) < 3000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(20, 120)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    while len(people) < 11000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(140, 240)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    while len(people) < 18000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(260, 360)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    while len(people) < 21000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(380, 480)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    while len(people) < 26000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(500, 600)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)


def create_potential(map_wall, map_potential):
    temp1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    temp2 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    for now in map_wall.door:
        if map_wall.door_dic[tuple(now)] >= 1 and map_wall.door_dic[tuple(now)] <= 4:
            queue = []
            queue.append(now)
            map_potential[now[0]][now[1]] = 700
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
        elif map_wall.door_dic[tuple(now)] >= 5 and map_wall.door_dic[tuple(now)] <= 13:
            queue = []
            queue.append(now)
            map_potential[now[0]][now[1]] = 630
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
        elif map_wall.door_dic[tuple(now)] >= 26 and map_wall.door_dic[tuple(now)] <= 28:
            queue = []
            queue.append(now)
            map_potential[now[0]][now[1]] = 500
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
        elif map_wall.door_dic[tuple(now)] >= 14 and map_wall.door_dic[tuple(now)] <= 21:
            queue = []
            queue.append(now)
            map_potential[now[0]][now[1]] = 530
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
        elif map_wall.door_dic[tuple(now)] >= 22 and map_wall.door_dic[tuple(now)] <= 25:
            queue = []
            queue.append(now)
            map_potential[now[0]][now[1]] = 400
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
                if map_potential[y + temp_y][x + temp_x] <= map_potential[y][x]:
                    min_y = temp_y
                    min_x = temp_x
                    break
        else:
            while True:
                i = random.randint(0, len(temp) - 1)
                temp_y, temp_x = temp[i]
                if map_potential[y + temp_y * 2][x + temp_x * 2] <= map_potential[y][x]:
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

    for man in people:
        x = man.x
        y = man.y
        map_count[y][x] += 1
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
            if map_potential[i][j] > 1020:
                pygame.draw.circle(screen, (0, 0, 0), (j, i), 0)
            else:
                pygame.draw.circle(screen, (
                    (255 - 0.25 * map_potential[i][j]), (255 - 0.25 * map_potential[i][j]),
                    (255 - 0.25 * map_potential[i][j])), (j, i), 0)
            if map_people[i][j]:
                pygame.draw.circle(screen, (0, 100, 180), (j, i), 0)
            if map_wall.wall[i][j] == 1:
                pygame.draw.circle(screen, (50, 50, 50), (j, i), 0)
            elif map_wall.wall[i][j] == -1:
                pygame.draw.circle(screen, (150, 0, 0), (j, i), 0)
    for y, x in map_wall.door:
        pygame.draw.circle(screen, (0, 180, 0), (x, y), 0)


# def show_count(screen, map_wall, map_count):
#     for i in range(map_wall.len_y):
#         for j in range(map_wall.len_x):
#             if map_count[i][j] > 255:
#                 pygame.draw.circle(screen, (255, 0, 0), (j, i), 0)
#             else:
#                 pygame.draw.circle(screen, (255, (255 - map_count[i][j]), (255 - map_count[i][j])),
#                                    (j, i), 0)
#             if map_wall.wall[i][j] == 1:
#                 pygame.draw.circle(screen, (0, 0, 0), (j, i), 0)
#             elif map_wall.wall[i][j] == -1:
#                 pygame.draw.circle(screen, (150, 0, 0), (j, i), 0)
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
    screen = pygame.display.set_mode((1000, 620))
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
            update_all(map_wall, people, map_people, map_potential, map_count)
            # show_all(screen, map_wall, map_people, map_potential)
            show_count(screen, map_wall, map_count)
            print(count_step, map_wall.count_door)
        else:
            show_count(screen, map_wall, map_count)
            print(count_step)
        pygame.display.flip()


gui()
