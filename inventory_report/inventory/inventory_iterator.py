from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data: list, current: int = 0):
        self.data = data
        self.current = current

    def get_index(self):
        return self.data[self.current]

    def __next__(self):
        curr = self.get_index()
        if not curr:
            raise StopIteration()
        self.current += 1
        return curr
