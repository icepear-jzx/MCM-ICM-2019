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
        self.max_speed = 1.32 * 2
        self.team_member = []
        self.foreign = 0
        self.disable = 0

    def update(self, map_wall):
        if self.disable:
            if map_wall.wall[int(self.py + self.speed[0])][self.x] != 1:
                self.py += self.speed[0]
                self.y = int(self.py)
            if map_wall.wall[self.y][int(self.px + self.speed[1])] != 1:
                self.px += self.speed[1]
                self.x = int(self.px)
        else:
            if not map_wall.wall[int(self.py + self.speed[0])][self.x]:
                self.py += self.speed[0]
                self.y = int(self.py)
            if not map_wall.wall[self.y][int(self.px + self.speed[1])]:
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
        # for i in range(43, 47):
        #     for j in range(17, 20):
        #         self.door.append([i, j])
        #         self.wall[i][j] = 0
        for i in range(17, 20):
            for j in range(73, 78):
                self.door.append([i, j])
                self.wall[i][j] = 0


def create_people(map_wall, people, map_people):
    # while len(people) < 200:
    #     x = random.randint(120, map_wall.len_x - 20)
    #     y = random.randint(20, map_wall.len_y - 20)
    #     if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
    #         man = Man(y, x)
    #         map_people[y][x].append(man)
    #         people.append(man)
    # while len(people) < 1000:
    #     x = random.randint(20, 120)
    #     y = random.randint(20, map_wall.len_y - 20)
    #     if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
    #         man = Man(y, x)
    #         map_people[y][x].append(man)
    #         people.append(man)

    # while len(people) < 1000:
    #     x = random.randint(20, map_wall.len_x - 20)
    #     y = random.randint(20, map_wall.len_y - 20)
    #     if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
    #         man = Man(y, x)
    #         map_people[y][x].append(man)
    #         people.append(man)
    # global count_able
    while len(people) < 1000:
        x = random.randint(20, map_wall.len_x - 20)
        y = random.randint(20, map_wall.len_y - 20)
        if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
            man = Man(y, x)
            map_people[y][x].append(man)
            people.append(man)
    # while len(people) < 900:
    #     x = random.randint(20, map_wall.len_x - 20)
    #     y = random.randint(20, map_wall.len_y - 20)
    #     if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
    #         man = Man(y, x)
    #         man.foreign = 1
    #         map_people[y][x].append(man)
    #         people.append(man)
    # while len(people) < 1000:
    #     x = random.randint(20, map_wall.len_x - 20)
    #     y = random.randint(20, map_wall.len_y - 20)
    #     if len(map_people[y][x]) == 0 and not map_wall.wall[y][x]:
    #         man = Man(y, x)
    #         man.disable = 1
    #         man.max_speed = 0.8
    #         map_people[y][x].append(man)
    #         people.append(man)
    # for k in range(count_able):
    #     temp = []
    #     for i in range(20 * k, 20 * k + 20):
    #         temp.append(people[i])
    #     for man in temp:
    #         man.team_member = temp

    # count = 0
    # j = 0
    # for j in range(20, map_wall.len_x - 20):
    #     for i in range(20, map_wall.len_y - 20):
    #         count += len(map_people[i][j])
    #         if count == 500:
    #             break
    #     if count == 500:
    #         break
    # for i in range(20, map_wall.len_y - 19):
    #     map_wall.wall[i][j] = -1
    #     map_wall.wall[i][j + 1] = -1
    # for i in range(20, map_wall.len_y - 19):
    #     map_wall.wall[i][82] = -1
    #     map_wall.wall[i][83] = -1
    for i in range(20, map_wall.len_y - 19):
        map_wall.wall[i][120] = -1
        map_wall.wall[i][121] = -1
    # for i in range(20, map_wall.len_y - 19):
    #     map_wall.wall[i][90] = -1
    #     map_wall.wall[i][91] = -1
    # for j in range(123, 146):
    #     map_wall.wall[35][j] = -1
    #     map_wall.wall[36][j] = -1

    # for i in range(20, 27):
    #     map_wall.wall[i][121] = -1
    #     map_wall.wall[i][122] = -1


