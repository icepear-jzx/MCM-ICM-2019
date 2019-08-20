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
        self.len_y = 100
        self.len_x = 100
        # self.door = [[50, 50], [50, 51], [51, 50], [51, 51], [50, 448], [51, 448], [51, 449], [50, 449], [448, 50],
        #              [448, 51], [449, 51], [449, 50], [448, 448], [448, 449], [449, 448], [449, 449]]

        self.wall = [] * self.len_y
        for i in range(self.len_y):
            self.wall.append([0] * self.len_x)
        for i in range(self.len_y):
            for j in range(self.len_x):
                if i < 20 or i > 80 or j < 20 or j > 80:
                    self.wall[i][j] = 1

        self.door = []
        # for i in range(17, 20):
        #     for j in range(46, 58):
        #         self.door.append([i, j])
        #         self.wall[i][j] = 0
        for i in range(48, 53):
            for j in range(48, 53):
                self.door.append([i, j])
                self.wall[i][j] = 0


def create_people(map_wall, people, map_people):
    while len(people) < 3000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(20, map_wall.len_y - 20)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)


# def create_potential(map_wall, map_potential):
#     temp = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
#     for now in map_wall.door:
#         queue = []
#         queue.append(now)
#         map_potential[now[0]][now[1]] = 0
#         while queue:
#             now = queue.pop(0)
#             for y, x in temp:
#                 next = [now[0] + y, now[1] + x]
#                 if map_wall.wall[next[0]][next[1]] != 1 and map_potential[next[0]][next[1]] > map_potential[now[0]][
#                     now[1]] + 1:
#                     map_potential[next[0]][next[1]] = map_potential[now[0]][now[1]] + 1
#                     queue.append(next)

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
        if [y, x] in map_wall.door and count_door:
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
            # if map_potential[i][j] > 510:
            #     pygame.draw.circle(screen, (0, 0, 0), (j, i), 0)
            # else:
            #     pygame.draw.circle(screen, (
            #         0.3 * (255 - 0.5 * map_potential[i][j]), 0.3 * (255 - 0.5 * map_potential[i][j]),
            #         0.3 * (255 - 0.5 * map_potential[i][j])),
            #                        (j, i), 0)
            if map_people[i][j]:
                pygame.draw.circle(screen, (0, 100, 180), (10 * j + 5, 10 * i + 5), 4)
            if map_wall.wall[i][j]:
                pygame.draw.rect(screen, (50, 50, 50), ((10 * j, 10 * i), (10, 10)))


def gui():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
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
    # for i in range(50, 450):
    #     print(''.join(str(map_potential[i])))
    # file = open('data.txt', 'w')
    # for i in range(500):
    #     line = ''
    #     for j in range(500):
    #         line += str(map_potential[i][j]) + ' '
    #     line = line[:-1]
    #     line += '\r\n'
    #     file.write(line)
    file = open('data.txt', 'w')
    count_step = 0
    while people:
        # print(len(people))
        count_step += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)

        update_all(map_wall, people, map_people, map_potential)
        show_all(screen, map_wall, map_people, map_potential)
        pygame.display.flip()
        # print(people[0].speed)
        # count = 0
        # speed_y = 0
        # for i in range(20, 22):
        #     for j in range(48, 53):
        #         for item in map_people[i][j]:
        #             count += 1
        #             speed_y += item.speed[0]
        #
        # file.write(str(count / 10 / 0.25) + ' ' + str(abs(speed_y / (count + 0.0000000001) / 2)) + '\r\n')
        #
        # if count_step % 50 == 1:
        #     pygame.image.save(screen, 'simulation' + str(int(count_step / 50)) + '.jpg')
        time.sleep(0.01)
    print(count_step)


def no_gui():
    # pygame.init()
    # screen = pygame.display.set_mode((500, 500))
    # bg_color = (230, 230, 230)
    # pygame.display.set_caption('Simulation')

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
    # for i in range(50, 450):
    #     print(''.join(str(map_potential[i])))
    # file = open('data.txt', 'w')
    # for i in range(500):
    #     line = ''
    #     for j in range(500):
    #         line += str(map_potential[i][j]) + ' '
    #     line = line[:-1]
    #     line += '\r\n'
    #     file.write(line)

    count_step = 0
    while people:
        print(len(people))
        count_step += 1
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # screen.fill(bg_color)

        update_all(map_wall, people, map_people, map_potential)
        # show_all(screen, map_wall, map_people, map_potential)
        # pygame.display.flip()
        # print(people[0].speed)
        time.sleep(0.01)
    print(count_step)


gui()
