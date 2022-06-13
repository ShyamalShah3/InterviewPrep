BLANK = object()


class HashTable:
    def __init__(self, size):
        self.__size = size
        self.values = size * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % self.__size
        self.values[index] = value

    def __getitem__(self, item):
        index = hash(item) % self.__size
        value = self.values[index]
        if value is BLANK:
            raise KeyError(item)
        return value

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        else:
            return True
