from operator import add, mul

OPCODE_DICT = {
    99: False,
    1: add,
    2: mul,
    -1e20: 'Something went wrong.'
    }


def translate(opcode):
    for i in range(0, len(opcode)-4, 4):
        code_func = OPCODE_DICT.get(opcode[i], -1e20)
        val1_index, val2_index, store_index = opcode[i+1:i+4]

        if code_func:
            try:
                opcode[store_index] = code_func(opcode[val1_index], 
                                                opcode[val2_index]) 
            except Exception as e:
                print(e, code_func)
                break
    return opcode


if __name__ == "__main__":

    with open('opcode.txt', 'r') as f:
        input = f.read().split(',')
    opcode = [int(i) for i in input]
    opcode[1] = 12
    opcode[2] = 2

    result = translate(opcode)

    print(result)