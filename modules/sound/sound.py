import os

# Select media player change to mpg123 for use on PI
player = "mpv --no-audio-display "

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
