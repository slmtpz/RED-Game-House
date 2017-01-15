from tkinter import *
from GameSlot import GameSlot
from BillDetails import BillDetails
from consumption_parser import *

max_game_slots_in_one_row = 3
parse_consumption()
game_types = [
    {
        'name': 'Playstation',
        'charge': 5.00
    },
    {
        'name': 'Loca/Playstation',
        'charge': 10.00
    }
]
game_slots_info = [
    {
        'name': 'RED 1',
        'type': game_types[0],
    },
    {
        'name': 'RED 2',
        'type': game_types[0],
    },
    {
        'name': 'RED 3',
        'type': game_types[0],
    },
    {
        'name': 'RED 4',
        'type': game_types[0],
    },
    {
        'name': 'RED 5',
        'type': game_types[0],
    },
    {
        'name': 'RED 6',
        'type': game_types[0],
    },
    {
        'name': 'RED 7',
        'type': game_types[0],
    },
    {
        'name': 'RED 8',
        'type': game_types[0],
    },
    {
        'name': 'Loca 1',
        'type': game_types[1],
    },
    {
        'name': 'Loca 2',
        'type': game_types[1],
    },
    {
        'name': 'Loca 3',
        'type': game_types[1],
    },
]

root = Tk()
root.wm_title("RED Playstation")

# I HATE FRONTEND
# after all is finished, get the full screen size and assign frames with percentages..


game_slots_frame = Frame(root, width=500, height=608, highlightbackground="Orange", highlightthickness=4)
game_slots_frame.pack(side=LEFT, fill=BOTH)

bill_detail_frame = Frame(root, width=400, height=608, highlightbackground="Purple", highlightthickness=4)
bill_detail_frame.pack(side=LEFT, fill=BOTH)


saved_clicked_game_slot = -1


def generate_bill_details(event):
    global saved_clicked_game_slot
    clicked_game_slot = event.widget

    if saved_clicked_game_slot == clicked_game_slot:
        clicked_game_slot.set_released()
        bill_details.set_bill_empty()
        saved_clicked_game_slot = -1
    else:
        clicked_game_slot.set_clicked()
        if saved_clicked_game_slot != -1:
            saved_clicked_game_slot.set_released()
        saved_clicked_game_slot = clicked_game_slot
        bill_details.set_bill_for_game_slot(clicked_game_slot)


def transact_game_slot(org_game_slot):
    menu = Toplevel()
    menu.title("Taşı...")

    for game_slot in game_slots_frame.winfo_children():
        if not game_slot.bill.is_active:
            Button(menu, text=str(game_slot.game_info['name']), font=("Helvetica", 16), command=lambda game_slot=game_slot: transact(org_game_slot, game_slot, menu)).pack()

    quit_button = Button(menu, text="Kapat", fg="red", command=menu.destroy).pack()


def transact(org_game_slot, new_game_slot, menu):
    menu.destroy()
    bill = org_game_slot.bill
    org_game_slot.pay_bill(0)
    new_game_slot.set_bill(bill)

for i in range(0, game_slots_info.__len__()):
    game_slot = GameSlot(game_slots_frame, i + 1, game_slots_info[i])
    game_slot.grid(row=int(i/max_game_slots_in_one_row), column=i % max_game_slots_in_one_row, padx=10, pady=10)
    game_slot.bind("<Button-1>", generate_bill_details)

    game_slot.transact_game_slot_button = Button(game_slot.middle_left_frame, text="Taşı", fg="brown", font=("Helvetica", 12), command=lambda game_slot=game_slot: transact_game_slot(game_slot))

bill_details = BillDetails(bill_detail_frame)
bill_details.pack(side=LEFT, fill=BOTH)

# root.update()
# print("height")
# print(root.winfo_height())
# print("width")
# print(root.winfo_width())
root.mainloop()

