class AirCastle:
    def __init__(self, height, blocks, color):
        self.height = height
        self.blocks = blocks
        self.color = color

    def change_height(self, val):
        self.height = max(self.height + val, 0)

    def __iadd__(self, other):
        self.blocks += other
        self.height += other // 5
        return self

    def __call__(self, *args, **kwargs):
        return self.height // args[0] * self.blocks

    def __str__(self):
        return f'The AirCastle at an altitude of ' \
            f'{self.height} meters is {self.color} with {self.blocks} clouds.'

    def __eq__(self, other):
        if self.blocks == other.blocks and self.height == other.height and self.color == other.color:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.blocks > other.blocks:
            return False
        elif self.blocks == other.blocks:
            if self.height > other.height:
                return False
            elif self.height == other.height:
                if self.color > other.color:
                    return False
                elif self.color == other.color:
                    return False
        return True

    def __gt__(self, other):
        return not self < other and not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other
