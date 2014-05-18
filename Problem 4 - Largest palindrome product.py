'''

This prorgram determines the largest palindrome product under 1000.

It naively iterates upwards from a lower bound at 900.
It would have been faster to step backwards from 999*999, but this way you get to see a screen full of numbers scrolling really fast. Yeeeeah.

"A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."

'''

def determine_if_this_string_is_a_palindrome(inputted_string):

    ## If the string is even...
    if ( ( len(inputted_string) % 2 ) == 0 ):
    
        print("String is even number of digits.")
    
        ## For each digit in the first half of the string...
        for each_incrementing_digit_index in range(0, ( ( len(inputted_string) // 2 ) + 1 ) ):
            
            ## If the digit at this location is not the same as the corresponding digit the same number of indices back from the end...
            if inputted_string[each_incrementing_digit_index] != inputted_string[-(each_incrementing_digit_index + 1)]:
            
                print("    %r != %r" % (inputted_string[each_incrementing_digit_index], inputted_string[-(each_incrementing_digit_index + 1)]))

                return False
                
            else:
            
                print(" %r == %r" % (inputted_string[each_incrementing_digit_index], inputted_string[-(each_incrementing_digit_index + 1)]))
                

    
    ## If the string is odd...
    elif ( ( len(inputted_string) % 2 ) == 1 ):
    
        print("String is ODD number of digits!")    
        
        ## For each digit in the first half of the string...
        for each_incrementing_digit_index in range(0, ( ( len(inputted_string) // 2 ) ) ): # <--- no +1 for odd strings, round down instead and simply ignore the odd middle digit because palindrome.
            
            ## If the digit at this location is 
            if inputted_string[each_incrementing_digit_index] != inputted_string[-(each_incrementing_digit_index + 1)]:
                
                return False    
                
    ## If no False was returned, return True.         
    return True
                      

def get_largest_palindrome_product_under_one_thousand():


    largest_palindrome_yet_factor_alpha, largest_palindrome_yet_factor_beta, largest_palindrome_yet = 0, 0, 0

    for each_first_factor in range(900, 1000):
    
        for each_second_factor in range(900, 1000):
                
            product_of_the_two_factors = (each_first_factor * each_second_factor)
                
            print("%r * %r == %r" % (each_first_factor, each_second_factor, product_of_the_two_factors))
                
            if determine_if_this_string_is_a_palindrome( str(product_of_the_two_factors) ) == True:
                
                largest_palindrome_yet_factor_alpha, largest_palindrome_yet_factor_beta, largest_palindrome_yet = each_first_factor, each_first_factor, product_of_the_two_factors
                    
                print("    Palindrome found: %r" % (largest_palindrome_yet))
                    
                    
    return largest_palindrome_yet_factor_alpha, largest_palindrome_yet_factor_beta, largest_palindrome_yet
                    
                    
                    
                    
largest_palindrome_yet_factor_alpha, largest_palindrome_yet_factor_beta, the_largest_palindrome_product_for_two_numbers_under_one_thousand = get_largest_palindrome_product_under_one_thousand()                    
                    
                    
print("\nSuccess.\n    %r * %r == %r" % (largest_palindrome_yet_factor_alpha, largest_palindrome_yet_factor_beta, the_largest_palindrome_product_for_two_numbers_under_one_thousand))
                    
