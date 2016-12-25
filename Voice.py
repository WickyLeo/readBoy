# coding:utf-8
import pyttsx
import sys
import time
import random

reload(sys)
sys.setdefaultencoding('utf8')
# __author__ = 'Wicky'
# __date__ = '2016/12/24'
# __Desc__ = 文字转语音

texts = ['中华人民共和国', '美国', '法国', '德国', '澳大利亚', '英国', '巴西', '俄罗斯',
            '纽西兰', '意大利', '阿根廷', '日本', '韩国', '新加坡', '马来西亚', '斯里兰卡']

voices = ['com.apple.speech.synthesis.voice.mei-jia',
        'com.apple.speech.synthesis.voice.sin-ji.premium',
        'com.apple.speech.synthesis.voice.ting-ting'];

def printText(name):
    time.sleep(2)
    print name

engine = pyttsx.init()
engine.connect('started-utterance', printText)
engine.setProperty('voice', random.choice(voices))

for text in texts:
    engine.say(text, name=text)
engine.runAndWait()

