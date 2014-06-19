the_grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8 ], [ 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0 ], [ 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65 ], [ 52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91 ], [ 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80 ], [ 24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50 ], [ 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70 ], [ 67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21 ], [ 24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72 ], [ 21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95 ], [ 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92 ], [ 16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57 ], [ 86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58 ], [ 19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40 ], [ 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66 ], [ 88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69 ], [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36 ], [ 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16 ], [ 20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54 ], [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

for each_row in the_grid:
    print(str(each_row))



pattern_length = 4
grid_width = 20 # for convenience we will assume this program only needs to operate on perfectly square grids


## First, horizontals.

highest_horizontal_sum_of_all_time = 0
the_numbers_that_sum_to_the_highest_horizontal_sum_of_all_time = []

for each_row_index in range(0, len(the_grid)):

    for each_column_index in range(0, (len(the_grid[each_row_index]) - (pattern_length - 1))):
    
        the_running_sum = 0
        the_running_sum_constituents = []
        
        for each_next_column_index in range(0, pattern_length):
            

            the_running_sum += the_grid[each_row_index][(each_column_index + each_next_column_index)]
            the_running_sum_constituents.append(the_grid[each_row_index][(each_column_index + each_next_column_index)])
            
        if the_running_sum > highest_horizontal_sum_of_all_time:
        
            print("\nNew highest_horizontal_sum_of_all_time found at the_grid[%r][%r]" % (each_row_index, each_column_index))
            print("    %r" % (the_running_sum_constituents))
            
        
        
            highest_horizontal_sum_of_all_time = the_running_sum
            
            del the_numbers_that_sum_to_the_highest_horizontal_sum_of_all_time
            the_numbers_that_sum_to_the_highest_horizontal_sum_of_all_time = the_running_sum_constituents
            
        else:
        
            the_running_sum = 0
            del the_running_sum_constituents

            

## Second, verticals.

highest_vertical_sum_of_all_time = 0
the_numbers_that_sum_to_the_highest_vertical_sum_of_all_time = []

for each_row_index in range(0, (len(the_grid) - (pattern_length - 1))):

    for each_column_index in range(0, (len(the_grid[each_row_index]))):
    
        the_running_sum = 0
        the_running_sum_constituents = []
        
        for each_next_row_index in range(0, pattern_length):
   
            
            
            the_running_sum += the_grid[(each_row_index + each_next_row_index)][each_column_index]
            the_running_sum_constituents.append(the_grid[(each_row_index + each_next_row_index)][each_column_index])
            
            
        if the_running_sum > highest_vertical_sum_of_all_time:
        
        
            print("\nNew highest_vertical_sum_of_all_time found at the_grid[%r][%r]" % (each_row_index, each_column_index))
            print("    %r" % (the_running_sum_constituents))
        
            highest_vertical_sum_of_all_time = the_running_sum
            
            del the_numbers_that_sum_to_the_highest_vertical_sum_of_all_time
            the_numbers_that_sum_to_the_highest_vertical_sum_of_all_time = the_running_sum_constituents
            
        else:
        
            the_running_sum = 0
            del the_running_sum_constituents
            
            
            
## Now the right diagonals,

## Right diagonals require the most restricting range limitations of both verticals and horizontals.

highest_right_diagonal_sum_of_all_time = 0
the_numbers_that_sum_to_the_highest_right_diagonal_sum_of_all_time = []

for each_row_index in range(0, (len(the_grid) - (pattern_length - 1))):

    for each_column_index in range(0, (len(the_grid[each_row_index]) - (pattern_length - 1))):

        the_running_sum = 0
        the_running_sum_constituents = []
        
        
        ## Here is the principal difference between diagonals and sameagonals.
        ## each_next_diagonal_increment_index increases both the x and y offsets, because diagonal.
        for each_next_diagonal_increment_index in range(0, pattern_length):
          
            the_running_sum += the_grid[(each_row_index + each_next_diagonal_increment_index)][(each_column_index + each_next_diagonal_increment_index)]
            the_running_sum_constituents.append(the_grid[(each_row_index + each_next_diagonal_increment_index)][(each_column_index + each_next_diagonal_increment_index)])
            
            
        if the_running_sum > highest_right_diagonal_sum_of_all_time:
        
            print("\nNew highest_right_diagonal_sum_of_all_time found at the_grid[%r][%r]" % (each_row_index, each_column_index))
            print("    %r" % (the_running_sum_constituents))
  
        
            highest_right_diagonal_sum_of_all_time = the_running_sum
            
            del the_numbers_that_sum_to_the_highest_right_diagonal_sum_of_all_time
            the_numbers_that_sum_to_the_highest_right_diagonal_sum_of_all_time = the_running_sum_constituents
            
        else:
        
            the_running_sum = 0
            del the_running_sum_constituents            
        
        
        
## Now the left diagonals.

## Left diagonals are exactly like right diagonals, except that they start pattern_length to the right and apply their horizontal index offset subtractively.
## NOTE: Row indices must still be increased! These are downlefts, not uplefts.

highest_left_diagonal_sum_of_all_time = 0
the_numbers_that_sum_to_the_highest_left_diagonal_sum_of_all_time = []

for each_row_index in range(0, (len(the_grid) - (pattern_length - 1))):

    for each_column_index in range((pattern_length - 1), len(the_grid[each_row_index])):

        the_running_sum = 0
        the_running_sum_constituents = []
        
        
        ## Here is the principal difference between diagonals and sameagonals.
        ## each_next_diagonal_increment_index (de)creases both the x and y offsets, because (left) diagonal.
        for each_next_diagonal_increment_index in range(0, pattern_length):
          
            the_running_sum += the_grid[(each_row_index + each_next_diagonal_increment_index)][(each_column_index - each_next_diagonal_increment_index)]
            the_running_sum_constituents.append(the_grid[(each_row_index + each_next_diagonal_increment_index)][(each_column_index - each_next_diagonal_increment_index)])
            
            
        if the_running_sum > highest_left_diagonal_sum_of_all_time:
        
            print("\nNew highest_left_diagonal_sum_of_all_time found at the_grid[%r][%r]" % (each_row_index, each_column_index))
            print("    %r" % (the_running_sum_constituents))
  
        
            highest_left_diagonal_sum_of_all_time = the_running_sum
            
            del the_numbers_that_sum_to_the_highest_left_diagonal_sum_of_all_time
            the_numbers_that_sum_to_the_highest_left_diagonal_sum_of_all_time = the_running_sum_constituents
            
        else:
        
            the_running_sum = 0
            del the_running_sum_constituents            
        
        


            
            
   
            
            
            


print("\nthe_numbers_that_sum_to_the_highest_horizontal_sum_of_all_time --> %r" % (the_numbers_that_sum_to_the_highest_horizontal_sum_of_all_time))
print("highest_horizontal_sum_of_all_time --> %r" % (highest_horizontal_sum_of_all_time))
            
            
print("\nthe_numbers_that_sum_to_the_highest_vertical_sum_of_all_time --> %r" % (the_numbers_that_sum_to_the_highest_vertical_sum_of_all_time))
print("highest_vertical_sum_of_all_time --> %r" % (highest_vertical_sum_of_all_time))

            
print("\nthe_numbers_that_sum_to_the_highest_right_diagonal_sum_of_all_time --> %r" % (the_numbers_that_sum_to_the_highest_right_diagonal_sum_of_all_time))
print("highest_right_diagonal_sum_of_all_time --> %r" % (highest_right_diagonal_sum_of_all_time))

            
print("\nthe_numbers_that_sum_to_the_highest_left_diagonal_sum_of_all_time --> %r" % (the_numbers_that_sum_to_the_highest_left_diagonal_sum_of_all_time))
print("highest_left_diagonal_sum_of_all_time --> %r" % (highest_left_diagonal_sum_of_all_time))

highest_sum_in_any_direction = max(highest_horizontal_sum_of_all_time, highest_vertical_sum_of_all_time, highest_right_diagonal_sum_of_all_time, highest_left_diagonal_sum_of_all_time)

print("\n\nProject Euler highest sum in any direction --> %r" % (highest_sum_in_any_direction))


input("\n\nPress enter to end program . . . ")






