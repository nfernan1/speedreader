#Nicholas Fernando 12659548

import tkinter
import othelloguitest

DEFAULT_FONT= ('Helvetica', 16)
DFONT = ('Helvetica', 14)


class InputBox:
    '''Inputs that are put into the gamestate'''

    def __init__(self):#, col: int, row: int, player: str, winning_method: str):


        self._dialog_window = tkinter.Tk()
        self._dialog_window.resizable(width = 'False', height = 'False')
        self._dialog_window.title('Input Options')
        
        self.col = tkinter.IntVar()
        self.col.set(4)
        
        self.row = tkinter.IntVar()
        self.row.set(4)
        
        self.win_strang = tkinter.StringVar()
        self.win_strang.set('m')
        
        self.player_strang = tkinter.StringVar()
        self.player_strang.set('B')

        self.start_strang = tkinter.StringVar()
        self.start_strang.set('W')


        #important options
        option_label = tkinter.Label(
            self._dialog_window, text = 'Input Important Options',
            font = DEFAULT_FONT)

        option_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 12,
            sticky = tkinter.N)

        #column size   
        column_label = tkinter.Label(self._dialog_window, text = 'Select a Column Size:',
                                    font = DFONT).grid(row = 1, column = 0, columnspan = 1, padx = 10,
                                                 sticky = tkinter.W)

        col4 = tkinter.Radiobutton(self._dialog_window, text = '4', padx=10, variable=self.col,
                                   value = 4).grid(row = 2, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)
        
        col6 = tkinter.Radiobutton(self._dialog_window, text = '6', padx=10, variable=self.col,
                                   value = 6).grid(row = 3, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)

        col8 = tkinter.Radiobutton(self._dialog_window, text = '8', padx=10, variable=self.col,
                                   value = 8).grid(row = 4, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)
        
        col10 = tkinter.Radiobutton(self._dialog_window, text = '10', padx=10, variable=self.col,
                                   value = 10).grid(row = 5, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)
        
        col12 = tkinter.Radiobutton(self._dialog_window, text = '12', padx=10, variable=self.col,
                                   value = 12).grid(row = 6, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)

        col14 = tkinter.Radiobutton(self._dialog_window, text = '14', padx=10, variable=self.col,
                                   value = 14).grid(row = 7, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)

        col16 = tkinter.Radiobutton(self._dialog_window, text = '16', padx=10, variable=self.col,
                                   value = 16).grid(row = 8, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)

        

        #row size
        row_label = tkinter.Label(
            self._dialog_window, text = 'Select a Row size: ',
            font = DFONT).grid(row = 1, column = 1, columnspan = 1, padx = 10, pady = 10,
                                sticky = tkinter.E)

        row4 = tkinter.Radiobutton(self._dialog_window, text = '4', padx=10, variable=self.row,
                                   value = 4).grid(row = 2, column = 0, columnspan = 2,
                                                padx = 19, sticky = tkinter.E)
        
        row6 = tkinter.Radiobutton(self._dialog_window, text = '6', padx=10, variable=self.row,
                                   value = 6).grid(row = 3, column = 0, columnspan = 2,
                                                padx = 19, sticky = tkinter.E)

        row8 = tkinter.Radiobutton(self._dialog_window, text = '8', padx=10, variable=self.row,
                                   value = 8).grid(row = 4, column = 0, columnspan = 2,
                                                padx = 19, sticky = tkinter.E)
        
        row10 = tkinter.Radiobutton(self._dialog_window, text = '10', padx=10, variable=self.row,
                                   value = 10).grid(row = 5, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.E)
        
        row12 = tkinter.Radiobutton(self._dialog_window, text = '12', padx=10, variable=self.row,
                                   value = 12).grid(row = 6, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.E)

        row14 = tkinter.Radiobutton(self._dialog_window, text = '14', padx=10, variable=self.row,
                                   value = 14).grid(row = 7, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.E)

        row16 = tkinter.Radiobutton(self._dialog_window, text = '16', padx=10, variable=self.row,
                                   value = 16).grid(row = 8, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.E)


        #player choice
        player_label = tkinter.Label(
            self._dialog_window, text = 'Select a Player: ',
            font = DFONT).grid(row = 9, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        row4 = tkinter.Radiobutton(self._dialog_window, text = 'Black', padx=10, variable=self.player_strang,
                                   value = 'B').grid(row = 10, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)
        
        row6 = tkinter.Radiobutton(self._dialog_window, text = 'White', padx=10, variable=self.player_strang,
                                   value = 'W').grid(row = 11, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)


        #winning_method choice
        winningmethod_label = tkinter.Label(
            self._dialog_window, text = '''Select a Winning Method:
        [M]ost or [L]east Discs''',
            font = DFONT)

        winningmethod_label.grid(
            row = 9, column = 1, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        winM = tkinter.Radiobutton(self._dialog_window, text = 'Most Discs', padx=10, variable=self.win_strang,
                                   value = 'm').grid(row = 10, column = 0, columnspan = 2,
                                                padx = 12, sticky = tkinter.E)
        
        winL = tkinter.Radiobutton(self._dialog_window, text = 'Least Discs', padx=10, variable=self.win_strang,
                                   value = 'l').grid(row = 11, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.E)

        

        #starting tile placement
        starttileplace_label = tkinter.Label(
            self._dialog_window, text = 'Select Tile Color in left corner: ', 
            font = DFONT).grid(row = 12, column = 0, columnspan = 1, padx = 10, pady = 10,
                            sticky = tkinter.W)

        spieceW = tkinter.Radiobutton(self._dialog_window, text = 'White', padx=10, variable=self.start_strang,
                                   value = 'W').grid(row = 13, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)
        
        spieceB = tkinter.Radiobutton(self._dialog_window, text = 'Black', padx=10, variable=self.start_strang,
                                   value = 'B').grid(row = 14, column = 0, columnspan = 2,
                                                padx = 10, sticky = tkinter.W)






        button_frame = tkinter.Frame(self._dialog_window)

        button_frame.grid(
            row = 15, column = 0, columnspan = 2, padx = 10, pady = 20,
            sticky = tkinter.E + tkinter.S)


        ok_button = tkinter.Button(
            button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok)



        ok_button.grid(row = 15, column = 0, padx = 10)


        cancel_button = tkinter.Button(
            button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel)



        cancel_button.grid(row = 15, column = 1, padx = 10)

        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._ok_clicked = False
        
    
    def show(self):
        '''Lets another window pop up the inputbox'''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self):
        '''Checks if the ok button was clicked'''

        return self._ok_clicked

        
    def _on_ok(self):
        'Assigns the information the user inputs into the othellogui'
        self._ok_clicked = True

        self._column = self.col.get()
        self._row = self.row.get()
        self._player_strang = self.player_strang.get()
        self._win_strang = self.win_strang.get()
        self._start_strang = self.start_strang.get()
    

        self._dialog_window.destroy()

        othelloguitest.OthelloGui(self._column, self._row,self._player_strang,
                                  self._win_strang, self._start_strang).start()




    def _on_cancel(self):
        'Destroys the input box window when cancel is clicked'

        self._dialog_window.destroy()

        
    def start(self):
        '''Starts the input box window'''
        self._dialog_window.mainloop()

class StartGameApplication:
    'Button that pops up the InputBox window'
    def __init__(self):
        self._root = tkinter.Tk()

        startgame_button = tkinter.Button(
            self._root, text = 'Click Here to Start Game', font = ('Helvetica', 50),
            command = self._startg, width = 10, height = 5)

        startgame_button.grid(
            row = 0, column = 0, padx = 20, pady = 10,
            sticky = tkinter.N)


        self._root.rowconfigure(0, weight = 1)
        self._root.rowconfigure(1, weight = 1)
        self._root.columnconfigure(0, weight = 1)

    def start(self):
        'Starts the window for the start game button'
        self._root.mainloop()

    def _startg(self):
        'Destroys the start game root window and pops up the input box root window'
        self._root.destroy()
        choice = InputBox()
        choice.show()


if __name__ == '__main__':

    StartGameApplication().start()


