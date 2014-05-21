'''

This program determines the difference between (the sum of (each number between one and one hundred, squared)) and (the square product of (the sum of each number between one and one hundred)).

This seems like a nearly useless mathematical question, so I just made it a little script. Would be interested in knowing if problem 6 had any interesting applications I missed.

"The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."


'''

sum_of_the_squares = 0

for each in range (1, 101):

	sum_of_the_squares = sum_of_the_squares + (each * each)


    
the_bases_sum = 0

for each in range(1, 101):
        
    the_bases_sum += each
        
square_of_the_sum = the_bases_sum * the_bases_sum


difference_between_the_sum_of_the_squares_and_the_square_of_the_sum = (square_of_the_sum - sum_of_the_squares)

print(difference_between_the_sum_of_the_squares_and_the_square_of_the_sum)



the_end = input("\n\nPress enter to end program . . .\n> ")
