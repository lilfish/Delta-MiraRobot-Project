import face_recognition
import picamera
import numpy as np

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# face_count=0

def getfacecount():
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)

    # If the numer of faces found changed print
    current_face_count = len(face_locations)
    return current_face_count
    # if face_count != current_face_count:
    #     face_count = current_face_count
    #     print(current_face_count)
