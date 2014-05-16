def find_all_numbers_divisible_by_these_numbers_in_this_range(*parameters, range_start, range_end):

    ''' Divides every number in a given range by every parameter given. If a modulo-zero match is found, adds the original number to the pile. '''

    
    
    sum_of_all_numbers_divisible_by_these_parameters = 0
    
    
    
    for each_number in range(int(range_start), int(range_end)):
        
        found_a_match = False
        
        for each_parameter in parameters:
        
            modulo_result = (each_number % each_parameter)
        
            if (modulo_result == 0) and (found_a_match == False):
                
                print("\n%r mod %r == %r" % (str(each_number), str(each_parameter), str(modulo_result)))
                print("  %r + %r == %r" % (str(sum_of_all_numbers_divisible_by_these_parameters), str(each_number), str(sum_of_all_numbers_divisible_by_these_parameters + each_number)))
                sum_of_all_numbers_divisible_by_these_parameters += each_number
                
                found_a_match = True
    
    
    
    return sum_of_all_numbers_divisible_by_these_parameters
    
    
    
the_results = find_all_numbers_divisible_by_these_numbers_in_this_range(3, 5, range_start=1, range_end=1000)


print(str(the_results))


kek = input("\n\n\nPress enter to end program . . .\n> ")
