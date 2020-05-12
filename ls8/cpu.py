"""CPU functionality."""

import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b1000110


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0]*256
        self.register = [0]*8
        self.running = True

        # branch setup
        # self.branchtable = {}
        # self.branchtable[LDI] = self.handle_LDI
        # self.branchtable[PRN] = self.handle_PRN
        # self.branchtable[HLT] = self.handle_HLT
        # self.branchtable[MUL] = self.handle_MUL
        # self.branchtable[PUSH] = self.handle_PUSH
        # self.branchtable[POP] = self.handle_POP

        # self.branchtable = {
        #     HLT: self.HLT,
        #     MUL: self.alu,
        #     ADD: self.alu,
        #     PUSH: self.PUSH,
        #     POP: self.POP,
        #     LDI: self.LDI,
        #     PRN: self.PRN

        # }
        # self.branchtable[PUSH] = self.handle_push
        # self.branchtable[POP] = self.handle_pop

    # def handle_LDI(self, a):
    #     print("op LDI: " + a)

    # def handle_PRN(self, a):
    #     print("op PRN: " + a)

    # def handle_HLT(self, a):
    #     print("op HLT: " + a)

    # def handle_MUL(self, a):
    #     print("op MUL: " + a)

    # def handle_PUSH(self, a):
    #     print("op PUSH: " + a)

    # def handle_POP(self, a):
    #     print("op POP: " + a)

    def load(self):
        """Load a program into memory."""

        address = 0

        print(sys.argv)
        if len(sys.argv) != 2:
            print("Need proper file name passed")
            sys.exit(1)

        filename = sys.argv[1]
        with open(filename) as f:
            for line in f:
                # print("line=>", line)
                if line == '':
                    continue
                comment_split = line.split('#')
                # print(comment_split) # everything
                # print(comment_split)
                num = comment_split[0].strip()
                # print("num=>", num)

                x = int(num, 2)

                self.ram_write(address, x)

                address += 1

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]

        # for instruction in program:
            # self.ram[address] = instruction
            # address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        reg_a = int(reg_a)
        reg_b = int(reg_b)

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc

        elif op == MUL:
            # print("INSIDE MUL")
            self.register[reg_a] *= self.register[reg_b]
            self.pc += 3

        # if op == LDI:
        #     ram_write(register[0], 8)
        else:
            raise Exception("Unsupported ALU OPERATION")

    def ram_read(self, address_to_read):
        # print("reading_ram@address_to_read=>", address_to_read)
        return self.ram[address_to_read]

    def ram_write(self, address_to_write, value):
        self.ram[address_to_write] = value
        # print("ram_written-address_to_write,value=> ", address_to_write, value)

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.running:
            instruction_register = self.pc
            op = self.ram_read(instruction_register)

            operand_a = self.ram_read(instruction_register + 1)
            operand_b = self.ram_read(instruction_register + 2)

            # instruction_register = op
            # self.branchtable[instruction_register]("foo")

            # instruction_register = op
            # self.branchtable[instruction_register]("bar")

            # if op in self.branchtable:
            #     pass

            if op == HLT:
                print("HALTING")
                self.running = False
                print("HALTED")
                self.pc += 1

            elif op == LDI:
                self.register[operand_a] = operand_b
                self.pc += 3

            elif op == PRN:
                # code_to_print = self.ram_read(operand_a)
                print(self.register[operand_a])
                self.pc += 2

            elif op == MUL:
                self.alu(op, operand_a, operand_b)

            else:
                print(f"Unknown instruction: {op}")
                sys.exit(1)
