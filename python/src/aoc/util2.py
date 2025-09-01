from typing import *
from pathlib import Path


def split_input(fname: str, type: Type = str) -> Tuple[Type]:
    """Split the input into a tuple of typed variables

    :param type: Type to convert the variables to
    :return: Tuple of variables from the input
    """
    with open(fname, 'r') as file:
        lines = file.readlines()
        return tuple(x for x in map(type, lines))

def list_input(fname: str, *types) -> List[Type]:
    """Split the input into a list of typed variables

    :param type: Type to convert the variables to
    :return: Tuple of variables from the input
    """
    path = Path(__file__).parent / 'input' / fname
    print(path.absolute())
    with open(path, 'r') as file:
        lines = [line.strip() for line in file]
        
        def cast_all(*types, values: List[str]):
            if len(types) == 1:
                if len(values) == 1:
                    return types[0](values[0])
                
                return tuple(types[0](value) for value in values)
            
            return tuple(type(value) for type, value in zip(types, values))

        return list(cast_all(*types, values=x.split()) for x in lines)

