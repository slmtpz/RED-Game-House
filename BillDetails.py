from tkinter import *


class BillDetails(Frame):

    def __init__(self, bill_details_frame):
        Frame.__init__(self, bill_details_frame, width=400, height=608)
        self.pack_propagate(0)

    def set_bill_for_game_slot(self, game_slot):
        self.forget_bill()
        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM, fill=X)

        total_text_label = Label(bottom_frame, text="TOPLAM: ", fg="red", font=("Helvetica", 30))
        total_text_label.pack(side=LEFT)
        total_charge_label = Label(bottom_frame, text=game_slot.bill.total_charge, fg="red", font=("Helvetica", 30))
        total_charge_label.pack(side=RIGHT)

        for game in game_slot.bill.games:  # (game_type, number_of_players, time_passed_in_sec, game_charge)
            game_frame = Frame(self)
            game_frame.pack(side=BOTTOM, fill=X)
            m, s = divmod(game[2], 60)
            time = "%d:%02d " % (m, s)
            game_label = Label(game_frame, text=str(game[1])+" kişilik "+game[0]["name"]+", Süre: "+time, font=("Helvetica", 16))
            game_label.pack(side=LEFT)
            game_charge_label = Label(game_frame, text=str(game[3]), font=("Helvetica", 16))
            game_charge_label.pack(side=RIGHT)

        for extra in game_slot.bill.extras: # extra
            extra_frame = Frame(self)
            extra_frame.pack(side=BOTTOM, fill=X)
            extra_label = Label(extra_frame, text=extra['name'], font=("Helvetica", 16))
            extra_label.pack(side=LEFT)
            extra_charge_label = Label(extra_frame, text=extra['charge'], font=("Helvetica", 16))
            extra_charge_label.pack(side=RIGHT)

        for other in game_slot.bill.others:  # (name, charge)
            other_frame = Frame(self)
            other_frame.pack(side=BOTTOM, fill=X)
            other_label = Label(other_frame, text=other[0], font=("Helvetica", 16))
            other_label.pack(side=LEFT)
            other_charge_label = Label(other_frame, text=other[1], font=("Helvetica", 16))
            other_charge_label.pack(side=RIGHT)

    def set_bill_empty(self):
        self.forget_bill()

    def forget_bill(self):
        for widget in self.pack_slaves():
            widget.pack_forget()
        Label(self, text="RED PlayStation", fg="red", font=("fixedsys", 30, "bold")).pack()
