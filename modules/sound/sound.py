import os

# Select media player change to mpg123 for use on PI
player = "mpv --no-audio-display "

def setup():
    # set output to id 1. id 1 = analogue jack, id 2 = hdmi
    os.system("amixer cset numid=3 1")
def play(audiofile):
    os.system(player + audiofile)
def happy():
    play("./data/happy.mp3")
def sad():
    play("./data/sad.mp3")
def cheerful():
    play("./data/cheerful.mp3")
def excited():
    play("./data/excited.mp3")
