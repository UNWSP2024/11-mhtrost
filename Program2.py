#Micah Trost
#4/15/2026
#Program 2

import tkinter
class MyGUI:
    def __init__ (self):
        self.main_window = tkinter.Tk()
        self.main_window.title("My Info")
        self.label1 = tkinter.Label(self.main_window,
                                   text="My name is Micah Trost.")
        self.label2 = tkinter.Label(self.main_window,
                                    text = "I live at 19399 Inga Ave. Hastings, MN 55033")
        self.button1 = tkinter.Button(self.main_window,
                                     text = "Show Info",
                                     command = self.show_info)
        self.button2 = tkinter.Button(self.main_window,
                                     text = "Quit",
                                     command = self.main_window.destroy)
        self.button1.pack()
        self.button2.pack()

    def show_info(self):
        self.label1.pack()
        self.label2.pack()

if __name__  == "__main__":
    my_gui = MyGUI()
    tkinter.mainloop()