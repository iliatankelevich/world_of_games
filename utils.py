from typing import TypeVar, List
from collections.abc import Callable

T = TypeVar('T')
runtime_type = T.__name__


def get_value_from_user(description: str, output_type: runtime_type, validator: Callable[[T], bool] = None) -> runtime_type:
    while True:
        print(description)
        input_str = input('')
        try:
            if output_type == str:
                if input_str.isnumeric():
                    raise ValueError('Invalid input type, must be a string')
                else:
                    return input_str
            input_casted = output_type(input_str)
        except ValueError:
            print(f'you must provide {output_type.__name__}')
            continue

        if validator:
            if validator(input_casted):
                return input_casted
        else:
            return input_casted

        print("not valid input")


def is_list_equal(list1: List[int], list2: List[int]) -> bool:
    for element in list1:
        if element not in list2:
            return False
    for element in list2:
        if element not in list1:
            return False
    return True
