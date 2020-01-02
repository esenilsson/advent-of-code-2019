full_range = [111122, 123444, 112233]


filtered_range = []
for number in full_range:
    number_str = str(number)
    for digit_index, digit in enumerate(number_str):
        if digit_index != 0:
            if digit_index+1 != len(number_str): # if not last
                if digit == number_str[digit_index-1] and digit != number_str[digit_index+1]: # If same as previous
                    adj_digit_same = True
            elif digit == number_str[digit_index-1] and digit != number_str[digit_index-2]:
                adj_digit_same = True
            
            if digit < number_str[digit_index-1]:
                decreasing_digits = False
        print('now:', digit, 'adj_digit_same:', adj_digit_same)

    if adj_digit_same and decreasing_digits:
        filtered_range.append(number)
                


         

number = 155589
adj_digit_same = False
decreasing_digits = True

number_str = str(number)
for digit_index, digit in enumerate(number_str):
    if digit_index != 0:
        if digit_index+1 != len(number_str): # if not last
            if digit == number_str[digit_index-1] and digit != number_str[digit_index+1]: # If same as previous
                adj_digit_same = True
        elif digit == number_str[digit_index-1] and digit != number_str[digit_index-2]:
            adj_digit_same = True
        
        if digit < number_str[digit_index-1]:
            decreasing_digits = False
    print('now:', digit, 'adj_digit_same:', adj_digit_same)

if adj_digit_same and decreasing_digits:
    print('success')
    filtered_range.append(number)
                
                
print('Number of potential candidates: ', len(filtered_range))











number = 124558
lst = str(number)
any(i==j for i,j in zip(lst, lst[2:]))







number = 124558
adj_digit_same = False
decreasing_digits = True
consecutive_digits = 0

number_str = str(number)
for digit_index, digit in enumerate(number_str):
    print(consecutive_digits)
    if digit_index != 0:
        if digit == number_str[digit_index-1]:
            consecutive_digits+=1
        else:
            consecutive_digits=0
            
        if consecutive_digits == 1 and (digit != number_str[digit_index-1] or digit_index == len(number_str)):
            adj_digit_same = True
        
        if digit < number_str[digit_index-1]:
            decreasing_digits = False
    

    print('now:', digit, 'adj_digit_same:', adj_digit_same)

if adj_digit_same and decreasing_digits:
    print('success')
    filtered_range.append(number)
                
                
print('Number of potential candidates: ', len(filtered_range))




























