import time
import random


class Node:
    def __init__(self, x, y):
        self.pre = None
        self.x = x
        self.y = y


class Man:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.door = -1
        self.way = []

    def set_door(self, door):
        self.door = door


class Map:
    def __init__(self, floor):
        self.floor = floor
        self.len_x = 40
        self.len_y = 26
        self.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 2, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1]]


def show(M):
    for i in range(M.len_y):
        temp = ''
        for j in range(M.len_x):
            if M.map[i][j] == 1:
                temp += '# '
            elif M.map[i][j] == 0:
                temp += '  '
            elif M.map[i][j] == 2:
                temp += '& '
            else:
                temp += 'o '
        print(temp)
    print('\n')


def main():
    # create map
    M = Map(1)
    D = []
    for i in range(M.len_y):
        for j in range(M.len_x):
            if M.map[i][j] == 2:
                D.append([i, j])

    # create people
    people = []
    while len(people) < 200:
        x = random.randint(0, M.len_x - 1)
        y = random.randint(0, M.len_y - 1)
        if M.map[y][x] == 0:
            M.map[y][x] = 3
            man = Man(x, y, 1)
            people.append(man)

    # show
    show(M)

    # find best way for everyone
    for man in people:
        visit = []
        queue = []
        now = Node(man.x, man.y)
        queue.append(now)
        visit.append([now.y, now.x])
        while queue:
            now = queue.pop(0)
            if M.map[now.y][now.x] == 2:
                break
            if M.map[now.y][now.x + 1] != 1 and [now.y, now.x + 1] not in visit:
                next = Node(now.x + 1, now.y)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y][now.x - 1] != 1 and [now.y, now.x - 1] not in visit:
                next = Node(now.x - 1, now.y)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y + 1][now.x] != 1 and [now.y + 1, now.x] not in visit:
                next = Node(now.x, now.y + 1)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y - 1][now.x] != 1 and [now.y - 1, now.x] not in visit:
                next = Node(now.x, now.y - 1)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y + 1][now.x + 1] != 1 and [now.y + 1, now.x + 1] not in visit:
                next = Node(now.x + 1, now.y + 1)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y + 1][now.x - 1] != 1 and [now.y + 1, now.x - 1] not in visit:
                next = Node(now.x - 1, now.y + 1)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y - 1][now.x + 1] != 1 and [now.y - 1, now.x + 1] not in visit:
                next = Node(now.x + 1, now.y - 1)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
            if M.map[now.y - 1][now.x - 1] != 1 and [now.y - 1, now.x - 1] not in visit:
                next = Node(now.x - 1, now.y - 1)
                next.pre = now
                queue.append(next)
                visit.append([next.y, next.x])
        man.door = D.index([now.y, now.x])
        while now:
            man.way.append([now.y, now.x])
            now = now.pre
        man.way.reverse()
        man.way.pop(0)
        # print(man.door)
        # print(man.way)

    # people move
    count = 0
    while people:
        count += 1
        for man in people:
            if [man.y,man.x] == D[man.door]:
                people.pop(people.index(man))
                continue
            next = man.way[0]
            if M.map[next[0]][next[1]] == 0:
                man.way.pop(0)
                M.map[man.y][man.x] = 0
                man.y = next[0]
                man.x = next[1]
                M.map[man.y][man.x] = 3
            elif M.map[next[0]][next[1]] == 2:
                man.way.pop(0)
                M.map[man.y][man.x] = 0
                man.y = next[0]
                man.x = next[1]
        show(M)
        input()
    print(count)


print(0 % 10)