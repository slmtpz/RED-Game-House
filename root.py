from tkinter import *
from GameSlot import *


number_of_game_slots = 15
game_slots = []
grid_size = 25
game_slot_places = [1, 1, 1, 1, 1,
                    1, 0, 0, 0, 1,
                    0, 0, 1, 1, 1,
                    0, 0, 1, 1, 1,
                    1, 1, 1, 0, 0]
game_types = ['Playstation', 'Guitar Hero']


root = Tk()
root.wm_title("RED Game House")

game_slot_frames = []
for i in range(0, grid_size):
    frame = Frame(root, width=200, height=160, highlightbackground="black", highlightthickness=2)
    frame.grid(row=int(i/5), column=i % 5, padx=10, pady=10)
    game_slot_frames.append(frame)

for i in range(grid_size):
    if game_slot_places[i] == 1:
        game_slot = GameSlot(game_slot_frames[i])
        game_slots.append(game_slot)

root.mainloop()
