import tkinter


DEFAULT_FONT = ('Helvetica', 20)

class NameDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        who_label = tkinter.Label(
            self._dialog_window, text = 'Who do you want to greet?',
            font = DEFAULT_FONT)

        who_label.grid(row = 0, colun = 0, columnspan = 2,
                       sticky = tkinter.W)

        first_name_entry = tkinter.Entry(
            self._dialog_window, width = 20, font = DEFAULT_FONT)

        first_name_entry.grid(row = 1, column =1, padx = 10, pady = 10,
                              sticky = tkinter.W + tkinter.E)

        first_name_label = tkinter.Label(
            self._dialog_window, text = 'First Name: ',
            font = DEFAULT_FONT)

        last_name_entry.grid(row = 2, column =1, padx = 10, pady =10,
                             sticky = tkinter.W + tkinter.E)

        last_name_label = tkinter.Label(
            self._dialog_window, text = 'Last Name: ',
            font = DAFUALT_FONT)

        last_name_label.grid(row = 2, column = 0, padx = 10, pady =10)

        button_frame = tkinter.Frame(self._dialog_window)

        button_grame.grid(row = 3)

        
    def show(self)-> None:
        # These make the dialog box 'modal', i.e., it's fully in charge 
        # what it means to grab--if anything happens in this app then only you handle it
        # I want to set you to do the grabbing
        self._dialog_window.grab_set()
        # wait for this window to go away--somebody clicks on greet
        self._dialog_window.wait_window()



        

class GreetingApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()
        

        #Only thing that needs to be known about the button is that
        #it only has one job: TELL ME WHEN SOMEONE CLICKS YOU
        #NEVER need to look at the button again
        
        greet_button = tkinter.Button(
            self._root_window, text = 'Greet', font = DEFAULT_FONT,
            command = self._on_greet)

        greet_button.grid(row = 0, column = 0,padx = 10, pady =10)

        # changes value of multiple things in GUI
        self._greeting_text = tkinter.StringVar()
        self._greeting_text.set('No greeting yet!')

        greeting_label = tkinter.Label(
            self._root_window, textvariable = self._greeting_text,
            font = DEFAULT_FONT)

        greeting_label.grid(
            row = 1, column = 0,padx = 10,pady = 10,
            sticky = tkinter.S)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        
        
        
    def start(self)-> None:
        self._root_window.mainloop()

    def _on_greet(self):
        self.NameDialog.show()



if __name__ == "__main__":
    GreetingApplication().start()


# sooner you can validate where you want to be the better
# Not to make that label a string--when setting label as a string = display text
# and I dont plan to change it
# how to tell tkinter to allow the text to change--instead of mkaing text a string
# use a control variable--associate with the label--a stringVar--special string
# put the value 'no greeting yet'
#
