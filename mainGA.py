import random
import math
import helperGA
from helperGA import *

def do_GA(selection_func, fitness_func, crossover_func, mutation_func):

	pop_digit[]
	pop_letter[]
	fitness_array[]
	solution_fitness = None
	solution_digit = None
	solution_alpha = None
	
	for i in range (0,5):
		population = self.generate_population()
		pop_digit[i] = population
		population1 = self.generate_population1()
		pop_letter[i] = population1
		fitness_array[i] = fitness_function(pop_digit[i],pop_letter[i])
		
	wheel = makeWheel(population, population1, fitness_array)
		
	iteration = 20 #20 bar test korbo
    while(iteration>=0):
		iteration -=1
		#selecting digits combination
		selected_parents_digit[0], selected_parents_letter[0] = selection_function(wheel)
		selected_parents_digit[1], selected_parents_letter[1] = selection_function(wheel)
		selected_pop_digit_1 = selected_parents_digit[0]
		selected_pop_letter_1 = selected_parents_letter[0]
		selected_pop_digit_2 = selected_parents_digit[1]
		selected_pop_letter_2 = selected_parents_letter[1]
		
		
		#Calculate fitness of selected parents
		fitness_of_selected[0] = fitness_function(selected_pop_digit_1, selected_pop_letter_1)
		fitness_of_selected[1] = fitness_function(selected_pop_digit_2, selected_pop_letter_2)
		
		#Crossover for the numbers
		child_digit = OX1_crossover(selected_parents_digit[0], selected_parents_digit[1])
		#Scramble the alphas
		child_alpha = shuffle_function(selected_pop_letter_1)
		#Mutation
		child_digit = swap_mutation(child_digit)
		child_alpha = swap_mutation(child_alpha)
		#Calculate fitness of child
		fitness_of_child = fitness_function(child_digit, child_alpha)
		
		min_value = min(fitness_array)
		for i in range (0,5):
			if fitness_array[i] == min_value:
				if fitness_of_child > fitness_array[i]:
					fitness_array[i] = fitness_of_child
					pop_digit[i] = child_digit
					pop_letter[i] = child_alpha
	
	
	max_value = max(fitness_array)
	for i in range (0,5):
		if fitness_array[i] == max_value:
			solution_fitness = fitness_array[i]
			solution_digit = pop_digit[i]
			solution_alpha = pop_letter[i]
			
	return solution_digit, solution_alpha, solution_fitness
				
		
if __name__ == "__main__":
    random.seed()
    print("Solving 4 queen 4 rook problem")
    solution_digit, solution_alpha, solution_fitness = do_GA(selection_func = select_from_wheel, 
															fitness_func = fitness_function,
															crossover_func = OX1_crossover,
															mutation_func = swap_mutation)
    print("Solution using Genetic Algortihm")
    helperGA.printBoard(solution_digit, solution_alpha)
    print("Fitness is ",solution_fitness)
				
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		