                                                                     
                                                                     
                                                                     
                                             
import tkinter





DEFAULT_FONT = ('Helvetica', 20)





class SimpleLayoutApplication:

    def __init__(self):

        self._root_window = tkinter.Tk()



        self._button1 = tkinter.Button(

            self._root_window, text = 'Button 1', font = DEFAULT_FONT)



        self._button1.grid(

            row = 0, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W + tkinter.E)



        self._button2 = tkinter.Button(

            self._root_window, text = 'Button 2', font = DEFAULT_FONT)



        self._button2.grid(

            row = 0, column = 1, padx = 10, pady = 10,

            sticky = tkinter.E + tkinter.S)



        self._canvas = tkinter.Canvas(

            self._root_window, background = '#600000')



        self._canvas.grid(

            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,

            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



        self._button_frame = tkinter.Frame(

            self._root_window, background = '#006000')



        self._button_frame.grid(

            row = 0, column = 2, rowspan = 2, padx = 10, pady = 10,

            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



        for i in range(1, 8):

            b = tkinter.Button(

                self._button_frame, text = '{}'.format(i),

                font = DEFAULT_FONT)



            b.grid(row = i - 1, column = 0)



        self._root_window.rowconfigure(0, weight = 1)

        self._root_window.rowconfigure(1, weight = 10)

        self._root_window.columnconfigure(0, weight = 1)

        self._root_window.columnconfigure(1, weight = 2)





    def start(self) -> None:

        self._root_window.mainloop()









if __name__ == '__main__':

    SimpleLayoutApplication().start()
