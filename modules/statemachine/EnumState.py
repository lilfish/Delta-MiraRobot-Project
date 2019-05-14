from enum import Enum 

class State(Enum):
    IDLE = 0,
    FACE_FOUND = 1,
    FACE_HANDLE = 2