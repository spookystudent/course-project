import pyttsx3
import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
import datetime
import win32com.client as wincl
import site
import calculator
import envelope
import translator
opts = {"alias": ('pythonguru', 'пайтонгуру', 'гурупайтон'),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как','сколько','поставь','переведи', "засеки",'запусти','сколько будет'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "засеки время"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "останови"),
             "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', "шутка", "прикол"),
             "calc": ('прибавить','умножить','разделить','степень','вычесть','поделить','х','+','-','/'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи', 'выключи компьютер'),
             "conv": ("валюта", "конвертер","доллар",'руб','евро'),
             "internet": ("открой", "вк", "гугл", "сайт", 'вконтакте', "ютуб"),
             "translator": ("переводчик","translate"),
             "deals": ("дела","делишки", 'как сам', 'как дела')}}
startTime = 0
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = "str"