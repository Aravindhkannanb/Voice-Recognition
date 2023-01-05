import speech_recognition as sr
import csv
list=[]
 
def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
 
        audio = r.listen(source)
 
        print("Recognizing Now .... ")
 
  
        try:
            print("You have said \n" + r.recognize_google(audio))
            list.append(r.recognize_google(audio))
            print(list)
            print("Audio Recorded Successfully \n ")
 
 
        except Exception as e:
            print("Error :  " + str(e))
 
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
 

main()
file=open('D:\\python\\data.csv','a',newline='')
writer=csv.writer(file)
writer.writerows(list)
file.close()