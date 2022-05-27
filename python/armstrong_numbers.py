# How can you make this more scalable and reusable later?
import math

def find_armstrong_numbers(numbers):
    result = [];
    for number in numbers:
        expo = len(str(number))
        test_num = [int(n) for n in str(number)]
        sum = math.floor(math.fsum(n**expo for n in test_num))
        if sum == number:
            result.append(sum)
    return result

#print(find_armstrong_numbers(list(range(0,15))))
