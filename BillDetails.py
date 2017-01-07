from tkinter import *


class BillDetails(Frame):

    def __init__(self, bill_details_frame):
        Frame.__init__(self, bill_details_frame, width=400, height=608)
        self.pack_propagate(0)

    def set_bill_for_game_slot(self, game_slot):
        self.forget_bill()
        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM, fill=X)
        bottom_left_frame = Frame(bottom_frame)
        bottom_left_frame.pack(side=LEFT)
        bottom_right_frame = Frame(bottom_frame)
        bottom_right_frame.pack(side=RIGHT)

        total_text_label = Label(bottom_left_frame, text="TOPLAM: ", font=("Helvetica", 24))
        total_text_label.pack(side=LEFT)
        total_charge_label = Label(bottom_right_frame, text=game_slot.bill.total_charge, font=("Helvetica", 24))
        total_charge_label.pack(side=RIGHT)

    def forget_bill(self):
        for widget in self.pack_slaves():
            widget.pack_forget()
