class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if -1 < index < len(self.queue):
            return self.queue[index]
        else:
            raise IndexError
