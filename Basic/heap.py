import heapq


# order 1:오름차순, -1:내림차순
def heapsort(iterable, order: int):
    h = []
    result = []

    # push
    [heapq.heappush(h, order*val) for val in iterable]

    # pop
    while h:
        result.append(order*heapq.heappop(h))

    return result


iterable = [1, 3, 4, 5, 6, 2, 9, 7, 0, 8]
print(heapsort(iterable, 1))
print(heapsort(iterable, -1))