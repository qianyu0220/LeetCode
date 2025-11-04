class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window_sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        if self.size == len(self.queue):
            self.window_sum -= self.queue.popleft()
        self.queue.append(val)
        self.window_sum += val
        return self.window_sum / len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)