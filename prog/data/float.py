import numpy as np

def float_bin_repr(a_float, format_str):
    return format(int.from_bytes(a_float.data.tobytes(), 'little'), format_str)

def binary_reduction(a_bit_string):
    n = 0
    for i in reversed(a_bit_string):
        n = (n + int(i))/2
    return n
    
def print_float(a_number, float_name='float'):
    desc = {
        'float': {
            'constructor': np.float32,
            'format': '032b',
            'exp': 8,
            'man': 23
         },
        'double': {
            'constructor': np.float64,
            'format': '064b',
            'exp': 11,
            'man': 52
         }
    }[float_name]
    assert desc is not None
    
    a_float = desc['constructor'](a_number)
    b_repr = float_bin_repr(a_float, desc['format'])
    print(b_repr)
    print(hex(int(b_repr, 2)))

    
    sig, exp, man = b_repr[0], b_repr[1:(1+desc['exp'])], '1' + b_repr[(1+desc['exp']):]
    print(sig, exp, man)
    
    signed_exp = int(exp, 2) - 127
    if signed_exp > 0:
        print(sig, signed_exp,
              str(int(man[:signed_exp + 1], 2)),
              str(binary_reduction(man[signed_exp + 1:])))        
if __name__ == '__main__':
    print_float(2.6)