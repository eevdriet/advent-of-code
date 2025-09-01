from typing import List

def find_id(boarding_pass: str) -> int:
    def bin_search(partitions: str, lower_letter: chr) -> int:
        target = 2 ** len(partitions) - 1
        left, right = 0, target
        
        for letter in partitions:
            mid = left + (right - left) // 2

            if letter == lower_letter:
                right = mid
            else:
                left = mid + 1
                
        return left

    row = bin_search(boarding_pass[:7], 'F')
    col = bin_search(boarding_pass[7:], 'L')
    
    return 8 * row + col

def binary_boarding(boarding_passes: List[str]):
    return max(find_id(boarding_pass) for boarding_pass in boarding_passes)

def binary_boarding_2(boarding_passes: List[str]):
    ids = [find_id(boarding_pass) for boarding_pass in boarding_passes]
    ids.sort()
    
    for prev_id, next_id in zip(ids, ids[1:]):
        if next_id - prev_id == 2:
            return prev_id + 1
        
    return None

def main():
    boarding_passes = [line.strip() for line in open(0).readlines()]
    print(binary_boarding_2(boarding_passes))

if __name__ == '__main__':
    main()