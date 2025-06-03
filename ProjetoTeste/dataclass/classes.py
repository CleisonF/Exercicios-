class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[0] = value
        self._index += 1


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria')
    lista.append('João')
    print(lista._data)
    