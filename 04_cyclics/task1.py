"""
Формулировка задания:
Дан циклический ({code_n}, {code_k})-код с порождающим многочленом в векторной форме {code_poly}.
Определите кодирование двоичной последовательности {message}.
"""


from utils import chunk, cyclic_unshift, ring2_sum


def solve(code_n: int, code_k: int, code_poly: str, message: str) -> str:
    chunks = chunk(message, code_k)
    full_poly = code_poly.zfill(code_n)
    origin_matrix = [cyclic_unshift(full_poly, i) for i in range(code_k)]
    codes = []
    for c in chunks:
        code = "0".zfill(code_n)
        for i in range(code_k):
            if c[-i - 1] == "1":
                code = ring2_sum(code, origin_matrix[i])
        codes.append(code)
    return "".join(codes)


if __name__ == "__main__":
    code_n = 7
    code_k = 4
    code_poly = "1011"
    message = "101001001011"

    print(solve(code_n, code_k, code_poly, message))
