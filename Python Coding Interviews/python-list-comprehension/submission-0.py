from typing import List


def create_list_of_odds(n: int) -> List[int]:
    odd_list = [i for i in range(1, n + 1,) if i % 2 == 1]
    return odd_list

# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
