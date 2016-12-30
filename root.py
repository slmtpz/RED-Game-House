from tkinter import *
from GameSlot import *
import random


number_of_game_slots = 14
max_game_slots_in_one_row = 5
game_slot_places = [1, 1, 1, 1, 1,
                    1, 0, 0, 0, 1,
                    0, 0, 1, 1, 1,
                    0, 0, 1, 1, 1,
                    1, 1, 0]
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


root = Tk()
root.wm_title("RED Game House")

# I HATE FRONTEND
# after all is finished, get the full screen size and assign frames with percentages..


game_slots_frame = Frame(root, width=1100, height=908, highlightbackground="Orange", highlightthickness=4)
game_slots_frame.pack(side=LEFT, fill=BOTH)

bill_detail_frame = Frame(root, width=400, height=908, highlightbackground="Purple", highlightthickness=4)
bill_detail_frame.pack(side=LEFT, fill=BOTH)


saved_clicked_game_slot = -1


def generate_bill_details(event):
    global saved_clicked_game_slot
    clicked_game_slot = event.widget

    if saved_clicked_game_slot == clicked_game_slot:
        clicked_game_slot.config(highlightbackground="black")
        saved_clicked_game_slot = -1
    else:
        clicked_game_slot.config(highlightbackground="red")
        if saved_clicked_game_slot != -1:
            saved_clicked_game_slot.config(highlightbackground="black")
        saved_clicked_game_slot = clicked_game_slot


for i in range(0, len(game_slot_places)):
    game_slot = GameSlot(game_slots_frame, i + 1, random.choice(game_types))
    game_slot.grid(row=int(i/max_game_slots_in_one_row), column=i % max_game_slots_in_one_row, padx=10, pady=10)
    game_slot.bind("<Button-1>", generate_bill_details)

root.update()
print("height")
print(root.winfo_height())
print("width")
print(root.winfo_width())
root.mainloop()

