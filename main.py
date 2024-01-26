import speech_recognition as sr 

#cria um reconhecedor
r = sr.Recognizer()

#abre e define o microfone como fonte de audio
with sr.Microphone() as source:
    #redução de ruido externo
    r.adjust_for_ambient_noise(source)

    print('Say something: ')
    audio = r.listen(source)
    print(r.recognize_google(audio))