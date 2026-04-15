#Micah Trost
#4/15/2026
#Simple GUI
#Create a GUI window that displays your favorite saying.

import tkinter

class MyGUI:
    def __init__ (self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Favorite Saying")
        self.label1 = tkinter.Label(self.main_window,
                                   text="I like John Deere tractors!")
        self.label2 = tkinter.Label(self.main_window,
                                    text = "They are the best!")
        self.label1.pack()
        self.label2.pack()
        tkinter.mainloop()

if __name__ == "__main__":
    my_gui = MyGUI()