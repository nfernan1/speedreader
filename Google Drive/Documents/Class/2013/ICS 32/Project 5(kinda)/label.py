                                                                     
                                                                     
                                                                     
                                             
import tkinter







DEFAULT_FONT = ('Helvetica', 20)







class NameDialog:

    def __init__(self):

        self._dialog_window = tkinter.Toplevel()



        who_label = tkinter.Label(

            self._dialog_window, text = 'Who do you want to greet?',

            font = DEFAULT_FONT)



        who_label.grid(

            row = 0, column = 0, columnspan = 2, padx = 10, pady = 20,

            sticky = tkinter.W)



        first_name_label = tkinter.Label(

            self._dialog_window, text = 'First Name: ',

            font = DEFAULT_FONT)



        first_name_label.grid(

            row = 1, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W)



        self._first_name_entry = tkinter.Entry(

            self._dialog_window, width = 20, font = DEFAULT_FONT)



        self._first_name_entry.grid(

            row = 1, column = 1, padx = 10, pady = 10,

            sticky = tkinter.W + tkinter.E)



        last_name_label = tkinter.Label(

            self._dialog_window, text = 'Last Name: ',

            font = DEFAULT_FONT)



        last_name_label.grid(

            row = 2, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W)



        self._last_name_entry = tkinter.Entry(

            self._dialog_window, width = 20, font = DEFAULT_FONT)



        self._last_name_entry.grid(

            row = 2, column = 1, padx = 10, pady = 10,

            sticky = tkinter.W + tkinter.E)



        button_frame = tkinter.Frame(self._dialog_window)



        button_frame.grid(

            row = 3, column = 0, columnspan = 2, padx = 10, pady = 20,

            sticky = tkinter.E + tkinter.S)



        ok_button = tkinter.Button(

            button_frame, text = 'OK', font = DEFAULT_FONT,

            command = self._on_ok)



        ok_button.grid(row = 0, column = 0, padx = 10)



        cancel_button = tkinter.Button(

            button_frame, text = 'Cancel', font = DEFAULT_FONT,

            command = self._on_cancel)



        cancel_button.grid(row = 0, column = 1, padx = 10)



        self._dialog_window.rowconfigure(3, weight = 1)

        self._dialog_window.columnconfigure(1, weight = 1)



        self._ok_clicked = False

        self._first_name = ''

        self._last_name = ''





    def show(self) -> None:

        # These make the dialog box "modal", i.e., it's fully in charge

        # of everything until it goes away.

        self._dialog_window.grab_set()

        self._dialog_window.wait_window()





    def get_first_name(self) -> None:

        return self._first_name





    def get_last_name(self) -> None:

        return self._last_name





    def was_ok_clicked(self) -> bool:

        return self._ok_clicked





    def _on_ok(self) -> None:

        self._ok_clicked = True

        self._first_name = self._first_name_entry.get()

        self._last_name = self._last_name_entry.get()



        self._dialog_window.destroy()





    def _on_cancel(self) -> None:

        self._dialog_window.destroy()







class GreetingApplication:

    def __init__(self):

        self._root_window = tkinter.Tk()



        greet_button = tkinter.Button(

            self._root_window, text = 'Greet', font = DEFAULT_FONT,

            command = self._on_greet)



        greet_button.grid(

            row = 0, column = 0, padx = 10, pady = 10,

            sticky = tkinter.N)



        self._greeting_text = tkinter.StringVar()

        self._greeting_text.set('No greeting yet!')



        greeting_label = tkinter.Label(

            self._root_window, textvariable = self._greeting_text,

            font = DEFAULT_FONT)




        greeting_label.grid(

            row = 1, column = 0, padx = 10, pady = 10,

            sticky = tkinter.S)



        self._root_window.rowconfigure(0, weight = 1)

        self._root_window.rowconfigure(1, weight = 1)

        self._root_window.columnconfigure(0, weight = 1)





    def start(self) -> None:

        self._root_window.mainloop()





    def _on_greet(self) -> None:

        dialog = NameDialog()

        dialog.show()



        if dialog.was_ok_clicked():

            self._greeting_text.set(

                'Hello, ' + dialog.get_first_name()

                + ' ' + dialog.get_last_name() + '!')







if __name__ == '__main__':

    GreetingApplication().start()
