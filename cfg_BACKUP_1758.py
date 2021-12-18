import os

IMAGE_PATHS = {
    'gold': os.path.join(os.getcwd(), 'resources/images/gold.png'),
    'apple': os.path.join(os.getcwd(), 'resources/images/apple.png'),
<<<<<<< HEAD
    'background': os.path.join(os.getcwd(),'resources/images/iit-mandi.jpg' ),
=======
    'background': os.path.join(os.getcwd(), 'resources/images/iitmandi2.jpg'),
>>>>>>> upstream/challenge-7
    'hero': [os.path.join(os.getcwd(), 'resources/images/%d.png' % i) for i in range(1, 11)]
}



AUDIO_PATHS = {
    'bgm': os.path.join(os.getcwd(), 'resources/audios/bgm.mp3'),
    'get': os.path.join(os.getcwd(), 'resources/audios/get.wav'),
}

FONT_PATH = os.path.join(os.getcwd(), 'resources/font/font.TTF')

HIGHEST_SCORE_RECORD_FILEPATH = 'highest.rec'

SCREENSIZE = (800,600)

BACKGROUND_COLOR = (0, 160, 233)

FPS = 80
