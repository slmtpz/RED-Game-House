from tkinter import *
from GameSlot import *
import random


number_of_game_slots = 14
game_slots = []
grid_size = 23
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
        'name': 'Pool',
        'charge': 10.00
    }
]


root = Tk()
root.wm_title("RED Game House")


game_slot_frames = []
for i in range(0, grid_size):
    frame = Frame(root, width=200, height=160, highlightbackground="black", highlightthickness=2)
    frame.grid(row=int(i/max_game_slots_in_one_row), column=i % max_game_slots_in_one_row, padx=10, pady=10)
    game_slot_frames.append(frame)

for i in range(grid_size):
    if game_slot_places[i] == 1:
        game_slot = GameSlot(game_slot_frames[i], i+1, random.choice(game_types))
        #game_slot.activate()
        game_slots.append(game_slot)

root.update()
print("height")
print(root.winfo_height())
print("width")
print(root.winfo_width())
root.mainloop()
