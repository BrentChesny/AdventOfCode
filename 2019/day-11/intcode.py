ADD = 1
MUL = 2
IN = 3
OUT = 4
JIT = 5
JIF = 6
LT = 7
EQ = 8
REL = 9

n_args = {
    ADD: 3,
    MUL: 3,
    IN: 1,
    OUT: 1,
    JIT: 2,
    JIF: 2,
    LT: 3,
    EQ: 3,
    REL: 1,
}


class IntCodeProcessor:
    def __init__(self, program, input):
        self.program = program[:] + [0] * 100000
        self.ip = 0
        self.input = input
        self.relative_base = 0

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

    def get_param(self, i, mode):
        if mode == 0:
            return self.program[self.program[self.ip+i]]
        elif mode == 1:
            return self.program[self.ip+i]
        elif mode == 2:
            return self.program[self.relative_base + self.program[self.ip+i]]
        else:
            print("Invalid parameter mode")

    def set_value(self, i, mode, value):
        if mode == 0:
            self.program[self.program[self.ip+i]] = value
        elif mode == 2:
            self.program[self.relative_base + self.program[self.ip+i]] = value
        else:
            print("Invalid parameter mode")

    def execute(self):
        output = []

        while self.program[self.ip] != 99:
            opcode = self.program[self.ip]
            instruction, modes = self.decode_opcode(opcode)
            if instruction == ADD:
                result = self.get_param(1, modes[0]) + self.get_param(2, modes[1])
                self.set_value(3, modes[2], result)
                self.ip += len(modes) + 1
            elif instruction == MUL:
                result = self.get_param(1, modes[0]) * self.get_param(2, modes[1])
                self.set_value(3, modes[2], result)
                self.ip += len(modes) + 1
            elif instruction == IN:
                if len(self.input) == 0:
                    return output
                self.set_value(1, modes[0], self.input.pop(0))
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
                result = 1 if self.get_param(1, modes[0]) < self.get_param(2, modes[1]) else 0
                self.set_value(3, modes[2], result)
                self.ip += len(modes) + 1
            elif instruction == EQ:
                result = 1 if self.get_param(1, modes[0]) == self.get_param(2, modes[1]) else 0
                self.set_value(3, modes[2], result)
                self.ip += len(modes) + 1
            elif instruction == REL:
                self.relative_base += self.get_param(1, modes[0])
                self.ip += len(modes) + 1

        return output
