from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    maxScore = 0
    for x, y in scores:
        if y > maxScore:
            maxScore = y
            best = x
    return best


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
