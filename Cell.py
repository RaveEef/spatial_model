class Cell:

    def __init__(self, x, y, z, state, type, death_period, age):

        self.__x = x
        self.__y = y
        self.__z = z
        self.__state = state
        self.__type = type
        self.__death_period = death_period
        self.__age = age

    @property
    def type(self):
        return self.__type

    @property
    def state(self):
        return self.__state

    @type.setter
    def type(self, t):
        self.type = t


    def is_alive(self):
        if self.state == 1:
            return True
        return False
