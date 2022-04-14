import sys
from copy import deepcopy


class GFSystem:
    def __init__(self, a: list, base: int) -> None:
        self._a = deepcopy(a)
        self._prev_a = deepcopy(self._a)
        self._cols = len(self._a[0])
        self._base = base

    def print(self) -> None:
        for row in self._a:
            for i in range(self._cols - 1):
                print("{:2d} ".format(row[i]), end="")
            print("| {:2d}".format(row[-1]))

    def do(self, row_l: int, row_r: int, coef: int = 1) -> None:
        self._prev_a = deepcopy(self._a)
        print("({}) {} {} * ({})".format(row_l,
              "+" if coef > 0 else "-", abs(coef), row_r))
        row_l -= 1
        row_r -= 1
        for i in range(self._cols):
            self._a[row_l][i] = (
                self._a[row_l][i] + (self._a[row_r][i] * coef) % self._base) % self._base

    def undo(self) -> None:
        temp = deepcopy(self._a)
        self._a = self._prev_a
        self._prev_a = temp


###############################################################################
###############################################################################
###############################################################################

_s = GFSystem([
    [2, 3, 1, 0],
    [3, 2, 1, 1],
    [4, 2, 3, 4],
], base=5)

###############################################################################
###############################################################################
###############################################################################


def do(row_l: int, row_r: int, coef: int = 1):
    global _s
    _s.do(row_l, row_r, coef)
    _s.print()


def undo():
    global _s
    _s.undo()
    _s.print()


if __name__ == "__main__" and not sys.__stdin__.isatty():
    print("Please run in interactive mode via python -i", __file__)
    exit(1)

print("Welcome to interactive linear system calculator over Galois fields.")
print("Available methods:")
print("  do(row_l, row_r, coef) -> executes (row_l) + coef * (row_r) on _s system")
print("  undo()                 -> reverts the previous method")
print("Modify _s system right in Python file", __file__, "on line 39 if needed.")
print("_s system is:")
_s.print()
