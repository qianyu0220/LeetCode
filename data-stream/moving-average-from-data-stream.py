class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        if self.size == len(self.queue):
            self.window_sum -= self.queue.popleft()

        self.window_sum += val
        self.queue.append(val)
        return self.window_sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)