def create_potential(map_wall, map_potential, map_potential_door):
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
    for now in map_wall.door:
        queue = []
        queue.append(now)
        map_potential_door[now[0]][now[1]] = 0
        while queue:
            now = queue.pop(0)
            for y, x in temp1:
                next = [now[0] + y, now[1] + x]
                if map_wall.wall[next[0]][next[1]] != 1 and map_potential_door[next[0]][next[1]] > \
                        map_potential_door[now[0]][
                            now[1]] + 1:
                    map_potential_door[next[0]][next[1]] = map_potential_door[now[0]][now[1]] + 1
                    queue.append(next)
            for y, x in temp2:
                next = [now[0] + y, now[1] + x]
                if map_wall.wall[next[0]][next[1]] != 1 and map_potential_door[next[0]][next[1]] > \
                        map_potential_door[now[0]][
                            now[1]] + 1.4:
                    map_potential_door[next[0]][next[1]] = map_potential_door[now[0]][now[1]] + 1.4
                    queue.append(next)


def update_all(map_wall, people, map_people, map_potential, map_count, count_step, map_potential_door):
    temp = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
    global p
    for man in people:
        if man.foreign and count_step < 5:
            continue
        if man.team_member:
            avg_x = 0
            avg_y = 0
            for item in man.team_member:
                avg_x += item.x
                avg_y += item.y
            avg_x /= len(man.team_member)
            avg_y /= len(man.team_member)
            dis = abs(man.x - avg_x) + abs(man.y - avg_y)
            man.max_speed = 1.32 * math.exp(-dis) + 1.32
        if man.disable == 2:
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

            if map_potential_door[y][x] < 10:
                while True:
                    i = random.randint(0, len(temp) - 1)
                    temp_y, temp_x = temp[i]
                    if map_potential_door[y + temp_y][x + temp_x] < map_potential_door[y][x]:
                        min_y = temp_y
                        min_x = temp_x
                        break
            else:
                while True:
                    i = random.randint(0, len(temp) - 1)
                    temp_y, temp_x = temp[i]
                    if map_potential_door[y + temp_y * 2][x + temp_x * 2] < map_potential_door[y][x]:
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
                man.speed[0] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_down - 1 / 5.4))) * c
                if avg_speed[1] > 0:
                    man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
                elif avg_speed[1] < 0:
                    man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
                else:
                    man.speed[1] = 0
            elif avg_speed[0] < 0:
                theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001)) + math.pi
                c = math.cos(theta)
                s = math.sin(theta)
                man.speed[0] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_up - 1 / 5.4))) * c
                if avg_speed[1] > 0:
                    man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
                elif avg_speed[1] < 0:
                    man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
            else:
                man.speed[0] = 0
                if avg_speed[1] > 0:
                    man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4)))
                elif avg_speed[1] < 0:
                    man.speed[1] = -man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4)))
                else:
                    man.speed[1] = 0
            man.speed[0] = max([-man.max_speed, min([man.speed[0], man.max_speed])])
            man.speed[1] = max([-man.max_speed, min([man.speed[1], man.max_speed])])
            continue
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
            man.speed[0] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_down - 1 / 5.4))) * c
            if avg_speed[1] > 0:
                man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
            elif avg_speed[1] < 0:
                man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
            else:
                man.speed[1] = 0
        elif avg_speed[0] < 0:
            theta = math.atan(avg_speed[1] / (avg_speed[0] + 0.0000001)) + math.pi
            c = math.cos(theta)
            s = math.sin(theta)
            man.speed[0] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_up - 1 / 5.4))) * c
            if avg_speed[1] > 0:
                man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4))) * s
            elif avg_speed[1] < 0:
                man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4))) * s
        else:
            man.speed[0] = 0
            if avg_speed[1] > 0:
                man.speed[1] = man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_right - 1 / 5.4)))
            elif avg_speed[1] < 0:
                man.speed[1] = -man.max_speed * (1 - math.exp(-p * (10 * 0.25 / count_left - 1 / 5.4)))
            else:
                man.speed[1] = 0
        man.speed[0] = max([-man.max_speed, min([man.speed[0], man.max_speed])])
        man.speed[1] = max([-man.max_speed, min([man.speed[1], man.max_speed])])

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


