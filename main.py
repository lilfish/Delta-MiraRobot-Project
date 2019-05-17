# import modules.facialdetection.facialdetection as facialdetection
import modules.statemachine.StateHandler as StateHandler

# init
state = StateHandler.StateHandler(StateHandler.EnumState.State.FACE_FOUND)

# Main loop
while (True):
    state.handle()
    # print(facialdetection.getfacecount())
