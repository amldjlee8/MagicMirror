# -*- coding: utf-8 -*-

from tkinter import *
from datetime import date
import time
import weatherModule


class HomeScreen:

    def __init__(self, master):
        self.master = master
        master.title("HomeScreen")

        self.clockLabel = Label(master, text='', font=('Helvetica', 100), fg = 'white', bg = 'black')
        self.clockLabel.grid(row=0, sticky=W)

        self.dateLabel = Label(master, text='', font=('Helvetica', 20), fg = 'white', bg = 'black')
        self.dateLabel.grid(row=1, sticky=W)

        self.weatStatusLabel = Label(master, text='', font=('Helvetica', 20), fg = 'white', bg = 'black')
        self.weatStatusLabel.grid(row=1, column= 1, sticky=E)

        self.updateClockDate()
        self.updateWeather()

    def updateClockDate(self):
        self.curTime = time.strftime('%H:%M')
        self.clockLabel.configure(text=self.curTime)
        self.curDate = date.today().strftime('%A %d %B %Y')
        self.dateLabel.configure(text=self.curDate)
        root.after(1000, lambda: self.updateClockDate())

    def updateWeather(self):
        #self.curWeatStat, self.curTemp = weatherModule.getCurWeatInfo()
        self.curWeatStat, self.curTemp = 'Clear', '26°C'
        self.weatStatusLabel.configure(text=self.curWeatStat + ' ' + self.curTemp)
        root.after(3600000, lambda: self.updateClockDate())


root = Tk()
root.geometry("480x800")
root.configure(background='black')
magicMirror = HomeScreen(root)
root.mainloop()