def show_all(screen, map_wall, map_people, map_potential, map_potential_door):
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
            # if map_potential_door[i][j] > 255:
            #     pygame.draw.rect(screen, (0, 0, 0), ((5 * j, 5 * i), (5, 5)))
            # else:
            #     pygame.draw.rect(screen, (
            #         (255 - map_potential_door[i][j]), (255 - map_potential_door[i][j]),
            #         (255 - map_potential_door[i][j])),
            #                      ((5 * j, 5 * i), (5, 5)))
            if map_people[i][j]:
                if map_people[i][j][0].foreign:
                    pygame.draw.circle(screen, (150, 0, 150), (5 * j + 3, 5 * i + 3), 2)
                elif map_people[i][j][0].disable:
                    pygame.draw.circle(screen, (0, 150, 0), (5 * j + 3, 5 * i + 3), 2)
                elif map_people[i][j][0].team_member:
                    pygame.draw.circle(screen, (150, 150, 0), (5 * j + 3, 5 * i + 3), 2)
                else:
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
    map_potential_door = [] * map_wall.len_y
    for i in range(map_wall.len_y):
        map_people.append([])
        for j in range(map_wall.len_x):
            map_people[i].append([])
        map_potential.append([1000] * map_wall.len_x)
        map_potential_door.append([1000] * map_wall.len_x)
        map_count.append([0] * map_wall.len_x)
    create_people(map_wall, people, map_people)
    create_potential(map_wall, map_potential, map_potential_door)
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
    # file = open('data.txt', 'w')
    count_step = 0
    while True:
        # print(len(people))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        if people:
            count_step += 1
            update_all(map_wall, people, map_people, map_potential, map_count, count_step, map_potential_door)
            show_all(screen, map_wall, map_people, map_potential, map_potential_door)
            # print(count_step, map_wall.count_door)
        else:
            show_count(screen, map_wall, map_count)
            # pygame.image.save(screen, 'pic3' + '.jpg')
            print(count_step)
            break
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
        # if count_step == 89:
        #     update_potential(map_wall, map_potential)

        # if len(people) < 100:
        #     for man in people:
        #         if man.disable:
        #             man.max_speed = 1.6
        # if count_step == 20:
        #     pygame.image.save(screen, 'pic1' + '.jpg')
        # if count_step == 90:
        #     pygame.image.save(screen, 'pic2' + '.jpg')
        # time.sleep(0.01)
    # print(count_step)


def no_gui():
    map_wall = Map()
    people = []
    map_people = [] * map_wall.len_y
    map_potential = [] * map_wall.len_y
    map_count = [] * map_wall.len_y
    map_potential_door = [] * map_wall.len_y
    for i in range(map_wall.len_y):
        map_people.append([])
        for j in range(map_wall.len_x):
            map_people[i].append([])
        map_potential.append([1000] * map_wall.len_x)
        map_potential_door.append([1000] * map_wall.len_x)
        map_count.append([0] * map_wall.len_x)
    create_people(map_wall, people, map_people)
    create_potential(map_wall, map_potential, map_potential_door)
    count_step = 0
    while True:
        if people:
            count_step += 1
            update_all(map_wall, people, map_people, map_potential, map_count, count_step, map_potential_door)
        else:
            print(count_step)
            break


for k in range(10, 31):
    p = k / 10
    gui()
