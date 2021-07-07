import speech_recognition as sr
import webbrowser as web 

def main():
    #path ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    path =  "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("speak the website for eg youtube.com,instagram.com,google.com")
        print("listing ..")
        
  
        audio = r.listen(source)

        print("Recognizing ...")

        try:
            dest=r.recognize_google(audio)
            print("Did you say  "+ dest)
            print("wait it may take some time ")

            a=web.get(path).open(dest)
            open(a)
        except Exception as e:
            print("Error.."+str(e))  

if __name__ =="__main__":
    main()
                         