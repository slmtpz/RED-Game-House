from tkinter import *


class GameSlot():

    def __init__(self, master, slot_number, game_type):


        #top_frame = Frame(self.frame)  # have to be self?
        #top_frame.pack()
        #bottom_frame = Frame(self.frame)
        #bottom_frame.pack(side=BOTTOM)


        self.frame = master
        self.frame.grid_propagate(0)

        self.number_label = Label(self.frame, text=slot_number, bg="red")
        self.number_label.grid(row=0, column=0)

        self.game_type_label = Label(self.frame, text=game_type['name'], bg="green")
        self.game_type_label.grid(row=0, column=1)

        self.total_charge = 0.00
        self.charge_label = Label(self.frame, text=self.total_charge, bg="blue")
        self.charge_label.grid(columnspan=2)

        self.status = 0

        self.delog_frame_sizes()

    def activate(self):
        self.status = 1
        self.frame.config(highlightbackground="red")

    def delog_frame_sizes(self):
        self.frame.update()
        print(self.frame.winfo_height())
        print(self.frame.winfo_width())
