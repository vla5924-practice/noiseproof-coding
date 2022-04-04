"""
Формулировка задания:
Линейный код построен по матрице {matrix}. Определите, какие из следующих сообщений {codes} являются кодовыми, а какие содержат ошибку.
"""


from utils import code_from_basis


def solve(matrix, codes):
    res = []
    # possible_codes = code_from_basis(matrix)
    for i in codes:
        if i in code_from_basis(matrix):
            res.append('Correct')
        else:
            res.append('Error')
    return res


if __name__ == "__main__":
    matrix = ['1000111',
              '0100101',
              '0010011',
              '0001110']

    codes = ['1101100', '0110110', '1100111', '0011001', '0010011']

    print(solve(matrix, codes))
