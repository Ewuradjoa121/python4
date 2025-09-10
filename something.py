import pyttsx3

engine =pyttsx3.init()

password=4545
Password=int(input("enter password:"))
if password< password :
    engine.say( " leave this place ")
    engine.runAndWait()

else:
    engine.say ("welcome home ")
    engine. runAndWait()
