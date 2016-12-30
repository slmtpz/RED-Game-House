from tkinter import *


class GameSlot(Frame):

    def __init__(self, game_slots_frame, slot_number, game_type):

        Frame.__init__(self, game_slots_frame, width=200, height=160, highlightbackground="black", highlightthickness=3)

        self.slot_number = slot_number
        self.game_type = game_type
        self.total_charge = 0.00
        self.status = 0

        self.set_inner_widgets()

    def set_inner_widgets(self):
        self.pack_propagate(0)

        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=X)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM)

        top_left_frame = Frame(top_frame, highlightthickness=1)
        top_left_frame.pack(side=LEFT)
        top_right_frame = Frame(top_frame, highlightthickness=1)
        top_right_frame.pack(side=RIGHT)

        number_label = Label(top_left_frame, text=self.slot_number, font=("Helvetica", 16))
        number_label.pack(side=LEFT)

        game_type_label = Label(top_right_frame, text=self.game_type['name'], font=("Helvetica", 16))
        game_type_label.pack(side=RIGHT)

        self.charge_label = Label(bottom_frame, text=self.total_charge, font=("Helvetica", 24))
        self.charge_label.pack()

    def set_clicked(self):
        self.config(highlightbackground="red")

    def set_released(self):
        self.config(highlightbackground="black")

    def activate(self):
        self.status = 1
        self.charge_label.config(fg="red")
