import parse


def is_valid_1(low: int, high: int, char: chr, password: str) -> bool:
    return low <= password.count(char) <= high

def is_valid_2(low: int, high: int, char: chr, password: str) -> bool:
    has_low =  1 <= low <= len(password) and password[low - 1] == char
    has_high = 1 <= high <= len(password) and password[high - 1] == char

    return has_low ^ has_high

def main():
    count = 0

    for line in open(0).readlines():
        low, high, char, password = parse.parse("{:d}-{:d} {}: {}", line)
        count += is_valid_2(low, high, char, password)
        
    print(count)

if __name__ == '__main__':
    main()