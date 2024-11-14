def count_bits(n):
    binary = bin(n)[2:]
    count = 0
    return binary.count("1")


count_bits(5)  # output: 2
