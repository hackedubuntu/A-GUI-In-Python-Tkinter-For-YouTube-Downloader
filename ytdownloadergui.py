from tkinter import *
from pytube import YouTube as yt
from tkinter import messagebox
import os
import sys

class App:
    def __init__(self, root):
        #setting title
        root.title("YouTube Video Downloader")
        root.geometry(newGeometry="510x510")
        root.resizable(width=False, height=False)

        self.url = StringVar()
        self.url.set("")
        self.sesvar = IntVar()
        self.sesvar.set(0)

        self.urlentry=Entry(root,borderwidth = "1px",font={'family':'Consolas','size':12},fg = "#333333",justify = "center",text = "URL",textvariable=self.url)
        self.urlentry.place(x=81,y=100,width=355,height=45)

        self.urllabel=Label(root,font={'family':'Consolas','size':12},fg = "#333333",justify = "center",text = "URL")
        self.urllabel.place(x=0,y=100,width=80,height=45)

        self.sescheck=Checkbutton(root,font={'family':'Consolas','size':12},fg = "#333333",justify = "center",text = "Ses",variable=self.sesvar)
        self.sescheck.place(x=440,y=100,width=59,height=45)

        self.resentry=Listbox(root,selectmode=SINGLE,font={'family':'Consolas','size':12},fg = "#333333")
        self.resentry.place(x=10,y=150,width=490,height=150)

        self.indirbut=Button(root,bg = "#efefef",font={'family':'Consolas','size':24},fg = "#000000",justify = "center",text = "İndir",command=self.indirfunc)
        self.indirbut.place(x=260,y=310,width=240,height=160)

        self.yazilabel=Label(root,font={'family':'Consolas','size':12},fg = "#333333",justify = "center",text = "YouTube Video İndirme Programı")
        self.yazilabel.place(x=10,y=10,width=501,height=86)

        self.kontrolbut=Button(root,bg = "#efefef",font={'family':'Consolas','size':24},fg = "#000000",justify = "center",text = "Kontrol Et",command=self.kontrolfunc)
        self.kontrolbut.place(x=10,y=310,width=240,height=160)


    def indirfunc(self):
        try:
            if not os.getcwd().split("\\")[-1] == "indirilenvideolar":
                os.chdir(os.getcwd()+"\\indirilenvideolar")
        except:
            os.mkdir(os.getcwd()+"\\indirilenvideolar")
            os.chdir(os.getcwd()+"\\indirilenvideolar")
        finally:
            if sys.platform == "win32":
                adres = self.url.get()
                indec = ""
                if int(self.sesvar.get()) == 0:
                    videolar = yt(adres).streams.filter(progressive=True,file_extension="mp4")
                    indec = str(self.resentry.curselection()).split(",")[0]
                elif int(self.sesvar.get()) == 1:
                    videolar = yt(adres).streams.filter(only_audio=True)
                    indec = str(self.resentry.curselection()).split(",")[0]
                videolar[int(indec[1:])].download()
                self.urlentry.delete(0,END)
                self.resentry.delete(0,END)
                messagebox.showinfo("Video İndirildi","Tebrikler Videoyu İndirdiniz!!")

    def kontrolfunc(self):
        adres = self.url.get()
        videolar = ""
        if int(self.sesvar.get()) == 0:
            self.resentry.delete(0,END)
            videolar = yt(adres).streams.filter(progressive=True,file_extension="mp4")
        elif int(self.sesvar.get()) == 1:
            self.resentry.delete(0,END)
            videolar = yt(adres).streams.filter(only_audio=True)
        index = 0
        for x in videolar:
            self.resentry.insert(END,str(index) + " " + str(x))
            index += 1

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()