import speech_recognition as sr
import pyttsx3
import makelist
import text2num
def takeorderfunction():
    print("INSTRUCTIONS: \n 1) Be clear \n 2) Mention Quantity, even for suborders \n 3) Avoid Repeating name for suborder")
    '''engine= pyttsx3.init()
    engine.setProperty("voice", "american")
    engine.setProperty("rate", "140")
    engine.say("hello, what would you like to eat?")
    engine.runAndWait()

    recog = sr.Recognizer()
    with sr.Microphone() as source:                             # use the default microphone as the audio source
       order = recog.listen(source)                            # listen for the first phrase and extract it into audio data
    try:
        order=recog.recognize_google(order)
        print("You said " + order)      # recognize speech using Google Speech Recognition'''
    order=input()         #remove after testing
    order = order.replace(" a ", " 1 ").replace(" a ", " 1 ")
    order = order.split()
    for k,v in enumerate(order):
        order[k]=str(text2num.text2num(v))
    print(order)          #remove after testing
    message="You said "+order
    makelist.makeorder(order)
    '''except sr.UnknownValueError:
       print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Sorry Service is Unavailible at the moment")'''
    return message