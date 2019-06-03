from gif_player import GifPlayer 
from gif_player import GifPlayerThread
from gif_protocol import SharedData, EnumGifEmotion

class ScreenManager():
    def __init__(self):
        self.t = GifPlayerThread()
        SharedData.change_emotion_id(int(EnumGifEmotion.NEUTRAL))

    def change_to_emotion(self, emotion_id):
        print("Changing to '%s'" % EnumGifEmotion(emotion_id).fullname)
        SharedData.change_emotion_id(emotion_id)