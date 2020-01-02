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


filtered_range = []
for number in full_range:
    adj_digit_same = False
    decreasing_digits = True
    number_str = str(number)
    for digit_index, digit in enumerate(number_str):
        if digit_index != 0: # Not first
            if digit_index+1 != len(number_str): # if not last
                if digit == number_str[digit_index-1] and digit != number_str[digit_index+1]: # If same as previous
                    adj_digit_same = True
            elif digit == number_str[digit_index-1] and digit != number_str[digit_index-2]:
                adj_digit_same = True
            
            if digit < number_str[digit_index-1]:
                decreasing_digits = False
        #print('now:', digit, 'adj_digit_same:', adj_digit_same)

    if adj_digit_same and decreasing_digits:
        filtered_range.append(number)
                
                
print('Number of potential candidates: ', len(filtered_range))

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            

number = 123444
adj_already = False
adj_digit_same = False
decreasing_digits = True


number_str = str(number)
for digit_index, digit in enumerate(number_str):
    if digit_index != 0:    
        if digit == number_str[digit_index-1] and adj_already == False:
            adj_digit_same = True
            adj_already = True
        else:
            adj_already = False
        if digit < number_str[digit_index-1]:
            decreasing_digits = False


