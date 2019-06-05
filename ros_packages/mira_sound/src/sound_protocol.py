from enum import Enum 

class EnumSoundEmotion(Enum):
    SAD = 1, 'Sad'
    CHEERFUL = 2, 'Cheerful'
    HAPPY = 3, 'Happy'
    EXCITED = 4, 'Excited'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value