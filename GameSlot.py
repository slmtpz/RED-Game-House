from tkinter import *
from Bill import *
from consumption_parser import foods, drinks
import CafeDB as db


class GameSlot(Frame):

    def __init__(self, game_slots_frame, slot_number, game_info):

        Frame.__init__(self, game_slots_frame, highlightbackground="black", highlightthickness=3)

        self.game_info = game_info
        self.slot_number = slot_number
        self.game_type = game_info['type']
        self.game_status = 0
        self.number_of_players = 0
        self.time_passed_in_sec = IntVar()
        self.bill = Bill()

        self.clickable_chidren = []
        self.set_inner_widgets()

    def set_bill(self, bill):
        self.bill = bill
        self.pay_bill_button.pack(side=RIGHT)
        self.add_extra_button.pack(side=LEFT)
        self.transact_game_slot_button.pack(side=LEFT)

    def set_inner_widgets(self):
        self.pack_propagate(0)

        self.top_frame = Frame(self)
        self.top_frame.pack(side=TOP, fill=X)
        self.clickable_chidren.append(self.top_frame)
        self.middle_frame = Frame(self)
        self.middle_frame.pack(side=BOTTOM, fill=X)
        self.clickable_chidren.append(self.middle_frame)
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM)
        self.clickable_chidren.append(self.bottom_frame)

        self.top_left_frame = Frame(self.top_frame, highlightthickness=1)
        self.top_left_frame.pack(side=LEFT)
        self.clickable_chidren.append(self.top_left_frame)
        self.top_right_frame = Frame(self.top_frame, highlightthickness=1)
        self.top_right_frame.pack(side=RIGHT)
        self.clickable_chidren.append(self.top_right_frame)

        self.middle_left_frame = Frame(self.middle_frame, highlightthickness=1)
        self.middle_left_frame.pack(side=LEFT)
        self.clickable_chidren.append(self.middle_left_frame)
        self.middle_right_frame = Frame(self.middle_frame, highlightthickness=1)
        self.middle_right_frame.pack(side=RIGHT)
        self.clickable_chidren.append(self.middle_right_frame)

        # number_label = Label(self.top_left_frame, text=self.slot_number, font=("Helvetica", 16))
        # number_label.pack(side=LEFT)
        self.game_slot_name_label = Label(self.top_left_frame, text=self.game_info['name'], font=("Helvetica", 16))
        self.game_slot_name_label.pack(side=LEFT)
        self.clickable_chidren.append(self.game_slot_name_label)

        # game_type_label = Label(self.top_right_frame, text=self.game_type['name'], font=("Helvetica", 16))
        # game_type_label.pack(side=RIGHT)

        self.number_of_players_var = IntVar(self.middle_left_frame)
        self.number_of_players_option = OptionMenu(self.middle_left_frame, self.number_of_players_var, *[1, 2, 3, 4])
        self.number_of_players_var.set(2)
        self.number_of_players_option.pack(side=LEFT)

        self.start_button = Button(self.middle_left_frame, text="Başlat", fg="green", font=("Helvetica", 12))
        self.start_button.bind("<Button-1>", self.start)
        self.start_button.pack(side=LEFT)

        # removed due to customer feedback
        # self.change_number_of_players_button = Button(self.middle_left_frame, text="Değiştir", fg="orange", font=("Helvetica", 12))
        # self.change_number_of_players_button.bind("<Button-1>", self.change_number_of_players)

        self.finish_button = Button(self.middle_right_frame, text="Bitir", fg="red", font=("Helvetica", 12))
        self.finish_button.bind("<Button-1>", self.finish)

        self.pay_bill_button = Button(self.middle_right_frame, text="Kapat", fg="red", font=("Helvetica", 12))
        self.pay_bill_button.bind("<Button-1>", self.pay_bill)

        self.game_status_text = StringVar()
        self.game_status_text.set(str(self.bill.get_total_charge(self.game_type, self.number_of_players, self.time_passed_in_sec.get())) + " / " + str(self.number_of_players))
        self.charge_label = Label(self.bottom_frame, textvariable=self.game_status_text, font=("Helvetica", 26))
        self.clickable_chidren.append(self.charge_label)

        self.add_extra_button = Button(self.middle_left_frame, text="Ekle", fg="purple", font=("Helvetica", 10))
        self.add_extra_button.bind("<Button-1>", self.add_extra)

        ## ## debug
        ## self.time_label = Label(self.top_left_frame, textvariable=self.time_passed_in_sec, font=("Helvetica", 16))
        ## self.time_label.pack(side=LEFT)
        ## ## debug

    def second_hit(self):
        if self.game_status == 1:
            self.time_passed_in_sec.set(self.time_passed_in_sec.get() + 1)
            self.game_status_text.set(str(self.bill.get_total_charge(self.game_type, self.number_of_players, self.time_passed_in_sec.get())) + " / " + str(self.number_of_players))
            self.after(1000, self.second_hit)

    def set_clicked(self):
        self.config(highlightbackground="red")

    def set_released(self):
        self.config(highlightbackground="black")

    def start(self, event):
        self.game_status = 1
        self.bill.is_active = True
        self.bill.startingTime = datetime.datetime.now()
        self.set_start_ui()
        self.update()  # update before delay

        self.time_passed_in_sec.set(-1)
        self.second_hit()  # delay

    def set_start_ui(self):
        self.charge_label.config(fg="red")
        self.number_of_players_option.forget()
        self.start_button.pack_forget()
        self.number_of_players = self.number_of_players_var.get()
        self.game_status_text.set(str(self.bill.get_total_charge(self.game_type, self.number_of_players, self.time_passed_in_sec.get())) + " / " + str(self.number_of_players))
        self.charge_label.pack()
        self.pay_bill_button.pack_forget()
        self.transact_game_slot_button.forget()
        self.finish_button.pack(side=RIGHT)
        #self.change_number_of_players_button.pack(side=LEFT)
        self.add_extra_button.pack(side=LEFT)

    # removed due to customer feedback
    # def change_number_of_players(self, event):
    #     self.bill.add_game(self.game_type, self.number_of_players, self.time_passed_in_sec.get())
    #     self.number_of_players = self.number_of_players_var.get()
    #     self.time_passed_in_sec.set(0)
    #     self.game_status_text.set(str(self.bill.get_total_charge(self.game_type, self.number_of_players, self.time_passed_in_sec.get())) + " / " + str(self.number_of_players))

    def finish(self, event):
        self.bill.add_game(self.game_type, self.number_of_players, self.time_passed_in_sec.get())
        self.game_status = 0
        self.number_of_players = 0

        self.set_finish_ui()

    def set_finish_ui(self):
        self.charge_label.config(fg="black")
        self.finish_button.pack_forget()
        self.pay_bill_button.pack(side=RIGHT)
        #self.change_number_of_players_button.forget()
        self.game_status_text.set(self.bill.total_charge)
        self.add_extra_button.forget()
        self.number_of_players_option.pack(side=LEFT)
        self.after(1000, self.start_button.pack(side=LEFT))
        self.add_extra_button.pack(side=LEFT)
        self.transact_game_slot_button.pack(side=LEFT)

    def pay_bill(self, event):
        self.set_pay_bill_ui()
        self.bill.endingTime = datetime.datetime.now()
        db.saveBill(self.bill)

        self.bill = Bill()

    def set_pay_bill_ui(self):
        self.pay_bill_button.pack_forget()
        self.charge_label.pack_forget()
        self.add_extra_button.forget()
        self.transact_game_slot_button.forget()

    def add_extra(self, event):
        menu = Toplevel()
        menu.title("Ekle...")

        row = 0
        column = 0
        for extra in foods:
            # PRINT(extra['name'] + " row: " + str(row) + " column: " + str(column))
            food_button = Button(menu, text=extra['name']+": "+str(extra['charge']), anchor=W, font=("Helvetica", 8), command=lambda extra=extra:self.bill.add_extra(extra))
            food_button.grid(row=row, column=column, sticky=W+E+S+N)
            row += 1
            if row > 20:
                row = 0
                column += 1
        row = 0
        column += 1
        for extra in drinks:
            drink_button = Button(menu, text=extra['name']+": "+str(extra['charge']), anchor=W, font=("Helvetica", 8), command=lambda extra=extra:self.bill.add_extra(extra))
            drink_button.grid(row=row, column=column, sticky=W+E+S+N)
            row += 1
            if row > 20:
                row = 1
                column += 1

        add_other_button = Button(menu, text="Başka...", fg="blue", font=("Helvetica", 12), command=self.add_other_popup)
        add_other_button.grid(columnspan=2, sticky=W+E+S+N)
        quit_button = Button(menu, text="Kapat", fg="red", font=("Helvetica", 12), command=menu.destroy)
        quit_button.grid(columnspan=2, sticky=W+E+S+N)



    def add_other_popup(self):
        menu = Toplevel()
        menu.title("Başka ekle...")

        desc_label = Label(menu, text="Açıklama:")
        charge_label = Label(menu, text="Ücret:")
        description = StringVar()
        desc_entry = Entry(menu, textvariable=description)
        charge = DoubleVar()
        charge_entry = Entry(menu, textvariable=charge)

        desc_label.grid(row=0)
        charge_label.grid(row=1)
        desc_entry.grid(row=0, column=1)
        charge_entry.grid(row=1, column=1)

        submit_button = Button(menu, text="Ekle", command=lambda: self.bill.add_other(description.get(), float(charge.get())))
        submit_button.grid(columnspan=2)
