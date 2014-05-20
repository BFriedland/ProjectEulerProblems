'''

This program will find and return the smallest positive number that is evenly divisible by all of the numbers from 1 to a user inputted positive integer.

I originally hardcoded 20 as the upper limit, but testing indicates that making the limit dependent on user-input is really cool and worth trying out, so I put it in for fun.

"2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

'''

import math

#### Classes ####


class BoxThatContainsARangeDivisibilityFigurerOuterGenerator:

    ''' Create a box within which there exists an engine for figuring out if a number is divisible by every number in a range. '''

    def __init__(self):
    
        ## This entire class exists to save the following variable as state for the method self.figure_out_if_this_number_is_divisible_by_all_numbers_in_this_range()
        self.highest_failure_maker_so_far = 0

    def figure_out_if_this_number_is_divisible_by_all_numbers_in_this_range(self, what_number, range_start, range_end):

        ## Made this a separate function to cleanly allow return to break it early in the overwhelming majority of cases.

        for each_number in range(range_start, (range_end + 1)):
                
            if what_number % each_number != 0:
                
                
                if each_number > self.highest_failure_maker_so_far:
                
                    self.highest_failure_maker_so_far = each_number
                             
                    print("  %r was failed by a new record! ---> %r" % (what_number, each_number))
                    
                else:
                
                    print("  %r was failed by: %r" % (what_number, each_number))
 


                return False                      

                
        return True
             
             
    def find_product_of_all_primes_in_this_range(self, range_start, range_end):
        
        ''' Return the product of all primes from range_start to range_end (inclusive). '''
        
        ## This function is useful for making the step size of the divisibility checker bigger without making it surpass the smallest number evenly divisible by all numbers in the target range.
        ## Primes cover this handily.
        
        the_prime_product = 1 # One is totally prime! Right? I don't remember, actually. Good thing it doesn't matter for this purpose, since we just need to init the variable. (( ONE IS NOT PRIME. ))
        
        for each_number in range(range_start, (range_end + 1)):
        
            if is_prime(each_number):
        
                the_prime_product *= each_number

            ## The following very long comment block is included to demonstrate my thought processes while trying to make this more efficient.
         
            ## ...
            ## I guess I need a more efficient algorithm if the following line of code is so helpful?
            ## It turns out that not including the following line can make the run time longer if you have the program set to report "failures" in the function figure_out_if_this_number_is_divisible_by_all_numbers_in_this_range().
            ## Fortunately it is still pretty speedy, even with it commented.
            ## Try uncommenting it to see how many modulo failure reports it skips! (( Using both 3 and 16 skips all of them for Euler 5. ))
            #the_prime_product *= 3 * 16
            ## The reason for that line was that it guaranteed the resulting number was a multiple of 3 and 16.
            ## This is handy because 3 is a prime and also catches things like 9 and 18, and 16 covers non-prime multiples of 4 and 8.
            ## I discovered the utility of including this while watching the algorithm "fail" consistently on certain numbers that were multiples of lowbie primes.
            ## Reasonably, multiplying the product by the least number that "covers" those failures would keep the thing we're checking under the upper bound we care about, while greatly reducing the number of failures the program wastes time on.
            ## Or something like that. I don't know anyone who cares enough about Project Euler problems to be able to explain this any better. For now.
        
            ## Incidentally, you could also have the user enter in numbers based on that sort of guesswork every time they see a failure stream... though this is obviously missing the mathematical point.

            ## There has got to be some sort of algorithm for doing this automatically.
            ## I played with it for an hour or two and decided to think on it since all my attempts kept making the result too large rather than increasing the step size properly.
            
            ## ...
            ## and then I realized the highest failure makers' highest discovered values were almost exclusively squares...
        
            #the_prime_product *= 3 * 4 # for 20
            #the_prime_product *= 3 * 4 * 5 # for 25
        
            ## The answer is, figure out the highest square equal to or lesser than range_end, and multiply the_prime_product by the root of that number.
            ## ...
            ## Including this in the algorithm allows for impressively enormous number ranges to be crunched very, very fast. Try 10000!
        
            ## Woo we're still in the looooooop
            elif is_prime(each_number) == False:
                
                ## If the square root of the non-prime number is an integer...
                if ((math.sqrt(each_number) % 1) == 0):
                    
                    ## Then multiply the_prime_product by that integer:
                    the_prime_product *= int(math.sqrt(each_number))
                    
            ## It very often, but not always, returns the goal immediately and accurately.
            ## User inputs of 8 and 9 got the correct results of 840 and 2520 but both raised highest failures of 8, which is not a perfect square.
            ## I remember seeing very large numbers raise highest failures of 27, so it's not an even number thing...
            ## There's some sort of extra divisibility intricacy going on in the mathematics behind it all that I'm not yet aware of. Intriguing!!
                    
            
        print("\nthe_prime_product == %r" % (the_prime_product))
           
        
        return the_prime_product
                
       
    def generate_numbers_evenly_divisible_by_all_numbers_in_this_range(self, range_start, range_end):


        ## This function used to be a call to find_greatest_prime_in_this_range(), but then I realized I could whittle it down far more efficiently.

        the_step_size = self.find_product_of_all_primes_in_this_range(range_start, range_end)


        ## The answer shouldn't be two. Make the first check equal to the first step size.
        the_number_we_are_now_checking = the_step_size

        
        ## Prevents the generator from spamming you with the end result.
        keep_going = True
        
        
        
        while keep_going == True:
        
            is_the_number_we_are_now_checking_actually_divisible_by_all_of_this_range = self.figure_out_if_this_number_is_divisible_by_all_numbers_in_this_range(the_number_we_are_now_checking, range_start, range_end)
        
            if is_the_number_we_are_now_checking_actually_divisible_by_all_of_this_range == True:
            
                print("\n    Divisibility check was %r for %r.\n\nThis means %r is the smallest positive integer that is evenly divisible by all numbers from %r to %r.\n" % (is_the_number_we_are_now_checking_actually_divisible_by_all_of_this_range, the_number_we_are_now_checking, the_number_we_are_now_checking, range_start, range_end))
            
                keep_going = False
            
                yield the_number_we_are_now_checking, True
                
            else:
                
                yield the_number_we_are_now_checking, False
            
                ## It will only ever be a multiple of the highest prime, which is conveniently the lowest step size near the top of the range that makes any sense. (Or is it?!)
                the_number_we_are_now_checking += the_step_size                
                    
                
                
                
                
                
