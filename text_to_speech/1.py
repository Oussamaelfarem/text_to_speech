from gtts import gTTS

import os 

f=open('C:/Users/admin/Desktop/portfolio_project/text_to_speech/1.txt', 'r')
x= f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")