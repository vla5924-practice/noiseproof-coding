"""
Формулировка задания:
Существует код с длиной слова {length}, исправляющий {corrects_errors} ошибок. 
"""


def solve(length, corrects_errors):
    return corrects_errors * 2 + 1 <= length


if __name__ == "__main__":
    length = 33
    corrects_errors = 17

    print(solve(length, corrects_errors))
