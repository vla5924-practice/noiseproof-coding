from math import floor


def chunk(src: str, piece: int) -> list:
    chunks = []
    for i in range(floor(len(src) / piece)):
        chunks.append(src[piece * i:piece * i + piece])
    return chunks


def cyclic_shift(src: str, distance: int = 1) -> str:
    return src if distance == 0 else src[-distance:] + src[0:-distance]


def cyclic_unshift(src: str, distance: int = 1) -> str:
    return src if distance == 0 else src[distance:] + src[0:distance]


def ring2_sum(lhs: str, rhs: str) -> str:
    result_len = max(len(lhs), len(rhs))
    lhs = lhs.zfill(result_len)
    rhs = rhs.zfill(result_len)
    result = []
    for i in range(result_len):
        result.append("1" if lhs[i] != rhs[i] else "0")
    return "".join(result)


def deg_diff(lhs: str, rhs: str) -> int:
    return (len(lhs) - lhs.index("1")) - (len(rhs) - rhs.index("1"))


def ring2_divide(lhs: str, rhs: str) -> tuple:
    deg = 0
    remainder = lhs
    deg = deg_diff(lhs, rhs)
    quotient = "0"
    while deg >= 0:
        part = ("0".zfill(deg) if deg > 0 else "")
        quotient = ring2_sum(quotient, "1" + part)
        temp = (rhs + part).zfill(len(lhs))
        remainder = ring2_sum(remainder, temp)
        try:
            deg = deg_diff(remainder, rhs)
        except ValueError:
            break
    return quotient, remainder
