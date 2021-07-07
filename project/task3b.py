import speech_recognition as sr
import webbrowser as web 

def main():

    #path =  str("https://docs.google.com/")+str(site)+str("/u/6/")

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("for opening google sites,docs,sheets,forms respectively\n\n")
        print("speak anyone from this presentation,document,spreadsheets,forms\n")
        print("listing .. ")
        
  
        audio = r.listen(source)

        print("Recognizing ...")

        try:
            site=r.recognize_google(audio)
            print("Did you say  "+ site)
            path =  str("https://docs.google.com/")+str(site)+str("/u/6/")

            a=web.open(path)
            open(a)
        except Exception as e:
            print("Error.."+str(e))  

if __name__ =="__main__":
    main()
            