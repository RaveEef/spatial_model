import os
from Population import Population
import math


class Process(object):

    def __init__(self, update_rate, initial_density, no_initial_pop, no_iterations, field_size, center_field_size,
                 interaction_r, dispersal_r, density_r):

        # all lists I need
        self.__the_selected = []            # (int)
        self.__the_cells_to_add = []        # (Cell)
        self.__the_cells_to_delete = []     # (int)

        '''Used when treatment is applied, totalCellsStd should store the saturated number of all cancer cell, 
        and it is the standard to decide when to stop/continue the treatment'''
        self.__total_cells_std = 0.0

        self.__growth_rate_for_selfish = 0.0
        self.__growth_rate_for_cooperative = 0.0
        self.__growth_rate_for_tkiller = 0.0

        self.__proliferation_probabilities = [0.0, 0.0, 0.0]
        self.__initial_density = initial_density
        self.__no_of_initial_pop = no_initial_pop
        self.__no_of_iterations = no_iterations

        self.__update_rate = update_rate

        self.__field_size = field_size           # (double)
        self.__center_field_size = center_field_size     # Put the initial cells in the center (double)
        self.__interaction_radius = interaction_r     # (double)
        self.__dispersal_radius = dispersal_r     # (double)
        self.__density_radius = density_r       # (double)

        pop = Population(self)

    @property
    def initial_density(self):
        return self.__initial_density

    @property
    def no_of_initial_pop(self):
        return self.__no_of_initial_pop

    @property
    def field_size(self):
        return self.__field_size

    @property
    def center_field_size(self):
        return self.__center_field_size
