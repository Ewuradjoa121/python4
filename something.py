import pyttsx3

engine =pyttsx3.init()

correct_password=4545

user_password=int(input("Enter password:"))
if  user_password !=correct_password:
    engine.say( " leave this place ")
    engine.runAndWait()

else:
    engine.say ("welcome home ")
    engine. runAndWait()
