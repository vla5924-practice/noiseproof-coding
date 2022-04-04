"""
Формулировка задания:
Линейный код задается с помощью порождающей матрицы {G}. Найдите кодовое слово, соответствующее информационной последовательности {inf}.
"""


from utils import xor


def solve(G, inf):
    res = ''.zfill(len(G[0]))
    for i, j in zip(G, inf):
        if j == '1':
            res = xor(res, i)
    return res


if __name__ == "__main__":
    G = ['101011', '011101', '011010']
    inf = '111'

    print(solve(G, inf))
