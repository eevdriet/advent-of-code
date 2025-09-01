from typing import List


def report_repair(numbers: List[int], target=2020):
    remainders = set()
    
    for number in numbers:
        remainder = target - number
        if remainder in remainders:
            return number * remainder
        
        remainders.add(number)
        
    return None

def report_repair_2(numbers: List[int], target=2020):
    numbers.sort()
    
    for idx, first in enumerate(numbers):
        if idx > 0 and first == numbers[idx - 1]:
            continue
        
        left, right = idx + 1, len(numbers) - 1
        while left < right:
            second, third = numbers[left], numbers[right]
            sum3 = first + second + third

            if sum3 == target:
                return first * second * third

            if sum3 > target:
                right -=1
            elif sum3 < target:
                left += 1
                    
    return None



def main():
    numbers = [int(line) for line in open(0).readlines()]
    print(report_repair_2(numbers))

if __name__ == '__main__':
    main()