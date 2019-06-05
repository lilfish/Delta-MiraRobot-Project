import os
from sound_protocol import EnumSoundEmotion

class SoundPlayer():
    # Select media player change to mpg123 for use on PI
    def __init__(self, sound_dir=''):
        self.sound_dir = sound_dir
        self.player = "mpv --no-audio-display "
 
    def change_to_emotion(self, emotion_id):
        print("Changing to '%s'" % EnumSoundEmotion(emotion_id).fullname)
        if (emotion_id == int(EnumSoundEmotion.HAPPY)):
            self.happy()
        elif (emotion_id == int(EnumSoundEmotion.SAD)):
            self.sad()
        elif (emotion_id == int(EnumSoundEmotion.CHEERFUL)):
            self.cheerful()
        elif (emotion_id == int(EnumSoundEmotion.EXCITED)):    
            self.excited()  
    
    def play(self, audiofile):
        os.system(self.player + audiofile)
    
    def happy(self):
        self.play(os.path.join(self.sound_dir, 'happy.mp3'))
    
    def sad(self):
        self.play(os.path.join(self.sound_dir, 'sad.mp3'))
    
    def cheerful(self):
        self.play(os.path.join(self.sound_dir, 'cheerful.mp3'))
    
    def excited(self):
        self.play(os.path.join(self.sound_dir, 'excited.mp3'))