# Author: Teddy Nueva Espana
# Date: 4/26/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program displays a gui to convert smoots to meters and vice versa

import tkinter 
from tkinter import messagebox

class SmootGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Smoot Converter")
        self.main_window.geometry("800x600")
        
        self.smootInfo = """The smoot /ˈsmuːt/ is a nonstandard, humorous unit of length created as 
part of an MIT fraternity prank. It is named after Oliver R. Smoot, a 
fraternity pledge to Lambda Chi Alpha, who in October 1958 lay down 
repeatedly on the Harvard Bridge (between Boston and Cambridge, 
Massachusetts) so that his fraternity brothers could use his height to 
measure the length of the bridge.

One smoot is equal to Oliver Smoot's height at the time of the prank, 5 
feet 7 inches (1.70 m). The bridge's length was measured to be 364.4 
smoots (2,035 ft; 620.1 m) "+/− 1 εar" with the "+/−" showing 
measurement uncertainty and spelled with an epsilon to further indicate 
possible error in the measurement. Over the years the "+/−" portion and 
"ε" spelling have gone astray in many citations, including some markings 
at the site itself, but the "+/−" is recorded on a 50th-anniversary plaque 
at the bridge's end."""
        
        # Create a Text widget
        self.smootTextArea = tkinter.Text(self.main_window, wrap = tkinter.WORD)
        self.smootTextArea.pack()
        self.smootTextArea.insert(tkinter.END, self.smootInfo)
        self.smootTextArea.config(state=tkinter.DISABLED)
        
        # Create input frame
        self.inputFrame = tkinter.Frame(self.main_window)
        # Create button frame
        self.buttonFrame = tkinter.Frame(self.main_window)
        
        # create smoot field and label
        self.smootField = tkinter.Entry(self.inputFrame, width = "10")
        self.smootLabel = tkinter.Label(self.inputFrame, text = "smoots")
        
        # create meter field and label
        self.meterField = tkinter.Entry(self.inputFrame, width = "10")
        self.meterLabel = tkinter.Label(self.inputFrame, text = "meters")
        
        # create conversion buttons
        self.smootMeterButton = tkinter.Button(self.buttonFrame, text = "smoot -> meter", command = self.getSmoots)
        self.meterSmootButton = tkinter.Button(self.buttonFrame, text = "meter -> smoot", command = self.getMeters)
        self.quitButton = tkinter.Button(self.buttonFrame, text = "Quit", command = self.main_window.destroy)
        
        # pack field and label widgets from left
        self.smootField.pack(side=tkinter.LEFT)
        self.smootLabel.pack(side=tkinter.LEFT)
        self.meterField.pack(side=tkinter.LEFT)
        self.meterLabel.pack(side=tkinter.LEFT)

        #pack buttons
        self.smootMeterButton.pack(side=tkinter.LEFT, padx = 50)
        self.meterSmootButton.pack(side=tkinter.LEFT, padx = 50)
        self.quitButton.pack(side=tkinter.LEFT, padx = 50)
        
        # pack widgets from top
        
        self.smootTextArea.pack(side=tkinter.TOP)
        self.inputFrame.pack(side=tkinter.TOP)
        self.buttonFrame.pack(side=tkinter.TOP)
        
        self.main_window.mainloop()
    
    def getSmoots(self):
        try: # Try to calculate from smootField
            smoots = float(self.smootField.get()) #convert to float
            meters = smoots * 1.7018  #calculate
            self.meterField.delete(0, tkinter.END) #clear field
            self.meterField.insert(0, "{:.2f}".format(meters)) #insert result to field
        except ValueError:
            tkinter.messagebox.showerror("Error", "Value not a valid distance")
            return
        
    def getMeters(self):
        try: # Try to calculate from meterField
            meters = float(self.meterField.get()) #convert to float
            smoots = meters / 1.7018 # calculate
            self.smootField.delete(0, tkinter.END) #clear field
            self.smootField.insert(0, "{:.2f}".format(smoots)) #insert result to field
        except ValueError:
            tkinter.messagebox.showerror("Error", "Value not a valid distance")
            return
        
def main():
    SmootGUI()

main()