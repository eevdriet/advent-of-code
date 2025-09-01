from typing import List


def custom_customs(groups: List[str]):
    count_sum = 0

    for group in groups:
        questions = set()
        
        for line in group.splitlines():
            questions.update(question for question in line)
            
        count_sum += len(questions)
        
    return count_sum

def custom_customs_2(groups: List[str]):
    count_sum = 0

    for group in groups:
        lines = group.splitlines()

        questions = set(lines[0])
        
        for line in lines[1:]:
            questions.intersection_update(question for question in line)
            
        count_sum += len(questions)
        
    return count_sum

def main():
    groups = open(0).read().split('\n\n')
    print(custom_customs_2(groups))

if __name__ == '__main__':
    main()