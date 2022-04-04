"""
Формулировка задания:
Вычислить синдром ошибки переданного сообщения {code}, если известна проверочная матрица линейного кода {H}.
"""


from utils import syndrom


def solve(H, code):
    return syndrom(code, H)


if __name__ == "__main__":
    H = ['0111100', '1011010', '1101001']
    code = '1000110'

    print(solve(H, code))
