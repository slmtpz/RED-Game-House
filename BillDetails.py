from tkinter import *


class BillDetails(Frame):

    def __init__(self, bill_details_frame):
        Frame.__init__(self, bill_details_frame, width=400, height=608)
        self.pack_propagate(0)

    def set_bill_for_game_slot(self, game_slot):
        self.forget_bill()
        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM, fill=X)

        total_text_label = Label(bottom_frame, text="TOPLAM: ", font=("Helvetica", 24))
        total_text_label.pack(side=LEFT)
        total_charge_label = Label(bottom_frame, text=game_slot.bill.total_charge, font=("Helvetica", 24))
        total_charge_label.pack(side=RIGHT)

        for game in game_slot.bill.games:  # (game_type, number_of_players, time_passed_in_sec, game_charge)
            game_frame = Frame(self)
            game_frame.pack(side=BOTTOM, fill=X)
            game_label = Label(game_frame, text=game[0]["name"]+" / "+str(game[1]), font=("Helvetica", 16))
            game_label.pack(side=LEFT)
            game_charge_label = Label(game_frame, text=str(game[2])+" / "+str(game[3]))
            game_charge_label.pack(side=RIGHT)


    def forget_bill(self):
        for widget in self.pack_slaves():
            widget.pack_forget()
