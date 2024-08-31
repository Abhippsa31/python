from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hey bot'):
        text.insert(END, "\n" + "Bot: hello")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif(e.get()=='I need some help can you help me '):
        text.insert(END, "\n" + "Bot: yes i can,state your problem to me...")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='pink', fg='black')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=50)
send = Button(root,text='Send',bg='black', fg='white', width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('ABHIPPSA BOT')
root.mainloop()
