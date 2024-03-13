import time
from collections import defaultdict, deque

from collections import defaultdict


class Box:
    def __init__(self):
        self.idx = -1
        self.weight = -1
        self.belt_num = -1

        self.prev = None
        self.next = None

class Belt:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, box):
        if self.head is None:
            self.head = box
            self.tail = box
        else:
            self.tail.next = box
            box.prev = self.tail
            self.tail = box
            box.next = None

    def extend(self, belt):
        if self.head is None:
            self.head = belt.head
            self.tail = belt.tail
        else:
            self.tail.next = belt.head
            belt.head.prev = self.tail
            self.tail = belt.tail

        belt.head = None
        belt.tail = None

    def popleft(self):
        if self.head is None:
            return None
        else:
            box = self.head
            self.head = box.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            return box

    def remove(self, box):
        if box.prev is None:
            self.head = box.next
        else:
            box.prev.next = box.next
        if box.next is None:
            self.tail = box.prev
        else:
            box.next.prev = box.prev

    def rotate(self, box):
        if box.prev is None:
            return
        else:
            self.tail.next = self.head
            self.head.prev = self.tail
            self.head = box
            self.tail = box.prev
            box.prev = None
            self.tail.next = None


boxes = [Box() for _ in range(100000)]
belts = [Belt() for _ in range(10)]
broken_belts = [False] * 10
idx2box = defaultdict(lambda: -1)

n = -1
m = -1

q = int(input())

for _ in range(q):
    # 100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
    order = list(map(int, input().split()))

    if order[0] == 100:
        n, m = order[1], order[2]
        devided = n // m

        for i in range(n):
            belt_num = int(i / devided)
            boxes[i].idx = order[3 + i]
            boxes[i].weight = order[3 + i + n]
            boxes[i].belt_num = belt_num
            belts[belt_num].append(boxes[i])
            idx2box[order[3 + i]] = boxes[i]

    elif order[0] == 200:
        w_max = order[1]
        w_sum = 0

        for belt in belts:
            if belt.head is not None:
                box = belt.popleft()
                if box.weight <= w_max:
                    w_sum += box.weight
                    idx2box[box.idx] = -1
                else:
                    belt.append(box)

        print(w_sum)

    elif order[0] == 300:
        idx = order[1]
        box = idx2box[idx]
        if box == -1:
            print(-1)
        else:
            belt = belts[box.belt_num]
            belt.remove(box)
            idx2box[idx] = -1
            print(idx)

    elif order[0] == 400:
        idx = order[1]
        box = idx2box[idx]
        if box == -1:
            print(-1)
        else:
            belt = belts[box.belt_num]
            belt.rotate(box)
            print(box.belt_num + 1)
    else:
        b_num = order[1] - 1

        if broken_belts[b_num]:
            print(-1)
        else:
            broken_belts[b_num] = True

            for i in range(b_num + 1, m + b_num):
                sel_num = i % m
                if not broken_belts[sel_num]:
                    box = belts[b_num].head
                    while box:
                        box.belt_num = sel_num
                        box = box.next
                    belts[sel_num].extend(belts[b_num])
                    print(b_num + 1)
                    break

belts = [deque() for _ in range(10)]
broken_belts = [False] * 10
idx2box = defaultdict(lambda: -1)

n = -1
m = -1

q = int(input())

for _ in range(q):
    start = time.time()
    order = list(map(int, input().split()))

    if order[0] == 100:
        # 100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
        n, m = order[1], order[2]
        devided = n // m

        for i in range(n):
            belt_num = int(i / devided)
            box = [order[3 + i], order[3 + i + n], belt_num] # idx, weight, belt_num
            belts[belt_num].append(box)
            idx2box[order[3 + i]] = box

    elif order[0] == 200:
        w_max = order[1]
        w_sum = 0

        for belt in belts:
            if belt:
                box = belt.popleft()
                if box[1] <= w_max:
                    w_sum += box[1]
                    idx2box[box[0]] = -1
                else:
                    belt.append(box)

        print(w_sum)

    elif order[0] == 300:
        idx = order[1]
        box = idx2box[idx]
        if box == -1:
            print(-1)
        else:
            belt = belts[box[2]]
            del belt[belt.index(box)]
            idx2box[idx] = -1
            print(idx)

    elif order[0] == 400:
        idx = order[1]
        box = idx2box[idx]
        if box == -1:
            print(-1)
        else:
            belt = belts[box[2]]
            belt.rotate(-belt.index(box))
            print(box[2] + 1)
    else:
        b_num = order[1] - 1

        if broken_belts[b_num]:
            print(-1)
        else:
            broken_belts[b_num] = True

            for i in range(b_num + 1, m + b_num):
                sel_num = i % m
                if not broken_belts[sel_num]:
                    for box in belts[b_num]:
                        box[2] = sel_num
                    belts[sel_num].extend(belts[b_num])
                    belts[b_num] = deque()
                    print(b_num + 1)
                    break
    print(order)
    print(time.time() - start)
    # for belt in belts:
    #     if belt:
    #         print([box[0] for box in belt])
    #         print([box[1] for box in belt])
    # print()