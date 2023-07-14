from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
from datetime import datetime
import webbrowser
import os
import openai
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config



#Все о дате
def get_date(date, split='-'):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split(split)
    return (day_list[int(date_list[0]) - 1] + ' ' +
        month_list[int(date_list[1]) - 1] + ' ' +
        date_list[2] + ' года')



#API chatgpt
openai.api_key = "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"







def listen_command():
    #Использует микрофон
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)

    #Распознает речь
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"



#Команды
def do_this_command(message):
    message = message.lower()

    #подключение chatgpt
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= message,
    temperature=0.5,
    max_tokens=2000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
  )
    
        
    #ответы на команды
    if "привет" in message:
        say_message("Доброго времени суток!")
    elif "пока" in message or "хватит" in message:
        say_message("Пока!")
        exit()
    elif "как дела" in message:
        say_message("Отлично!")
    elif "ты тупой" in message:
        say_message("Сам такой, идиот")
    elif "который час" in message or "сколько времени" in message:
        now = datetime.now()
        say_message(f"Сейчас {now.hour} часов {now.minute} минуты")
    elif "какое сегодня число" in message:
        now = datetime.now().strftime("%d-%m-%Y")
        say_message(f"Сегодня {get_date(now)}")
    elif "открой браузер" in message:
        webbrowser.open('https://www.google.com/')
        say_message("Открыла Google")
    elif "открой steam" in message:
        os.system('C:\Steam1\steam.exe')
        say_message("Открыла Steam!")
    elif "включи музыку" in message:
        webbrowser.open('https://www.youtube.com/watch?v=-dgca5_tjA0')
        say_message("Включила музыку!")
    elif "открой word" in message:
        os.system('"C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"')
        say_message("Открыла Word!")
    elif "открой новости" in message:
        webbrowser.open('https://www.rbc.ru/')
        say_message("Открыла новости")
    elif "включи песню для сигмы" in message:
        webbrowser.open('https://www.youtube.com/watch?v=NS9z2QHcZdY')
        say_message("Включила")

    else:
        say_message(response['choices'][0]['text'])

    

    

#Сохранение аудио файлов
def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Голосовой ассистент: "+message)


#Запуск программы
if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)