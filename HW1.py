class Iterator:
    def __init__(self, size):
        self.__x = 0
        self.__size = size
        self.__a = 0
        self.__b = 0
        self.__c = 1

    def __next__(self):
        self.__x += 1
        self.__a, self.__b, self.__d = self.__b, self.__c, self.__a + self.__b + self.__c
        self.__c = self.__d
        if self.__x > self.__size:
            raise StopIteration
        return self.__d


class IterationRange:
    def __init__(self, size):
        self.__size = size

    def __iter__(self):
        return Iterator(self.__size)


iteration = IterationRange(16)
for line in iteration:
    print(line)