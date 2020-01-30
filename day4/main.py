"""
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
"""


# Could potentially be solved by logic, but we built computers

full_range = range(145852,616942+1)

filtered_range = []
for number in full_range:
    adj_digit_same = False
    decreasing_digits = True
    
    number_str = str(number)
    for digit_index, digit in enumerate(number_str):
        if digit_index != 0:    
            if digit == number_str[digit_index-1]:
                adj_digit_same = True
            if digit < number_str[digit_index-1]:
                decreasing_digits = False
        
    if adj_digit_same and decreasing_digits:
        filtered_range.append(number)
                
                
print('Number of potential candidates: ', len(filtered_range))
    

# Part 2
from itertools import groupby


filtered_range = []
for number in full_range:
    adj_digit_double = False
    decreasing_digits = True
    number_str = str(number)
    for digit_index, digit in enumerate(number_str):
        if digit_index != 0:
            if digit < number_str[digit_index-1]:
                decreasing_digits = False
    if 2 in [sum(1 for _ in group) for _, group in groupby(number_str)]:
        adj_digit_double= True
    
    if adj_digit_double and decreasing_digits:
        filtered_range.append(number)
                
print('Number of potential candidates: ', len(filtered_range))

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
from itertools import groupby
     

number = 123444
adj_digit_double = False
decreasing_digits = True


number_str = str(number)
for digit_index, digit in enumerate(number_str):
    if digit_index != 0:
        if digit < number_str[digit_index-1]:
            decreasing_digits = False

if 2 in [sum(1 for _ in group) for _, group in groupby(number_str)]:
    adj_digit_double= True


