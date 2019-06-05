from enum import Enum 

class EnumExitProtocol(Enum):
    SCREEN = 1,
    SOUND = 2

    def __new__(cls, value):
        member = object.__new__(cls)
        member._value_ = value
        return member

    def __int__(self):
        return self.value