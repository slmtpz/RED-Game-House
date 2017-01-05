from tkinter import *
from Bill import *
import time


class GameSlot(Frame):

    def __init__(self, game_slots_frame, slot_number, game_type, bill=Bill()):

        Frame.__init__(self, game_slots_frame, width=200, height=160, highlightbackground="black", highlightthickness=3)

        self.slot_number = slot_number
        self.game_type = game_type
        self.game_status = 0
        self.number_of_players = 0
        self.time_passed_in_sec = IntVar()
        self.bill = bill

        self.set_inner_widgets()

    def set_inner_widgets(self):
        self.pack_propagate(0)

        top_frame = Frame(self)
        top_frame.pack(side=TOP, fill=X)
        middle_frame = Frame(self)
        middle_frame.pack(side=BOTTOM, fill=X)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM)

        top_left_frame = Frame(top_frame, highlightthickness=1)
        top_left_frame.pack(side=LEFT)
        top_right_frame = Frame(top_frame, highlightthickness=1)
        top_right_frame.pack(side=RIGHT)

        middle_left_frame = Frame(middle_frame, highlightthickness=1)
        middle_left_frame.pack(side=LEFT)
        middle_right_frame = Frame(middle_frame, highlightthickness=1)
        middle_right_frame.pack(side=RIGHT)

        number_label = Label(top_left_frame, text=self.slot_number, font=("Helvetica", 16))
        number_label.pack(side=LEFT)

        game_type_label = Label(top_right_frame, text=self.game_type['name'], font=("Helvetica", 16))
        game_type_label.pack(side=RIGHT)

        self.number_of_players_var = IntVar(middle_left_frame)
        number_of_players_option = OptionMenu(middle_left_frame, self.number_of_players_var, *[1, 2, 3, 4, 5, 6])
        self.number_of_players_var.set(2)
        number_of_players_option.pack(side=LEFT)

        self.start_button = Button(middle_left_frame, text="Başlat", fg="green", font=("Helvetica", 12))
        self.start_button.bind("<Button-1>", self.start)
        self.start_button.pack(side=LEFT)

        self.change_number_of_players_button = Button(middle_left_frame, text="Değiştir", fg="orange", font=("Helvetica", 12))
        self.change_number_of_players_button.bind("<Button-1>", self.change_number_of_players)

        self.finish_button = Button(middle_right_frame, text="Bitir", fg="red", font=("Helvetica", 12))
        self.finish_button.bind("<Button-1>", self.finish)

        self.game_status_text = StringVar()
        self.game_status_text.set(str(self.bill.total_charge) + " / " + str(self.number_of_players))
        self.charge_label = Label(bottom_frame, textvariable=self.game_status_text, font=("Helvetica", 26))

        ## debug
        self.time_label = Label(top_left_frame, textvariable=self.time_passed_in_sec, font=("Helvetica", 16))
        self.time_label.pack(side=LEFT)
        ## debug

    def second_hit(self):
        if self.game_status == 1:
            self.time_passed_in_sec.set(self.time_passed_in_sec.get() + 1)
            self.game_status_text.set(str(self.bill.total_charge) + " / " + str(self.number_of_players))
            self.after(1000, self.second_hit)

    def set_clicked(self):
        self.config(highlightbackground="red")

    def set_released(self):
        self.config(highlightbackground="black")

    def start(self, event):
        self.game_status = 1
        self.bill.is_active = True

        self.set_start_ui()
        self.update()  # update before delay

        self.time_passed_in_sec.set(-1)
        self.second_hit()  # delay

    def set_start_ui(self):
        self.charge_label.config(fg="red")
        self.start_button.pack_forget()
        self.number_of_players = self.number_of_players_var.get()
        self.game_status_text.set(str(self.bill.total_charge) + " / " + str(self.number_of_players))
        self.charge_label.pack()
        self.finish_button.pack(side=RIGHT)
        self.change_number_of_players_button.pack(side=LEFT)

    def change_number_of_players(self, event):
        self.bill.add_game(self.game_type, self.number_of_players, self.time_passed_in_sec)
        self.number_of_players = self.number_of_players_var.get()
        self.time_passed_in_sec.set(0)
        self.game_status_text.set(str(self.bill.total_charge) + " / " + str(self.number_of_players))

    def finish(self, event):
        self.bill.add_game(self.game_type, self.number_of_players, self.time_passed_in_sec)
        self.game_status = 0
        self.number_of_players = 0

        self.set_finish_ui()

    def set_finish_ui(self):
        self.charge_label.config(fg="black")
        self.finish_button.pack_forget()
        self.change_number_of_players_button.forget()
        self.game_status_text.set(str(self.bill.total_charge))
        self.after(1000, self.start_button.pack(side=LEFT))

    def pay_bill(self):
        self.bill = Bill()
        self.charge_label.forget()



