# Part 1

"""
99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
"""

def read_opcode(opcode, noun, verb):
    opcode_updated = opcode.copy()
    opcode_updated[1] = noun
    opcode_updated[2] = verb

    i=0
    while i < len(opcode):
        v = opcode_updated[i]
        if v==99:
            break
        elif v==1:
            opcode_updated[opcode_updated[i+3]] = opcode_updated[opcode_updated[i+1]] + opcode_updated[opcode_updated[i+2]]
            #print('added {:d} together with {:d}'.format(opcode_updated[opcode_updated[i+1]], opcode_updated[opcode_updated[i+2]]))
        elif v==2:
            opcode_updated[opcode_updated[i+3]] = opcode_updated[opcode_updated[i+1]] * opcode_updated[opcode_updated[i+2]]
            #print('multiplied {:d} together with {:d}'.format(opcode_updated[opcode_updated[i+1]], opcode_updated[opcode_updated[i+2]]))
        i = i+4
    return opcode_updated[0]


op = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,9,19,23,1,13,23,27,1,5,27,31,2,31,6,35,1,35,5,39,1,9,39,43,1,43,5,47,1,47,5,51,2,10,51,55,1,5,55,59,1,59,5,63,2,63,9,67,1,67,5,71,2,9,71,75,1,75,5,79,1,10,79,83,1,83,10,87,1,10,87,91,1,6,91,95,2,95,6,99,2,99,9,103,1,103,6,107,1,13,107,111,1,13,111,115,2,115,9,119,1,119,6,123,2,9,123,127,1,127,5,131,1,131,5,135,1,135,5,139,2,10,139,143,2,143,10,147,1,147,5,151,1,151,2,155,1,155,13,0,99,2,14,0,0]

read_opcode(op_upd,12,2)


# part 2
for noun in range(100):
    for verb in range(100):
        if read_opcode(op_upd,noun, verb) == 19690720:
            print('SUCCESS with noun: {:d}, and verb: {:d}, which gives us an answer of {:d}'.format(noun, verb, noun*100 + verb))
            break

            

# TODO: add logs instead of prints