#### Top-Level Functions ####             
                
## If you have a better way to find primes, feel free to swap it in for is_prime()! Must return a boolean.

                
def is_prime(x):

    ''' Returns a boolean describing the primeness of the inputted number. '''

    ## 2 is the first prime.
    if (x == 2):
    
        return True   
        
    ## Non-integer numbers cannot be primes.
    if ((x % int(x)) != 0):
        
        return False
    
    
    ## Check for evenness. Wipes out half of all possible checks if no such check was used.
    ## ... 
    ## or maybe I should make a function based around upwards-iterating division?
    if (x % 2 != 0):
        ## Implicitly check for clean divisibility by 3, too.
        x_handler = ( (x // 3) + 1 ) #the +1 is because -1 is necessary for checking, see below
    
    ## otherwise it's even, and therefore not prime.
    else:
    
        return False


        
    if (x < 2):
    
        return False
        

        
    else:
    
        while (x_handler > 2):
        
            if ((x % (x_handler - 1)) == 0):
            
                return False    
                
            x_handler = (x_handler - 1)
            
            #print x_handler                  # DEBUGGING CODE -- Perfectly spammy on large numbers

        return True    

       
              
#### Execution ####            
            
            
## The program's welcome mat:
print("2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.")            
            
            
while True:     

    try:
        
        the_top_of_the_range = input("\n\nEnter a positive integer to find the smallest number that can be divided by each of the numbers from 1 to that positive integer without any remainder.\n> ")
        
        if int(the_top_of_the_range) <= 0:
        
            raise ValueError
        
        
        fresh_instance_of_the_box_that_contains_a_divisibility_generator = BoxThatContainsARangeDivisibilityFigurerOuterGenerator()
        the_divisibility_generator_inside_the_box = fresh_instance_of_the_box_that_contains_a_divisibility_generator.generate_numbers_evenly_divisible_by_all_numbers_in_this_range(1, int(the_top_of_the_range))
       
        
        for is_it_really_so_divisible, the_resulting_number in the_divisibility_generator_inside_the_box:
                
                
            if is_it_really_so_divisible == True:
            
                break
            
            elif is_it_really_so_divisible == False:
                
                ## Manual stepping for observation purposes:
                kek = input("        Press enter to step forwards.")
                
                ## pass allows you to comment the above line so you don't have to step through the program. Does not need to be commented in either case.
                pass
            
            
    except ValueError:
        
        print("\nPlease enter a positive integer.\n")

        
## IDLE-friendliness.
kek = input("\n\nPress enter to end program.\n> ")
        
        
