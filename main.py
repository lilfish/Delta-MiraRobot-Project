# import modules.facialdetection.facialdetection as facialdetection
import modules.statemachine.StateHandler as StateHandler

# init
state = StateHandler.StateHandler(StateHandler.EnumState.State.IDLE)

# Main loop
while (True):
    state.handle()
    # print(facialdetection.getfacecount())
