class RingBuffer:
    def __init__(self, capacity = 3):
        self.capacity = capacity
        self.size = 0
        self.first_value = 0
        self.data = []

    def append(self, value):
        if self.size >= self.capacity:
            self.data[self.first_value] = value
        else:
            self.data.append(value)
            self.size += 1

        if self.first_value < (self.capacity -1):
            self.first_value += 1
        else:
            self.first_value = 0

    def get(self):
        return self.data