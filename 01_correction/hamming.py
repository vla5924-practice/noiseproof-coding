"""
Reference: https://levelup.gitconnected.com/explaining-error-detection-and-correction-codes-with-python-be517596d42f
Source: https://gist.github.com/sausheong/c926843150957e16f0c387578b58f350
"""

# using Hamming (15, 11) code with 4 parity bits at positions 1, 2, 4, 8
num_parity_bits = 4


# get a list of parity bit positions, given the number of parity bits
def hamming(n):
    r = []
    for i in range(n):
        r.append(pow(2, i))
    return r


# insert 0 into the bit position
def insert_zero(num, pos):
    mask = pow(2, pos - 1) - 1
    t = num & mask
    num = (num >> (pos - 1)) << pos
    num = num + t
    return num


# create the bit positions first, set the parity bits to 0
def setup(data):
    bits = hamming(num_parity_bits)
    for b in bits:
        data = insert_zero(data, b)
    return data


# find the bit positions that have their bits set
def pos(num):
    r = []
    for i in range(1, num.bit_length()+1):
        if num & 1:
            r.append(i)
        num = num >> 1
    return r


# XOR the list of numbers
def xor(poslist):
    r = 0
    for n in poslist:
        r = r ^ n
    return r


# set the parity bits, given the bits to set, and the block to set
def set_parity(bits, block):
    for i, n in enumerate(hamming(num_parity_bits)):
        if bits & pow(2, i):
            block = block | pow(2, n-1)
    return block


# remove bit at given position
def remove_bit(num, pos):
    mask = pow(2, pos - 1) - 1
    t = num & mask
    num = (num >> pos) << (pos - 1)
    return num + t


# flip a bit in the data at a given position
def flip(pos, data):
    return data ^ (1 << pos - 1)


# encode
def encode(d):
    data = setup(d)
    positions = pos(data)
    bits = xor(positions)
    encoded = set_parity(bits, data)
    return encoded


# decode
def decode(e):
    c = xor(pos(e))
    if c:
        e = flip(c, e)  # flip the bit if there's an error
    bits = hamming(num_parity_bits)
    bits.reverse()
    for b in bits:
        e = remove_bit(e, b)
    return e


def p(text, num): print(text, bin(num))


original = 0b1001101
p("original:", original)

encoded = encode(original)
p("encoded :", encoded)

decoded = decode(encoded)
p("decoded :", decoded)

print()

# flip a bit at position 8 to create an error
err = flip(8, encoded)
p("original:", original)
p("encoded :", encoded)
p("flipped :", err)

decoded = decode(err)
p("decoded :", decoded)
