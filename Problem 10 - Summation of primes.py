'''

This program takes a user inputted number and prints the sum of all of the primes beneath that number.

NOTE: The uncommented code is my attempt to tackle the problem with my own inefficient prime finder algorithm, which I made because I figured Project Euler problems weren't supposed to involve much mathematical research about the major element in each problem.
I now believe that to be a faulty assumption.
Project Euler problems are best approached as an opportunity to synthesize one's ability to research, comprehend and implement algorithmic solutions to mathematical questions at least as much as they are about answering the mathematical questions themselves.

Therefore, I have included my implementation of someone else's much faster prime finder, now that I know it even exists.
That code is uncommented because I don't want to waste anyone's time on first execution.

"The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."

ref: < https://projecteuler.net/problem=10 >

'''

'''
## This is the code I paraphrased. Yes, mine is longer, which I consider important for learning purposes.
## I think the credit goes to "jiva" from one of the Project Euler post-success forum responses. Or perhaps an ancient Greek philosopher or something, originally.
i=2
total=0
while i<2000000:
    j=2
    while j<=(i/j):
        if not (i%j):
            break;
        j+=1
    if j>(i/j):
        total+=i
    i+=1
print(total)
'''

## The time module is included for testing purposes and because it's fun to quantify the algorithms' efficiency.
import time


def quick_sum_all_primes_beneath_this_number(the_limiting_number):

    ''' Return the sum of all prime numbers from 2 to the supplied parameter. '''

    ## This algorithm finds primes by creating a division equation in which each part is separately incremented and checked for primeness according to rules which minimize the amount of time it needs to spend doing this.
    ## I'm pretty sure the way it works is: It increments the divisor until it passes some number related to the square root, checking for even divisibility along the way.
    ## If it passes these tests, the dividend becomes the new prime sensei, and is then incremented by two and sent on a quest to find its inner primeness or get incremented again in an epic story set in the Forever Plane of Mathematics that reflects on the impermanence of worldly things.
    ## Or that's what it seems like. If I should at some point need to know more about the perfect timeless Platonic Truth behind this prime finder, I'll break out the rubber ducky and let it tell me.
    
    ## Prep by skipping 2, the first prime. This fact is taken into account in several places.
    the_dividend_minder = 3
    the_sum_of_all_primes = 2

    while the_dividend_minder < the_limiting_number:
        
        the_divisor_minder = 2
        
        while the_divisor_minder <= (the_dividend_minder / the_divisor_minder):
            
            ## If the number is evenly divisible by something less than itself and greater than one it can't be prime.
            if (the_dividend_minder % the_divisor_minder) == 0:

                break

            if the_divisor_minder == 2:
                
                the_divisor_minder += 1
                
            else:
                
                the_divisor_minder += 2

                
        if the_divisor_minder > (the_dividend_minder / the_divisor_minder):
            
            the_sum_of_all_primes += the_dividend_minder

            
        ## Jiva's version increments the dividend by 1, but this is inefficient and unnecessary as it checks even numbers too.
        ## Starting from 3, each prime is necessarily some multiple of 2 higher than the last, because it has to skip actual multiples of 2.
        the_dividend_minder += 2
        
    return the_sum_of_all_primes

    
## Note: Execution block is below the commented code.

"""

## The old, slow code.    
    
import math

def is_this_number_divisible_by_anything_in_this_list(the_suspect, the_lineup):
 
    for each_convicted_prime in the_lineup:
        if ( (the_suspect % each_convicted_prime) == 0 ):
            return False
    return True


def sum_all_primes_beneath_this_number(the_limit):

    the_list_of_primes = [2]

    number_we_are_checking = 3
    
    the_sum_of_all_primes = 0
    
    
    while number_we_are_checking < the_limit:

        if is_this_number_divisible_by_anything_in_this_list(number_we_are_checking, the_list_of_primes) == True:
            the_list_of_primes.append(number_we_are_checking)
            
        ## Note that because we are finding all primes up to but not over this number, and that the while loop halts with less-than, this must come AFTER the appending logic.
        ## Ofc, += 2 because primes aren't even.
        number_we_are_checking += 2
    
    for each_prime in the_list_of_primes:
        the_sum_of_all_primes += each_prime
    
     
    return the_sum_of_all_primes

    
def is_prime(x):

    ''' Return a boolean reflecting the primeness of the supplied parameter. '''

    ## 2 is something of a special prime compared to the ordinary rules for determining the rest of them.
    ## Therefore it has a conditional reserved for itself.
    if (x == 2):
    
        return True

    ## Non-integer numbers (other than two) cannot be primes. Incidentally Project Euler sez 1 is not a prime in problem 10.
    if ((x % int(x)) != 0):
        
        return False
    
    
    ## Check for evenness. Wipes out half of all possible checks if no such check was used.
    ## ... 
    ## or maybe I should make a function based around upwards-iterating division?
    if (x % 2 != 0):
        ## Implicitly check for clean divisibility by 3, too.
        x_handler = ( (x // 3) + 1 ) # the +1 is because -1 is necessary for checking, see below
    
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
            
            
        return True        

        
        
def generate_ascending_primes_below_this_number(limiting_number):
    
    ''' Beginning from 2, yield each prime number beneath the supplied parameter. '''
    
    number_to_be_checked = 2 # the first prime
    
    while number_to_be_checked < int(limiting_number):
        
        if is_prime(number_to_be_checked):
            
            print(number_to_be_checked)
            
            yield number_to_be_checked
        
        if number_to_be_checked == 2:
            
            ## Primes go 2 3 5 7 11 13 17
            ## so return 2 first, then 3 with +1 increment...
            number_to_be_checked += 1
            
        else:
            
            ## then return 5 with +2 increment, etc to forever after skip even numbers.
            number_to_be_checked += 2
            
            
## End of old, slow code. ... Remember to swap the commenting in the try:except block below if you're testing it.         
            
"""

    
while True:

    try:
        
        the_input = int(input("\nEnter a number to sum all primes with values beneath it: "))
        
        ## NOTE: time.time() will round down to 0 for very short calculation times.
        ## For interesting results, I suggest checking 11111, then 22222, then 33333...
        starting_time = time.time()
        print("\n  Sum of all primes beneath %r: %r" % (the_input, quick_sum_all_primes_beneath_this_number(the_input)))
        ending_time = time.time()
        
        print("\n    Time taken: %r\n" % (ending_time - starting_time))
        
        ## These lines use my old, slow code.
        #starting_time = time.time()
        #print("\n  Sum of all primes beneath %r using the slow method: %r\n" % (the_input, sum_all_primes_beneath_this_number(the_input)))
        #ending_time = time.time()
        
        #print("\n    Time taken: %r\n" % (ending_time - starting_time))
        
        
    except ValueError:
        
        print("\nPlease enter a positive integer.")
