import modules.statemachine.EnumState as EnumState
import modules.sound.sound as soundController

class StateHandler():
    currentState = EnumState.State.IDLE

    def __init__(self, initState):
        self.currentState = initState

    def handle(self):
        if (self.currentState == EnumState.State.IDLE):
            self.handle_idle_state()
        elif (self.currentState == EnumState.State.FACE_FOUND):
            self.handle_face_found_state()
        elif (self.currentState == EnumState.State.FACE_HANDLE):
            self.handle_face_handle_state()

    def handle_idle_state(self):
        print("Idle state")

    def handle_face_found_state(self):
        print("Face found state")
        soundController.happy()

    def handle_face_handle_state(self):
        print("Face handle state")
