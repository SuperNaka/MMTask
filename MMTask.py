import numpy

class GridDimentions:
    '''
    Solves the task
    '''

    #stores how many times the targeted box was green
    target_green = 0

    def __init__ (self):
        '''
        Sets dimentions and creats grid, sets Gen0, 
        creates targets box in number of generations
        loops N Generations
        '''
        self.set_dimentions()
        self.set_gen_0()
        self.set_target_and_gens()
        self.go_to_gen_n()

    def set_dimentions (self):
        '''
        Sets dimentions and sets grid with 0s
        We surround the grid with a border of 0s to simplify the logic
        '''
        self.x, self.y = [int(x) for x in input().replace(" ", "").split(',')] 
        self.current_gen = numpy.zeros((self.y+2, self.x+2), dtype=numpy.intc) 

    def set_gen_0 (self):
        '''
        Sets Generation 0 from user input
        '''
        for j in range(0, self.y): 
            x_line = input()
            for i in range(0, self.x):
                self.current_gen[j+1][i+1] = x_line[i]

    def set_target_and_gens(self):
        '''
        Sets coordinates for targeted box and number of generations to calculate
        '''
        self.target_x, self.target_y, self.gens = [int(x) for x in input().replace(" ", "").split(',')]
        self.update_target_green()

    def get_next_gen(self):
        '''
        Calculates the next Generation following the rules from the task
        Loops through every box, sums all of the surrounding boxes and checks which rule applies
        '''
        next_gen = numpy.zeros((self.y+2, self.x+2), dtype=numpy.intc)

        for j in range(1, self.y+1):
            for i in range(1, self.x+1):
                #sum = sum of boxes around current box
                sum = self.current_gen[j-1][i-1]+self.current_gen[j-1][i]+self.current_gen[j-1][i+1]
                sum += self.current_gen[j][i-1] + self.current_gen[j][i+1]
                sum += self.current_gen[j+1][i-1]+self.current_gen[j+1][i]+self.current_gen[j+1][i+1]

                #check which rule applies and asign new value
                if sum == 3 or sum == 6 or (sum == 2 and self.current_gen[j][i] == 1):
                    next_gen[j][i] = 1
                else:
                    next_gen[j][i] = 0
                        
        return next_gen
    
    def go_to_gen_n(self):
        '''
        loops through N generations and checks the targeted box
        '''
        for _ in range(0, self.gens):
            self.current_gen = self.get_next_gen()
            self.update_target_green()

    def update_target_green(self):
        '''
        check if the targeted box is gren(1) and updates the value of target_green if yes
        '''
        if self.current_gen[self.target_y+1][self.target_x+1]:
            self.target_green += 1

    def get_target_green(self):
        '''
        ethod for returning target_green
        '''
        return self.target_green

grid = GridDimentions()

print(grid.get_target_green())