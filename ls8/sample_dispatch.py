POP = 0b10101010
PUSH = 0b11110000


class Foo:

    def __init__(self):
        # Set up the branch table
        self.branchtable = {}
        # self.branchtable = {
        # POP:self.handle_POP
        # PUSH:self.handle_PUSH
        # }
        self.branchtable[POP] = self.handle_POP
        self.branchtable[PUSH] = self.handle_PUSH

    def handle_POP(self, a):
        print("op 1: " + a)

    def handle_PUSH(self, a):
        print("op 2: " + a)

    def run(self):
        # Example calls into the branch table
        instruction_register = POP
        self.branchtable[instruction_register]("foo")

        instruction_register = PUSH
        self.branchtable[instruction_register]("bar")


c = Foo()
c.run()
