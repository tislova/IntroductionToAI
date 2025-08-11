#Adeliya Tislova
#The program solves the tile sliding game using A* search
import heapq
from typing import List, Tuple

#The function returns a list of moves that will result in a final solution
def solveSlider(size:int,grid:List[int]) -> List[int]:

	#Heuristic function that uses Manhattan distance
	def h_function(next_node: Tuple[int]) -> int: #The tuple of the state of the board is passed
		total_distance = 0
		for i, tile_number in enumerate(next_node): #Iterate over each tile in the state
			if tile_number == 0: #If an empty tile is encounetred, pass
				continue
			#Calculate positions of the tile
			row = tile_number // size 
			column = tile_number % size
			current_row = i // size 
			current_column = i % size  
			#Use positions to find Manhattan distance and total estimated cost
			total_distance = total_distance + abs(row - current_row) + abs(column - current_column)
		return total_distance

	#The function finds new states when a new tile is moved; the tuple of the state of the board is passed
	def expand_states(current_state: Tuple[int]) -> List[Tuple[Tuple[int], int]]: #Returns a list of tuples that stores the next state and new index of the empty tile
		next_nodes = []
		empty_tile = current_state.index(0)
		for move in possible_moves:
			is_valid = move + empty_tile #New index of the empty tile
			if 0 <= is_valid <= size * size - 1: #Check the validity of the move(Tiles should stay within the grid)
				if abs(move) == 1 and (empty_tile // size != is_valid // size): #Check if a move is a horizontal one
					#If a row resulted from the move is different than it was before, continue to prevent an illegal move
					continue
				#Create an updated state by swapping tiles
				updated_state = list(current_state) 
				moved_tile = current_state[is_valid]
				updated_state[empty_tile], updated_state[is_valid] = updated_state[is_valid], updated_state[empty_tile]
				next_nodes.append((tuple(updated_state), moved_tile)) #Append a list of tuples that stores the next state and new index of the empty tile
		return next_nodes
	
	#Perform A* search
	goal_state = tuple(range(size * size)) #Goal state is a completed solution where all numbers are in inreasing order
	initial_state = tuple(grid) #Initial state of the board is passed as grid; I use tuples since they are faster to access than lists
	possible_moves = (1, -1, size, -size) #Possible moves include going right, left, down, and up
												 
	my_heap = [(h_function(initial_state), 0, [], initial_state)] #Create a min heap with f score, g score, path, and current state
	already_visited = set() #Create a set with already visited nodes to reduce time
	while my_heap:
		best_state = heapq.heappop(my_heap) #Pop a tuple from the heap with the best(lowest) f score
		#Extract values from the tuple
		g_score = best_state[1]
		path = best_state[2]
		current_state = best_state[3]
		if current_state in already_visited: #If a state that we are exploring has been already visited, continue search
			continue
		already_visited.add(current_state) #Add state into the set
		if goal_state == current_state:
			return path #If the goal state matches extracted state, return list of moves that will result in a final solution
		#Otherwise, explore more nodes
		for next_nodes, new_move in expand_states(current_state): #Iterate over all new states that we explored
			if next_nodes not in already_visited: #If the state is not explored, update path
				updated_path = path + [new_move]
				heapq.heappush(my_heap, (1 + g_score + h_function(next_nodes), 1 + g_score, updated_path, next_nodes)) #Add new state to the heap
	return [] #[] output shouldn't happen if the game is solvable