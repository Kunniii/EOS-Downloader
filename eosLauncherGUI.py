from eosDownloader import EOS_DOWNLOADER
import zipfile, os
from tkinter import *

class EOS_Launcher(Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.create_widget()

    def create_widget(self):
        self.window.resizable(0, 0)
        self.window.geometry("400x280")
        self.window.title("EOS Launcher")
        Label(self.window, text="EOS Launcher v.0.1", fg='#000', font="Consolas 20").pack()
        self.btnDownload = Button(self.window, text="Download EOS-Client", font='Consolas 13', fg='#fff', bg='#5aa469', command=self.clickDownload)
        self.btnDownload.place(x=25, y=50)
        self.btnRunEOS = Button(self.window, text="Run EOS-Client", font='Consolas 13', fg="#fff", bg="black", command=self.runEOS)
        self.btnRunEOS.place(x=230, y=50)
        self.btnExit = Button(self.window, text="Exit", font='Consolas 13', fg='#fff', bg='#d35d6e', command=self.window.destroy)
        self.btnExit.place(x=345, y=242)

    def unzip(self):
        try:
            with zipfile.ZipFile(f"D:\\EOSs\\{self.savedFileName}") as self.pack:                      
                self.pack.extractall("D:\\EOSs\\")
            Label(self.window, text="Extract successful!", fg='green', font='Consolas 10').place(x=30, y=110)
        except Exception as e:
             Label(self.window, text=f"{e}", fg='red').place()
    
    def runEOS(self):
        self.path = 'D:\\Coding\\Py\\DriveAPI\\EOSClient.lnk'
        os.system(self.path)
        
    def clickDownload(self):
        self.fileId='15orxKbmGm4foV5Lpc0RYnz9Imvp3IbWF'
        self.savedFileName='EOS-Client.zip'
        self.downloader = EOS_DOWNLOADER(fileId=self.fileId, savedFileName=self.savedFileName)
        self.downloader.launch()
        if not self.downloader.status:
            Label(self.window, text="Download failed! Please download manually.", font='Consolas 10', fg='red').place(x=30, y=90)
            return
        else:
            Label(self.window, text="Download successful!", font='Consolas 10', fg='green').place(x=30, y=90)
            self.unzip()

window = Tk()
launcher = EOS_Launcher(window=window)
launcher.mainloop()