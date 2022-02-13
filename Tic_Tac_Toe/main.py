import tkinter as tk


class MyButton(tk.Button):
    def __init__(self, x=0, master=None, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.number = x
        self.text = ''


class TicTac:
    window = tk.Tk()
    window.title('Tic Tac Toe')
    window.geometry('400x300')

    def __init__(self):
        self.btn_restart = tk.Button(text='Restart', command=self.restart)
        self.btn_restart.grid(column=4, row=1)

    def create_table(self):
        self.IS_GAME_OVER = False
        self.label = tk.Label(text='Добро пожаловать!\n Первый ход игрока_1 - X')
        self.label.grid(column=4, row=0)
        self.buttons = []
        self.step = 1
        self.but_is = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        for i in range(3):
            temp = []
            for j in range(3):
                btn = MyButton(text='', width=5, heigh=2)
                btn.config(command=lambda but=btn: self.click(but))
                temp.append(btn)
            self.buttons.append(temp)
        btn_numb = 1
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.number = btn_numb
                btn_numb += 1
                btn.grid(column=j, row=i)

    def restart(self):
        self.game_start()

    def game_start(self):
        self.create_table()
        self.window.mainloop()

    def check(self, button):
        win_comb = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        if self.step > 4:
            for each in win_comb:
                if button[each[0]] == button[each[1]] == button[each[2]]:
                    if button[each[0]] == 'X':
                        self.label.config(text="Игрок_1 победил")
                    elif button[each[0]] == 'O':
                        self.label.config(text="Игрок_2 победил")
                    self.IS_GAME_OVER = True

    def click(self, btn):
        if self.IS_GAME_OVER:
            return
        if btn.text != 'X' and btn.text != 'O':
            if self.step % 2 != 0:
                self.label.config(text='Ход игрока_2')
                btn.config(text='X')
                btn.text = 'X'
                self.but_is[btn.number] = 'X'
                self.check(self.but_is)
                self.step += 1
            else:
                self.label.config(text='Ход игрока_1')
                btn.config(text='O')
                btn.text = 'O'
                self.but_is[btn.number] = 'O'
                self.check(self.but_is)
                self.step += 1


game = TicTac()
game.game_start()
