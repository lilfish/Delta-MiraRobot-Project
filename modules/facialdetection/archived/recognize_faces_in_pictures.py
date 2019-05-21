import face_recognition
import cv2 as cv
import pickle

# Load the jpg files into numpy arrays
print("Loading images...")
image = face_recognition.load_image_file("lin-manuel-miranda.png")

print("Loading known encoding...")
obama_encoding = pickle.load(open("obama_dumped", "rb"))

try:
    # resize to 1/10 
    small_frame = cv.resize(image, (0,0), fx=0.1, fy=0.1)
    rgb_small_frame = small_frame[:, :, ::-1]
    image_encoding = face_recognition.face_encodings(image)[0]
    # pickle.dump(biden_face_encoding, open("obama_dumped", "wb"))
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    obama_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, image_encoding)

print("Is the unknown face a picture of Obama? {}".format(results[0]))