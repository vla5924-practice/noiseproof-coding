def xor(a: str, b: str):
    y = int(a, 2) ^ int(b, 2)
    return bin(y)[2:].zfill(len(a))


def pairs_all(x):
    res = []
    for i in x:
        for j in x:
            if (i, j) not in res and (j, i) not in res:
                res.append((i, j))
    return res


def code_from_basis(x):
    res = x
    for i, j in pairs_all(x):
        if xor(i, j) not in res:
            res.append(xor(i, j))
    return res


def code_len(code: str):
    return sum(int(i) for i in code)


def bitwise_and(a: str, b: str):
    y = int(a, 2) & int(b, 2)
    return bin(y)[2:].zfill(len(a))


def syndrom(code, test_matrix):
    res = []
    for i in test_matrix:
        res.append(code_len(bitwise_and(code, i)) % 2)
    return res
