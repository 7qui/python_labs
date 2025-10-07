def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) <= 0:
        return ValueError
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = sorted(set(nums))
    return nums


def flatten(mat: list[list | tuple]) -> list:
    true_mat = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            print("TypeError")
            return
        for k in i:
            if isinstance(k, str):
                print("TypeError")
                return

    for i in range(len(mat)):
        for k in mat[i]:
            true_mat.append(k)
    return true_mat


print(flatten([
    [1, 2, 3],
    [],
    [4, 5]
]))