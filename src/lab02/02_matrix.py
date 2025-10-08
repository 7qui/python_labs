def transpose(mat: list[list[float | int]]) -> list[list]:
    result = []

    for i in range(len(mat) - 1):
        if len(mat[i]) < len(mat[i + 1]) or (len(mat[i]) > len(mat[i + 1])):
            print('ValueError')
            return

    for i in range(len(mat[0])):
        new_list = []
        for k in range(len(mat)):
            new_list.append(mat[k][i])
        result.append(new_list)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    sum_list = []

    for i in range(len(mat)):
        summ = 0
        for k in (mat[i]):
            summ += k
        sum_list.append(summ)
    return sum_list


def col_sums(mat: list[list[float | int]]) -> list[float]:
    sum_list = []

    for i in range(len(mat[0])):
        summ = 0
        for k in range(len(mat)):
            summ += mat[k][i]
        sum_list.append(summ)

    return sum_list


print(row_sums([[1, 2, 3], [4, 5, 6]]))