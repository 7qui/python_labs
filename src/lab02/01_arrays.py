def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError(f"Элемент должен быть списком или кортежем, получен {type(item)}")
        result.extend(item)
    return result

print(min_max([3, 1, 2, 1, 3]))