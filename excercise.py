# A program to find all numbers 
# divisible by 7 and
# not multiples of 5

# range : 2000 - 3200 inclusive


def find_num():
    nums = []
    init = 2000
    while init < 3201:
        if init%7 == 0 and not (init%5 == 0):
            nums.append(init)
        init += 1
        
    return nums

print(find_num())
    


