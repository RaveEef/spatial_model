import os
import math

# System Configurations

order = 19  # To choose one a-f order from 1-22 orderings (int)

fieldSize = 50  # The entire field is [0,50) x [0,50) (double)
noOfIterations = 300  # The no. of generations, and at one generation all cells are checked. (int)
noOfInitialPop = 100  # The no. of initial cells	(int)
initialDensity = [0.33, 0.33, 0.33]  # Initially types have equal proportions (double[])

'''At each generation, you check each individual cell from the population by 
generating a random value from [0,1), if the random value is less or equal to updateRate, then this 
cell is selected. (double) '''
updateRate = 1

centerFieldSize = 10  # Put the initial cells in the center (double)
interactionRadius = 1 # (double)
dispersalRadius = 1 # (double)
densityRadius = 1 # (double)
simul = True  # To do interaction simultaneously or not (boolean)

''' Where I save the generated file, such that I can plot the field in Matlab '''
savingPath = os.curdir  # (string)

'''If you run this in the server, the codes will automatically grab the 
working directory of the server. '''
runInServer = False #(boolean)

maxNoOfCellsPerUnitSqure = 10  # Density threshold per 1x1 area in field (int)

# Settings - death
ageControlOn = False  # Deterministic Death  (boolean)
deathRatio = 0.05  # Stochastic Death Rate (double)
ageLimit = 20 # (int)
deathPeriodLimit = 5  # This specifies how many generations a dead cells can stay in the field. (int)

# Setting - invasion cases
''' Invasion=0,1,2,3. 
 Invasion describes the case, when only two types are initially present in the field,
 and at a certain generation the third type is introduced into the field (we call invasion), and you will 
 see whether the third type can invade successfully or not. See different values of invasion:
 invasion = 0: no invasion happens during any generation, and the simulation starts with the initialDensity;
 invasion = i (for i = 1,2,3): at a certain generation type i starts to appear, by switching some of the dead 
 cells into type i. In this case, the simulation starts with a population consists of only two types, i.e., 
 type j!=i and type k!=i (for j,k=1,2,3). Besides, the frequency should be the two-type-equilibrium.'''
invasion = 0 # (int)

''' Number of zombies (the dead cells which are still staying in the field). This is used 
for the invasion case, when at a certain generation you turn/wake up e.g., 50 zombies into alive new cells of the 
invasive type'''
noZombies = 50 # (int)

'''This is to specify at which generation you wake up the zombies, if invasion = 1, 
we set the wakeupPoint = -100 as default value'''
wakeupPoint = 100 # (int)

# Setting - mutation
'''Mutation happens when cell reproduce, with prob. mutationRate, a cell type 
can mutate to one of the other two types, with equal probability, 0.5'''
mutationRate = 0 #(double)


class Process:

    def __init__(self):

        # all lists I need
        self.__the_selected = []            # (int)
        self.__the_cells_to_add = []        # (Cell)
        self.__the_cells_to_delete = []     # (int)

        self.__pop = None                   # Population

        '''Used when treatment is applied, totalCellsStd should store the saturated number of all cancer cell, 
        and it is the standard to decide when to stop/continue the treatment'''
        self.__total_cells_std = 0.0

        self.__growth_rate_for_selfish = 0.0
        self.__growth_rate_for_cooperative = 0.0
        self.__growth_rate_for_tkiller = 0.0

        self.__proliferation_probabilities = [0.0, 0.0, 0.0]
        self.__initial_density = [0.0, 0.0, 0.0]
        self.__no_of_initial_pop = 0
        self.__no_of_iterations = 0

        self.__update_rate = 1

        self.__field_size = 50.0            # (double)
        self.__center_field_size = 10.0     # Put the initial cells in the center (double)
        self.__interaction_radius = 1.0     # (double)
        self.__dispersal_radius = 1.0       # (double)
        self.__density_radius = 1.0         # (double)

    @property
    def initial_density(self):
        return self.initial_density

    @property
    def no_of_initial_pop(self):
        return self.no_of_initial_pop

    @property
    def field_size(self):
        return self.field_size

    @property
    def center_field_size(self):
        return self.center_field_size
