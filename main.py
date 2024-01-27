import speech_recognition as sr 
import os

#cria um reconhecedor
rec = sr.Recognizer()

#abre e define o microfone como fonte de audio
with sr.Microphone() as mic:

    print('Diga alguma coisa: ')

    while True:

        #redução de ruido externo
        rec.adjust_for_ambient_noise(mic)

        audio = rec.listen(mic)

        #transcreve o que foi dito
        text = rec.recognize_google(audio, language='pt-BR')

        if "navegador" in text:
            os.system("start msedge.exe")

        print(text)

        