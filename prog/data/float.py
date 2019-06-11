import numpy as np

def print_float(a_number):
    a_float = np.float32(a_number)
    b_repr = format(int.from_bytes(a_float.data.tobytes(), 'little'), '032b')
    sig, exp, man = b_repr[0], b_repr[1:9], '1' + b_repr[9:]
    print(sig, exp, man)
    # int_exp = twos_comp(int(exp, 2), 8)
    # print(sig, int_exp, str(int(man[:int_exp + 1], 2)) + '.' +str(int(man[int_exp + 1:])))

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is
