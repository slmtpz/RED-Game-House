from tkinter import *
from GameSlot import GameSlot
from BillDetails import BillDetails
import random


number_of_game_slots = 22
max_game_slots_in_one_row = 5
game_types = [
    {
        'name': 'Playstation',
        'charge': 5.00
    },
    {
        'name': 'Guitar Hero',
        'charge': 7.00
    },
    {
        'name': 'Bilardo',
        'charge': 10.00
    },
    {
        'name': 'Langırt',
        'charge': 1.00
    }
]
extras = [
    {
        'name': 'Cake',
        'charge': 0.50
    },
    {
        'name': 'Coke 330ml',
        'charge': 2.50
    }
]


root = Tk()
root.wm_title("RED Game House")

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


for i in range(0, number_of_game_slots):
    game_slot = GameSlot(game_slots_frame, i + 1, random.choice(game_types))
    game_slot.grid(row=int(i/max_game_slots_in_one_row), column=i % max_game_slots_in_one_row, padx=10, pady=10)
    game_slot.bind("<Button-1>", generate_bill_details)

bill_details = BillDetails(bill_detail_frame)
bill_details.pack(side=LEFT, fill=BOTH)

root.update()
print("height")
print(root.winfo_height())
print("width")
print(root.winfo_width())
root.mainloop()

