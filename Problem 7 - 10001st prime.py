'''

My first attempt, with no outside input while writing it, is commented in double quotes below.
The second attempt further down was informed by my finding a faster prime finder. It is both faster and nicer-looking and is the one to use when checking the result.

'''


"""

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
        

        
def generate_ascending_primes_up_to_the_thisth_prime_in_sequence(limiting_ordinal):
    
    
    number_to_be_checked = 2 # the first prime
    
    number_of_primes_found = 0
    
    while number_of_primes_found < int(limiting_ordinal):
        
        if is_prime(number_to_be_checked):
            
            number_of_primes_found += 1
            
            yield number_of_primes_found, number_to_be_checked
            
        number_to_be_checked += 1
        
        
        
        
for what_is_its_ordinal, what_is_the_prime in generate_ascending_primes_up_to_the_thisth_prime_in_sequence(10001):  
        
    print("%r: %r" % (what_is_its_ordinal, what_is_the_prime))

"""



## Below is the part that works more efficiently/looks nicer.


def generate_primes():

    ''' Yield primes from 2 to infinity. '''

    ## Copied from Jiva's example on Project Euler, who probably got it from someone else in a long chain leading back to some ancient Greek.
    
    ## The dividend of the algorithm is also the prime in question, determined when it passes the divisor without being cleanly divisible by anything.
    ## Initialize the generator by skipping 2, the first prime...
    the_dividend_minder = 3
    
    ## ... and yielding it manually. This is to keep us from having to increment by anything other than 2 (to skip even numbers).
    yield 2
    
    ## Runs forever. Include a limiter when calling this generator.
    while True:
        
        the_divisor_minder = 2
        
        while the_divisor_minder <= (the_dividend_minder / the_divisor_minder):
            
            if (the_dividend_minder % the_divisor_minder) == 0:

                break

            if the_divisor_minder == 2:
                
                the_divisor_minder += 1
                
            else:
                
                the_divisor_minder += 2

                
        if the_divisor_minder > (the_dividend_minder / the_divisor_minder):
            
            yield the_dividend_minder

        the_dividend_minder += 1


def print_all_primes_to_this_ordinal(the_limiting_ordinal):
    
    the_current_ordinal = 0
    
    the_prime_generator = generate_primes()
    
    while the_current_ordinal < the_limiting_ordinal:
        
        the_next_prime = next(the_prime_generator)
        
        the_current_ordinal += 1
        
        print("%r: %r" % (the_current_ordinal, the_next_prime))
    
    
    
   
while True:
    try:
        
        user_inputted_ordinal = int(input("\n\nEnter a number to calculate a series up primes up to that ordinal: "))
        
        print("\n")
        
        print_all_primes_to_this_ordinal(user_inputted_ordinal)    
    
    except:
    
        print("\nPlease enter a positive integer.")
    
    
## IDLE-friendliness.
the_end = input("\n\nPress enter to end program . . .\n> ")
