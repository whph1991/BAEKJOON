from collections import deque

box = [5, 6]
q = deque([[1, 2], [3, 4], box])

print(id(box))
idx = q.index(box)
del box
print(id(q[idx]))

q.rotate(-1)
print(q)