""" 
4 queen 4 rook problem 
with genetic algorithm 
ID: 15-01-04-063
"""
import random
import math
import re
from itertools import permutations

k_value_for_selection = 5
default_gene_size = 8
default_iteration = 20
default_population_size = 5
default_crossover_rate = 0.5
default_mutation_rate = 0.05
default_bit_generation_probability = [0.5]*default_gene_size


	
"""
Generate random combination of digits (12345678) for population
"""
def generate_population():
        #Generates a random combination of digits for GA
        population = []
        for i in range(population_size):
            combination = "12345678"
			# Get all permutations of string combination
            perms = permutations(combination)
			# Making the list of all permutations
            permList = list(perms)
			# generating a random index in [0,len(list)-1]
            idx = random.randint(0,len(permList))  
			#concataneting all the characters of new permutation  
            gene = ''.join(permList[idx])
            print(gene)
            population.append(gene)
        print(population)    
        return population
		
		
"""
Generate random combination of alphabets (qqqqrrrr) for population
"""
def generate_population1():
        #Generates a random combination of digits for GA
        population1 = []
        for i in range(population_size):
            combination1 = "qqqqrrrr"
			# Get all permutations of string combination
            perms1 = permutations(combination)
			# Making the list of all permutations
            permList1 = list(perms1)
			# generating a random index in [0,len(list)-1]
            idx1 = random.randint(0,len(permList1))  
			#concataneting all the characters of new permutation  
            gene1 = ''.join(permList1[idx1])
            print(gene1)
            population.append(gene1)
        print(population1)    
        return population1
	
#letters = generate_population1()



	
	
"""
SHUFFLE FUNCTION FOR THE ALPHABETIC PART
"""
def shuffle_function(combination_main):
    #Making temporary string
    combination = combination_main [:]
    #Generating random start and endpoints for shuffling
    i = random.randint(0,len(combination)-2)
    j = random.randint(i+1,len(combination)-1)

    list_combination = list(combination)
    #Shuffling in [i,j] interval
    shuffle_list = list_combination[i:j+1]
    random.shuffle(shuffle_list)
    list_combination[i:j+1] = shuffle_list
    combination = ''.join(list_combination)
    return combination
	
"""
FITNESS FUNCTION
"""
def fitness_function(digits, letters):
    """
	parameters:
	combination - solution string
	returns fitness of a solution string
	"""
    fitness = 28 #non-attacking pairs
    for i in range(0,7):
        for j in range(i+1,8):
            if re.match(r'q', letters[i]):
                if abs(i-j) == abs( int(digits[i])- int(digits[j])):
                    fitness -= 1 #one attacking pair found
    return fitness

	
""" 
MUTATION TECHNIQUE
"""
def swap_mutation(combination_main, mutation_rate):
    """
    parameters:
    combination_main -- input combination string (child)
    we select two positions on the chromosome at random, and interchange the values
	returns child gene value after swap mutation
    """
    combination = combination_main [:]
    #Generating random start and endpoints for shuffling
    i = random.randint(0,len(combination)-2)
    j = random.randint(i,len(combination)-1)
    #Swapping in [i,j] interval
    list_combination = list(combination)
	p = random.random()
	if p <= mutation_rate:
		list_combination[i],list_combination[j] = list_combination[j],list_combination[i]
    combination = ''.join(list_combination)
    return combination
	
"""
CROSSOVER TECHNIQUE
"""
def OX1_crossover(parent_1, parent_2)
	X = random.randint(0, len(parent_1)-2)
	# X is the leftmost index of the set
	Y = random.randint(X+1, len(parent_1)-1)
	# Y is the rightmost index of the set
	
	child_1 = []
	temp_p1 = []
	temp_p2 = []
	
	for i in range (0,8):
		copy_p1[i] = parent_1[i]
		copy_p2[i] = parent_2[i]
	
	#Copy the random swath of consecutive alleles from parent 1
	for i in range (X,Y):
		child_1[i] = parent_1[i]
		
	#Ignore the bits that are common in child1 and parent2, replace them with star symbol
	for i in range (0,8):
		for j in range (0,8):
			if copy_p2[i] == child_1[j]:
				copy_p2[i] = '*'
				
	#Fill position Y+1 to 8 of child_1, values coming from parent_2 (copy_p2)
	for i in range (Y+1, 8):
		j=i
		while copy_p2[j] == '*':
			j++ #keep incrementing j till we find a value in parent_2 
			if j>8: #if end of parent_2 string
				j=0 #start searching from beginning
		if copy_p2[j] != '*':
			child_1[i] = copy_p2[j]
			copy_p2[j] = '*'
			
	
	#Fill position 0 to X-1 of child_1, values coming from parent_2 (copy_p2)
	for i in range (0, X-1):
		j=i
		while copy_p2[j] == '*':
			j++ #keep incrementing j till we find a value in parent_2 
		if copy_p2[j] != '*':
			child_1[i] = copy_p2[j]
			copy_p2[j] = '*'
	
	#For child 2
			

""" 
SELECTION TECHNIQUE
"""	

def makeWheel(population, population1, fitness_func):
    """
    returns a list which will work as the "roulette wheel" in stochastic universal sampling. 
	Each element contains the start and end of the fitness-probability interval and the individual associated with it  
    parameters: 
    population- list of digit combination
	population1- list of letters combination
    fitness- fitness function passed as parameters 
    """
	#wheel stores digit, letter and the fitness associated with each combination
	wheel = []#Dimention 5x4
	start[]
	end[]
	#Filling the wheel with empty string
    for i in range(0,5):
        wheel.append([])
        for j in range(0,4):
            wheel[i].append("")
	
	#Calculate sun of fitnesses
	for i in range (0,5):
		fitness[i] = fitness_func(population[i], population1[i])
		total += fitness[i]
	
	p[0] = 0
	for i in range (1,6):
		p[i] = (fitness[i-1]/total)*100
		
	end[0] = 0
	for i in range (1,6):
		end[i] = end[i-1] + p[i]
		start[i] = end[i-1]
		
	
	for i in range (1,6):
		#for j in range (0,3):
			wheel[i-1][0] = population[i-1]
			wheel[i-1][1] = population1[i-1]
			wheel[i-1][2] = start[i]
			wheel[i-1][4] = end[i]
			
	
	return wheel
	
	
	
def select_from_wheel(wheel):
	"""
	parameters:
	wheel- wheel built in makeWheel function
	Returns digits and letters
	The individual for which r exceeds  is the chosen individual.
	"""
	r = random.randint(0,100)
	for i in range (0,5):
		if r > wheel[i][3]:
			if r <= wheel[i][4]:
				digits = wheel[i][0]
				letters = wheel[i][1]
	return digits, letters
	
	




	

		
"""
Function for printing the solution
"""		
def printBoard(combination, letters):
    #board to be print, dimension 8X8
    board_array = []
    #Filling the board with *
    for i in range(0,8):
        board_array.append([])
        for j in range(0,8):
            board_array[i].append("*")
			
    #Placing queens and rooks in the board based on input combination
    for i in range(len(combination)):
        board_array[i][int(combination[i])-1] = letters[i]
    for i in range(0,8):
        print(board_array[i])



    
   
			
		
	
	

	



	

	


