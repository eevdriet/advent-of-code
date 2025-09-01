from typing import List
import re


def passport_processing(passports: List[dict]) -> int:
    required_fields = [
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    ]
    
    def is_valid(passport: dict) -> bool:
        return all(field in passport for field in required_fields)
    
    return sum(is_valid(passport) for passport in passports)
    
def passport_processing_2(passports: List[dict]) -> int:
    def validate_height(height_str: str) -> bool:
        if not (match := re.match(r'(\d{2,3})(cm|in)', height_str)):
            return False
        
        height, type = match.groups()
        validators = {
            "cm": lambda height: 150 <= int(height) <= 193,
            "in": lambda height: 59 <= int(height) <= 76,
        }
        
        return validators[type](height)

    required_fields = {
        "hgt": validate_height,
        "byr": lambda year: 1920 <= int(year) <= 2002,
        "iyr": lambda year: 2010 <= int(year) <= 2020,
        "eyr": lambda year: 2020 <= int(year) <= 2030,
        "hcl": lambda color: re.match(r'^#[0-9a-f]{6}$', color),
        "ecl": lambda color: color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda year: re.match(r'^[0-9]{9}$', year)
    }
    
    def is_valid(passport: dict) -> bool:
        return all(field in passport and validator(passport[field]) for field, validator in required_fields.items())

    return sum(is_valid(passport) for passport in passports)

def main():
    passports = []

    for data in open(0).read().split('\n\n'):
        passport = {}

        for field in data.strip().split():
            key, val = field.split(':')
            passport[key] = val
            
        passports.append(passport)
        
    print(passport_processing_2(passports))


if __name__ == '__main__':
    main()