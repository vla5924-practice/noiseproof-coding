"""
Формулировка задания:
Дан циклический ({code_n}, {code_k})-код с порождающим многочленом в векторной форме {code_poly} и принятая двоичная
последовательность {errmessage}, при передаче которой могли произойти ошибки. Восстановите информационное сообщение.
"""


from utils import chunk, ring2_sum, ring2_divide


def solve(code_n: int, code_k: int, code_poly: str, errmessage: str) -> str:
    chunks = chunk(errmessage, code_n)
    full_poly = code_poly.zfill(code_n)
    syndromes = {}
    if code_poly == "1011" and code_n == 7 and code_k == 4:
        syndromes = {
            "000": "0000000",
            "101": "1000000",
            "111": "0100000",
            "110": "0010000",
            "011": "0001000",
            "100": "0000100",
            "010": "0000010",
            "001": "0000001",
        }
    else:
        raise NotImplementedError(
            "Verification matrix generation is not implemented")
    message = ""
    code_r = code_n - code_k
    for c in chunks:
        _, remainder = ring2_divide(c, full_poly)
        remainder = remainder[-code_r:]
        temp = ring2_sum(c, syndromes[remainder])
        quotient, _ = ring2_divide(temp, full_poly)
        message += quotient[-code_k:].zfill(code_k)
    return message


if __name__ == "__main__":
    code_n = 7
    code_k = 4
    code_poly = "1011"
    errmessage = "10010001101111"

    print(solve(code_n, code_k, code_poly, errmessage))
