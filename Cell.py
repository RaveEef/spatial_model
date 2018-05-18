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
        return self.type

    @type.setter
    def type(self, t):
        self.type = t

