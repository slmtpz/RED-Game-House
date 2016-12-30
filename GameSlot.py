from tkinter import *


class GameSlot(Frame):

    def __init__(self, game_slots_frame, slot_number, game_type):

        Frame.__init__(self, game_slots_frame, width=200, height=160, highlightbackground="black", highlightthickness=2)

        self.pack_propagate(0)

        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=X)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM)

        top_left_frame = Frame(top_frame, highlightthickness=1, highlightbackground="black")
        top_left_frame.pack(side=LEFT)
        top_right_frame = Frame(top_frame, highlightthickness=1, highlightbackground="black")
        top_right_frame.pack(side=RIGHT)

        self.number_label = Label(top_left_frame, text=slot_number, font=("Helvetica", 16))
        self.number_label.pack(side=LEFT)

        self.game_type_label = Label(top_right_frame, text=game_type['name'], font=("Helvetica", 16))
        self.game_type_label.pack(side=RIGHT)

        self.total_charge = 0.00
        self.charge_label = Label(bottom_frame, text=self.total_charge, font=("Helvetica", 24))
        self.charge_label.pack()

        self.status = 0

    def activate(self):
        self.status = 1
        self.config(highlightbackground="red")