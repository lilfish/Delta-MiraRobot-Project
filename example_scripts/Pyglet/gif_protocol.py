from enum import Enum

class EnumGifEmotion(Enum):
    NEUTRAL = 1, 'Neutral'
    NEUTRAL_TO_HAPPY = 2, 'Neutral to Happy'
    HAPPY = 3, 'Happy'
    HAPPY_TO_NEUTRAL = 4, 'Happy to Neutral'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

class Gif():
    def __init__(self, filename=''):
        self.filename = filename

class TransitionGif():
    def __init__(self, gifs = {}):
        self.gifs = gifs

class GifPlayerData():
    gif_data_table = {
        1: Gif(filename='fast_wink.gif'), 
        2: TransitionGif(gifs={
                                'neutral_to_happy.gif': 0.0, 
                                'happy_wink.gif': 1.0
                                }),
        3: Gif(filename='happy_wink.gif'), 
        4: TransitionGif(gifs={
                                'happy_to_neutral.gif': 0.0, 
                                'fast_wink.gif': 1.0
                                })
    }
    emotion_with_transitions = [2, 4]

class SharedData():
    global_dict = {
        'emotion_id': -1,
        'emotion_handled': False,
        'transitioning': False,
        'final_gif': ''
    }
    buffer = {}
    @staticmethod
    def change_emotion_id(emotion_id):
        SharedData.global_dict['emotion_id'] = emotion_id
        SharedData.global_dict['emotion_handled'] = False 

        if (emotion_id in GifPlayerData.emotion_with_transitions):
            SharedData.buffer = GifPlayerData.gif_data_table[emotion_id].gifs 
            SharedData.global_dict['transitioning'] = True
        else:
            SharedData.global_dict['final_gif'] = GifPlayerData.gif_data_table[emotion_id].filename 
        print(SharedData.global_dict)
    
    @staticmethod 
    def emotion_handled():
        SharedData.global_dict['emotion_handled'] = True

    @staticmethod
    def transition_handled():
        SharedData.global_dict['emotion_handled'] = True
        SharedData.global_dict['transitioning'] = False 
        