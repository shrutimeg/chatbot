

import random
from tkinter import *

# GUI

root = Tk()

root.title("Chatbot")

BG_GRAY = "#ABB2B9"

BG_COLOR = "#17202A"

TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"

FONT_BOLD = "Helvetica 13 bold"



# Send function

def send():
    h = ["hi", "hello", "hello, is there anyone here?"]
    n = ["whats your name", "what is your name", "do you have any name", "what should i call you"]
    a = ["what is the address of aec","what is your address", "address"]
    i = ["contact", "contact details"]
    s = ["total number of students", "total students","total number of students in aec","how many numbers of students in aec"]
    f = ["total number of faculties", "total faculties","total number of faculties in aec","how many numbers of faculties in aec"]
    d1 = ["total number of courses in aec", "how many courses are available in aec", "number of courses","total number of courses"]
    d2 = ["different courses in aec","courses offer by aec"]
    a3 = ["total number of alumni", "total alumni","total number of alumni in aec","numbers of alumni in aec"]
    l = ["total number of laboratories", "total laboratories","total number of laboratories in aec","numbers of laboratories in aec","number of labs"]
    a1 = ["aec affiliated to", "aec affiliated with"]
    a2 = ["aec approved by","is aec approved by by aicte"]
    y = ["establishment year of aec", "in which year aec was established", "establishment year"]
    j = ["website of aec", "website"]
    g = ["fee of aec", "fee details", "fee information"]
    z = ["timing of opening and closing", "time of open & close"]
    x = ["award winning", "how many awards are winning"]
    k = ["mass recruiters companies in aec", "which companies are take maximum students"]
    c = ["infrastructure of aec", "infrastructure"]
    d3 = ["who is your developer", "developer information"]
    b = ["cya", "see you later", "bye", "goodbye", "i am leaving"]
    send = "You -> " + e.get()

    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if user in h:
        botanswer = ["Hello !", "Hi", "hello, How can I help you", "Welcome"]


        txt.insert(END, "\n" + "Bot -> "+ random.choice(botanswer))


    elif user in n:

        txt.insert(END, "\n" + "Bot -> My name is AEC Support Assistant.")


    elif user in a:

        txt.insert(END, "\n" + "Bot -> Vivekananda Sarani, Kanyapur, Asansol - 713305")

    elif user in i:
        txt.insert(END,
                   "\n" + "Bot ->  \t Email id - principal.office@aecwb.edu.in \n\t\tprincipal.aecwb@gmail.com \n\t Phone no- 9073683912,8100192408")


    elif user in s:
        txt.insert(END, "\n" + "Bot -> 3072 Students")


    elif user in f:
        txt.insert(END, "\n" + "Bot -> 159 faculties")

    elif user in d1:
        botanswer = ["There are 16 courses available in AEC","AEC offers 16 different courses "]
        txt.insert(END, "\n" + "Bot -> "+ random.choice(botanswer))

    elif user in d2:
        txt.insert(END, "\n" +  "Bot -> " + "CSE, ECE, IT, ME, EE, CSBS,\n           AIML, CSE(IOT & CSIBCT), CE,  \n            BBA, BBA(HM) ,CA(BCA, MCA), BSHU")

    elif user in a3:
        txt.insert(END, "\n" + "Bot -> 12246 Alumni")

    elif user in l:
        txt.insert(END, "\n" + "Bot -> 74 Laboratories")

    elif user in a1:
        txt.insert(END, "\n" + "Bot -> AEC Affiliated with MAKAUT")

    elif user in a2:
        txt.insert(END, "\n" + "Bot -> AEC Approved by AICTE")

    elif user in y:
        txt.insert(END, "\n" + "Bot -> AEC Established in 1998")

    elif user in j:
        txt.insert(END, "\n" + "Bot -> https://www.aecwb.edu.in/?pn=3")


    elif user in g:
        txt.insert(END,
                   "\n" + "Bot ->  \tFee of B.Tech -> 448272 \n\t Fee of M.tech -> 191600\n\t Fee of BCA -> 280300\n\t Fee of MCA -> 239024\n\t Fee of BBA -> 277277")


    elif user in z:
        botanswer = ["Monday to Friday 9:30 am - 5:30 pm", "9:30 am to 5:30 pm [ Monday to Friday] "]

        txt.insert(END, "\n" + "Bot -> " + random.choice(botanswer))

    elif user in x:
        txt.insert(END, "\n" + "Bot -> AEC won 25 Awards")


    elif user in k:
        txt.insert(END, "\n" + "Bot -> \tTCS\n\t Infosys\n\t IBM\n\t wipro\n\t Accenture\n\t cognizant\n\t Virtusa")

    elif user in c:
        txt.insert(END, "\n" + "Bot ->  \tCentral Library\n\tSeminar Hall\n\t Medical Center\n\t Hostel\n\t Sports & Games\n\t Gymnesium\n\t Cafeteria")

    elif user in d3:
        txt.insert(END, "\n" + "Bot -> I was developed by team QuadCoders, is a team of 4 Students \n            named are \n\t1. Saptarshi Banerjee(10800221153) \n\t2.Priya Jha(10800220020) \n\t3.Shruti Kiran(10800220016) \n\t4.Yuvraj Singh(10800221137)")

    elif user in b:
        botanswer = ["Sad to see you go :(", "bye", "come again"]
        txt.insert(END, "\n" + "Bot -> " + random.choice(botanswer))



    else:

        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to AEC", font=FONT_BOLD, pady=10, width=20, height=1).grid(

    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)

txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)

scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)

e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,

              command=send).grid(row=2, column=1)

