ADD = 1
MUL = 2
IN = 3
OUT = 4
JIT = 5
JIF = 6
LT = 7
EQ = 8

n_args = {
    ADD: 3,
    MUL: 3,
    IN: 1,
    OUT: 1,
    JIT: 2,
    JIF: 2,
    LT: 3,
    EQ: 3,
}


class IntCodeProcessor:
    def __init__(self, program, input):
        self.program = program[:]
        self.ip = 0
        self.input = input

    def is_halted(self):
        return self.program[self.ip] == 99

    def pad(self, l, width):
        l.extend([0] * (width - len(l)))
        return l

    def decode_opcode(self, opcode):
        instruction = opcode % 100
        params = opcode // 100
        modes = list(map(int, reversed(str(params))))
        return instruction, self.pad(modes, n_args[instruction])

    def get_param(self, i, immediate_mode=True):
        param = self.program[self.ip+i]
        if immediate_mode:
            return param
        return self.program[param]

    def execute(self):
        output = []

        while self.program[self.ip] != 99:
            opcode = self.program[self.ip]
            instruction, modes = self.decode_opcode(opcode)
            if instruction == ADD:
                self.program[self.get_param(3)] = self.get_param(
                    1, modes[0]) + self.get_param(2, modes[1])
                self.ip += len(modes) + 1
            elif instruction == MUL:
                self.program[self.get_param(3)] = self.get_param(
                    1, modes[0]) * self.get_param(2, modes[1])
                self.ip += len(modes) + 1
            elif instruction == IN:
                if len(self.input) == 0:
                    return output
                self.program[self.get_param(1)] = self.input.pop(0)
                self.ip += len(modes) + 1
            elif instruction == OUT:
                output.append(self.get_param(1, modes[0]))
                self.ip += len(modes) + 1
            elif instruction == JIT:
                if self.get_param(1, modes[0]):
                    self.ip = self.get_param(2, modes[1])
                else:
                    self.ip += len(modes) + 1
            elif instruction == JIF:
                if not self.get_param(1, modes[0]):
                    self.ip = self.get_param(2, modes[1])
                else:
                    self.ip += len(modes) + 1
            elif instruction == LT:
                self.program[self.get_param(3)] = 1 if self.get_param(
                    1, modes[0]) < self.get_param(2, modes[1]) else 0
                self.ip += len(modes) + 1
            elif instruction == EQ:
                self.program[self.get_param(3)] = 1 if self.get_param(
                    1, modes[0]) == self.get_param(2, modes[1]) else 0
                self.ip += len(modes) + 1

        return output
