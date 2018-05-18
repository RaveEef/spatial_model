from Cell import Cell
import math
import random

class Population:

    def __init__(self, cells=None, process=None):

        self.__cells = cells
        self.__process = process

        self.__no_type1 = math.floor(float(self.process.no_of_initial_pop) * self.process.initial_density[0])
        self.__no_type2 = math.floor(float(self.process.no_of_initial_pop) * self.process.initial_density[1])
        self.__no_type3 = math.floor(float(self.process.no_of_initial_pop) * self.process.initial_density[2])
        self.__total_no = self.no_type1 + self.no_type2 + self.no_type3

        self.__fix_initial_fields = False
        self.__points = []
        for i in range(self.total_no):
            self.__points.append([])

        center_min = (self.process.field_size - self.process.center_field_size)/2.0
        center_max = center_min + self.process.center_field_size
        x, y, z, cell_type = None, None, None, None

        for i in range(self.total_no):

            if i < self.no_type1:
                cell_type = 1
            elif i < (self.no_type1 + self.no_type2):
                cell_type = 2
            else:
                cell_type = 3

            if not self.fix_initial_fields:
                x = random.uniform(center_min, center_max)
                y = random.uniform(center_min, center_max)
                z = random.uniform(center_min, center_max)
            else:
                x = self.points[i][0]
                y = self.points[i][1]
                z = self.points[i][2]

            self.cells.append(Cell(x, y, z, 1, type, -1, -1))

    @property
    def cells(self):
        return self.cells

    @property
    def process(self):
        return self.process

    @property
    def no_type1(self):
        return self.no_type1

    @property
    def no_type2(self):
        return self.no_type2

    @property
    def no_type3(self):
        return self.no_type3

    @property
    def total_no(self):
        return self.total_no

    @property
    def fix_initial_fields(self):
        return self.fix_initial_fields

    @property
    def points(self):
        return self.points

    def count_density(self):
        density = [0, 0, 0]
        for cell in self.cells:
            density[cell.type - 1] += 1
        return density


